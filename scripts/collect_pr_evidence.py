#!/usr/bin/env python3
"""Collect one pull request's GitHub evidence into evidence-pack/v1 reports.

The collector performs GitHub REST GET requests only. It writes generated JSON
and Markdown to a local output directory; it does not mutate GitHub state or
make readiness, approval, merge, publication, or release decisions.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

import evidence_pack

PER_PAGE = 100
MAX_PAGES = 20
MAX_WORKFLOW_RUNS = 20
MAX_BODY_EXCERPT = 4_000
API_VERSION = "2022-11-28"
REPOSITORY_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
CLOSING_REFERENCE_PATTERN = re.compile(
    r"(?i)\b(?:close[sd]?|fix(?:e[sd])?|resolve[sd]?)\s*:?[ \t]+#(?P<number>[1-9][0-9]*)\b"
)


class CollectionFailure(RuntimeError):
    """Raised when the target cannot be resolved or collection cannot start safely."""


class GitHubAPIError(RuntimeError):
    """A bounded, sanitised GitHub API failure."""

    def __init__(self, endpoint: str, status: int | None, message: str) -> None:
        self.endpoint = endpoint
        self.status = status
        self.message = message
        status_text = f"HTTP {status}" if status is not None else "transport error"
        super().__init__(f"{status_text} for {endpoint}: {message}")


Transport = Callable[[str, Mapping[str, str]], tuple[Mapping[str, str], Any]]


class GitHubClient:
    """Small read-only GitHub REST client with deterministic page-based pagination."""

    def __init__(
        self,
        token: str,
        api_url: str = "https://api.github.com",
        transport: Transport | None = None,
        max_pages: int = MAX_PAGES,
    ) -> None:
        if not token:
            raise ValueError("a non-empty GitHub token is required")
        if max_pages <= 0:
            raise ValueError("max_pages must be positive")
        self._token = token
        self.api_url = api_url.rstrip("/")
        self._transport = transport or self._urllib_transport
        self.max_pages = max_pages

    def absolute_url(self, path: str, params: Mapping[str, Any] | None = None) -> str:
        if not path.startswith("/"):
            raise ValueError("GitHub API paths must start with '/'")
        query = urllib.parse.urlencode(
            [(key, str(value)) for key, value in sorted((params or {}).items()) if value is not None]
        )
        return f"{self.api_url}{path}" + (f"?{query}" if query else "")

    def get(self, path: str, params: Mapping[str, Any] | None = None) -> Any:
        url = self.absolute_url(path, params)
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self._token}",
            "User-Agent": "IssueOps-evidence-pack/1",
            "X-GitHub-Api-Version": API_VERSION,
        }
        _, payload = self._transport(url, headers)
        return payload

    def get_paginated(
        self,
        path: str,
        params: Mapping[str, Any] | None = None,
        *,
        item_key: str | None = None,
    ) -> list[Any]:
        collected: list[Any] = []
        declared_total: int | None = None
        for page in range(1, self.max_pages + 1):
            page_params = dict(params or {})
            page_params.update({"per_page": PER_PAGE, "page": page})
            payload = self.get(path, page_params)
            if item_key is None:
                if not isinstance(payload, list):
                    raise GitHubAPIError(
                        self.absolute_url(path, page_params),
                        None,
                        "paginated response must be an array",
                    )
                items = payload
            else:
                if not isinstance(payload, Mapping) or not isinstance(payload.get(item_key), list):
                    raise GitHubAPIError(
                        self.absolute_url(path, page_params),
                        None,
                        f"paginated response must contain array field {item_key!r}",
                    )
                items = payload[item_key]
                raw_total = payload.get("total_count")
                if raw_total is not None:
                    if not isinstance(raw_total, int) or isinstance(raw_total, bool) or raw_total < 0:
                        raise GitHubAPIError(
                            self.absolute_url(path, page_params),
                            None,
                            "total_count must be a non-negative integer",
                        )
                    if declared_total is None:
                        declared_total = raw_total
                    elif declared_total != raw_total:
                        raise GitHubAPIError(
                            self.absolute_url(path, page_params),
                            None,
                            "total_count changed during pagination",
                        )
            if len(items) > PER_PAGE:
                raise GitHubAPIError(
                    self.absolute_url(path, page_params),
                    None,
                    f"page returned more than {PER_PAGE} items",
                )
            collected.extend(items)
            if len(items) < PER_PAGE:
                if declared_total is not None and len(collected) < declared_total:
                    raise GitHubAPIError(
                        self.absolute_url(path, page_params),
                        None,
                        f"pagination ended after {len(collected)} of {declared_total} declared items",
                    )
                return collected
        raise GitHubAPIError(
            self.absolute_url(
                path,
                {**dict(params or {}), "per_page": PER_PAGE, "page": self.max_pages},
            ),
            None,
            f"pagination exceeded the {self.max_pages}-page safety limit",
        )

    @staticmethod
    def _urllib_transport(url: str, headers: Mapping[str, str]) -> tuple[Mapping[str, str], Any]:
        request = urllib.request.Request(url, headers=dict(headers), method="GET")
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw = response.read()
                response_headers = dict(response.headers.items())
        except urllib.error.HTTPError as exc:
            message = "GitHub API request failed"
            try:
                payload = json.loads(exc.read().decode("utf-8", errors="replace"))
                if isinstance(payload, Mapping) and isinstance(payload.get("message"), str):
                    message = payload["message"]
            except (json.JSONDecodeError, OSError, UnicodeDecodeError):
                pass
            raise GitHubAPIError(url, exc.code, message) from exc
        except urllib.error.URLError as exc:
            raise GitHubAPIError(url, None, str(exc.reason)) from exc
        try:
            payload = json.loads(raw.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            raise GitHubAPIError(url, None, "response was not valid JSON") from exc
        return response_headers, payload


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _excerpt(value: str | None) -> tuple[str, bool]:
    text = value or ""
    if len(text) <= MAX_BODY_EXCERPT:
        return text, False
    return text[:MAX_BODY_EXCERPT], True


def _require_mapping(value: Any, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise CollectionFailure(f"{context} response was not an object")
    return value


def _require_string(value: Any, context: str) -> str:
    if not isinstance(value, str) or not value:
        raise CollectionFailure(f"{context} was missing a required string")
    return value


def _source_timestamp(value: Any) -> str | None:
    return value if isinstance(value, str) and value else None


def _closing_issue_numbers(body: str | None) -> list[int]:
    return sorted({int(match.group("number")) for match in CLOSING_REFERENCE_PATTERN.finditer(body or "")})


def _api_error(errors: list[dict[str, Any]], code: str, exc: GitHubAPIError) -> None:
    errors.append({"code": code, "message": exc.message, "source_url": exc.endpoint})


def collect_report(
    repository: str,
    pull_request: int,
    client: GitHubClient,
    *,
    clock: Callable[[], str] = utc_now,
) -> evidence_pack.EvidenceReport:
    if not REPOSITORY_PATTERN.fullmatch(repository):
        raise CollectionFailure("repository must use owner/name form")
    if not isinstance(pull_request, int) or isinstance(pull_request, bool) or pull_request <= 0:
        raise CollectionFailure("pull request must be a positive integer")

    pr_path = f"/repos/{repository}/pulls/{pull_request}"
    try:
        initial_pr = _require_mapping(client.get(pr_path), "pull request")
    except GitHubAPIError as exc:
        raise CollectionFailure(f"unable to resolve pull request: {exc}") from exc

    pr_url = _require_string(initial_pr.get("html_url"), "pull request html_url")
    head = _require_mapping(initial_pr.get("head"), "pull request head")
    head_sha_start = _require_string(head.get("sha"), "pull request head SHA")
    started_at = clock()
    evidence: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []

    base = initial_pr.get("base") if isinstance(initial_pr.get("base"), Mapping) else {}
    user = initial_pr.get("user") if isinstance(initial_pr.get("user"), Mapping) else {}
    evidence.append(
        {
            "id": "pr.metadata",
            "classification": "repository-observed",
            "summary": f"Pull request #{pull_request} metadata was resolved at head {head_sha_start}.",
            "source_url": pr_url,
            "source_timestamp": _source_timestamp(initial_pr.get("updated_at")),
            "details": {
                "title": initial_pr.get("title"),
                "state": initial_pr.get("state"),
                "draft": bool(initial_pr.get("draft")),
                "author": user.get("login"),
                "base_ref": base.get("ref"),
                "head_sha": head_sha_start,
            },
        }
    )

    body = initial_pr.get("body") if isinstance(initial_pr.get("body"), str) else ""
    if body.strip():
        excerpt, truncated = _excerpt(body)
        evidence.append(
            {
                "id": "pr.body",
                "classification": "contributor-reported",
                "summary": "The pull-request body contains contributor-reported scope, validation or contract assertions.",
                "source_url": pr_url,
                "source_timestamp": _source_timestamp(initial_pr.get("updated_at")),
                "details": {"body_excerpt": excerpt, "truncated": truncated},
            }
        )

    issue_numbers = _closing_issue_numbers(body)
    linked_issue = issue_numbers[0] if len(issue_numbers) == 1 else None
    if len(issue_numbers) > 1:
        evidence.append(
            {
                "id": "issue.linkage",
                "classification": "conflicting",
                "summary": "The pull-request body declares more than one same-repository closing issue reference.",
                "source_url": pr_url,
                "details": {"issue_numbers": issue_numbers},
            }
        )
    elif linked_issue is not None:
        issue_path = f"/repos/{repository}/issues/{linked_issue}"
        try:
            issue = _require_mapping(client.get(issue_path), "linked issue")
            issue_url = _require_string(issue.get("html_url"), "linked issue html_url")
            issue_body, issue_body_truncated = _excerpt(
                issue.get("body") if isinstance(issue.get("body"), str) else ""
            )
            evidence.append(
                {
                    "id": "issue.contract",
                    "classification": "contributor-reported",
                    "summary": f"Issue #{linked_issue} is declared as the pull request's execution contract.",
                    "source_url": issue_url,
                    "source_timestamp": _source_timestamp(issue.get("updated_at")),
                    "details": {
                        "title": issue.get("title"),
                        "state": issue.get("state"),
                        "body_excerpt": issue_body,
                        "truncated": issue_body_truncated,
                    },
                }
            )
        except (GitHubAPIError, CollectionFailure) as exc:
            if isinstance(exc, GitHubAPIError):
                _api_error(errors, "issue.contract", exc)
            else:
                errors.append(
                    {
                        "code": "issue.contract",
                        "message": str(exc),
                        "source_url": client.absolute_url(issue_path),
                    }
                )

    def collect_list(
        code: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        item_key: str | None = None,
    ) -> list[Any] | None:
        try:
            return client.get_paginated(path, params, item_key=item_key)
        except GitHubAPIError as exc:
            _api_error(errors, code, exc)
            return None

    files_path = f"/repos/{repository}/pulls/{pull_request}/files"
    files = collect_list("pr.files", files_path)
    if files is not None:
        valid_files = [item for item in files if isinstance(item, Mapping)]
        filenames = sorted(
            str(item.get("filename"))
            for item in valid_files
            if isinstance(item.get("filename"), str)
        )
        evidence.append(
            {
                "id": "pr.changed-files",
                "classification": "repository-observed",
                "summary": f"GitHub returned {len(valid_files)} changed files for the pull request.",
                "source_url": f"{pr_url}/files",
                "details": {
                    "count": len(valid_files),
                    "additions": sum(
                        item.get("additions", 0)
                        for item in valid_files
                        if isinstance(item.get("additions"), int)
                    ),
                    "deletions": sum(
                        item.get("deletions", 0)
                        for item in valid_files
                        if isinstance(item.get("deletions"), int)
                    ),
                    "filenames": filenames[:100],
                    "filenames_truncated": len(filenames) > 100,
                },
            }
        )

    comments = collect_list(
        "pr.comments", f"/repos/{repository}/issues/{pull_request}/comments"
    )
    if comments is not None:
        valid_comments = [item for item in comments if isinstance(item, Mapping)]
        authors = Counter(
            str(item.get("user", {}).get("login"))
            for item in valid_comments
            if isinstance(item.get("user"), Mapping)
            and isinstance(item.get("user", {}).get("login"), str)
        )
        evidence.append(
            {
                "id": "pr.comments",
                "classification": "repository-observed",
                "summary": f"GitHub returned {len(valid_comments)} pull-request conversation comments.",
                "source_url": pr_url,
                "details": {
                    "count": len(valid_comments),
                    "authors": dict(sorted(authors.items())),
                },
            }
        )

    reviews = collect_list(
        "pr.reviews", f"/repos/{repository}/pulls/{pull_request}/reviews"
    )
    if reviews is not None:
        valid_reviews = [item for item in reviews if isinstance(item, Mapping)]
        states = Counter(
            str(item.get("state", "unknown")).lower() for item in valid_reviews
        )
        evidence.append(
            {
                "id": "pr.reviews",
                "classification": "repository-observed",
                "summary": f"GitHub returned {len(valid_reviews)} submitted pull-request reviews.",
                "source_url": f"{pr_url}/reviews",
                "details": {
                    "count": len(valid_reviews),
                    "states": dict(sorted(states.items())),
                },
            }
        )

    checks = collect_list(
        "checks.runs",
        f"/repos/{repository}/commits/{head_sha_start}/check-runs",
        item_key="check_runs",
    )
    if checks is not None:
        valid_checks = [item for item in checks if isinstance(item, Mapping)]
        if not valid_checks:
            evidence.append(
                {
                    "id": "checks.absent",
                    "classification": "repository-observed",
                    "summary": "No check runs were present for the resolved pull-request head.",
                    "source_url": f"{pr_url}/checks",
                    "details": {"count": 0},
                }
            )
        for check in sorted(
            valid_checks,
            key=lambda item: (str(item.get("name", "")), int(item.get("id", 0))),
        ):
            check_id = int(check.get("id", 0))
            status = str(check.get("status", "unknown"))
            conclusion = check.get("conclusion")
            classification = (
                "pending" if status != "completed" else "repository-observed"
            )
            source_url = (
                check.get("html_url")
                if isinstance(check.get("html_url"), str)
                else f"{pr_url}/checks"
            )
            evidence.append(
                {
                    "id": f"check.{check_id}",
                    "classification": classification,
                    "summary": f"Check {check.get('name') or check_id} is {status} with conclusion {conclusion!r}.",
                    "source_url": source_url,
                    "source_timestamp": _source_timestamp(
                        check.get("completed_at") or check.get("started_at")
                    ),
                    "details": {
                        "name": check.get("name"),
                        "status": status,
                        "conclusion": conclusion,
                    },
                }
            )

    runs = collect_list(
        "actions.runs",
        f"/repos/{repository}/actions/runs",
        params={"head_sha": head_sha_start, "event": "pull_request"},
        item_key="workflow_runs",
    )
    if runs is not None:
        valid_runs = [item for item in runs if isinstance(item, Mapping)]
        if len(valid_runs) > MAX_WORKFLOW_RUNS:
            errors.append(
                {
                    "code": "actions.run-limit",
                    "message": f"{len(valid_runs)} workflow runs exceeded the {MAX_WORKFLOW_RUNS}-run collection limit.",
                    "source_url": client.absolute_url(
                        f"/repos/{repository}/actions/runs",
                        {"head_sha": head_sha_start, "event": "pull_request"},
                    ),
                }
            )
            valid_runs = sorted(
                valid_runs,
                key=lambda item: int(item.get("id", 0)),
                reverse=True,
            )[:MAX_WORKFLOW_RUNS]
        if not valid_runs:
            evidence.append(
                {
                    "id": "workflows.absent",
                    "classification": "repository-observed",
                    "summary": "No pull-request workflow runs were present for the resolved head.",
                    "source_url": f"{pr_url}/checks",
                    "details": {"count": 0},
                }
            )
        for run in sorted(valid_runs, key=lambda item: int(item.get("id", 0))):
            run_id = int(run.get("id", 0))
            status = str(run.get("status", "unknown"))
            conclusion = run.get("conclusion")
            jobs = collect_list(
                f"actions.jobs.{run_id}",
                f"/repos/{repository}/actions/runs/{run_id}/jobs",
                item_key="jobs",
            )
            job_details: list[dict[str, Any]] = []
            pending_job = False
            if jobs is not None:
                for job in sorted(
                    (item for item in jobs if isinstance(item, Mapping)),
                    key=lambda item: (
                        str(item.get("name", "")),
                        int(item.get("id", 0)),
                    ),
                ):
                    job_status = str(job.get("status", "unknown"))
                    if job_status != "completed":
                        pending_job = True
                    job_details.append(
                        {
                            "name": job.get("name"),
                            "status": job_status,
                            "conclusion": job.get("conclusion"),
                        }
                    )
            classification = (
                "pending"
                if status != "completed" or pending_job
                else "repository-observed"
            )
            run_url = (
                run.get("html_url")
                if isinstance(run.get("html_url"), str)
                else f"{pr_url}/checks"
            )
            evidence.append(
                {
                    "id": f"workflow.{run_id}",
                    "classification": classification,
                    "summary": f"Workflow {run.get('name') or run_id} is {status} with conclusion {conclusion!r}.",
                    "source_url": run_url,
                    "source_timestamp": _source_timestamp(
                        run.get("updated_at") or run.get("run_started_at")
                    ),
                    "details": {
                        "name": run.get("name"),
                        "event": run.get("event"),
                        "run_number": run.get("run_number"),
                        "status": status,
                        "conclusion": conclusion,
                        "jobs": job_details,
                    },
                }
            )

    head_sha_end = head_sha_start
    try:
        final_pr = _require_mapping(client.get(pr_path), "final pull request")
        final_head = _require_mapping(final_pr.get("head"), "final pull request head")
        head_sha_end = _require_string(
            final_head.get("sha"), "final pull request head SHA"
        )
    except (GitHubAPIError, CollectionFailure) as exc:
        if isinstance(exc, GitHubAPIError):
            _api_error(errors, "pr.final-head", exc)
        else:
            errors.append(
                {
                    "code": "pr.final-head",
                    "message": str(exc),
                    "source_url": pr_url,
                }
            )

    raw_report = {
        "schema_version": evidence_pack.SCHEMA_VERSION,
        "target": {
            "repository": repository,
            "pull_request": pull_request,
            "url": pr_url,
            **({"linked_issue": linked_issue} if linked_issue is not None else {}),
        },
        "collection": {
            "started_at": started_at,
            "completed_at": clock(),
            "head_sha_start": head_sha_start,
            "head_sha_end": head_sha_end,
        },
        "evidence": evidence,
        "errors": errors,
    }
    try:
        return evidence_pack.parse_report(raw_report)
    except evidence_pack.EvidenceValidationError as exc:
        raise CollectionFailure(
            f"collected evidence did not satisfy evidence-pack/v1: {exc}"
        ) from exc


def write_report(report: evidence_pack.EvidenceReport, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "evidence-pack.json").write_text(
        report.render_json(), encoding="utf-8"
    )
    (output_dir / "evidence-pack.md").write_text(
        report.render_markdown(), encoding="utf-8"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", help="target repository in owner/name form")
    parser.add_argument(
        "pull_request", type=int, help="positive pull-request number"
    )
    parser.add_argument(
        "--api-url",
        default=os.environ.get("GITHUB_API_URL", "https://api.github.com"),
    )
    parser.add_argument(
        "--token-env",
        default="GITHUB_TOKEN",
        help="environment variable containing the token",
    )
    parser.add_argument(
        "--output-dir",
        default="evidence-pack-output",
        help="directory for generated reports",
    )
    args = parser.parse_args(argv)

    token = os.environ.get(args.token_env, "")
    if not token:
        print(
            f"Evidence collection failed: environment variable {args.token_env!r} is not set",
            file=sys.stderr,
        )
        return 1
    try:
        client = GitHubClient(token, api_url=args.api_url)
        report = collect_report(args.repository, args.pull_request, client)
        write_report(report, Path(args.output_dir))
    except (CollectionFailure, GitHubAPIError, OSError, ValueError) as exc:
        print(f"Evidence collection failed: {exc}", file=sys.stderr)
        return 1

    print(f"Evidence collection status: {report.status.value}")
    return 0 if report.status is evidence_pack.ReportStatus.COMPLETE else 2


if __name__ == "__main__":
    raise SystemExit(main())
