#!/usr/bin/env python3
"""Validate the compact IssueOps delivery graph."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "delivery-graph/v1"
NODE_TYPES = {
    "stage",
    "problem",
    "decision",
    "issue",
    "pull_request",
    "workflow_run",
    "artifact",
    "boundary",
    "lesson",
    "release",
}
EDGE_TYPES = {
    "enabled",
    "motivated",
    "revealed_problem",
    "resolved_by",
    "implemented_by",
    "proved_by",
    "produced",
    "validated_by",
    "preserved",
    "carried_forward_to",
}
STAGE_STATUSES = {"shaping", "approved", "delivering", "completed", "superseded"}
REQUIRED_NODE_FIELDS = {"id", "type", "title", "summary"}
FORBIDDEN_GENERATED_PREFIXES = ("_site/", "site/")


def load_graph(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("delivery graph root must be an object")
    return data


def validate_graph(data: dict[str, Any], root: Path) -> list[str]:
    errors: list[str] = []

    if data.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must equal {SCHEMA_VERSION!r}")

    nodes = data.get("nodes")
    edges = data.get("edges")
    if not isinstance(nodes, list) or not nodes:
        errors.append("nodes must be a non-empty list")
        nodes = []
    if not isinstance(edges, list):
        errors.append("edges must be a list")
        edges = []

    ids: set[str] = set()
    for index, node in enumerate(nodes):
        label = f"nodes[{index}]"
        if not isinstance(node, dict):
            errors.append(f"{label} must be an object")
            continue

        missing = sorted(REQUIRED_NODE_FIELDS - node.keys())
        if missing:
            errors.append(f"{label} missing required fields: {', '.join(missing)}")

        node_id = node.get("id")
        if not isinstance(node_id, str) or not node_id:
            errors.append(f"{label}.id must be a non-empty string")
        elif node_id in ids:
            errors.append(f"duplicate node id: {node_id}")
        else:
            ids.add(node_id)

        node_type = node.get("type")
        if node_type not in NODE_TYPES:
            errors.append(f"{label} has invalid node type {node_type!r}")

        if node_type == "stage":
            status = node.get("status")
            if status not in STAGE_STATUSES:
                errors.append(f"{label} stage status is invalid or missing: {status!r}")

        path_value = node.get("path")
        if path_value is not None:
            if not isinstance(path_value, str) or not path_value:
                errors.append(f"{label}.path must be a non-empty string")
            else:
                normalised = path_value.replace("\\", "/")
                if normalised.startswith(FORBIDDEN_GENERATED_PREFIXES):
                    errors.append(f"{label} represents generated site output as committed source: {path_value}")
                elif not (root / path_value).is_file():
                    errors.append(f"{label} references missing local path: {path_value}")

    for index, edge in enumerate(edges):
        label = f"edges[{index}]"
        if not isinstance(edge, dict):
            errors.append(f"{label} must be an object")
            continue

        source = edge.get("from")
        target = edge.get("to")
        edge_type = edge.get("type")
        if source not in ids:
            errors.append(f"{label} has missing source node: {source!r}")
        if target not in ids:
            errors.append(f"{label} has missing target node: {target!r}")
        if edge_type not in EDGE_TYPES:
            errors.append(f"{label} has invalid edge type {edge_type!r}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--graph",
        type=Path,
        default=Path("planning/delivery/delivery.yaml"),
    )
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    try:
        data = load_graph(args.graph)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Delivery graph validation failed: {exc}")
        return 1

    errors = validate_graph(data, args.root.resolve())
    if errors:
        print("Delivery graph validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Delivery graph validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
