#!/usr/bin/env python3
"""Bounded read-only GitHub Actions trigger/permissions inventory.

This intentionally recognises only a small block-style YAML subset. It is not a
YAML parser or a workflow-security proof. Unsupported relevant syntax is reported
explicitly and returns exit code 2.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from typing import Any, Sequence

MAX_FILE_BYTES = 1024 * 1024
SUFFIXES = {".yml", ".yaml"}
FILTER_KEYS = {"branches", "branches-ignore", "paths", "paths-ignore", "types"}
PERMISSION_VALUES = {"read", "write", "none"}
PLAIN_KEY = re.compile(r"^[A-Za-z0-9_.-]+$")
LOCAL_WORKFLOW = re.compile(r"^\./\.github/workflows/[^@\s]+\.(?:yml|yaml)$")
NOTICE = (
    "Static bounded review assistance only. This report does not prove workflow "
    "security, establish IssueOps policy compliance, authorise remediation, approve "
    "a workflow change, or authorise merge."
)


class AuditFailure(RuntimeError):
    pass


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _ignore(line: str) -> bool:
    return not line.strip() or line.lstrip().startswith("#")


def _mapping(line: str) -> tuple[str, str] | None:
    match = re.match(r"^([^:]+):(.*)$", line.strip())
    return (match.group(1).strip(), match.group(2).strip()) if match else None


def _without_comment(value: str) -> str:
    quote = None
    escaped = False
    for index, char in enumerate(value):
        if quote == '"' and escaped:
            escaped = False
            continue
        if quote == '"' and char == "\\":
            escaped = True
            continue
        if char in {"'", '"'}:
            if quote is None:
                quote = char
            elif quote == char:
                quote = None
        elif char == "#" and quote is None and (index == 0 or value[index - 1].isspace()):
            return value[:index].rstrip()
    return value.rstrip()


def _scalar(value: str) -> str:
    value = _without_comment(value.strip())
    if not value:
        raise ValueError("expected scalar")
    if "${{" in value or value[0] in "&*!|>[{":
        raise ValueError("complex, templated, or flow-style scalar is unsupported")
    if value[0] == "'":
        if len(value) < 2 or value[-1] != "'":
            raise ValueError("unterminated single-quoted scalar")
        return value[1:-1].replace("''", "'")
    if value[0] == '"':
        if len(value) < 2 or value[-1] != '"':
            raise ValueError("unterminated double-quoted scalar")
        try:
            decoded = json.loads(value)
        except json.JSONDecodeError as exc:
            raise ValueError("unsupported quoted-scalar escape") from exc
        if not isinstance(decoded, str):
            raise ValueError("quoted scalar must decode to text")
        return decoded
    return value


def _unsupported(workflow: dict[str, Any], line: int, section: str, reason: str) -> None:
    item = {"line": line, "section": section, "reason": reason}
    if item not in workflow["unsupported_reasons"]:
        workflow["unsupported_reasons"].append(item)
        workflow["parse_status"] = "unsupported"


def _meta(key: str, value: str) -> str | None:
    if key == "<<":
        return "YAML merge keys are unsupported"
    if key.startswith(("&", "*", "!")) or value.startswith(("&", "*", "!")):
        return "YAML anchors, aliases, or tags are unsupported"
    return None


def _top_sections(lines: Sequence[str], workflow: dict[str, Any]) -> dict[str, tuple[int, int, str]]:
    non_ignored = [i for i, line in enumerate(lines) if not _ignore(line)]
    if non_ignored:
        root_indent = min(_indent(lines[i]) for i in non_ignored)
        if root_indent != 0:
            _unsupported(
                workflow,
                non_ignored[0] + 1,
                "global",
                "indented document root is outside the supported top-level structure",
            )
            return {}
    top = [i for i in non_ignored if _indent(lines[i]) == 0]
    starts: dict[str, tuple[int, str]] = {}
    seen: set[str] = set()
    relevant = {"name", "on", "permissions", "jobs"}
    for i in top:
        stripped = lines[i].strip()
        if re.match(r"^[\"'](?:on|permissions|jobs)[\"']\s*:", stripped):
            _unsupported(workflow, i + 1, "global", "quoted relevant top-level keys are unsupported")
            continue
        if stripped.startswith("%"):
            _unsupported(workflow, i + 1, "global", "YAML directives are unsupported")
            continue
        if stripped.startswith(("?", "{", "[", "*", "!")):
            _unsupported(workflow, i + 1, "global", "complex or flow-style top-level structure is unsupported")
            continue
        parsed = _mapping(lines[i])
        if not parsed:
            _unsupported(workflow, i + 1, "global", "top-level entries must use plain mapping syntax")
            continue
        key, value = parsed
        reason = _meta(key, value)
        if reason:
            _unsupported(workflow, i + 1, "global", reason)
            continue
        if not PLAIN_KEY.fullmatch(key):
            _unsupported(workflow, i + 1, "global", "complex top-level mapping keys are unsupported")
            continue
        if key in {"on", "permissions", "jobs"}:
            if key in seen:
                _unsupported(workflow, i + 1, key, f"duplicate top-level {key!r} key")
            seen.add(key)
        if key in relevant and key not in starts:
            starts[key] = (i, value)
    ranges: dict[str, tuple[int, int, str]] = {}
    for key, (start, value) in starts.items():
        end = next((i for i in top if i > start), len(lines))
        ranges[key] = (start, end, value)
    return ranges


def _parse_events(lines: Sequence[str], section: tuple[int, int, str] | None, workflow: dict[str, Any]) -> None:
    if section is None:
        return
    start, end, value = section
    if _without_comment(value).strip():
        _unsupported(workflow, start + 1, "on", "only block-style top-level 'on:' is supported")
        return
    events: dict[str, dict[str, Any]] = {}
    current: dict[str, Any] | None = None
    active_filter: tuple[str, list[str], int] | None = None
    seen_events: set[str] = set()
    seen_filters: dict[str, set[str]] = {}
    for i in range(start + 1, end):
        line, line_no = lines[i], i + 1
        if _ignore(line):
            continue
        if "\t" in line[: len(line) - len(line.lstrip(" \t"))]:
            _unsupported(workflow, line_no, "on", "tabs in structural indentation are unsupported")
            continue
        indent = _indent(line)
        if indent <= 6 and indent % 2:
            _unsupported(workflow, line_no, "on", "ambiguous trigger indentation")
            active_filter = None
            continue
        if indent == 2:
            active_filter = None
            parsed = _mapping(line)
            if not parsed:
                _unsupported(workflow, line_no, "on", "event entries must be mapping keys")
                current = None
                continue
            key, raw = parsed
            reason = _meta(key, raw)
            if reason or not PLAIN_KEY.fullmatch(key):
                _unsupported(workflow, line_no, "on", reason or "complex event keys are unsupported")
                current = None
                continue
            if key in seen_events:
                _unsupported(workflow, line_no, "on", f"duplicate event key {key!r}")
                current = None
                continue
            seen_events.add(key)
            if _without_comment(raw).strip():
                _unsupported(workflow, line_no, "on", "event declarations must use block-style 'EVENT:' syntax")
                current = None
                continue
            current = {"name": key, "line": line_no, "filters": [], "unanalysed_configuration_keys": []}
            events[key] = current
            seen_filters[key] = set()
            continue
        if indent == 4:
            active_filter = None
            if current is None:
                _unsupported(workflow, line_no, "on", "event configuration has no supported event")
                continue
            parsed = _mapping(line)
            if not parsed:
                _unsupported(workflow, line_no, "on", "event configuration must use mapping keys")
                continue
            key, raw = parsed
            reason = _meta(key, raw)
            if reason or not PLAIN_KEY.fullmatch(key):
                _unsupported(workflow, line_no, "on", reason or "complex event configuration keys are unsupported")
                continue
            if key not in FILTER_KEYS:
                if key not in current["unanalysed_configuration_keys"]:
                    current["unanalysed_configuration_keys"].append(key)
                continue
            if key in seen_filters[current["name"]]:
                _unsupported(workflow, line_no, "on", f"duplicate filter key {key!r}")
                continue
            seen_filters[current["name"]].add(key)
            if _without_comment(raw).strip():
                _unsupported(workflow, line_no, "on", f"filter {key!r} must use a block sequence")
                continue
            values: list[str] = []
            active_filter = (key, values, line_no)
            current["filters"].append({"name": key, "line": line_no, "values": values})
            continue
        if active_filter is not None:
            key, values, _ = active_filter
            if indent != 6 or not line.strip().startswith("- "):
                _unsupported(workflow, line_no, "on", f"filter {key!r} expects direct '- scalar' entries")
                continue
            raw_item = line.strip()[2:]
            plain_item = _without_comment(raw_item.strip())
            if plain_item and plain_item[0] not in {"'", '"'} and (
                plain_item.startswith(("- ", "? ")) or re.search(r":(?:\s|$)", plain_item)
            ):
                _unsupported(workflow, line_no, "on", f"filter {key!r} contains complex sequence structure")
                continue
            try:
                values.append(_scalar(raw_item))
            except ValueError as exc:
                _unsupported(workflow, line_no, "on", f"unsupported filter scalar: {exc}")
        # Deeper configuration below an unanalysed key is intentionally ignored.
    for event in events.values():
        event["filters"].sort(key=lambda item: item["name"])
        event["unanalysed_configuration_keys"].sort()
    workflow["events"] = list(events.values())


def _permission_scalar(raw: str, line: int, section: str, workflow: dict[str, Any]) -> dict[str, Any]:
    value = _without_comment(raw).strip()
    if value == "{}":
        return {"declaration_kind": "empty", "line": line, "scopes": []}
    if value in {"read-all", "write-all"}:
        return {"declaration_kind": value, "line": line, "scopes": []}
    _unsupported(workflow, line, section, "permissions scalar must be read-all, write-all, or {}")
    return {"declaration_kind": "not-declared", "line": line, "scopes": []}


def _permission_mapping(lines: Sequence[str], start: int, end: int, indent: int, section: str, workflow: dict[str, Any]) -> dict[str, Any]:
    scopes: list[dict[str, Any]] = []
    seen: set[str] = set()
    for i in range(start + 1, end):
        line, line_no = lines[i], i + 1
        if _ignore(line):
            continue
        level = _indent(line)
        if level < indent:
            break
        if level != indent:
            _unsupported(workflow, line_no, section, "permissions must contain direct scalar scope entries")
            continue
        parsed = _mapping(line)
        if not parsed:
            _unsupported(workflow, line_no, section, "permission scope must be a mapping entry")
            continue
        key, raw = parsed
        reason = _meta(key, raw)
        if reason or not PLAIN_KEY.fullmatch(key):
            _unsupported(workflow, line_no, section, reason or "complex permission scope keys are unsupported")
            continue
        if key in seen:
            _unsupported(workflow, line_no, section, f"duplicate permission scope {key!r}")
            continue
        seen.add(key)
        value = _without_comment(raw).strip()
        if value not in PERMISSION_VALUES:
            _unsupported(workflow, line_no, section, f"unsupported permission value for {key!r}")
            continue
        scopes.append({"name": key, "value": value, "line": line_no})
    return {"declaration_kind": "mapping", "line": start + 1, "scopes": scopes}


def _parse_workflow_permissions(lines: Sequence[str], section: tuple[int, int, str] | None, workflow: dict[str, Any]) -> None:
    if section is None:
        return
    start, end, raw = section
    workflow["workflow_permissions"] = (
        _permission_scalar(raw, start + 1, "permissions", workflow)
        if _without_comment(raw).strip()
        else _permission_mapping(lines, start, end, 2, "permissions", workflow)
    )


def _parse_jobs(lines: Sequence[str], section: tuple[int, int, str] | None, workflow: dict[str, Any]) -> None:
    if section is None:
        return
    start, end, raw = section
    if _without_comment(raw).strip():
        _unsupported(workflow, start + 1, "jobs", "only block-style top-level 'jobs:' is supported")
        return
    jobs: dict[str, dict[str, Any]] = {}
    current: dict[str, Any] | None = None
    active_permissions = False
    seen_jobs: set[str] = set()
    seen_attrs: dict[str, set[str]] = {}
    seen_scopes: dict[str, set[str]] = {}
    for i in range(start + 1, end):
        line, line_no = lines[i], i + 1
        if _ignore(line):
            continue
        if "\t" in line[: len(line) - len(line.lstrip(" \t"))]:
            _unsupported(workflow, line_no, "jobs", "tabs in structural indentation are unsupported")
            continue
        indent = _indent(line)
        if indent <= 6 and indent % 2:
            _unsupported(workflow, line_no, "jobs", "ambiguous jobs indentation")
            active_permissions = False
            continue
        if indent == 2:
            active_permissions = False
            parsed = _mapping(line)
            if not parsed:
                _unsupported(workflow, line_no, "jobs", "job entries must be mapping keys")
                current = None
                continue
            key, value = parsed
            reason = _meta(key, value)
            if reason or not PLAIN_KEY.fullmatch(key) or _without_comment(value).strip():
                _unsupported(workflow, line_no, "jobs", reason or "job IDs must use plain block-style keys")
                current = None
                continue
            if key in seen_jobs:
                _unsupported(workflow, line_no, "jobs", f"duplicate job ID {key!r}")
                current = None
                continue
            seen_jobs.add(key)
            current = {
                "id": key,
                "line": line_no,
                "permissions": {"declaration_kind": "not-declared", "line": None, "scopes": []},
                "local_reusable_target": None,
                "local_reusable_target_line": None,
            }
            jobs[key] = current
            seen_attrs[key], seen_scopes[key] = set(), set()
            continue
        if indent == 4:
            active_permissions = False
            if current is None:
                continue
            stripped = line.strip()
            if re.match(r"^[\"'](?:permissions|uses)[\"']\s*:", stripped):
                _unsupported(workflow, line_no, f"jobs.{current['id']}", "quoted relevant job keys are unsupported")
                continue
            parsed = _mapping(line)
            if not parsed:
                continue
            key, value = parsed
            reason = _meta(key, value)
            if key == "<<":
                _unsupported(workflow, line_no, f"jobs.{current['id']}", reason or "YAML merge keys are unsupported")
                continue
            if key not in {"permissions", "uses"}:
                continue
            if reason:
                _unsupported(workflow, line_no, f"jobs.{current['id']}", reason)
                continue
            if key in seen_attrs[current["id"]]:
                _unsupported(workflow, line_no, f"jobs.{current['id']}", f"duplicate job attribute {key!r}")
                continue
            seen_attrs[current["id"]].add(key)
            if key == "permissions":
                if _without_comment(value).strip():
                    current["permissions"] = _permission_scalar(value, line_no, f"jobs.{current['id']}.permissions", workflow)
                else:
                    current["permissions"] = {"declaration_kind": "mapping", "line": line_no, "scopes": []}
                    active_permissions = True
                continue
            try:
                target = _scalar(value)
            except ValueError as exc:
                _unsupported(workflow, line_no, f"jobs.{current['id']}.uses", f"unsupported job-level uses: {exc}")
                continue
            if LOCAL_WORKFLOW.fullmatch(target):
                current["local_reusable_target"] = target
                current["local_reusable_target_line"] = line_no
            continue
        if active_permissions and current is not None:
            if indent != 6:
                _unsupported(workflow, line_no, f"jobs.{current['id']}.permissions", "job permissions must contain direct scalar scope entries")
                continue
            parsed = _mapping(line)
            if not parsed:
                _unsupported(workflow, line_no, f"jobs.{current['id']}.permissions", "permission scope must be a mapping entry")
                continue
            key, value = parsed
            reason = _meta(key, value)
            if reason or not PLAIN_KEY.fullmatch(key):
                _unsupported(workflow, line_no, f"jobs.{current['id']}.permissions", reason or "complex permission scope key is unsupported")
                continue
            if key in seen_scopes[current["id"]]:
                _unsupported(workflow, line_no, f"jobs.{current['id']}.permissions", f"duplicate permission scope {key!r}")
                continue
            seen_scopes[current["id"]].add(key)
            scalar = _without_comment(value).strip()
            if scalar not in PERMISSION_VALUES:
                _unsupported(workflow, line_no, f"jobs.{current['id']}.permissions", f"unsupported permission value for {key!r}")
                continue
            current["permissions"]["scopes"].append({"name": key, "value": scalar, "line": line_no})
    workflow["jobs"] = list(jobs.values())


def parse_workflow_text(text: str, path: str) -> dict[str, Any]:
    workflow: dict[str, Any] = {
        "path": path,
        "name": None,
        "parse_status": "supported",
        "unsupported_reasons": [],
        "events": [],
        "workflow_permissions": {"declaration_kind": "not-declared", "line": None, "scopes": []},
        "jobs": [],
    }
    lines = text.splitlines()
    for index, line in enumerate(lines, start=1):
        prefix = line[: len(line) - len(line.lstrip(" \t"))]
        if "\t" in prefix and len(prefix.split("\t", 1)[0]) <= 6:
            _unsupported(workflow, index, "global", "tabs in structural indentation are unsupported")
    sections = _top_sections(lines, workflow)
    if "name" in sections:
        try:
            workflow["name"] = _scalar(sections["name"][2])
        except ValueError:
            pass
    _parse_events(lines, sections.get("on"), workflow)
    _parse_workflow_permissions(lines, sections.get("permissions"), workflow)
    _parse_jobs(lines, sections.get("jobs"), workflow)
    workflow["unsupported_reasons"].sort(key=lambda item: (item["line"], item["section"], item["reason"]))
    return workflow


def discover_workflows(root: Path) -> list[tuple[Path, str]]:
    if not root.is_dir():
        raise AuditFailure(f"repository root is not a directory: {root}")
    directory = root / ".github" / "workflows"
    if not directory.exists():
        return []
    if not directory.is_dir():
        raise AuditFailure(f"workflow path is not a directory: {directory}")
    try:
        entries = list(directory.iterdir())
    except OSError as exc:
        raise AuditFailure(f"cannot list workflow directory: {exc}") from exc
    result = [(path, path.relative_to(root).as_posix()) for path in entries if path.suffix.lower() in SUFFIXES]
    return sorted(result, key=lambda item: item[1])


def _read(path: Path, relative: str) -> dict[str, Any]:
    try:
        stat = path.lstat()
    except OSError as exc:
        raise AuditFailure(f"cannot stat {relative}: {exc}") from exc
    if path.is_symlink():
        return {
            "path": relative, "name": None, "parse_status": "unsupported",
            "unsupported_reasons": [{"line": 1, "section": "file", "reason": "symlinked workflow files are not followed"}],
            "events": [], "workflow_permissions": {"declaration_kind": "not-declared", "line": None, "scopes": []}, "jobs": [],
        }
    if not path.is_file():
        raise AuditFailure(f"workflow path is not a regular file: {relative}")
    if stat.st_size > MAX_FILE_BYTES:
        raise AuditFailure(f"workflow file exceeds {MAX_FILE_BYTES} bytes: {relative}")
    try:
        data = path.read_bytes()
    except OSError as exc:
        raise AuditFailure(f"cannot read {relative}: {exc}") from exc
    try:
        return parse_workflow_text(data.decode("utf-8", errors="strict"), relative)
    except UnicodeDecodeError as exc:
        raise AuditFailure(f"workflow file is not valid UTF-8: {relative}") from exc


def audit_repository(root: Path) -> dict[str, Any]:
    workflows = [_read(path, relative) for path, relative in discover_workflows(root)]
    supported = [item for item in workflows if item["parse_status"] == "supported"]
    events: dict[str, list[dict[str, Any]]] = {}
    for workflow in supported:
        for event in workflow["events"]:
            events.setdefault(event["name"], []).append({"path": workflow["path"], "line": event["line"], "filters": event["filters"]})
    fanout = [{"event": name, "workflows": sorted(items, key=lambda item: item["path"])} for name, items in sorted(events.items())]
    paths = {item["path"] for item in workflows}
    edges = []
    for workflow in supported:
        for job in workflow["jobs"]:
            target = job["local_reusable_target"]
            if target:
                edges.append({
                    "caller_path": workflow["path"], "job_id": job["id"], "target": target,
                    "line": job["local_reusable_target_line"], "target_exists": target.removeprefix("./") in paths,
                })
    edges.sort(key=lambda item: (item["caller_path"], item["job_id"], item["target"]))
    advisories: list[dict[str, Any]] = []
    for name, items in sorted(events.items()):
        if len(items) > 1:
            advisories.append({
                "code": "A001",
                "summary": f"Event {name!r} is declared by more than one supported workflow; this is topology for human review, not a defect classification.",
                "sources": [{"path": item["path"], "line": item["line"]} for item in sorted(items, key=lambda item: item["path"])],
                "evidence": {"event": name, "workflow_count": len(items)},
            })
        code = {"pull_request_target": "A002", "workflow_run": "A003"}.get(name)
        if code:
            for item in items:
                advisories.append({"code": code, "summary": f"Explicit {name} trigger is present; contextual human review is required.", "sources": [{"path": item["path"], "line": item["line"]}], "evidence": {}})
    for workflow in supported:
        declarations = [("workflow", workflow["workflow_permissions"])] + [(f"job {job['id']!r}", job["permissions"]) for job in workflow["jobs"]]
        for owner, permission in declarations:
            if permission["declaration_kind"] == "write-all":
                advisories.append({"code": "A004", "summary": f"{owner} declares permissions: write-all; contextual human review is required.", "sources": [{"path": workflow["path"], "line": permission["line"]}], "evidence": {}})
            for scope in permission["scopes"]:
                if scope["value"] == "write":
                    advisories.append({"code": "A005", "summary": f"{owner} explicitly grants {scope['name']}: write; this may be legitimate and requires contextual human review.", "sources": [{"path": workflow["path"], "line": scope["line"]}], "evidence": {"scope": scope["name"]}})
    advisories.sort(key=lambda item: (item["code"], [(s["path"], s["line"]) for s in item["sources"]], item["summary"]))
    return {
        "authority_notice": NOTICE,
        "status": "unsupported" if any(item["parse_status"] == "unsupported" for item in workflows) else "complete",
        "workflow_count": len(workflows),
        "workflows": workflows,
        "event_fanout": fanout,
        "local_reusable_workflow_edges": edges,
        "advisories": advisories,
    }


def render_json(report: dict[str, Any]) -> str:
    return json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def _filters(event: dict[str, Any]) -> str:
    if not event["filters"]:
        return "unfiltered"
    return ", ".join(f"{f['name']}={json.dumps(f['values'], ensure_ascii=False)}" for f in event["filters"])


def _permissions(record: dict[str, Any]) -> str:
    if record["declaration_kind"] != "mapping":
        return record["declaration_kind"]
    return ", ".join(f"{s['name']}: {s['value']}" for s in record["scopes"]) or "mapping (no supported scopes)"


def render_markdown(report: dict[str, Any]) -> str:
    lines = ["# GitHub Actions workflow audit", "", f"> {NOTICE}", "", f"**Audit status:** `{report['status']}`  ", f"**Workflow files:** `{report['workflow_count']}`", "", "## Workflow inventory", ""]
    if not report["workflows"]:
        lines.append("No `.github/workflows/*.yml` or `.yaml` files were found.")
    for workflow in report["workflows"]:
        lines += [f"### `{workflow['path']}`", "", f"- Name: {workflow['name'] or '(simple scalar unavailable)'}", f"- Parse status: `{workflow['parse_status']}`", f"- Workflow permissions: `{_permissions(workflow['workflow_permissions'])}`"]
        lines.append("- Events: " + (", ".join(f"`{e['name']}`" for e in workflow["events"]) or "none in supported inventory"))
        for event in workflow["events"]:
            lines.append(f"  - `{event['name']}`: {_filters(event)}")
            if event["unanalysed_configuration_keys"]:
                lines.append("    - unanalysed configuration keys: " + ", ".join(f"`{key}`" for key in event["unanalysed_configuration_keys"]))
        for job in workflow["jobs"]:
            if job["permissions"]["declaration_kind"] != "not-declared":
                lines.append(f"- Job `{job['id']}` permissions: `{_permissions(job['permissions'])}`")
        lines.append("")
    lines += ["## Event fan-out", ""]
    if not report["event_fanout"]:
        lines.append("No supported event declarations were found.")
    for item in report["event_fanout"]:
        lines += [f"### `{item['event']}`", ""]
        for workflow in item["workflows"]:
            lines.append(f"- `{workflow['path']}` — {_filters(workflow)}")
        lines.append("")
    lines += ["## Direct local reusable-workflow edges", ""]
    if not report["local_reusable_workflow_edges"]:
        lines.append("None found in supported job-level `uses:` syntax.")
    for edge in report["local_reusable_workflow_edges"]:
        lines.append(f"- `{edge['caller_path']}` job `{edge['job_id']}` -> `{edge['target']}` (line {edge['line']}; {'target exists' if edge['target_exists'] else 'target missing'})")
    lines += ["", "## Advisory observations", ""]
    if not report["advisories"]:
        lines.append("No advisories from the closed A001–A005 rule set. This is not proof of workflow safety.")
    for advisory in report["advisories"]:
        sources = ", ".join(f"`{s['path']}:{s['line']}`" for s in advisory["sources"])
        lines.append(f"- **{advisory['code']}** — {advisory['summary']} Sources: {sources}")
    lines += ["", "## Unsupported syntax / coverage gaps", ""]
    reasons = [(w["path"], r) for w in report["workflows"] for r in w["unsupported_reasons"]]
    if not reasons:
        lines.append("None detected within the bounded scanner's relevant structural regions.")
    for path, reason in reasons:
        lines.append(f"- `{path}:{reason['line']}` [{reason['section']}] — {reason['reason']}")
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Bounded read-only GitHub Actions workflow inventory")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    args = parser.parse_args(argv)
    try:
        report = audit_repository(args.root)
    except AuditFailure as exc:
        print(f"audit failed: {exc}", file=sys.stderr)
        return 1
    sys.stdout.write(render_json(report) if args.format == "json" else render_markdown(report))
    return 2 if report["status"] == "unsupported" else 0


if __name__ == "__main__":
    raise SystemExit(main())