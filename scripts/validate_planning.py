#!/usr/bin/env python3
"""Validate the IssueOps planning control surface using only the standard library."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED_FILES = (
    "planning/README.md",
    "planning/roadmap/index.md",
    "planning/roadmap/stage-template.md",
    "planning/delivery/index.md",
    "planning/delivery/delivery-record-template.md",
    "planning/delivery-log.md",
)

ROADMAP_HEADINGS = (
    "## Problem statement",
    "## Outcome to prove",
    "## Non-goals",
    "## Operating and autonomy boundary",
    "## Target workflow or target state",
    "## Acceptance gates",
    "## Proposed implementation slices",
    "## Risks and controls",
    "## Definition of done",
    "## Likely next decision boundary",
)

DELIVERY_HEADINGS = (
    "## Original documented intent",
    "## Retrospective interpretation",
    "## What shipped",
    "## Linked issues and pull requests",
    "## Proof runs, checks and artefacts",
    "## Intended versus actual delivery",
    "## Observed limitations and friction",
    "## Boundaries preserved",
    "## Decisions and lessons",
    "## Implications for the next stage",
)

ALLOWED_STATUSES = {"shaping", "approved", "delivering", "completed", "superseded"}
TEMP_SUFFIXES = ("~", ".tmp", ".swp", ".bak")
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _check_headings(path: Path, required: tuple[str, ...], errors: list[str]) -> None:
    text = _read(path)
    for heading in required:
        if heading not in text:
            errors.append(f"{path}: missing required heading {heading!r}")


def _check_status_and_record_type(path: Path, errors: list[str]) -> None:
    text = _read(path)
    match = re.search(r"^Status:\s*([a-z-]+)\.?\s*$", text, re.MULTILINE)
    if not match:
        errors.append(f"{path}: missing Status field")
    elif match.group(1) not in ALLOWED_STATUSES:
        errors.append(f"{path}: unsupported status {match.group(1)!r}")

    record_match = re.search(r"^Record type:\s*(.+?)\.?\s*$", text, re.MULTILINE)
    if not record_match:
        errors.append(f"{path}: missing Record type field")
    elif "retrospective" in path.name and "retrospective" not in record_match.group(1).lower():
        errors.append(f"{path}: retrospective filename requires an explicit retrospective Record type")


def _check_links(planning_root: Path, errors: list[str]) -> None:
    for path in planning_root.rglob("*.md"):
        text = _read(path)
        for target in LINK_PATTERN.findall(text):
            target = target.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith(("mailto:", "#")):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{path}: broken relative link {target!r}")


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing required planning file: {relative}")

    planning_root = root / "planning"
    if not planning_root.is_dir():
        return errors

    for path in planning_root.rglob("*"):
        if path.is_file() and (path.name.startswith(".#") or path.name.endswith(TEMP_SUFFIXES)):
            errors.append(f"{path}: temporary or editor file is not allowed")

    roadmap_dir = planning_root / "roadmap"
    if roadmap_dir.is_dir():
        for path in roadmap_dir.glob("*.md"):
            if path.name in {"index.md", "stage-template.md"}:
                continue
            _check_headings(path, ROADMAP_HEADINGS, errors)
            _check_status_and_record_type(path, errors)

    delivery_dir = planning_root / "delivery"
    if delivery_dir.is_dir():
        excluded = {
            "index.md",
            "delivery-record-template.md",
            "graph.md",
            "graph-modelling-rules.md",
        }
        for path in delivery_dir.glob("*.md"):
            if path.name in excluded:
                continue
            _check_headings(path, DELIVERY_HEADINGS, errors)
            text = _read(path)
            match = re.search(r"^Status:\s*([a-z-]+)\.?\s*$", text, re.MULTILINE)
            if not match:
                errors.append(f"{path}: missing Status field")
            elif match.group(1) != "completed":
                errors.append(f"{path}: delivery record status must be 'completed'")

    _check_links(planning_root, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    errors = validate(args.root)
    if errors:
        print("Planning validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Planning validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
