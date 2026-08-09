from __future__ import annotations

import importlib.util
import json
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
CANONICAL_BODY = "## Execution contract\n\nIssue #80"


def pr_payload(body=CANONICAL_BODY, head=HEAD):
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


def review_thread_page(*, resolved=(), total_count=None, has_next=False, end_cursor=None):
    nodes = [{"isResolved": value} for value in resolved]
    return {
        "totalCount": len(nodes) if total_count is None else total_count,
        "pageInfo": {"hasNextPage": has_next, "endCursor": end_cursor},
        "nodes": nodes,
    }


class FakeTransport:
    def __init__(self, *, body=CANONICAL_BODY, final_head=HEAD, pending=False, fail_path=None, empty=False):
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


class FakeGraphQLTransport:
    def __init__(self, *, pages=None, payload=None, error=None):
        self.pages = pages if pages is not None else [review_thread_page(resolved=())]
        self.payload = payload
        self.error = error
        self.calls = []

    def __call__(self, url, headers, body):
        assert url == "https://api.github.com/graphql"
        assert headers["Authorization"] == "Bearer secret-token"
        assert headers["Accept"] == "application/vnd.github+json"
        assert headers["Content-Type"] == "application/json"
        request = json.loads(body.decode("utf-8"))
        self.calls.append(request)
        if self.error is not None:
            raise self.error
        if self.payload is not None:
            return {}, self.payload
        index = len(self.calls) - 1
        if index >= len(self.pages):
            raise AssertionError("unexpected GraphQL page request")
        return {}, {
            "data": {
                "repository": {
                    "pullRequest": {
                        "reviewThreads": self.pages[index],
                    }
                }
            }
        }


class CollectorTests(unittest.TestCase):
    def client(self, transport, max_pages=20, graphql_transport=None):
        return collector.GitHubClient(
            "secret-token",
            transport=transport,
            max_pages=max_pages,
            graphql_transport=graphql_transport or FakeGraphQLTransport(),
        )

    def clock(self):
        values = iter(["2026-07-11T08:00:00Z", "2026-07-11T08:00:05Z"])
        return lambda: next(values)

    @staticmethod
    def linkage(mapping):
        return next(item for item in mapping["evidence"] if item["id"] == "issue.linkage")

    @staticmethod
    def review_threads(mapping):
        return next(item for item in mapping["evidence"] if item["id"] == "pr.review-threads")

    def test_stable_collection_follows_pagination_and_reports_failed_checks_as_facts(self):
        transport = FakeTransport()
        report = collector.collect_report(REPO, PR, self.client(transport), clock=self.clock())
        self.assertEqual("complete", report.status.value)
        mapping = report.to_mapping()
        self.assertEqual(80, mapping["target"]["linked_issue"])
        self.assertEqual("canonical", self.linkage(mapping)["details"]["method"])
        changed = next(item for item in mapping["evidence"] if item["id"] == "pr.changed-files")
        self.assertEqual(101, changed["details"]["count"])
        workflow = next(item for item in mapping["evidence"] if item["id"] == "workflow.2")
        self.assertEqual("repository-observed", workflow["classification"])
        self.assertEqual("failure", workflow["details"]["conclusion"])
        threads = self.review_threads(mapping)
        self.assertEqual(0, threads["details"]["total_threads"])
        self.assertTrue(threads["details"]["complete"])
        self.assertTrue(all(url.startswith("https://api.github.com/") for url in transport.urls))

    def test_legacy_single_closing_reference_remains_supported(self):
        report = collector.collect_report(
            REPO, PR, self.client(FakeTransport(body="Closes #80")), clock=self.clock()
        )
        mapping = report.to_mapping()
        self.assertEqual("complete", report.status.value)
        self.assertEqual(80, mapping["target"]["linked_issue"])
        linkage = self.linkage(mapping)
        self.assertEqual("legacy-closing-keyword", linkage["details"]["method"])
        self.assertEqual([80], linkage["details"]["closing_issue_numbers"])

    def test_matching_canonical_and_closing_reference_use_canonical_linkage(self):
        body = "## Execution contract\n\nIssue #80\n\nCloses #80"
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(body=body)), clock=self.clock())
        mapping = report.to_mapping()
        self.assertEqual("complete", report.status.value)
        self.assertEqual(80, mapping["target"]["linked_issue"])
        linkage = self.linkage(mapping)
        self.assertEqual("canonical", linkage["details"]["method"])
        self.assertEqual([80], linkage["details"]["canonical_issue_numbers"])
        self.assertEqual([80], linkage["details"]["closing_issue_numbers"])

    def test_canonical_and_closing_disagreement_is_conflicting(self):
        body = "## Execution contract\n\nIssue #80\n\nCloses #81"
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(body=body)), clock=self.clock())
        mapping = report.to_mapping()
        self.assertEqual("conflicting", report.status.value)
        linkage = self.linkage(mapping)
        self.assertEqual("conflicting", linkage["classification"])
        self.assertEqual([80], linkage["details"]["canonical_issue_numbers"])
        self.assertEqual([81], linkage["details"]["closing_issue_numbers"])
        self.assertNotIn("linked_issue", mapping["target"])

    def test_multiple_canonical_declarations_are_conflicting(self):
        body = "## Execution contract\n\nIssue #80\nIssue #81"
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(body=body)), clock=self.clock())
        mapping = report.to_mapping()
        self.assertEqual("conflicting", report.status.value)
        self.assertEqual([80, 81], self.linkage(mapping)["details"]["canonical_issue_numbers"])
        self.assertNotIn("linked_issue", mapping["target"])

    def test_duplicate_execution_contract_sections_are_conflicting(self):
        body = "## Execution contract\n\nIssue #80\n\n## Evidence pack\n\n...\n\n## Execution contract\n\nIssue #80"
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(body=body)), clock=self.clock())
        mapping = report.to_mapping()
        self.assertEqual("conflicting", report.status.value)
        self.assertEqual(2, self.linkage(mapping)["details"]["section_count"])
        self.assertNotIn("linked_issue", mapping["target"])

    def test_malformed_canonical_declaration_is_conflicting(self):
        body = "## Execution contract\n\nIssue #not-a-number"
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(body=body)), clock=self.clock())
        mapping = report.to_mapping()
        self.assertEqual("conflicting", report.status.value)
        self.assertEqual(1, self.linkage(mapping)["details"]["malformed_declaration_count"])
        self.assertNotIn("linked_issue", mapping["target"])

    def test_fenced_canonical_example_is_not_linkage(self):
        body = "```md\n## Execution contract\n\nIssue #80\n```"
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(body=body)), clock=self.clock())
        mapping = report.to_mapping()
        self.assertEqual("incomplete", report.status.value)
        linkage = self.linkage(mapping)
        self.assertEqual("unavailable", linkage["classification"])
        self.assertEqual(0, linkage["details"]["section_count"])
        self.assertNotIn("linked_issue", mapping["target"])

    def test_html_commented_canonical_example_is_not_linkage(self):
        body = "<!--\n## Execution contract\n\nIssue #80\n-->"
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(body=body)), clock=self.clock())
        mapping = report.to_mapping()
        self.assertEqual("incomplete", report.status.value)
        linkage = self.linkage(mapping)
        self.assertEqual("unavailable", linkage["classification"])
        self.assertEqual(0, linkage["details"]["section_count"])
        self.assertNotIn("linked_issue", mapping["target"])

    def test_indented_canonical_example_is_not_linkage(self):
        body = "    ## Execution contract\n\n    Issue #80"
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(body=body)), clock=self.clock())
        mapping = report.to_mapping()
        self.assertEqual("incomplete", report.status.value)
        linkage = self.linkage(mapping)
        self.assertEqual("unavailable", linkage["classification"])
        self.assertEqual(0, linkage["details"]["section_count"])
        self.assertNotIn("linked_issue", mapping["target"])

    def test_tab_and_mixed_indented_canonical_examples_are_not_linkage(self):
        for indent in ("\t", " \t", "  \t", "   \t", "\t "):
            with self.subTest(indent=repr(indent)):
                body = f"{indent}## Execution contract\n\n{indent}Issue #80"
                report = collector.collect_report(
                    REPO, PR, self.client(FakeTransport(body=body)), clock=self.clock()
                )
                mapping = report.to_mapping()
                self.assertEqual("incomplete", report.status.value)
                linkage = self.linkage(mapping)
                self.assertEqual("unavailable", linkage["classification"])
                self.assertEqual(0, linkage["details"]["section_count"])
                self.assertNotIn("linked_issue", mapping["target"])

    def test_mixed_indented_example_does_not_conflict_with_real_canonical_linkage(self):
        body = CANONICAL_BODY + "\n\n \tIssue #81"
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(body=body)), clock=self.clock())
        mapping = report.to_mapping()
        self.assertEqual("complete", report.status.value)
        self.assertEqual(80, mapping["target"]["linked_issue"])
        linkage = self.linkage(mapping)
        self.assertEqual("canonical", linkage["details"]["method"])
        self.assertEqual([80], linkage["details"]["canonical_issue_numbers"])

    def test_three_space_markdown_indentation_remains_parseable(self):
        body = "   ## Execution contract\n\n   Issue #80"
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(body=body)), clock=self.clock())
        mapping = report.to_mapping()
        self.assertEqual("complete", report.status.value)
        self.assertEqual(80, mapping["target"]["linked_issue"])
        self.assertEqual("canonical", self.linkage(mapping)["details"]["method"])

    def test_fenced_example_does_not_conflict_with_real_canonical_linkage(self):
        body = CANONICAL_BODY + "\n\n~~~md\n## Execution contract\n\nIssue #81\n~~~"
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(body=body)), clock=self.clock())
        mapping = report.to_mapping()
        self.assertEqual("complete", report.status.value)
        self.assertEqual(80, mapping["target"]["linked_issue"])
        linkage = self.linkage(mapping)
        self.assertEqual("canonical", linkage["details"]["method"])
        self.assertEqual(1, linkage["details"]["section_count"])
        self.assertEqual([80], linkage["details"]["canonical_issue_numbers"])

    def test_missing_linkage_is_unavailable_and_incomplete(self):
        body = "## Evidence pack\n\nNo execution contract yet."
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(body=body)), clock=self.clock())
        mapping = report.to_mapping()
        self.assertEqual("incomplete", report.status.value)
        self.assertEqual("unavailable", self.linkage(mapping)["classification"])
        self.assertNotIn("linked_issue", mapping["target"])

    def test_pending_check_is_incomplete(self):
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(pending=True)), clock=self.clock())
        self.assertEqual("incomplete", report.status.value)
        self.assertTrue(any(item["classification"] == "pending" for item in report.to_mapping()["evidence"]))

    def test_validly_empty_surfaces_are_observed_absence(self):
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(empty=True)), clock=self.clock())
        self.assertEqual("complete", report.status.value)
        mapping = report.to_mapping()
        ids = {item["id"] for item in mapping["evidence"]}
        self.assertIn("checks.absent", ids)
        self.assertIn("workflows.absent", ids)
        threads = self.review_threads(mapping)
        self.assertEqual("repository-observed", threads["classification"])
        self.assertEqual(0, threads["details"]["total_threads"])
        self.assertFalse(mapping["errors"])

    def test_partial_api_failure_is_non_complete_with_sanitised_error(self):
        path = f"/repos/{REPO}/pulls/{PR}/reviews"
        report = collector.collect_report(REPO, PR, self.client(FakeTransport(fail_path=path)), clock=self.clock())
        self.assertEqual("incomplete", report.status.value)
        self.assertEqual("pr.reviews", report.to_mapping()["errors"][0]["code"])
        self.assertNotIn("secret-token", str(report.to_mapping()["errors"]))

    def test_review_threads_are_counted_separately_from_submitted_reviews(self):
        graphql = FakeGraphQLTransport(
            pages=[review_thread_page(resolved=(False, True, False), total_count=3)]
        )
        report = collector.collect_report(
            REPO,
            PR,
            self.client(FakeTransport(), graphql_transport=graphql),
            clock=self.clock(),
        )
        mapping = report.to_mapping()
        self.assertEqual("complete", report.status.value)
        threads = self.review_threads(mapping)
        self.assertEqual(
            {
                "total_threads": 3,
                "unresolved_threads": 2,
                "resolved_threads": 1,
                "complete": True,
                "retrieval_surface": "GitHub GraphQL pullRequest.reviewThreads",
            },
            threads["details"],
        )
        reviews = next(item for item in mapping["evidence"] if item["id"] == "pr.reviews")
        self.assertEqual(0, reviews["details"]["count"])
        self.assertEqual(1, len(graphql.calls))

    def test_review_thread_cursor_pagination_reconciles_total(self):
        graphql = FakeGraphQLTransport(
            pages=[
                review_thread_page(
                    resolved=(False,), total_count=2, has_next=True, end_cursor="cursor-1"
                ),
                review_thread_page(resolved=(True,), total_count=2),
            ]
        )
        report = collector.collect_report(
            REPO,
            PR,
            self.client(FakeTransport(), graphql_transport=graphql),
            clock=self.clock(),
        )
        self.assertEqual("complete", report.status.value)
        self.assertEqual(2, len(graphql.calls))
        self.assertIsNone(graphql.calls[0]["variables"]["after"])
        self.assertEqual("cursor-1", graphql.calls[1]["variables"]["after"])
        self.assertEqual(1, self.review_threads(report.to_mapping())["details"]["unresolved_threads"])

    def test_review_thread_partial_page_fails_closed(self):
        graphql = FakeGraphQLTransport(
            pages=[review_thread_page(resolved=(False,), total_count=2)]
        )
        report = collector.collect_report(
            REPO,
            PR,
            self.client(FakeTransport(), graphql_transport=graphql),
            clock=self.clock(),
        )
        mapping = report.to_mapping()
        self.assertEqual("incomplete", report.status.value)
        threads = self.review_threads(mapping)
        self.assertEqual("unavailable", threads["classification"])
        self.assertFalse(threads["details"]["complete"])
        self.assertTrue(any(error["code"] == "pr.review-threads" for error in mapping["errors"]))

    def test_review_thread_non_progressing_cursor_fails_closed(self):
        graphql = FakeGraphQLTransport(
            pages=[
                review_thread_page(
                    resolved=(False,), total_count=3, has_next=True, end_cursor="cursor-1"
                ),
                review_thread_page(
                    resolved=(True,), total_count=3, has_next=True, end_cursor="cursor-1"
                ),
            ]
        )
        report = collector.collect_report(
            REPO,
            PR,
            self.client(FakeTransport(), graphql_transport=graphql),
            clock=self.clock(),
        )
        self.assertEqual("incomplete", report.status.value)
        self.assertEqual("unavailable", self.review_threads(report.to_mapping())["classification"])

    def test_review_thread_page_limit_fails_closed(self):
        graphql = FakeGraphQLTransport(
            pages=[
                review_thread_page(
                    resolved=(False,), total_count=2, has_next=True, end_cursor="cursor-1"
                )
            ]
        )
        report = collector.collect_report(
            REPO,
            PR,
            self.client(FakeTransport(), max_pages=1, graphql_transport=graphql),
            clock=self.clock(),
        )
        self.assertEqual("incomplete", report.status.value)
        self.assertTrue(
            any(
                "safety limit" in error["message"]
                for error in report.to_mapping()["errors"]
                if error["code"] == "pr.review-threads"
            )
        )

    def test_review_thread_graphql_errors_fail_closed_even_with_partial_data(self):
        payload = {
            "data": {
                "repository": {
                    "pullRequest": {
                        "reviewThreads": review_thread_page(resolved=(False,), total_count=1)
                    }
                }
            },
            "errors": [{"message": "Resource not accessible by integration"}],
        }
        graphql = FakeGraphQLTransport(payload=payload)
        report = collector.collect_report(
            REPO,
            PR,
            self.client(FakeTransport(), graphql_transport=graphql),
            clock=self.clock(),
        )
        mapping = report.to_mapping()
        self.assertEqual("incomplete", report.status.value)
        self.assertEqual("unavailable", self.review_threads(mapping)["classification"])
        error = next(error for error in mapping["errors"] if error["code"] == "pr.review-threads")
        self.assertEqual("Resource not accessible by integration", error["message"])
        self.assertNotIn("secret-token", str(mapping["errors"]))

    def test_review_thread_transport_failure_fails_closed(self):
        graphql = FakeGraphQLTransport(
            error=collector.GitHubAPIError(
                "https://api.github.com/graphql", 403, "forbidden"
            )
        )
        report = collector.collect_report(
            REPO,
            PR,
            self.client(FakeTransport(), graphql_transport=graphql),
            clock=self.clock(),
        )
        mapping = report.to_mapping()
        self.assertEqual("incomplete", report.status.value)
        self.assertEqual("unavailable", self.review_threads(mapping)["classification"])
        self.assertTrue(any(error["code"] == "pr.review-threads" for error in mapping["errors"]))

    def test_review_thread_malformed_node_fails_closed(self):
        malformed_page = review_thread_page(resolved=(False,), total_count=1)
        malformed_page["nodes"] = [{"isResolved": "false"}]
        graphql = FakeGraphQLTransport(pages=[malformed_page])
        report = collector.collect_report(
            REPO,
            PR,
            self.client(FakeTransport(), graphql_transport=graphql),
            clock=self.clock(),
        )
        self.assertEqual("incomplete", report.status.value)
        self.assertEqual("unavailable", self.review_threads(report.to_mapping())["classification"])

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
        conflict = self.linkage(report.to_mapping())
        self.assertEqual([80, 81], conflict["details"]["closing_issue_numbers"])
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
