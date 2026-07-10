from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_planning.py"
SPEC = importlib.util.spec_from_file_location("validate_planning", MODULE_PATH)
assert SPEC and SPEC.loader
validate_planning = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate_planning)


ROADMAP = """# Stage 9 — Test

Status: completed.

Record type: retrospective reconstruction.

## Problem statement
x
## Outcome to prove
x
## Non-goals
x
## Operating and autonomy boundary
x
## Target workflow or target state
x
## Acceptance gates
x
## Proposed implementation slices
x
## Risks and controls
x
## Definition of done
x
## Likely next decision boundary
x
"""

DELIVERY = """# Stage 9 — Test

Status: completed.

## Original documented intent
x
## Retrospective interpretation
x
## What shipped
x
## Linked issues and pull requests
x
## Proof runs, checks and artefacts
x
## Intended versus actual delivery
x
## Observed limitations and friction
x
## Boundaries preserved
x
## Decisions and lessons
x
## Implications for the next stage
x
"""


class PlanningValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        required = {
            "planning/README.md": "# Planning\n",
            "planning/roadmap/index.md": "# Roadmap\n",
            "planning/roadmap/stage-template.md": "# Template\n",
            "planning/delivery/index.md": "# Delivery\n",
            "planning/delivery/delivery-record-template.md": "# Template\n",
            "planning/delivery-log.md": "# Log\n",
            "planning/roadmap/stage-09-retrospective-test.md": ROADMAP,
            "planning/delivery/stage-09-test.md": DELIVERY,
        }
        for relative, content in required.items():
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_valid_tree_passes(self) -> None:
        self.assertEqual([], validate_planning.validate(self.root))

    def test_missing_heading_fails(self) -> None:
        path = self.root / "planning/roadmap/stage-09-retrospective-test.md"
        path.write_text(ROADMAP.replace("## Acceptance gates\n", ""), encoding="utf-8")
        errors = validate_planning.validate(self.root)
        self.assertTrue(any("Acceptance gates" in error for error in errors))

    def test_unsupported_status_fails(self) -> None:
        path = self.root / "planning/roadmap/stage-09-retrospective-test.md"
        path.write_text(ROADMAP.replace("Status: completed.", "Status: archived."), encoding="utf-8")
        errors = validate_planning.validate(self.root)
        self.assertTrue(any("unsupported status" in error for error in errors))

    def test_broken_relative_link_fails(self) -> None:
        path = self.root / "planning/README.md"
        path.write_text("# Planning\n\n[Missing](missing.md)\n", encoding="utf-8")
        errors = validate_planning.validate(self.root)
        self.assertTrue(any("broken relative link" in error for error in errors))

    def test_temporary_file_fails(self) -> None:
        path = self.root / "planning/roadmap/notes.md~"
        path.write_text("temporary", encoding="utf-8")
        errors = validate_planning.validate(self.root)
        self.assertTrue(any("temporary or editor file" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
