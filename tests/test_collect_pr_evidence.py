from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlparse

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
SPEC = importlib.util.spec_from_file_location("collect_pr_evidence", SCRIPTS / "collect_pr_evidence.py")
assert SPEC and SPEC.loader
collector = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = collector
SPEC.loader.exec_module(collector)

REPO = "8ft0-ai/IssueOps"
PR = 81
HEAD = "a" * 40
NEW_HEAD = "b" * 40


def pr_payload(body="Closes #80", head=HEAD):
    return {
        "html_url": f"https://github.com/{REPO}/pull/{PR}",
        "title": "Collector test",
        "state": "open",
        "draft": False,
        "updated_at": "2026-07-11T08:00:00Z",
        "body": body,
        "user": {"login": "8ft0-ai"},
        "base": {"ref": "main"},
        "head": {"sha": head},
    }


def issue_payload():
    return {
        "html_url": f"https://github.com/{REPO}/issues/80",
        "title": "Execution contract",
        "state": "open",
        "updated_at": "2026-07-11T07:00:00Z",
        "body": "Contract body",
    }


class FakeTransport:
    def __init__(self, *, body="Closes #80", final_head=HEAD, pending=False, fail_path=None, empty=False):
        self.body = body
        self.final_head = final_head
        self.pending = pending
        self.fail_path = fail_path
        self.empty = empty
        self.urls = []
        self.pr_calls = 0

    def __call__(self, url, headers):
        self.urls.append(url)
        self.assert_headers(headers)
        parsed = urlparse(url)
        path = parsed.path
        query = parse_qs(parsed.query)
        if self.fail_path and path == self.fail_path:
            raise collector.GitHubAPIError(url, 503, "temporary failure")
        if path == f"/repos/{REPO}/pulls/{PR}":
            self.pr_calls += 1
            return {}, pr_payload(self.body, HEAD if self.pr_calls == 1 else self.final_head)
        if path == f"/repos/{REPO}/issues/80":
            return {}, issue_payload()
        if path == f"/repos/{REPO}/pulls/{PR}/files":
            page = int(query["page"][0])
            if page == 1:
                size = 0 if self.empty else 100
                return {}, [
                    {"filename": f"file-{i:03d}.txt", "additions": 1, "deletions": 0}
                    for i in range(size)
                ]
            if page == 2 and not self.empty:
                return {}, [{"filename": "last.txt", "additions": 2, "deletions": 1}]
            return {}, []
        if path == f"/repos/{REPO}/issues/{PR}/comments":
            return {}, []
        if path == f"/repos/{REPO}/pulls/{PR}/reviews":
            return {}, []
        if path == f"/repos/{REPO}/commits/{HEAD}/check-runs":
            checks = [] if self.empty else [{
                "id": 1,
                "name": "tests",
                "status": "in_progress" if self.pending else "completed",
                "conclusion": None if self.pending else "success",
                "html_url": f"https://github.com/{REPO}/runs/1",
                "started_at": "2026-07-11T08:00:01Z",
                "completed_at": None if self.pending else "2026-07-11T08:00:02Z",
            }]
            return {}, {"total_count": len(checks), "check_runs": checks}
        if path == f"/repos/{REPO}/actions/runs":
            runs = [] if self.empty else [{
                "id": 2,
                "name": "CI",
                "event": "pull_request",
                "run_number": 1,
                "status": "completed",
                "conclusion": "failure",
                "html_url": f"https://github.com/{REPO}/actions/runs/2",
                "updated_at": "2026-07-11T08:00:03Z",
            }]
            return {}, {"total_count": len(runs), "workflow_runs": runs}
        if path == f"/repos/{REPO}/actions/runs/2/jobs":
            jobs = [{"id": 3, "name": "build", "status": "completed", "conclusion": "failure"}]
            return {}, {"total_count": 1, "jobs": jobs}
        raise AssertionError(f"unexpected URL: {url}")

    @staticmethod
    def assert_headers(headers):
        assert headers["Authorization"] == "Bearer secret-token"
        assert headers["Accept"] == "application/vnd.github+json"


class CollectorTests(unittest.TestCase):
    def client(self, transport, max_pages=20):
        return collector.GitHubClient("secret-token", transport=transport, max_pages=max_pages)

    def clock(self):
        values = iter(["2026-07-11T08:00:00Z", "2026-07-11T08:00:05Z"])
        return lambda: next(values)

    def test_stable_collection_follows_pagination_and_reports_failed_checks_as_facts(self):
        transport = FakeTransport()
        report = collector.collect_report(REPO, PR, self.client(transport), clock=self.clock())
        self.assertEqual("complete", report.status.value)
        mapping = report.to_mapping()
        changed = next(item for item in mapping["evidence"] if item["id"] == "pr.changed-files")
        self.assertEqual(101, changed["details"]["count"])
        workflow = next(item for item in mapping["evidence"] if item["id"] == "workflow.2")
        self.assertEqual("repository-observed", workflow["classification"])
        self.assertEqual("failure", workflow["details"]["conclusion"])
        self.assertTrue(all(url.startswith("https://api.github.com/") for url in transport.urls))

    def test_pending_check_is_incomplete(self):
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(pending=True)), clock=self.clock())
        self.assertEqual("incomplete", report.status.value)
        self.assertTrue(any(item["classification"] == "pending" for item in report.to_mapping()["evidence"]))

    def test_validly_empty_surfaces_are_observed_absence(self):
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(empty=True)), clock=self.clock())
        self.assertEqual("complete", report.status.value)
        ids = {item["id"] for item in report.to_mapping()["evidence"]}
        self.assertIn("checks.absent", ids)
        self.assertIn("workflows.absent", ids)
        self.assertFalse(report.to_mapping()["errors"])

    def test_partial_api_failure_is_non_complete_with_sanitised_error(self):
        path = f"/repos/{REPO}/pulls/{PR}/reviews"
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(fail_path=path)), clock=self.clock())
        self.assertEqual("incomplete", report.status.value)
        self.assertEqual("pr.reviews", report.to_mapping()["errors"][0]["code"])
        self.assertNotIn("secret-token", str(report.to_mapping()["errors"]))

    def test_unresolved_target_fails_before_report_construction(self):
        class FailingTransport:
            def __call__(self, url, headers):
                raise collector.GitHubAPIError(url, 401, "Bad credentials")
        with self.assertRaisesRegex(collector.CollectionFailure, "unable to resolve pull request"):
            collector.collect_report(REPO, PR, self.client(FailingTransport()), clock=self.clock())

    def test_multiple_closing_references_are_conflicting(self):
        report = collector.collect_report(
            REPO,
            PR,
            self.client(FakeTransport(body="Closes #80 and fixes #81")),
            clock=self.clock(),
        )
        self.assertEqual("conflicting", report.status.value)
        conflict = next(item for item in report.to_mapping()["evidence"] if item["id"] == "issue.linkage")
        self.assertEqual([80, 81], conflict["details"]["issue_numbers"])
        self.assertNotIn("linked_issue", report.to_mapping()["target"])

    def test_moving_head_is_stale(self):
        report = collector.collect_report(
            REPO, PR, self.client(FakeTransport(final_head=NEW_HEAD)), clock=self.clock()
        )
        self.assertEqual("stale", report.status.value)

    def test_excessive_pagination_fails_closed(self):
        class EndlessFiles(FakeTransport):
            def __call__(self, url, headers):
                parsed = urlparse(url)
                if parsed.path == f"/repos/{REPO}/pulls/{PR}/files":
                    self.urls.append(url)
                    self.assert_headers(headers)
                    return {}, [
                        {"filename": f"file-{i}.txt", "additions": 1, "deletions": 0}
                        for i in range(100)
                    ]
                return super().__call__(url, headers)
        report = collector.collect_report(REPO, PR, self.client(EndlessFiles(), max_pages=2), clock=self.clock())
        self.assertEqual("incomplete", report.status.value)
        self.assertTrue(any(error["code"] == "pr.files" for error in report.to_mapping()["errors"]))

    def test_write_report_creates_only_local_json_and_markdown(self):
        report = collector.collect_report(REPO, PR, self.client(FakeTransport()), clock=self.clock())
        with tempfile.TemporaryDirectory() as temp:
            collector.write_report(report, Path(temp))
            self.assertEqual({"evidence-pack.json", "evidence-pack.md"}, {p.name for p in Path(temp).iterdir()})


if __name__ == "__main__":
    unittest.main()
