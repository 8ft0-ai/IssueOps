from __future__ import annotations

import importlib.util
import inspect
import json
import os
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
from unittest import mock
from urllib.parse import parse_qs, urlparse

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
SPEC = importlib.util.spec_from_file_location(
    "inspect_issueops_issue", SCRIPTS / "inspect_issueops_issue.py"
)
assert SPEC and SPEC.loader
inspector = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = inspector
SPEC.loader.exec_module(inspector)

REPO = "8ft0-ai/IssueOps"
ISSUE = 185
TOKEN = "secret-test-token"


def issue_payload(*, body="## Current boundary\n\nThe exact next permitted action is:\n\n```text\npost the detailed implementation plan\n```", pr_shaped=False):
    payload = {
        "number": ISSUE,
        "html_url": f"https://github.com/{REPO}/issues/{ISSUE}",
        "title": "Inspector contract",
        "state": "open",
        "body": body,
        "created_at": "2026-08-12T07:21:17Z",
        "updated_at": "2026-08-12T07:40:55Z",
        "user": {"login": "8ft0-ai", "type": "User"},
    }
    if pr_shaped:
        payload["pull_request"] = {"url": "https://api.github.com/pr"}
    return payload


def comment_payload(
    comment_id,
    body,
    *,
    created_at,
    association="OWNER",
    user_type="User",
    author="8ft0-ai",
):
    return {
        "id": comment_id,
        "html_url": f"https://github.com/{REPO}/issues/{ISSUE}#issuecomment-{comment_id}",
        "body": body,
        "created_at": created_at,
        "updated_at": created_at,
        "author_association": association,
        "user": {"login": author, "type": user_type},
    }


def timeline_candidate(number):
    return {
        "event": "cross-referenced",
        "source": {
            "issue": {
                "number": number,
                "repository": {"full_name": REPO},
                "pull_request": {
                    "url": f"https://api.github.com/repos/{REPO}/pulls/{number}"
                },
            }
        },
    }


def pr_payload(number, body, *, state="open", draft=True):
    return {
        "number": number,
        "html_url": f"https://github.com/{REPO}/pull/{number}",
        "state": state,
        "draft": draft,
        "merged": False,
        "merged_at": None,
        "body": body,
        "base": {"ref": "main", "sha": "a" * 40},
        "head": {"ref": f"feature/{number}", "sha": "b" * 40},
    }


class FakeTransport:
    def __init__(
        self,
        *,
        issue=None,
        comment_pages=None,
        timeline_pages=None,
        prs=None,
        fail=None,
        error_message="temporary failure",
    ):
        self.issue = issue if issue is not None else issue_payload()
        self.comment_pages = comment_pages if comment_pages is not None else {1: []}
        self.timeline_pages = timeline_pages if timeline_pages is not None else {1: []}
        self.prs = prs or {}
        self.fail = fail or set()
        self.error_message = error_message
        self.urls = []
        self.headers = []

    def __call__(self, url, headers):
        self.urls.append(url)
        self.headers.append(dict(headers))
        self.assert_headers(headers)
        parsed = urlparse(url)
        path = parsed.path
        page = int(parse_qs(parsed.query).get("page", ["1"])[0])
        if (path, page) in self.fail or path in self.fail:
            raise inspector.GitHubAPIError(url, 503, self.error_message)
        if path == f"/repos/{REPO}/issues/{ISSUE}":
            return {}, self.issue
        if path == f"/repos/{REPO}/issues/{ISSUE}/comments":
            return {}, self.comment_pages.get(page, [])
        if path == f"/repos/{REPO}/issues/{ISSUE}/timeline":
            return {}, self.timeline_pages.get(page, [])
        prefix = f"/repos/{REPO}/pulls/"
        if path.startswith(prefix):
            number = int(path[len(prefix):])
            if number not in self.prs:
                raise inspector.GitHubAPIError(url, 404, "not found")
            return {}, self.prs[number]
        raise AssertionError(f"unexpected URL {url}")

    @staticmethod
    def assert_headers(headers):
        assert headers["Authorization"] == f"Bearer {TOKEN}"
        assert headers["Accept"] == "application/vnd.github+json"
        assert headers["X-GitHub-Api-Version"] == inspector.API_VERSION


def client(transport, *, max_pages=inspector.MAX_PAGES):
    return inspector.GitHubClient(TOKEN, transport=transport, max_pages=max_pages)


class InspectorTests(unittest.TestCase):
    def test_valid_lifecycle_and_owner_plan_approval(self):
        readiness = comment_payload(
            1001,
            "## Planning readiness\n\n- Decision: **Ready to implement.**",
            created_at="2026-08-12T07:30:00Z",
        )
        plan = comment_payload(
            1002,
            "## Detailed implementation plan — bounded inspector\n\nPlan.",
            created_at="2026-08-12T07:31:00Z",
        )
        approval = comment_payload(
            1003,
            "## Human implementation-plan approval\n\n"
            "I approve the detailed implementation plan recorded in issue comment `1002`.",
            created_at="2026-08-12T07:32:00Z",
        )
        transport = FakeTransport(comment_pages={1: [approval, readiness, plan]})
        report = inspector.collect_report(REPO, ISSUE, client(transport))
        self.assertEqual(report["collection_status"], "complete")
        self.assertEqual(
            [item["record_class"] for item in report["lifecycle_records"]],
            ["readiness", "implementation_plan", "human_plan_approval"],
        )
        approvals = [
            item
            for item in report["derived_observations"]
            if item.get("kind") == "plan_approval_record"
        ]
        self.assertEqual(len(approvals), 1)
        self.assertEqual(approvals[0]["classification"], "supported_derived_observation")
        self.assertEqual(approvals[0]["referenced_plan_comment"], 1002)

    def test_invalid_input_and_pr_shaped_primary_target(self):
        transport = FakeTransport()
        with self.assertRaisesRegex(inspector.CollectionFailure, "owner/name"):
            inspector.collect_report("bad repo", ISSUE, client(transport))
        with self.assertRaisesRegex(inspector.CollectionFailure, "positive"):
            inspector.collect_report(REPO, 0, client(transport))
        pr_transport = FakeTransport(issue=issue_payload(pr_shaped=True))
        with self.assertRaisesRegex(inspector.CollectionFailure, "pull request"):
            inspector.collect_report(REPO, ISSUE, client(pr_transport))

    def test_paginated_comments_have_deterministic_chronology(self):
        first_page = [
            comment_payload(
                2000 + index,
                "ordinary",
                created_at=f"2026-08-12T07:{59 - (index % 50):02d}:00Z",
            )
            for index in range(100)
        ]
        last = comment_payload(
            1500, "ordinary", created_at="2026-08-12T06:00:00Z"
        )
        transport = FakeTransport(comment_pages={1: first_page, 2: [last]})
        report = inspector.collect_report(REPO, ISSUE, client(transport))
        comments = [
            item for item in report["observed_facts"] if item.get("kind") == "issue_comment"
        ]
        self.assertEqual(len(comments), 101)
        keys = [(item["created_at"], item["id"]) for item in comments]
        self.assertEqual(keys, sorted(keys))
        comment_urls = [url for url in transport.urls if "/comments?" in url]
        self.assertEqual(len(comment_urls), 2)

    def test_free_form_prose_is_not_lifecycle_authority(self):
        freeform = comment_payload(
            3001,
            "This seems ready and I approve the plan, but this is just prose.",
            created_at="2026-08-12T07:30:00Z",
        )
        transport = FakeTransport(comment_pages={1: [freeform]})
        report = inspector.collect_report(REPO, ISSUE, client(transport))
        self.assertEqual(report["lifecycle_records"], [])
        self.assertFalse(
            any(
                item.get("kind") == "plan_approval_record"
                for item in report["derived_observations"]
            )
        )

    def test_approval_shaped_failures_remain_ambiguous(self):
        plan = comment_payload(
            4001,
            "## Detailed implementation plan\n\nPlan.",
            created_at="2026-08-12T07:31:00Z",
        )
        cases = [
            comment_payload(
                4002,
                "## Human implementation-plan approval\n\n"
                "I approve the detailed implementation plan recorded in issue comment `4001`.",
                created_at="2026-08-12T07:32:00Z",
                association="MEMBER",
            ),
            comment_payload(
                4003,
                "## Human implementation-plan approval\n\nI approve something.",
                created_at="2026-08-12T07:33:00Z",
            ),
            comment_payload(
                4004,
                "## Human implementation-plan approval\n\n"
                "I approve the detailed implementation plan recorded in issue comment `9999`.",
                created_at="2026-08-12T07:34:00Z",
            ),
            comment_payload(
                4005,
                "## Human implementation-plan approval\n\n"
                "I approve the detailed implementation plan recorded in issue comment `4001`.\n"
                "I approve the detailed implementation plan recorded in issue comment `4001`.",
                created_at="2026-08-12T07:35:00Z",
            ),
        ]
        transport = FakeTransport(comment_pages={1: [plan, *cases]})
        report = inspector.collect_report(REPO, ISSUE, client(transport))
        approvals = [
            item
            for item in report["derived_observations"]
            if item.get("kind") == "plan_approval_record"
        ]
        self.assertEqual(len(approvals), 4)
        self.assertTrue(
            all(item["classification"] == "ambiguous_or_unsupported" for item in approvals)
        )

    def test_approval_reference_ignores_ineligible_markdown_regions(self):
        plan = comment_payload(
            4201,
            "## Detailed implementation plan\n\nPlan.",
            created_at="2026-08-12T07:31:00Z",
        )
        approval_sentence = (
            "I approve the detailed implementation plan recorded in issue comment `4201`."
        )
        hidden_regions = {
            "fenced": f"```text\n{approval_sentence}\n```",
            "html_comment": f"<!--\n{approval_sentence}\n-->",
            "indented": f"    {approval_sentence}",
        }
        for offset, (name, hidden) in enumerate(hidden_regions.items(), start=1):
            with self.subTest(region=name):
                approval = comment_payload(
                    4201 + offset,
                    "## Human implementation-plan approval\n\n" + hidden,
                    created_at=f"2026-08-12T07:32:0{offset}Z",
                )
                transport = FakeTransport(
                    issue=issue_payload(body="No explicit boundary."),
                    comment_pages={1: [plan, approval]},
                )
                report = inspector.collect_report(REPO, ISSUE, client(transport))
                item = next(
                    item
                    for item in report["derived_observations"]
                    if item.get("kind") == "plan_approval_record"
                )
                self.assertEqual(item["classification"], "ambiguous_or_unsupported")
                self.assertNotIn("referenced_plan_comment", item)

    def test_wrong_chronology_approval_is_ambiguous(self):
        approval = comment_payload(
            4101,
            "## Human implementation-plan approval\n\n"
            "I approve the detailed implementation plan recorded in issue comment `4102`.",
            created_at="2026-08-12T07:31:00Z",
        )
        plan = comment_payload(
            4102,
            "## Detailed implementation plan\n\nPlan.",
            created_at="2026-08-12T07:32:00Z",
        )
        report = inspector.collect_report(
            REPO, ISSUE, client(FakeTransport(comment_pages={1: [approval, plan]}))
        )
        approval_item = next(
            item
            for item in report["derived_observations"]
            if item.get("kind") == "plan_approval_record"
        )
        self.assertIn("does not predate", " ".join(approval_item["reasons"]))

    def test_explicit_next_boundary_and_provenance(self):
        boundary = comment_payload(
            5001,
            "## Detailed implementation plan\n\n"
            "### Work\n\nSomething.\n\n"
            "## Exact next permitted action\n\n```text\nhuman review of this plan\n```",
            created_at="2026-08-12T07:50:00Z",
        )
        report = inspector.collect_report(
            REPO, ISSUE, client(FakeTransport(comment_pages={1: [boundary]}))
        )
        found = report["recorded_next_boundary"]
        self.assertEqual(found["status"], "recorded")
        self.assertEqual(found["value"], "human review of this plan")
        self.assertEqual(found["source"]["id"], 5001)

    def test_multiple_boundaries_in_latest_source_are_ambiguous(self):
        boundary = comment_payload(
            5101,
            "## Detailed implementation plan\n\n"
            "The next permitted action is first action\n\n"
            "## Next owner decision\n\nsecond action",
            created_at="2026-08-12T07:50:00Z",
        )
        report = inspector.collect_report(
            REPO, ISSUE, client(FakeTransport(comment_pages={1: [boundary]}))
        )
        self.assertEqual(report["recorded_next_boundary"]["status"], "ambiguous")
        self.assertEqual(len(report["recorded_next_boundary"]["candidates"]), 2)

    def test_boundary_triggers_ignore_ineligible_markdown_regions(self):
        hidden_regions = {
            "fenced": "```text\nThe next permitted action is ship it\n```",
            "html_comment": "<!--\nThe exact next permitted action is: ship it\n-->",
            "indented": "    The next permitted action is ship it",
        }
        for offset, (name, hidden) in enumerate(hidden_regions.items(), start=1):
            with self.subTest(region=name):
                boundary = comment_payload(
                    5200 + offset,
                    "## Planning readiness\n\nReady.\n\n" + hidden,
                    created_at=f"2026-08-12T07:50:0{offset}Z",
                )
                transport = FakeTransport(
                    issue=issue_payload(body="No explicit boundary."),
                    comment_pages={1: [boundary]},
                )
                report = inspector.collect_report(REPO, ISSUE, client(transport))
                self.assertEqual(
                    report["recorded_next_boundary"]["status"], "not_recorded"
                )

        issue_boundary = issue_payload(
            body=(
                "## Current boundary\n\n"
                "```text\nThe exact next permitted action is:\nship it\n```"
            )
        )
        report = inspector.collect_report(
            REPO, ISSUE, client(FakeTransport(issue=issue_boundary))
        )
        self.assertEqual(report["recorded_next_boundary"]["status"], "not_recorded")

    def test_supersession_is_explicit_not_chronology_only(self):
        old = comment_payload(
            6001,
            "## Planning readiness\n\nReady.",
            created_at="2026-08-12T07:30:00Z",
        )
        newer = comment_payload(
            6002,
            "## Planning readiness\n\nNewer, but no supersession.",
            created_at="2026-08-12T07:31:00Z",
        )
        report = inspector.collect_report(
            REPO, ISSUE, client(FakeTransport(comment_pages={1: [old, newer]}))
        )
        self.assertFalse(
            any(item.get("kind") == "explicit_supersession" for item in report["derived_observations"])
        )
        superseding = comment_payload(
            6003,
            "## Planning readiness\n\nsupersedes issue comment 6001",
            created_at="2026-08-12T07:32:00Z",
        )
        report2 = inspector.collect_report(
            REPO,
            ISSUE,
            client(FakeTransport(comment_pages={1: [old, newer, superseding]})),
        )
        item = next(
            item
            for item in report2["derived_observations"]
            if item.get("kind") == "explicit_supersession"
        )
        self.assertEqual(item["source"]["id"], 6001)

    def test_supersession_ignores_ineligible_markdown_regions(self):
        old = comment_payload(
            6201,
            "## Planning readiness\n\nReady.",
            created_at="2026-08-12T07:30:00Z",
        )
        supersession_sentence = "supersedes issue comment 6201"
        hidden_regions = {
            "fenced": f"```text\n{supersession_sentence}\n```",
            "html_comment": f"<!--\n{supersession_sentence}\n-->",
            "indented": f"    {supersession_sentence}",
        }
        for offset, (name, hidden) in enumerate(hidden_regions.items(), start=1):
            with self.subTest(region=name):
                newer = comment_payload(
                    6201 + offset,
                    "## Planning readiness\n\nNewer.\n\n" + hidden,
                    created_at=f"2026-08-12T07:31:0{offset}Z",
                )
                transport = FakeTransport(
                    issue=issue_payload(body="No explicit boundary."),
                    comment_pages={1: [old, newer]},
                )
                report = inspector.collect_report(REPO, ISSUE, client(transport))
                self.assertFalse(
                    any(
                        item.get("kind") in {"explicit_supersession", "supersession"}
                        for item in report["derived_observations"]
                    )
                )

    def test_zero_verified_related_prs_is_observed_absence(self):
        report = inspector.collect_report(REPO, ISSUE, client(FakeTransport()))
        related = report["related_pull_request"]
        self.assertEqual(related["status"], "absent")
        self.assertEqual(related["classification"], "observed_fact")

    def test_one_canonical_related_pr_is_verified(self):
        number = 701
        body = f"## Execution contract\n\nIssue #{ISSUE}\n"
        transport = FakeTransport(
            timeline_pages={1: [timeline_candidate(number)]},
            prs={number: pr_payload(number, body)},
        )
        report = inspector.collect_report(REPO, ISSUE, client(transport))
        related = report["related_pull_request"]
        self.assertEqual(related["status"], "verified")
        self.assertEqual(related["pull_request"]["number"], number)
        self.assertEqual(related["pull_request"]["linkage_method"], "canonical")

    def test_legacy_closing_reference_is_verified(self):
        number = 702
        transport = FakeTransport(
            timeline_pages={1: [timeline_candidate(number)]},
            prs={number: pr_payload(number, f"Fixes #{ISSUE}")},
        )
        report = inspector.collect_report(REPO, ISSUE, client(transport))
        self.assertEqual(report["related_pull_request"]["status"], "verified")
        self.assertEqual(
            report["related_pull_request"]["pull_request"]["linkage_method"],
            "legacy-closing-keyword",
        )

    def test_cross_reference_that_only_mentions_issue_is_not_verified(self):
        number = 703
        transport = FakeTransport(
            timeline_pages={1: [timeline_candidate(number)]},
            prs={number: pr_payload(number, f"Discusses issue #{ISSUE}")},
        )
        report = inspector.collect_report(REPO, ISSUE, client(transport))
        self.assertEqual(report["related_pull_request"]["status"], "absent")
        self.assertEqual(report["related_pull_request"]["candidate_numbers"], [number])

    def test_multiple_verified_and_conflicting_prs_are_ambiguous(self):
        first, second = 704, 705
        transport = FakeTransport(
            timeline_pages={1: [timeline_candidate(first), timeline_candidate(second)]},
            prs={
                first: pr_payload(first, f"## Execution contract\n\nIssue #{ISSUE}"),
                second: pr_payload(second, f"## Execution contract\n\nIssue #{ISSUE}"),
            },
        )
        report = inspector.collect_report(REPO, ISSUE, client(transport))
        self.assertEqual(report["related_pull_request"]["status"], "ambiguous")
        conflict_number = 706
        conflict_transport = FakeTransport(
            timeline_pages={1: [timeline_candidate(conflict_number)]},
            prs={
                conflict_number: pr_payload(
                    conflict_number,
                    f"## Execution contract\n\nIssue #{ISSUE}\n\nFixes #999",
                )
            },
        )
        conflict_report = inspector.collect_report(
            REPO, ISSUE, client(conflict_transport)
        )
        self.assertEqual(conflict_report["related_pull_request"]["status"], "ambiguous")

    def test_comment_pagination_failure_suppresses_comment_dependent_conclusions(self):
        page = [
            comment_payload(
                8000 + index,
                "## Planning readiness\n\nReady.",
                created_at=f"2026-08-12T07:{index % 60:02d}:00Z",
            )
            for index in range(100)
        ]
        path = f"/repos/{REPO}/issues/{ISSUE}/comments"
        transport = FakeTransport(
            comment_pages={1: page},
            fail={(path, 2)},
        )
        report = inspector.collect_report(REPO, ISSUE, client(transport))
        self.assertEqual(report["collection_status"], "incomplete")
        self.assertEqual(
            report["recorded_next_boundary"]["status"], "unavailable"
        )
        self.assertEqual(report["lifecycle_records"][0]["record_class"], "unavailable")
        self.assertFalse(
            any(
                item.get("kind") == "plan_approval_record"
                for item in report["derived_observations"]
            )
        )

    def test_timeline_or_pr_failure_is_unavailable_without_corrupting_issue_facts(self):
        timeline_path = f"/repos/{REPO}/issues/{ISSUE}/timeline"
        timeline_fail = FakeTransport(fail={timeline_path})
        report = inspector.collect_report(REPO, ISSUE, client(timeline_fail))
        self.assertEqual(report["collection_status"], "incomplete")
        self.assertEqual(report["related_pull_request"]["status"], "unavailable")
        self.assertEqual(report["observed_facts"][0]["kind"], "issue")

        number = 900
        pr_fail = FakeTransport(
            timeline_pages={1: [timeline_candidate(number)]},
            fail={f"/repos/{REPO}/pulls/{number}"},
        )
        report2 = inspector.collect_report(REPO, ISSUE, client(pr_fail))
        self.assertEqual(report2["related_pull_request"]["status"], "unavailable")
        self.assertEqual(report2["observed_facts"][0]["number"], ISSUE)

    def test_invalid_authentication_or_inaccessible_target_fails_before_report(self):
        path = f"/repos/{REPO}/issues/{ISSUE}"
        transport = FakeTransport(fail={path}, error_message="Bad credentials")
        with self.assertRaisesRegex(inspector.CollectionFailure, "unable to resolve issue"):
            inspector.collect_report(REPO, ISSUE, client(transport))

    def test_token_sanitisation_and_renderer_absence(self):
        timeline_path = f"/repos/{REPO}/issues/{ISSUE}/timeline"
        transport = FakeTransport(
            fail={timeline_path}, error_message=f"failure leaked {TOKEN}"
        )
        report = inspector.collect_report(REPO, ISSUE, client(transport))
        clean = inspector._sanitise_report(report, TOKEN)
        markdown = inspector.render_markdown(clean)
        json_text = inspector.render_json(clean)
        self.assertNotIn(TOKEN, markdown)
        self.assertNotIn(TOKEN, json_text)
        self.assertIn("[REDACTED]", markdown)
        self.assertIn("[REDACTED]", json_text)

    def test_deterministic_markdown_and_json(self):
        plan = comment_payload(
            10001,
            "## Detailed implementation plan\n\nPlan.",
            created_at="2026-08-12T07:31:00Z",
        )
        transport = FakeTransport(comment_pages={1: [plan]})
        report = inspector.collect_report(REPO, ISSUE, client(transport))
        self.assertEqual(
            inspector.render_markdown(report), inspector.render_markdown(report)
        )
        self.assertEqual(inspector.render_json(report), inspector.render_json(report))
        parsed = json.loads(inspector.render_json(report))
        self.assertEqual(parsed["target"]["issue"], ISSUE)
        self.assertNotIn("generated_at", parsed)

    def test_cli_missing_token_is_sanitised_failure(self):
        stderr = StringIO()
        with mock.patch.dict(os.environ, {}, clear=True), redirect_stderr(stderr):
            result = inspector.main([REPO, str(ISSUE), "--token-env", "MISSING_TOKEN"])
        self.assertEqual(result, 1)
        self.assertIn("MISSING_TOKEN", stderr.getvalue())

    def test_production_transport_is_get_only_and_no_write_endpoint_exists(self):
        source = inspect.getsource(inspector.GitHubClient._urllib_transport)
        self.assertIn('method="GET"', source)
        for method in ("POST", "PUT", "PATCH", "DELETE"):
            self.assertNotIn(f'method="{method}"', source)
        module_source = Path(inspector.__file__).read_text(encoding="utf-8")
        self.assertNotIn("urllib.request.Request(url, data=", module_source)
        self.assertNotRegex(
            module_source,
            r"/(?:issues|pulls|git|contents|actions)[^\"']*(?:comments|merge|reviews)[^\"']*\"\s*,\s*method=",
        )


if __name__ == "__main__":
    unittest.main()
