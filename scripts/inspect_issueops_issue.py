#!/usr/bin/env python3
"""Inspect one IssueOps issue using conservative, read-only GitHub evidence.

The report is disposable navigation assistance. GitHub/repository records remain
canonical; this tool does not decide substantive readiness, approve a plan,
confirm contract fulfilment, authorise continuation, or authorise merge.
"""

from __future__ import annotations

import argparse
from datetime import datetime
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Callable, Mapping, Sequence

PER_PAGE = 100
MAX_PAGES = 20
API_VERSION = "2022-11-28"
REPOSITORY_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
CLOSING_REFERENCE_PATTERN = re.compile(
    r"(?i)\b(?:close[sd]?|fix(?:e[sd])?|resolve[sd]?)\s*:?[ \t]+#(?P<number>[1-9][0-9]*)\b"
)
CANONICAL_REFERENCE_PATTERN = re.compile(r"^Issue #(?P<number>[1-9][0-9]*)$")
ISSUE_SHAPED_PATTERN = re.compile(r"(?i)^Issue\b")
APPROVAL_REFERENCE_PATTERN = re.compile(
    r"(?im)^[ \t]*I approve the detailed implementation plan recorded in issue comment "
    r"`(?P<id>[1-9][0-9]*)`[ \t]*[.!]?[ \t]*$"
)
SUPERSEDES_PATTERN = re.compile(
    r"(?i)\bsupersedes\s+(?:issue\s+)?comment\s+`?(?P<id>[1-9][0-9]*)`?\b"
)
SUPERSEDED_BY_PATTERN = re.compile(
    r"(?i)\bsuperseded\s+by\s+(?:issue\s+)?comment\s+`?(?P<id>[1-9][0-9]*)`?\b"
)
AUTHORITY_NOTICE = (
    "GitHub/repository records remain canonical. This report is read-only navigation "
    "assistance and does not establish substantive readiness, approve a plan, confirm "
    "contract fulfilment, authorise continuation or authorise merge."
)


class CollectionFailure(RuntimeError):
    """Raised when the primary target cannot be safely resolved."""


class GitHubAPIError(RuntimeError):
    """A bounded GitHub API error whose message can be sanitised."""

    def __init__(self, endpoint: str, status: int | None, message: str) -> None:
        self.endpoint = endpoint
        self.status = status
        self.message = message
        status_text = f"HTTP {status}" if status is not None else "transport error"
        super().__init__(f"{status_text} for {endpoint}: {message}")


Transport = Callable[[str, Mapping[str, str]], tuple[Mapping[str, str], Any]]


def sanitise(value: str, token: str) -> str:
    """Remove the configured credential if it appears in external error text."""
    if token:
        value = value.replace(token, "[REDACTED]")
    return value


class GitHubClient:
    """Small GET-only GitHub REST client with bounded numbered pagination."""

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

    def absolute_url(
        self, path: str, params: Mapping[str, Any] | None = None
    ) -> str:
        if not path.startswith("/"):
            raise ValueError("GitHub API paths must start with '/'")
        query = urllib.parse.urlencode(
            [
                (key, str(value))
                for key, value in sorted((params or {}).items())
                if value is not None
            ]
        )
        return f"{self.api_url}{path}" + (f"?{query}" if query else "")

    def get(self, path: str, params: Mapping[str, Any] | None = None) -> Any:
        url = self.absolute_url(path, params)
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self._token}",
            "User-Agent": "IssueOps-primary-record-inspector/1",
            "X-GitHub-Api-Version": API_VERSION,
        }
        _, payload = self._transport(url, headers)
        return payload

    def get_paginated(
        self, path: str, params: Mapping[str, Any] | None = None
    ) -> list[Any]:
        collected: list[Any] = []
        for page in range(1, self.max_pages + 1):
            page_params = dict(params or {})
            page_params.update({"per_page": PER_PAGE, "page": page})
            payload = self.get(path, page_params)
            if not isinstance(payload, list):
                raise GitHubAPIError(
                    self.absolute_url(path, page_params),
                    None,
                    "paginated response must be an array",
                )
            if len(payload) > PER_PAGE:
                raise GitHubAPIError(
                    self.absolute_url(path, page_params),
                    None,
                    f"page returned more than {PER_PAGE} items",
                )
            collected.extend(payload)
            if len(payload) < PER_PAGE:
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
    def _urllib_transport(
        url: str, headers: Mapping[str, str]
    ) -> tuple[Mapping[str, str], Any]:
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


def _require_mapping(value: Any, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise CollectionFailure(f"{context} response was not an object")
    return value


def _require_string(value: Any, context: str) -> str:
    if not isinstance(value, str) or not value:
        raise CollectionFailure(f"{context} was missing a required string")
    return value


def _require_git_sha(value: Any, context: str) -> str:
    sha = _require_string(value, context)
    if not re.fullmatch(r"[0-9a-fA-F]{40}", sha):
        raise CollectionFailure(f"{context} was malformed")
    return sha


def _source_ref(kind: str, identifier: int | str, url: str) -> dict[str, Any]:
    return {"kind": kind, "id": identifier, "url": url}


def _user_login(item: Mapping[str, Any]) -> str | None:
    user = item.get("user")
    if isinstance(user, Mapping) and isinstance(user.get("login"), str):
        return user["login"]
    return None


def _user_type(item: Mapping[str, Any]) -> str | None:
    user = item.get("user")
    if isinstance(user, Mapping) and isinstance(user.get("type"), str):
        return user["type"]
    return None


def _markdown_events(text: str) -> list[tuple[int, str, bool]]:
    """Return (line index, raw line, eligible) while excluding code/comments."""
    events: list[tuple[int, str, bool]] = []
    in_html_comment = False
    fence_char: str | None = None
    fence_length = 0
    for index, raw_line in enumerate(text.splitlines()):
        left = raw_line.lstrip(" \t")
        indent = len(raw_line) - len(left)

        if fence_char is not None:
            closing = re.fullmatch(
                rf"{re.escape(fence_char)}{{{fence_length},}}[ \t]*", left
            )
            events.append((index, raw_line, False))
            if indent <= 3 and closing:
                fence_char = None
                fence_length = 0
            continue

        if in_html_comment:
            events.append((index, raw_line, False))
            if "-->" in raw_line:
                in_html_comment = False
            continue

        if indent >= 4:
            events.append((index, raw_line, False))
            continue

        if "<!--" in raw_line:
            events.append((index, raw_line, False))
            after = raw_line.split("<!--", 1)[1]
            if "-->" not in after:
                in_html_comment = True
            continue

        opening = re.match(r"(?P<fence>`{3,}|~{3,})", left)
        if opening:
            marker = opening.group("fence")
            fence_char = marker[0]
            fence_length = len(marker)
            events.append((index, raw_line, False))
            continue

        events.append((index, raw_line, True))
    return events


def _eligible_lines(text: str) -> list[str]:
    return [raw for _, raw, eligible in _markdown_events(text) if eligible]


def _eligible_text(text: str) -> str:
    return "\n".join(_eligible_lines(text))


def _first_h2(text: str) -> str | None:
    for line in _eligible_lines(text):
        match = re.fullmatch(r"[ \t]{0,3}##[ \t]+(.+?)[ \t]*", line)
        if match:
            return match.group(1).strip()
    return None


def _h2_sections(text: str) -> list[tuple[str, int, int]]:
    lines = text.splitlines()
    headings: list[tuple[str, int]] = []
    for index, raw, eligible in _markdown_events(text):
        if not eligible:
            continue
        match = re.fullmatch(r"[ \t]{0,3}##[ \t]+(.+?)[ \t]*", raw)
        if match:
            headings.append((match.group(1).strip(), index))
    sections: list[tuple[str, int, int]] = []
    for position, (heading, start) in enumerate(headings):
        end = headings[position + 1][1] if position + 1 < len(headings) else len(lines)
        sections.append((heading, start, end))
    return sections


def classify_heading(heading: str | None) -> str | None:
    if not heading:
        return None
    normal = " ".join(heading.split()).casefold()
    if normal in {
        "planning readiness",
        "issue readiness assessment",
        "repository-standard readiness and dependency assessment",
    } or normal.startswith("fresh readiness assessment"):
        return "readiness"
    if (
        normal == "detailed implementation plan"
        or normal.startswith("detailed implementation plan —")
        or normal.startswith("detailed implementation plan -")
        or (normal.startswith("detailed implementation /") and normal.endswith(" plan"))
    ):
        return "implementation_plan"
    if normal == "human implementation-plan approval":
        return "human_plan_approval"
    if re.search(r"\bhandover\b", normal):
        return "handover"
    if (
        normal.startswith("independent review")
        or normal.startswith("fresh independent review")
        or normal.startswith("fresh independent approval review")
        or normal == "groundedness review"
        or normal.startswith("pre-approval groundedness review")
    ):
        return "review"
    if "close-out" in normal or "closeout" in normal:
        return "close_out"
    return None


def _comment_record(comment: Mapping[str, Any]) -> dict[str, Any]:
    comment_id = comment.get("id")
    if not isinstance(comment_id, int) or isinstance(comment_id, bool) or comment_id <= 0:
        raise CollectionFailure("comment was missing a positive integer id")
    url = _require_string(comment.get("html_url"), "comment html_url")
    body = comment.get("body") if isinstance(comment.get("body"), str) else ""
    heading = _first_h2(body)
    return {
        "id": comment_id,
        "url": url,
        "author": _user_login(comment),
        "author_type": _user_type(comment),
        "author_association": (
            comment.get("author_association")
            if isinstance(comment.get("author_association"), str)
            else None
        ),
        "created_at": (
            comment.get("created_at") if isinstance(comment.get("created_at"), str) else None
        ),
        "updated_at": (
            comment.get("updated_at") if isinstance(comment.get("updated_at"), str) else None
        ),
        "body": body,
        "first_h2": heading,
        "record_class": classify_heading(heading),
        "source": _source_ref("issue_comment", comment_id, url),
    }


def _chronology_key(record: Mapping[str, Any]) -> tuple[str, int]:
    timestamp = record.get("created_at")
    return (timestamp if isinstance(timestamp, str) else "", int(record["id"]))


def _parse_github_timestamp(value: Any) -> datetime | None:
    if not isinstance(value, str) or not re.fullmatch(
        r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]+)?Z",
        value,
    ):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None


def _verify_plan_approvals(
    comments: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    by_id = {int(record["id"]): record for record in comments}
    supported: list[dict[str, Any]] = []
    ambiguous: list[dict[str, Any]] = []
    for record in comments:
        if record.get("record_class") != "human_plan_approval":
            continue
        reasons: list[str] = []
        if record.get("author_type") == "Bot":
            reasons.append("approval-shaped comment was authored by a Bot")
        if record.get("author_association") != "OWNER":
            reasons.append("author_association is not OWNER")
        matches = list(
            APPROVAL_REFERENCE_PATTERN.finditer(
                _eligible_text(str(record.get("body", "")))
            )
        )
        if len(matches) != 1:
            reasons.append("expected exactly one canonical plan-reference sentence")
            referenced_id = None
        else:
            referenced_id = int(matches[0].group("id"))
        plan: dict[str, Any] | None = None
        if referenced_id is not None:
            plan = by_id.get(referenced_id)
            if plan is None:
                reasons.append("referenced plan comment was not collected")
            elif plan.get("record_class") != "implementation_plan":
                reasons.append("referenced comment is not a recognised implementation plan")
            else:
                plan_ts = plan.get("created_at")
                approval_ts = record.get("created_at")
                if not isinstance(plan_ts, str) or not isinstance(approval_ts, str):
                    reasons.append("plan/approval chronology is unavailable")
                elif plan_ts >= approval_ts:
                    reasons.append("referenced plan does not predate approval")
        item = {
            "classification": (
                "ambiguous_or_unsupported" if reasons else "supported_derived_observation"
            ),
            "kind": "plan_approval_record",
            "summary": (
                "Approval-shaped comment could not be mechanically verified."
                if reasons
                else f"Owner plan-approval record references implementation plan comment {referenced_id}."
            ),
            "source": record["source"],
            "derived_from": (
                [record["source"], plan["source"]] if not reasons and plan is not None else [record["source"]]
            ),
        }
        if referenced_id is not None:
            item["referenced_plan_comment"] = referenced_id
        if reasons:
            item["reasons"] = sorted(reasons)
            ambiguous.append(item)
        else:
            supported.append(item)
    return supported, ambiguous


def _extract_following_value(lines: list[str], start_index: int, end_index: int) -> str | None:
    index = start_index
    while index < end_index and not lines[index].strip():
        index += 1
    if index >= end_index:
        return None
    stripped = lines[index].strip()
    fence = re.fullmatch(r"(?P<fence>`{3,}|~{3,}).*", stripped)
    if fence:
        marker = fence.group("fence")
        char = marker[0]
        minimum = len(marker)
        captured: list[str] = []
        index += 1
        while index < end_index:
            candidate = lines[index].strip()
            if re.fullmatch(rf"{re.escape(char)}{{{minimum},}}[ \t]*", candidate):
                break
            captured.append(lines[index])
            index += 1
        value = "\n".join(captured).strip()
        return value or None
    return stripped or None


def _boundaries_in_source(
    body: str, record_class: str | None, *, issue_body: bool = False
) -> list[str]:
    lines = body.splitlines()
    eligible_indices = {
        index for index, _, eligible in _markdown_events(body) if eligible
    }
    candidates: list[str] = []

    for heading, start, end in _h2_sections(body):
        normal = " ".join(heading.split()).casefold()
        if normal in {
            "next permitted action",
            "exact next permitted action",
            "next owner decision",
        }:
            value = _extract_following_value(lines, start + 1, end)
            if value:
                candidates.append(value)
        if issue_body and normal == "current boundary":
            for index in range(start + 1, end):
                if (
                    index in eligible_indices
                    and lines[index].strip() == "The exact next permitted action is:"
                ):
                    value = _extract_following_value(lines, index + 1, end)
                    if value:
                        candidates.append(value)

    if record_class is not None:
        for index, line in enumerate(lines):
            if index not in eligible_indices:
                continue
            match = re.match(
                r"^[ \t]*(?:The )?(?:exact )?next permitted action is(?P<tail>:|[ \t]+)(?P<rest>.*)$",
                line,
                flags=re.IGNORECASE,
            )
            if not match:
                continue
            rest = match.group("rest").strip()
            if rest:
                candidates.append(rest)
            else:
                value = _extract_following_value(lines, index + 1, len(lines))
                if value:
                    candidates.append(value)

    unique: list[str] = []
    for candidate in candidates:
        if candidate not in unique:
            unique.append(candidate)
    return unique


def _recorded_next_boundary(
    issue: Mapping[str, Any], comments: list[dict[str, Any]]
) -> dict[str, Any]:
    candidates: list[dict[str, Any]] = []
    issue_body = issue.get("body") if isinstance(issue.get("body"), str) else ""
    issue_values = _boundaries_in_source(issue_body, None, issue_body=True)
    issue_url = _require_string(issue.get("html_url"), "issue html_url")
    if issue_values:
        candidates.append(
            {
                "timestamp": (
                    issue.get("created_at") if isinstance(issue.get("created_at"), str) else ""
                ),
                "source": _source_ref("issue", int(issue["number"]), issue_url),
                "values": issue_values,
            }
        )
    for record in comments:
        values = _boundaries_in_source(
            str(record.get("body", "")), record.get("record_class")
        )
        if values:
            candidates.append(
                {
                    "timestamp": record.get("created_at") or "",
                    "source": record["source"],
                    "values": values,
                }
            )
    if not candidates:
        return {
            "classification": "pending_or_unavailable",
            "status": "not_recorded",
            "summary": "No explicit recorded next boundary was recognised.",
        }
    if len(candidates) == 1:
        latest = candidates[0]
    else:
        dated = [
            (candidate, _parse_github_timestamp(candidate.get("timestamp")))
            for candidate in candidates
        ]
        if any(timestamp is None for _, timestamp in dated):
            return {
                "classification": "ambiguous_or_unsupported",
                "status": "ambiguous",
                "summary": "Competing explicit boundary sources cannot be safely ordered because created_at chronology is unavailable.",
                "sources": [candidate["source"] for candidate in candidates],
            }
        latest_timestamp = max(timestamp for _, timestamp in dated if timestamp is not None)
        latest_candidates = [
            candidate for candidate, timestamp in dated if timestamp == latest_timestamp
        ]
        if len(latest_candidates) != 1:
            return {
                "classification": "ambiguous_or_unsupported",
                "status": "ambiguous",
                "summary": "Competing explicit boundary sources share the latest available chronology.",
                "sources": [candidate["source"] for candidate in latest_candidates],
            }
        latest = latest_candidates[0]
    if len(latest["values"]) != 1:
        return {
            "classification": "ambiguous_or_unsupported",
            "status": "ambiguous",
            "summary": "The latest source contains multiple explicit boundary statements.",
            "candidates": latest["values"],
            "source": latest["source"],
        }
    return {
        "classification": "recorded_next_boundary",
        "status": "recorded",
        "value": latest["values"][0],
        "source": latest["source"],
    }


def _supersession_observations(
    comments: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    by_id = {int(record["id"]): record for record in comments}
    superseded: set[int] = set()
    ambiguous: list[dict[str, Any]] = []
    for record in comments:
        record_id = int(record["id"])
        body = _eligible_text(str(record.get("body", "")))
        for match in SUPERSEDES_PATTERN.finditer(body):
            target_id = int(match.group("id"))
            target = by_id.get(target_id)
            if target is None:
                ambiguous.append(
                    {
                        "classification": "ambiguous_or_unsupported",
                        "kind": "supersession",
                        "summary": f"Supersession reference points to unknown comment {target_id}.",
                        "source": record["source"],
                    }
                )
                continue
            target_timestamp = _parse_github_timestamp(target.get("created_at"))
            record_timestamp = _parse_github_timestamp(record.get("created_at"))
            if target_timestamp is None or record_timestamp is None:
                ambiguous.append(
                    {
                        "classification": "ambiguous_or_unsupported",
                        "kind": "supersession",
                        "summary": f"Supersession chronology for comment {target_id} is unavailable.",
                        "source": record["source"],
                    }
                )
                continue
            if target_timestamp >= record_timestamp:
                ambiguous.append(
                    {
                        "classification": "ambiguous_or_unsupported",
                        "kind": "supersession",
                        "summary": f"Supersession reference to comment {target_id} is not later than its target.",
                        "source": record["source"],
                    }
                )
                continue
            superseded.add(target_id)
        for match in SUPERSEDED_BY_PATTERN.finditer(body):
            replacement_id = int(match.group("id"))
            replacement = by_id.get(replacement_id)
            if replacement is None:
                ambiguous.append(
                    {
                        "classification": "ambiguous_or_unsupported",
                        "kind": "supersession",
                        "summary": f"Superseded-by reference points to unknown comment {replacement_id}.",
                        "source": record["source"],
                    }
                )
                continue
            record_timestamp = _parse_github_timestamp(record.get("created_at"))
            replacement_timestamp = _parse_github_timestamp(
                replacement.get("created_at")
            )
            if record_timestamp is None or replacement_timestamp is None:
                ambiguous.append(
                    {
                        "classification": "ambiguous_or_unsupported",
                        "kind": "supersession",
                        "summary": f"Superseded-by chronology for comment {replacement_id} is unavailable.",
                        "source": record["source"],
                    }
                )
                continue
            if replacement_timestamp <= record_timestamp:
                ambiguous.append(
                    {
                        "classification": "ambiguous_or_unsupported",
                        "kind": "supersession",
                        "summary": f"Superseded-by comment {replacement_id} does not postdate its source.",
                        "source": record["source"],
                    }
                )
                continue
            superseded.add(record_id)
    observations = [
        {
            "classification": "stale_or_superseded",
            "kind": "explicit_supersession",
            "summary": f"Issue comment {comment_id} is explicitly superseded by a collected later record.",
            "source": by_id[comment_id]["source"],
        }
        for comment_id in sorted(superseded)
    ]
    return observations, ambiguous


def _closing_issue_numbers(body: str) -> list[int]:
    eligible = "\n".join(_eligible_lines(body))
    return sorted(
        {
            int(match.group("number"))
            for match in CLOSING_REFERENCE_PATTERN.finditer(eligible)
        }
    )


def _canonical_issue_declarations(body: str) -> tuple[int, list[int], int]:
    section_count = 0
    issue_numbers: list[int] = []
    malformed_count = 0
    in_section = False
    for line in _eligible_lines(body):
        stripped = line.strip()
        if stripped == "## Execution contract":
            section_count += 1
            in_section = True
            continue
        if in_section and stripped.startswith("## "):
            in_section = False
        if not in_section or not stripped:
            continue
        match = CANONICAL_REFERENCE_PATTERN.fullmatch(stripped)
        if match:
            issue_numbers.append(int(match.group("number")))
        elif ISSUE_SHAPED_PATTERN.match(stripped):
            malformed_count += 1
    return section_count, issue_numbers, malformed_count


def resolve_pr_linkage(body: str) -> dict[str, Any]:
    section_count, canonical, malformed_count = _canonical_issue_declarations(body)
    closing = _closing_issue_numbers(body)
    conflicts: list[str] = []
    linked_issue: int | None = None
    method: str | None = None
    if section_count > 1:
        conflicts.append("multiple execution-contract sections")
    if len(canonical) > 1:
        conflicts.append("multiple canonical execution-contract declarations")
    if malformed_count:
        conflicts.append("malformed canonical execution-contract declaration")
    if not conflicts and len(canonical) == 1:
        linked_issue = canonical[0]
        method = "canonical"
        if any(number != linked_issue for number in closing):
            conflicts.append("canonical and closing issue references disagree")
            linked_issue = None
            method = None
    elif not conflicts and not canonical:
        if len(closing) > 1:
            conflicts.append("multiple legacy closing issue references")
        elif len(closing) == 1:
            linked_issue = closing[0]
            method = "legacy-closing-keyword"
    return {
        "linked_issue": linked_issue,
        "method": method,
        "conflicts": conflicts,
        "details": {
            "section_count": section_count,
            "canonical_issue_numbers": canonical,
            "closing_issue_numbers": closing,
            "malformed_declaration_count": malformed_count,
        },
    }


def _timeline_pr_candidates(
    timeline: list[Any], repository: str
) -> list[int]:
    candidates: set[int] = set()
    for event in timeline:
        if not isinstance(event, Mapping) or event.get("event") != "cross-referenced":
            continue
        source = event.get("source")
        source_issue = source.get("issue") if isinstance(source, Mapping) else None
        if not isinstance(source_issue, Mapping):
            continue
        repo = source_issue.get("repository")
        if not isinstance(repo, Mapping) or repo.get("full_name") != repository:
            continue
        if not isinstance(source_issue.get("pull_request"), Mapping):
            continue
        number = source_issue.get("number")
        if isinstance(number, int) and not isinstance(number, bool) and number > 0:
            candidates.add(number)
    return sorted(candidates)


def _pr_basic(
    pr: Mapping[str, Any], repository: str, expected_number: int
) -> dict[str, Any]:
    number = pr.get("number")
    if not isinstance(number, int) or isinstance(number, bool) or number <= 0:
        raise CollectionFailure("related pull request was missing a positive number")
    if number != expected_number:
        raise CollectionFailure("related pull request number did not match its candidate")
    url = _require_string(pr.get("html_url"), "related pull request html_url")
    parsed_url = urllib.parse.urlparse(url)
    if (
        parsed_url.scheme not in {"http", "https"}
        or not parsed_url.netloc
        or parsed_url.path.rstrip("/") != f"/{repository}/pull/{number}"
        or parsed_url.params
        or parsed_url.query
        or parsed_url.fragment
    ):
        raise CollectionFailure("related pull request html_url was malformed")
    state = pr.get("state")
    if state not in {"open", "closed"}:
        raise CollectionFailure("related pull request state was missing or malformed")
    draft = pr.get("draft")
    if not isinstance(draft, bool):
        raise CollectionFailure("related pull request draft state was missing or malformed")
    merged = pr.get("merged")
    if not isinstance(merged, bool):
        raise CollectionFailure("related pull request merged state was missing or malformed")
    if "merged_at" not in pr:
        raise CollectionFailure("related pull request merged_at was missing")
    merged_at = pr.get("merged_at")
    if merged_at is not None and _parse_github_timestamp(merged_at) is None:
        raise CollectionFailure("related pull request merged_at was malformed")
    if merged != (merged_at is not None):
        raise CollectionFailure("related pull request merge fields were inconsistent")
    if merged and state != "closed":
        raise CollectionFailure("related pull request state was inconsistent with merge state")
    base = _require_mapping(pr.get("base"), "related pull request base")
    head = _require_mapping(pr.get("head"), "related pull request head")
    return {
        "number": number,
        "url": url,
        "state": state,
        "draft": draft,
        "merged": merged,
        "merged_at": merged_at,
        "base_ref": _require_string(base.get("ref"), "related pull request base ref"),
        "base_sha": _require_git_sha(
            base.get("sha"), "related pull request base sha"
        ),
        "head_ref": _require_string(head.get("ref"), "related pull request head ref"),
        "head_sha": _require_git_sha(
            head.get("sha"), "related pull request head sha"
        ),
        "source": _source_ref("pull_request", number, url),
    }


def _related_pr_report(
    repository: str,
    issue_number: int,
    client: GitHubClient,
) -> tuple[dict[str, Any], list[dict[str, Any]], bool]:
    warnings: list[dict[str, Any]] = []
    try:
        timeline = client.get_paginated(
            f"/repos/{repository}/issues/{issue_number}/timeline"
        )
    except GitHubAPIError as exc:
        warnings.append(
            {
                "code": "related_pr.timeline",
                "message": exc.message,
                "source_url": exc.endpoint,
            }
        )
        return (
            {
                "classification": "pending_or_unavailable",
                "status": "unavailable",
                "summary": "Related pull-request discovery could not be completed.",
            },
            warnings,
            False,
        )
    candidates = _timeline_pr_candidates(timeline, repository)
    verified: list[dict[str, Any]] = []
    conflicts: list[dict[str, Any]] = []
    for candidate in candidates:
        try:
            raw_pr = _require_mapping(
                client.get(f"/repos/{repository}/pulls/{candidate}"),
                "related pull request",
            )
            if "body" not in raw_pr or not isinstance(raw_pr.get("body"), str):
                raise CollectionFailure(
                    "related pull request body was missing or malformed"
                )
            pr = _pr_basic(raw_pr, repository, candidate)
        except (GitHubAPIError, CollectionFailure) as exc:
            if isinstance(exc, GitHubAPIError):
                message, source_url = exc.message, exc.endpoint
            else:
                message = str(exc)
                source_url = client.absolute_url(
                    f"/repos/{repository}/pulls/{candidate}"
                )
            warnings.append(
                {
                    "code": f"related_pr.{candidate}",
                    "message": message,
                    "source_url": source_url,
                }
            )
            return (
                {
                    "classification": "pending_or_unavailable",
                    "status": "unavailable",
                    "summary": "At least one candidate pull request could not be safely verified.",
                    "candidate_numbers": candidates,
                },
                warnings,
                False,
            )
        linkage = resolve_pr_linkage(raw_pr["body"])
        if linkage["conflicts"]:
            conflicts.append(
                {
                    "number": candidate,
                    "url": pr["url"],
                    "reasons": linkage["conflicts"],
                    "linkage": linkage["details"],
                }
            )
        elif linkage["linked_issue"] == issue_number:
            pr["linkage_method"] = linkage["method"]
            verified.append(pr)
    if conflicts:
        return (
            {
                "classification": "ambiguous_or_unsupported",
                "status": "ambiguous",
                "summary": "One or more candidate pull requests have conflicting contract linkage.",
                "candidate_numbers": candidates,
                "verified": verified,
                "conflicts": conflicts,
            },
            warnings,
            True,
        )
    if len(verified) == 0:
        return (
            {
                "classification": "observed_fact",
                "status": "absent",
                "summary": "No verified related pull request was found on the bounded timeline discovery surface.",
                "candidate_numbers": candidates,
            },
            warnings,
            True,
        )
    if len(verified) == 1:
        return (
            {
                "classification": "supported_derived_observation",
                "status": "verified",
                "summary": "Exactly one related pull request has verified execution-contract linkage.",
                "pull_request": verified[0],
                "candidate_numbers": candidates,
            },
            warnings,
            True,
        )
    return (
        {
            "classification": "ambiguous_or_unsupported",
            "status": "ambiguous",
            "summary": "Multiple pull requests have verified execution-contract linkage.",
            "pull_requests": verified,
            "candidate_numbers": candidates,
        },
        warnings,
        True,
    )


def collect_report(
    repository: str, issue_number: int, client: GitHubClient
) -> dict[str, Any]:
    if not REPOSITORY_PATTERN.fullmatch(repository):
        raise CollectionFailure("repository must use owner/name form")
    if (
        not isinstance(issue_number, int)
        or isinstance(issue_number, bool)
        or issue_number <= 0
    ):
        raise CollectionFailure("issue number must be a positive integer")

    issue_path = f"/repos/{repository}/issues/{issue_number}"
    try:
        issue = _require_mapping(client.get(issue_path), "issue")
    except GitHubAPIError as exc:
        raise CollectionFailure(f"unable to resolve issue: {exc}") from exc
    if "pull_request" in issue:
        raise CollectionFailure(
            "target resolves to a pull request; primary issue inspection requires an issue"
        )

    number = issue.get("number")
    if number != issue_number:
        raise CollectionFailure("resolved issue number does not match requested issue")
    issue_url = _require_string(issue.get("html_url"), "issue html_url")
    title = _require_string(issue.get("title"), "issue title")
    observed_facts: list[dict[str, Any]] = [
        {
            "classification": "observed_fact",
            "kind": "issue",
            "number": issue_number,
            "url": issue_url,
            "title": title,
            "state": issue.get("state"),
            "author": _user_login(issue),
            "created_at": issue.get("created_at"),
            "updated_at": issue.get("updated_at"),
            "body": issue.get("body") if isinstance(issue.get("body"), str) else "",
            "source": _source_ref("issue", issue_number, issue_url),
        }
    ]
    warnings: list[dict[str, Any]] = []
    collection_complete = True

    try:
        raw_comments = client.get_paginated(
            f"/repos/{repository}/issues/{issue_number}/comments"
        )
        comments = [
            _comment_record(item)
            for item in raw_comments
            if isinstance(item, Mapping)
        ]
        if len(comments) != len(raw_comments):
            raise CollectionFailure("comment pagination contained a non-object item")
        comments.sort(key=_chronology_key)
        for record in comments:
            observed_facts.append(
                {
                    "classification": "observed_fact",
                    "kind": "issue_comment",
                    **record,
                }
            )
    except (GitHubAPIError, CollectionFailure) as exc:
        comments = []
        collection_complete = False
        if isinstance(exc, GitHubAPIError):
            message, source_url = exc.message, exc.endpoint
        else:
            message = str(exc)
            source_url = client.absolute_url(
                f"/repos/{repository}/issues/{issue_number}/comments"
            )
        warnings.append(
            {
                "code": "comments",
                "message": message,
                "source_url": source_url,
            }
        )

    lifecycle_records: list[dict[str, Any]] = []
    derived: list[dict[str, Any]] = []
    if comments:
        lifecycle_records = [
            {
                "classification": "observed_fact",
                "record_class": record["record_class"],
                "heading": record["first_h2"],
                "source": record["source"],
                "created_at": record["created_at"],
            }
            for record in comments
            if record.get("record_class") is not None
        ]
        supported_approvals, ambiguous_approvals = _verify_plan_approvals(comments)
        explicit_supersession, supersession_ambiguity = _supersession_observations(
            comments
        )
        derived.extend(supported_approvals)
        derived.extend(ambiguous_approvals)
        derived.extend(explicit_supersession)
        derived.extend(supersession_ambiguity)
        boundary = _recorded_next_boundary(issue, comments)
    elif collection_complete:
        boundary = _recorded_next_boundary(issue, [])
    else:
        lifecycle_records = [
            {
                "classification": "pending_or_unavailable",
                "record_class": "unavailable",
                "summary": "Lifecycle records were not classified because comment collection was incomplete.",
            }
        ]
        derived.append(
            {
                "classification": "pending_or_unavailable",
                "kind": "comment_dependent_observations",
                "summary": "Comment-dependent derived observations were suppressed because comment collection was incomplete.",
            }
        )
        boundary = {
            "classification": "pending_or_unavailable",
            "status": "unavailable",
            "summary": "Recorded next boundary is unavailable because comment collection was incomplete.",
        }

    related_pr, pr_warnings, pr_complete = _related_pr_report(
        repository, issue_number, client
    )
    warnings.extend(pr_warnings)
    collection_complete = collection_complete and pr_complete

    return {
        "target": {
            "repository": repository,
            "issue": issue_number,
            "url": issue_url,
        },
        "collection_status": "complete" if collection_complete else "incomplete",
        "observed_facts": observed_facts,
        "lifecycle_records": sorted(
            lifecycle_records,
            key=lambda item: (
                str(item.get("created_at", "")),
                str(item.get("source", {}).get("id", "")),
            ),
        ),
        "derived_observations": sorted(
            derived,
            key=lambda item: (
                str(item.get("classification", "")),
                str(item.get("kind", "")),
                str(item.get("source", {}).get("id", "")),
                str(item.get("summary", "")),
            ),
        ),
        "related_pull_request": related_pr,
        "recorded_next_boundary": boundary,
        "warnings_or_errors": sorted(
            warnings,
            key=lambda item: (
                str(item.get("code", "")),
                str(item.get("message", "")),
                str(item.get("source_url", "")),
            ),
        ),
        "authority_notice": AUTHORITY_NOTICE,
    }


def render_json(report: Mapping[str, Any]) -> str:
    return json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def _source_markdown(source: Any) -> str:
    if not isinstance(source, Mapping):
        return "source unavailable"
    url = source.get("url")
    identifier = source.get("id")
    kind = source.get("kind", "source")
    if isinstance(url, str):
        return f"[{kind} {identifier}]({url})"
    return f"{kind} {identifier}"


def render_markdown(report: Mapping[str, Any]) -> str:
    target = report["target"]
    lines = [
        "# IssueOps primary-record inspection",
        "",
        f"**Collection status:** `{report['collection_status']}`",
        "",
        "## Target",
        "",
        f"- Repository: `{target['repository']}`",
        f"- Issue: [#{target['issue']}]({target['url']})",
        "",
        "## Observed facts",
        "",
    ]
    for item in report["observed_facts"]:
        if item.get("kind") == "issue":
            lines.append(
                f"- Issue #{item['number']} is `{item.get('state')}`: {item.get('title')} "
                f"({_source_markdown(item.get('source'))})"
            )
        elif item.get("kind") == "issue_comment":
            lines.append(
                f"- Comment {item['id']} by `{item.get('author')}` at "
                f"`{item.get('created_at')}` ({_source_markdown(item.get('source'))})"
            )
    lines.extend(["", "## Lifecycle records", ""])
    if report["lifecycle_records"]:
        for item in report["lifecycle_records"]:
            if item.get("record_class") == "unavailable":
                lines.append(f"- **Pending / unavailable:** {item.get('summary')}")
            else:
                lines.append(
                    f"- `{item.get('record_class')}` — {item.get('heading')} "
                    f"({_source_markdown(item.get('source'))})"
                )
    else:
        lines.append("- No conventionally recognised lifecycle comments were observed.")

    lines.extend(["", "## Derived observations", ""])
    if report["derived_observations"]:
        for item in report["derived_observations"]:
            lines.append(
                f"- **{item.get('classification')}** — {item.get('summary')} "
                f"({_source_markdown(item.get('source')) if item.get('source') else 'no source'})"
            )
    else:
        lines.append("- No supported derived observations were emitted.")

    related = report["related_pull_request"]
    lines.extend(["", "## Related pull request", ""])
    lines.append(f"- **{related.get('classification')}** — {related.get('summary')}")
    if related.get("status") == "verified":
        pr = related["pull_request"]
        lines.append(
            f"- Verified PR: [#{pr['number']}]({pr['url']}) — state `{pr.get('state')}`, "
            f"draft `{pr.get('draft')}`, merged `{pr.get('merged')}`"
        )
        lines.append(
            f"- Base `{pr.get('base_ref')}` @ `{pr.get('base_sha')}`; "
            f"head `{pr.get('head_ref')}` @ `{pr.get('head_sha')}`"
        )
    elif related.get("candidate_numbers"):
        lines.append(
            "- Candidate PR numbers: "
            + ", ".join(f"#{number}" for number in related["candidate_numbers"])
        )

    boundary = report["recorded_next_boundary"]
    lines.extend(["", "## Recorded next boundary", ""])
    if boundary.get("status") == "recorded":
        lines.append(f"- {boundary.get('value')}")
        lines.append(f"- Source: {_source_markdown(boundary.get('source'))}")
    else:
        lines.append(
            f"- **{boundary.get('classification')}** — {boundary.get('summary')}"
        )

    lines.extend(["", "## Warnings or errors", ""])
    if report["warnings_or_errors"]:
        for warning in report["warnings_or_errors"]:
            lines.append(
                f"- `{warning.get('code')}`: {warning.get('message')} "
                f"({warning.get('source_url')})"
            )
    else:
        lines.append("- None.")

    lines.extend(
        [
            "",
            "## Authority notice",
            "",
            f"> {report['authority_notice']}",
            "",
        ]
    )
    return "\n".join(lines)


def _sanitise_report(report: dict[str, Any], token: str) -> dict[str, Any]:
    def clean(value: Any) -> Any:
        if isinstance(value, str):
            return sanitise(value, token)
        if isinstance(value, list):
            return [clean(item) for item in value]
        if isinstance(value, dict):
            return {key: clean(item) for key, item in value.items()}
        return value

    return clean(report)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", help="target repository in owner/name form")
    parser.add_argument("issue", type=int, help="positive issue number")
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        dest="output_format",
    )
    parser.add_argument(
        "--token-env",
        default="GITHUB_TOKEN",
        help="environment variable containing the GitHub token",
    )
    parser.add_argument(
        "--api-url",
        default=os.environ.get("GITHUB_API_URL", "https://api.github.com"),
    )
    args = parser.parse_args(argv)

    token = os.environ.get(args.token_env, "")
    if not token:
        print(
            f"Issue inspection failed: environment variable {args.token_env!r} is not set",
            file=sys.stderr,
        )
        return 1
    try:
        client = GitHubClient(token, api_url=args.api_url)
        report = collect_report(args.repository, args.issue, client)
        report = _sanitise_report(report, token)
    except (CollectionFailure, GitHubAPIError, ValueError) as exc:
        print(f"Issue inspection failed: {sanitise(str(exc), token)}", file=sys.stderr)
        return 1

    if args.output_format == "json":
        sys.stdout.write(render_json(report))
    else:
        sys.stdout.write(render_markdown(report))
    return 0 if report["collection_status"] == "complete" else 2


if __name__ == "__main__":
    raise SystemExit(main())
