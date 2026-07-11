from __future__ import annotations

import contextlib
import copy
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "evidence_pack.py"
SPEC = importlib.util.spec_from_file_location("evidence_pack", MODULE_PATH)
assert SPEC and SPEC.loader
evidence_pack = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = evidence_pack
SPEC.loader.exec_module(evidence_pack)

FIXTURE_ROOT = Path(__file__).parent / "fixtures" / "evidence_pack"


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURE_ROOT / name).read_text(encoding="utf-8"))


class EvidencePackTests(unittest.TestCase):
    def test_complete_fixture_renders_stable_output(self) -> None:
        data = load_fixture("complete.json")
        report = evidence_pack.parse_report(data)

        self.assertEqual(evidence_pack.ReportStatus.COMPLETE, report.status)
        first_json = report.render_json()
        first_markdown = report.render_markdown()

        reordered = copy.deepcopy(data)
        reordered["evidence"] = list(reversed(reordered["evidence"]))
        reordered_report = evidence_pack.parse_report(reordered)

        self.assertEqual(first_json, reordered_report.render_json())
        self.assertEqual(first_markdown, reordered_report.render_markdown())

        parsed_output = json.loads(first_json)
        self.assertEqual("complete", parsed_output["status"])
        self.assertTrue(parsed_output["human_decision_required"])
        self.assertEqual(
            [
                "pr.changed-files",
                "workflow.planning",
                "pr.asserted-validation",
                "scope.changed-files",
            ],
            [item["id"] for item in parsed_output["evidence"]],
        )

    def test_markdown_separates_observed_and_reported_evidence(self) -> None:
        markdown = evidence_pack.parse_report(load_fixture("complete.json")).render_markdown()

        self.assertIn("## Repository-observed evidence", markdown)
        self.assertIn("## Contributor-reported assertions", markdown)
        self.assertIn("## Derived evidence", markdown)
        self.assertLess(
            markdown.index("## Repository-observed evidence"),
            markdown.index("## Contributor-reported assertions"),
        )
        self.assertIn("Human verification and decision remain required", markdown)
        self.assertNotIn("Final recommendation", markdown)

    def test_pending_evidence_is_incomplete(self) -> None:
        report = evidence_pack.parse_report(load_fixture("pending.json"))

        self.assertEqual(evidence_pack.ReportStatus.INCOMPLETE, report.status)
        self.assertIn("## Pending evidence", report.render_markdown())
        self.assertEqual("incomplete", json.loads(report.render_json())["status"])

    def test_collection_error_is_incomplete(self) -> None:
        data = load_fixture("complete.json")
        data["errors"] = [
            {
                "code": "api.pagination",
                "message": "A required page could not be retrieved.",
                "source_url": "https://api.github.com/repos/8ft0-ai/IssueOps/pulls/77/files",
            }
        ]

        report = evidence_pack.parse_report(data)
        self.assertEqual(evidence_pack.ReportStatus.INCOMPLETE, report.status)
        self.assertIn("## Collection errors", report.render_markdown())

    def test_changed_head_is_stale_and_activates_circuit_breaker(self) -> None:
        report = evidence_pack.parse_report(load_fixture("stale.json"))

        self.assertEqual(evidence_pack.ReportStatus.STALE, report.status)
        markdown = report.render_markdown()
        self.assertIn("## Circuit breaker", markdown)
        self.assertIn("must not be treated as complete", markdown)

    def test_conflicting_evidence_has_precedence_over_incomplete(self) -> None:
        data = load_fixture("conflicting.json")
        data["evidence"].append(
            {
                "id": "workflow.pending",
                "classification": "pending",
                "summary": "Another workflow is still running.",
                "source_url": "https://github.com/8ft0-ai/IssueOps/actions/runs/30000000002",
            }
        )

        report = evidence_pack.parse_report(data)
        self.assertEqual(evidence_pack.ReportStatus.CONFLICTING, report.status)
        self.assertIn("## Conflicting evidence", report.render_markdown())

    def test_non_derived_evidence_requires_source_url(self) -> None:
        data = load_fixture("complete.json")
        del data["evidence"][1]["source_url"]

        with self.assertRaisesRegex(
            evidence_pack.EvidenceValidationError, "source_url is required"
        ):
            evidence_pack.parse_report(data)

    def test_derived_evidence_requires_existing_references(self) -> None:
        data = load_fixture("complete.json")
        data["evidence"][0]["derived_from"] = ["missing.item"]

        with self.assertRaisesRegex(
            evidence_pack.EvidenceValidationError, "references unknown evidence IDs"
        ):
            evidence_pack.parse_report(data)

    def test_duplicate_identifiers_fail_validation(self) -> None:
        data = load_fixture("complete.json")
        duplicate = copy.deepcopy(data["evidence"][0])
        duplicate["summary"] = "Duplicate identifier."
        data["evidence"].append(duplicate)

        with self.assertRaisesRegex(evidence_pack.EvidenceValidationError, "duplicate evidence id"):
            evidence_pack.parse_report(data)

    def test_invalid_classification_fails_validation(self) -> None:
        data = load_fixture("complete.json")
        data["evidence"][0]["classification"] = "approved"

        with self.assertRaisesRegex(
            evidence_pack.EvidenceValidationError, "classification must be one of"
        ):
            evidence_pack.parse_report(data)

    def test_invalid_target_and_unknown_fields_fail_validation(self) -> None:
        data = load_fixture("complete.json")
        data["target"]["repository"] = "IssueOps"

        with self.assertRaisesRegex(evidence_pack.EvidenceValidationError, "owner/name"):
            evidence_pack.parse_report(data)

        data = load_fixture("complete.json")
        data["approval"] = True
        with self.assertRaisesRegex(evidence_pack.EvidenceValidationError, "unsupported fields"):
            evidence_pack.parse_report(data)

    def test_cli_exit_codes_distinguish_complete_incomplete_and_invalid(self) -> None:
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            complete_code = evidence_pack.main(
                [str(FIXTURE_ROOT / "complete.json"), "--format", "json"]
            )
        self.assertEqual(0, complete_code)
        self.assertEqual("complete", json.loads(stdout.getvalue())["status"])

        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            incomplete_code = evidence_pack.main(
                [str(FIXTURE_ROOT / "pending.json"), "--format", "json"]
            )
        self.assertEqual(2, incomplete_code)
        self.assertEqual("incomplete", json.loads(stdout.getvalue())["status"])

        with tempfile.TemporaryDirectory() as temp_dir:
            invalid_path = Path(temp_dir) / "invalid.json"
            invalid_path.write_text("{not-json", encoding="utf-8")
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                invalid_code = evidence_pack.main([str(invalid_path)])
        self.assertEqual(1, invalid_code)
        self.assertIn("validation failed", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
