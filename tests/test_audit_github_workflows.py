from __future__ import annotations

import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "audit_github_workflows.py"
SPEC = importlib.util.spec_from_file_location("audit_github_workflows", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
AUDIT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = AUDIT
SPEC.loader.exec_module(AUDIT)


class WorkflowAuditTests(unittest.TestCase):
    def make_repo(self, files: dict[str, str | bytes]) -> Path:
        root = Path(self.tempdir.name)
        workflows = root / ".github" / "workflows"
        workflows.mkdir(parents=True, exist_ok=True)
        for name, content in files.items():
            path = workflows / name
            if isinstance(content, bytes):
                path.write_bytes(content)
            else:
                path.write_text(content, encoding="utf-8")
        return root

    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_discovery_is_lexical_and_limited_to_yaml_extensions(self) -> None:
        root = self.make_repo(
            {
                "z.yaml": "name: Z\non:\n  push:\n",
                "a.yml": "name: A\non:\n  pull_request:\n",
                "ignore.txt": "not a workflow",
            }
        )
        paths = [relative for _, relative in AUDIT.discover_workflows(root)]
        self.assertEqual(
            paths,
            [".github/workflows/a.yml", ".github/workflows/z.yaml"],
        )

    def test_no_workflow_directory_is_valid_empty_inventory(self) -> None:
        report = AUDIT.audit_repository(Path(self.tempdir.name))
        self.assertEqual(report["status"], "complete")
        self.assertEqual(report["workflows"], [])

    def test_trigger_filters_and_unanalysed_inputs_are_inventory_only(self) -> None:
        root = self.make_repo(
            {
                "filters.yml": """name: Filter test
on:
  pull_request:
    branches:
      - main
    branches-ignore:
      - legacy
    paths:
      - "scripts/**"
    paths-ignore:
      - docs/**
    types:
      - opened
      - synchronize
  workflow_dispatch:
    inputs:
      target:
        required: true
        type: string
permissions:
  contents: read
jobs:
  validate:
    runs-on: ubuntu-latest
"""
            }
        )
        report = AUDIT.audit_repository(root)
        workflow = report["workflows"][0]
        self.assertEqual(workflow["parse_status"], "supported")
        pull_request = next(event for event in workflow["events"] if event["name"] == "pull_request")
        filters = {item["name"]: item["values"] for item in pull_request["filters"]}
        self.assertEqual(filters["branches"], ["main"])
        self.assertEqual(filters["branches-ignore"], ["legacy"])
        self.assertEqual(filters["paths"], ["scripts/**"])
        self.assertEqual(filters["paths-ignore"], ["docs/**"])
        self.assertEqual(filters["types"], ["opened", "synchronize"])
        dispatch = next(event for event in workflow["events"] if event["name"] == "workflow_dispatch")
        self.assertEqual(dispatch["unanalysed_configuration_keys"], ["inputs"])

    def test_permissions_inventory_preserves_declared_and_not_declared(self) -> None:
        root = self.make_repo(
            {
                "permissions.yml": """name: Permissions
on:
  push:
permissions:
  contents: read
  packages: write
jobs:
  inherited:
    runs-on: ubuntu-latest
  empty:
    permissions: {}
    runs-on: ubuntu-latest
  read-all:
    permissions: read-all
    runs-on: ubuntu-latest
  write-all:
    permissions: write-all
    runs-on: ubuntu-latest
"""
            }
        )
        report = AUDIT.audit_repository(root)
        workflow = report["workflows"][0]
        self.assertEqual(workflow["workflow_permissions"]["declaration_kind"], "mapping")
        self.assertEqual(
            [(scope["name"], scope["value"]) for scope in workflow["workflow_permissions"]["scopes"]],
            [("contents", "read"), ("packages", "write")],
        )
        jobs = {job["id"]: job for job in workflow["jobs"]}
        self.assertEqual(jobs["inherited"]["permissions"]["declaration_kind"], "not-declared")
        self.assertEqual(jobs["empty"]["permissions"]["declaration_kind"], "empty")
        self.assertEqual(jobs["read-all"]["permissions"]["declaration_kind"], "read-all")
        self.assertEqual(jobs["write-all"]["permissions"]["declaration_kind"], "write-all")
        self.assertIn("A004", {item["code"] for item in report["advisories"]})
        self.assertIn("A005", {item["code"] for item in report["advisories"]})

    def test_direct_local_reusable_edges_and_missing_target(self) -> None:
        root = self.make_repo(
            {
                "caller.yml": """name: Caller
on:
  issue_comment:
    types:
      - created
jobs:
  existing:
    uses: ./.github/workflows/callee.yml
  missing:
    uses: ./.github/workflows/missing.yaml
  ordinary:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
""",
                "callee.yml": """name: Callee
on:
  workflow_call:
jobs:
  noop:
    runs-on: ubuntu-latest
""",
            }
        )
        report = AUDIT.audit_repository(root)
        edges = {(edge["job_id"], edge["target"], edge["target_exists"]) for edge in report["local_reusable_workflow_edges"]}
        self.assertEqual(
            edges,
            {
                ("existing", "./.github/workflows/callee.yml", True),
                ("missing", "./.github/workflows/missing.yaml", False),
            },
        )

    def test_closed_advisory_set_is_neutral_and_advisory_only(self) -> None:
        root = self.make_repo(
            {
                "a.yml": """name: A
on:
  pull_request_target:
  workflow_run:
permissions: write-all
jobs:
  deploy:
    permissions:
      pages: write
    runs-on: ubuntu-latest
""",
                "b.yml": """name: B
on:
  workflow_run:
jobs:
  test:
    runs-on: ubuntu-latest
""",
            }
        )
        report = AUDIT.audit_repository(root)
        self.assertEqual(report["status"], "complete")
        codes = {item["code"] for item in report["advisories"]}
        self.assertEqual(codes, {"A001", "A002", "A003", "A004", "A005"})
        a001 = next(item for item in report["advisories"] if item["code"] == "A001")
        self.assertIn("topology", a001["summary"])
        self.assertIn("not a defect", a001["summary"])
        stderr = io.StringIO()
        stdout = io.StringIO()
        with mock.patch("sys.stdout", stdout), mock.patch("sys.stderr", stderr):
            status = AUDIT.main(["--root", str(root), "--format", "json"])
        self.assertEqual(status, 0)
        self.assertEqual(stderr.getvalue(), "")

    def test_quoted_relevant_keys_and_yaml_directive_are_unsupported(self) -> None:
        workflow = AUDIT.parse_workflow_text(
            '%YAML 1.2\n"on":\n  pull_request:\njobs:\n  build:\n    "permissions":\n      contents: read\n',
            '.github/workflows/quoted.yml',
        )
        self.assertEqual(workflow["parse_status"], "unsupported")
        reasons = {item["reason"] for item in workflow["unsupported_reasons"]}
        self.assertIn("YAML directives are unsupported", reasons)
        self.assertIn("quoted relevant top-level keys are unsupported", reasons)
        self.assertIn("quoted relevant job keys are unsupported", reasons)

    def test_flow_style_trigger_fails_closed_with_exit_two(self) -> None:
        root = self.make_repo({"flow.yml": "name: Flow\non: [push, pull_request]\njobs:\n  test:\n    runs-on: ubuntu-latest\n"})
        report = AUDIT.audit_repository(root)
        self.assertEqual(report["status"], "unsupported")
        self.assertTrue(report["workflows"][0]["unsupported_reasons"])
        with mock.patch("sys.stdout", io.StringIO()), mock.patch("sys.stderr", io.StringIO()):
            self.assertEqual(AUDIT.main(["--root", str(root)]), 2)

    def test_indented_document_root_fails_closed(self) -> None:
        root = self.make_repo({"indented.yml": "  on:\n    push:\n  jobs:\n    test:\n      runs-on: ubuntu-latest\n"})
        report = AUDIT.audit_repository(root)
        self.assertEqual(report["status"], "unsupported")
        reasons = report["workflows"][0]["unsupported_reasons"]
        self.assertTrue(any("indented document root" in item["reason"] for item in reasons))
        with mock.patch("sys.stdout", io.StringIO()), mock.patch("sys.stderr", io.StringIO()):
            self.assertEqual(AUDIT.main(["--root", str(root)]), 2)

    def test_mixed_root_indentation_fails_closed_with_exit_two(self) -> None:
        cases = {
            "leading-indented.yml": (
                "  on:\n"
                "    push:\n"
                "jobs:\n"
                "  test:\n"
                "    runs-on: ubuntu-latest\n"
            ),
            "after-scalar.yml": (
                "name: Mixed root\n"
                "  on:\n"
                "    push:\n"
                "jobs:\n"
                "  test:\n"
                "    runs-on: ubuntu-latest\n"
            ),
        }
        for name, text in cases.items():
            with self.subTest(name=name):
                root = self.make_repo({name: text})
                report = AUDIT.audit_repository(root)
                workflow = report["workflows"][0]
                self.assertEqual(report["status"], "unsupported")
                self.assertEqual(workflow["parse_status"], "unsupported")
                self.assertTrue(
                    any(
                        "indented document root" in item["reason"]
                        or "indented content cannot follow a scalar top-level entry" in item["reason"]
                        for item in workflow["unsupported_reasons"]
                    )
                )
                with mock.patch("sys.stdout", io.StringIO()), mock.patch("sys.stderr", io.StringIO()):
                    self.assertEqual(AUDIT.main(["--root", str(root)]), 2)
                self.tempdir.cleanup()
                self.tempdir = tempfile.TemporaryDirectory()

    def test_top_level_wrappers_and_root_sequence_fail_closed(self) -> None:
        cases = {
            "document-marker.yml": "---\n  on:\n    push:\n  jobs:\n    test:\n      runs-on: ubuntu-latest\n",
            "root-anchor.yml": "&root\n  on:\n    push:\n  jobs:\n    test:\n      runs-on: ubuntu-latest\n",
            "root-sequence.yml": "- on:\n    push:\n  jobs:\n    test:\n      runs-on: ubuntu-latest\n",
        }
        for name, text in cases.items():
            with self.subTest(name=name):
                root = self.make_repo({name: text})
                report = AUDIT.audit_repository(root)
                self.assertEqual(report["status"], "unsupported")
                reasons = report["workflows"][0]["unsupported_reasons"]
                self.assertTrue(any("top-level" in item["reason"] for item in reasons))
                with mock.patch("sys.stdout", io.StringIO()), mock.patch("sys.stderr", io.StringIO()):
                    self.assertEqual(AUDIT.main(["--root", str(root)]), 2)
                self.tempdir.cleanup()
                self.tempdir = tempfile.TemporaryDirectory()

    def test_filter_mapping_or_nested_sequence_item_fails_closed(self) -> None:
        for item in ("foo: bar", "- nested"):
            root = self.make_repo(
                {
                    "complex-filter.yml": (
                        "name: Complex filter\n"
                        "on:\n"
                        "  pull_request:\n"
                        "    paths:\n"
                        f"      - {item}\n"
                        "jobs:\n"
                        "  test:\n"
                        "    runs-on: ubuntu-latest\n"
                    )
                }
            )
            report = AUDIT.audit_repository(root)
            self.assertEqual(report["status"], "unsupported")
            reasons = report["workflows"][0]["unsupported_reasons"]
            self.assertTrue(any("complex sequence structure" in entry["reason"] for entry in reasons))
            self.tempdir.cleanup()
            self.tempdir = tempfile.TemporaryDirectory()

    def test_unsupported_plain_scalars_fail_closed_with_exit_two(self) -> None:
        cases = {
            "at-filter.yml": (
                "name: At filter\n"
                "on:\n"
                "  pull_request:\n"
                "    paths:\n"
                "      - @foo\n"
                "jobs:\n"
                "  test:\n"
                "    runs-on: ubuntu-latest\n"
            ),
            "backtick-filter.yml": (
                "name: Backtick filter\n"
                "on:\n"
                "  pull_request:\n"
                "    paths:\n"
                "      - `foo\n"
                "jobs:\n"
                "  test:\n"
                "    runs-on: ubuntu-latest\n"
            ),
            "colon-uses.yml": (
                "name: Colon uses\n"
                "on:\n"
                "  push:\n"
                "jobs:\n"
                "  call:\n"
                "    uses: foo: bar\n"
            ),
        }
        expected = {
            "at-filter.yml": "plain-scalar leading indicator",
            "backtick-filter.yml": "plain-scalar leading indicator",
            "colon-uses.yml": "colon followed by whitespace",
        }
        for name, text in cases.items():
            with self.subTest(name=name):
                root = self.make_repo({name: text})
                report = AUDIT.audit_repository(root)
                workflow = report["workflows"][0]
                self.assertEqual(report["status"], "unsupported")
                self.assertEqual(workflow["parse_status"], "unsupported")
                self.assertTrue(
                    any(expected[name] in item["reason"] for item in workflow["unsupported_reasons"])
                )
                with mock.patch("sys.stdout", io.StringIO()), mock.patch("sys.stderr", io.StringIO()):
                    self.assertEqual(AUDIT.main(["--root", str(root)]), 2)
                self.tempdir.cleanup()
                self.tempdir = tempfile.TemporaryDirectory()

    def test_malformed_single_quoted_scalars_fail_closed_with_exit_two(self) -> None:
        cases = {
            "bad-filter.yml": (
                "name: Bad single quote\n"
                "on:\n"
                "  pull_request:\n"
                "    paths:\n"
                "      - 'foo'bar'\n"
                "jobs:\n"
                "  test:\n"
                "    runs-on: ubuntu-latest\n"
            ),
            "bad-uses.yml": (
                "name: Bad single quote uses\n"
                "on:\n"
                "  push:\n"
                "jobs:\n"
                "  call:\n"
                "    uses: 'foo'bar'\n"
            ),
        }
        for name, text in cases.items():
            with self.subTest(name=name):
                root = self.make_repo({name: text})
                report = AUDIT.audit_repository(root)
                workflow = report["workflows"][0]
                self.assertEqual(report["status"], "unsupported")
                self.assertEqual(workflow["parse_status"], "unsupported")
                self.assertTrue(
                    any("undoubled quote" in item["reason"] for item in workflow["unsupported_reasons"])
                )
                with mock.patch("sys.stdout", io.StringIO()), mock.patch("sys.stderr", io.StringIO()):
                    self.assertEqual(AUDIT.main(["--root", str(root)]), 2)
                self.tempdir.cleanup()
                self.tempdir = tempfile.TemporaryDirectory()

    def test_quoted_scalars_preserve_reserved_content(self) -> None:
        root = self.make_repo(
            {
                "caller.yml": """name: Caller
on:
  pull_request:
    paths:
      - "@foo"
jobs:
  call:
    uses: "./.github/workflows/callee.yml"
""",
                "callee.yml": """name: Callee
on:
  workflow_call:
jobs:
  noop:
    runs-on: ubuntu-latest
""",
            }
        )
        report = AUDIT.audit_repository(root)
        self.assertEqual(report["status"], "complete")
        caller = next(item for item in report["workflows"] if item["path"].endswith("caller.yml"))
        pull_request = next(event for event in caller["events"] if event["name"] == "pull_request")
        self.assertEqual(pull_request["filters"][0]["values"], ["@foo"])
        self.assertEqual(
            [(edge["job_id"], edge["target"], edge["target_exists"]) for edge in report["local_reusable_workflow_edges"]],
            [("call", "./.github/workflows/callee.yml", True)],
        )

    def test_valid_single_quoted_scalars_preserve_doubled_quotes(self) -> None:
        root = self.make_repo(
            {
                "caller.yml": """name: Caller
on:
  pull_request:
    paths:
      - 'foo''bar'
jobs:
  call:
    uses: './.github/workflows/callee''s.yml'
""",
                "callee's.yml": """name: Callee
on:
  workflow_call:
jobs:
  noop:
    runs-on: ubuntu-latest
""",
            }
        )
        report = AUDIT.audit_repository(root)
        self.assertEqual(report["status"], "complete")
        caller = next(item for item in report["workflows"] if item["path"].endswith("caller.yml"))
        pull_request = next(event for event in caller["events"] if event["name"] == "pull_request")
        self.assertEqual(pull_request["filters"][0]["values"], ["foo'bar"])
        self.assertEqual(
            [(edge["job_id"], edge["target"], edge["target_exists"]) for edge in report["local_reusable_workflow_edges"]],
            [("call", "./.github/workflows/callee's.yml", True)],
        )

    def test_flow_style_filter_fails_closed(self) -> None:
        root = self.make_repo(
            {"flow-filter.yml": "name: Flow\non:\n  pull_request:\n    paths: [scripts/**]\njobs:\n  test:\n    runs-on: ubuntu-latest\n"}
        )
        report = AUDIT.audit_repository(root)
        self.assertEqual(report["status"], "unsupported")
        self.assertTrue(any("block sequence" in item["reason"] for item in report["workflows"][0]["unsupported_reasons"]))

    def test_duplicate_relevant_keys_fail_closed(self) -> None:
        root = self.make_repo(
            {"dup.yml": "name: Dup\non:\n  push:\n  push:\njobs:\n  test:\n    runs-on: ubuntu-latest\n"}
        )
        report = AUDIT.audit_repository(root)
        self.assertEqual(report["status"], "unsupported")
        self.assertTrue(any("duplicate event key" in item["reason"] for item in report["workflows"][0]["unsupported_reasons"]))

    def test_tabs_in_structural_indentation_fail_closed(self) -> None:
        root = self.make_repo({"tabs.yml": "name: Tabs\non:\n\tpush:\n"})
        report = AUDIT.audit_repository(root)
        self.assertEqual(report["status"], "unsupported")
        self.assertTrue(any("tabs" in item["reason"] for item in report["workflows"][0]["unsupported_reasons"]))

    def test_top_level_and_job_merge_keys_fail_closed(self) -> None:
        root = self.make_repo(
            {
                "merge.yml": """name: Merge
defaults: &defaults
  permissions: write-all
<<: *defaults
on:
  push:
jobs:
  test:
    <<: *job-defaults
    runs-on: ubuntu-latest
"""
            }
        )
        report = AUDIT.audit_repository(root)
        self.assertEqual(report["status"], "unsupported")
        reasons = [item["reason"] for item in report["workflows"][0]["unsupported_reasons"]]
        self.assertTrue(any("anchors" in reason or "merge keys" in reason for reason in reasons))

    def test_explicit_or_root_flow_structure_fails_closed(self) -> None:
        for text in ("? on\n: push\n", "{on: push, jobs: {}}\n"):
            workflow = AUDIT.parse_workflow_text(text, ".github/workflows/complex.yml")
            self.assertEqual(workflow["parse_status"], "unsupported")
            self.assertTrue(
                any("complex or flow-style top-level structure" in item["reason"] for item in workflow["unsupported_reasons"])
            )

    def test_anchor_alias_and_merge_key_fail_closed_in_relevant_structure(self) -> None:
        root = self.make_repo(
            {"anchor.yml": "name: Anchor\non:\n  push: &trigger\npermissions:\n  <<: *defaults\njobs:\n  test:\n    runs-on: ubuntu-latest\n"}
        )
        report = AUDIT.audit_repository(root)
        self.assertEqual(report["status"], "unsupported")
        reasons = " ".join(item["reason"] for item in report["workflows"][0]["unsupported_reasons"])
        self.assertTrue("anchors" in reasons or "merge keys" in reasons)

    def test_invalid_permission_value_fails_closed(self) -> None:
        root = self.make_repo(
            {"bad-perms.yml": "name: Bad\non:\n  push:\npermissions:\n  contents: yes\njobs:\n  test:\n    runs-on: ubuntu-latest\n"}
        )
        report = AUDIT.audit_repository(root)
        self.assertEqual(report["status"], "unsupported")
        self.assertTrue(any("unsupported permission value" in item["reason"] for item in report["workflows"][0]["unsupported_reasons"]))

    def test_symlinked_workflow_is_not_followed(self) -> None:
        root = self.make_repo({"target.txt": "name: Not discovered\n"})
        workflow_dir = root / ".github" / "workflows"
        (workflow_dir / "link.yml").symlink_to(workflow_dir / "target.txt")
        report = AUDIT.audit_repository(root)
        self.assertEqual(report["status"], "unsupported")
        self.assertEqual(report["workflows"][0]["parse_status"], "unsupported")
        self.assertIn("symlinked", report["workflows"][0]["unsupported_reasons"][0]["reason"])

    def test_non_utf8_and_oversize_are_fatal(self) -> None:
        root = self.make_repo({"bad.yml": b"\xff\xfe"})
        with self.assertRaises(AUDIT.AuditFailure):
            AUDIT.audit_repository(root)

        root = self.make_repo({"large.yml": "x" * (AUDIT.MAX_FILE_BYTES + 1)})
        with self.assertRaises(AUDIT.AuditFailure):
            AUDIT.audit_repository(root)

    def test_json_rendering_is_deterministic_and_matches_report(self) -> None:
        root = self.make_repo({"one.yml": "name: One\non:\n  push:\npermissions:\n  contents: read\njobs:\n  test:\n    runs-on: ubuntu-latest\n"})
        report = AUDIT.audit_repository(root)
        first = AUDIT.render_json(report)
        second = AUDIT.render_json(report)
        self.assertEqual(first, second)
        payload = json.loads(first)
        self.assertEqual(payload["status"], "complete")
        self.assertEqual(payload["workflow_count"], 1)
        self.assertIn("does not prove workflow security", payload["authority_notice"])

    def test_markdown_contains_authority_and_unsupported_sections(self) -> None:
        root = self.make_repo({"one.yml": "name: One\non:\n  push:\njobs:\n  test:\n    runs-on: ubuntu-latest\n"})
        output = AUDIT.render_markdown(AUDIT.audit_repository(root))
        self.assertIn("does not prove workflow security", output)
        self.assertIn("## Unsupported syntax / coverage gaps", output)
        self.assertIn("not proof of workflow safety", output)

    def test_representative_issueops_topology_without_repository_specific_policy(self) -> None:
        root = self.make_repo(
            {
                "baseline-validation.yml": """name: Validate repository baseline
on:
  pull_request:
    branches:
      - main
  workflow_dispatch:
permissions:
  contents: read
jobs:
  validate:
    runs-on: ubuntu-latest
""",
                "collect-evidence-pack.yml": """name: Collect pull-request evidence pack
on:
  workflow_dispatch:
    inputs:
      pull_request:
        required: true
        type: string
  workflow_call:
    inputs:
      routed_pr_number:
        required: true
        type: number
permissions:
  contents: read
  pull-requests: read
  issues: read
  checks: read
  actions: read
jobs:
  collect:
    runs-on: ubuntu-latest
""",
                "evidence-collector-validation.yml": """name: Validate GitHub evidence collector
on:
  pull_request:
    branches:
      - main
    paths:
      - "scripts/collect_pr_evidence.py"
  workflow_dispatch:
    inputs:
      live_inspector:
        required: false
        type: boolean
permissions:
  contents: read
jobs:
  validate:
    runs-on: ubuntu-latest
  live-inspector:
    permissions:
      contents: read
      issues: read
      pull-requests: read
    runs-on: ubuntu-latest
""",
                "evidence-pack-validation.yml": """name: Validate evidence-pack core
on:
  pull_request:
    branches:
      - main
    paths:
      - "scripts/evidence_pack.py"
  workflow_dispatch:
permissions:
  contents: read
jobs:
  validate:
    runs-on: ubuntu-latest
""",
                "pages.yml": """name: Publish documentation site
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  workflow_dispatch:
jobs:
  build:
    permissions:
      contents: read
    runs-on: ubuntu-latest
  deploy:
    permissions:
      pages: write
      id-token: write
    runs-on: ubuntu-latest
""",
                "planning-validation.yml": """name: Validate planning artefacts
on:
  pull_request:
    branches:
      - main
    paths:
      - "planning/**"
  workflow_dispatch:
permissions:
  contents: read
jobs:
  validate:
    runs-on: ubuntu-latest
""",
                "pr-comment-command-router.yml": """name: Route pull-request comment commands
on:
  issue_comment:
    types:
      - created
jobs:
  validate-pr-diff:
    permissions:
      contents: read
      pull-requests: read
    uses: ./.github/workflows/pr-diff-validation.yml
  collect-evidence:
    permissions:
      contents: read
      pull-requests: read
      issues: read
      checks: read
      actions: read
    uses: ./.github/workflows/collect-evidence-pack.yml
""",
                "pr-diff-validation.yml": """name: Validate pull-request diff
on:
  pull_request:
    branches:
      - main
  workflow_call:
    inputs:
      routed_pr_number:
        required: true
        type: number
permissions:
  contents: read
  pull-requests: read
jobs:
  validate:
    runs-on: ubuntu-latest
""",
            }
        )
        report = AUDIT.audit_repository(root)
        self.assertEqual(report["status"], "complete")
        fanout = {item["event"]: len(item["workflows"]) for item in report["event_fanout"]}
        self.assertEqual(
            fanout,
            {
                "issue_comment": 1,
                "pull_request": 6,
                "push": 1,
                "workflow_call": 2,
                "workflow_dispatch": 6,
            },
        )
        self.assertEqual(len(report["local_reusable_workflow_edges"]), 2)
        self.assertTrue(all(edge["target_exists"] for edge in report["local_reusable_workflow_edges"]))
        a005 = [item for item in report["advisories"] if item["code"] == "A005"]
        self.assertEqual(len(a005), 2)
        self.assertEqual({item["evidence"]["scope"] for item in a005}, {"pages", "id-token"})
        codes = {item["code"] for item in report["advisories"]}
        self.assertNotIn("A002", codes)
        self.assertNotIn("A003", codes)
        self.assertNotIn("A004", codes)


if __name__ == "__main__":
    unittest.main()