#!/usr/bin/env python3
"""Validate and render deterministic IssueOps evidence-pack input.

This module is intentionally local and read-only. It does not access GitHub,
perform network calls, mutate repository state, or make approval decisions.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence
from urllib.parse import urlparse

SCHEMA_VERSION = "evidence-pack/v1"
MAX_EVIDENCE_ITEMS = 500
MAX_COLLECTION_ERRORS = 100
MAX_DETAILS_BYTES = 10_000
GENERATED_NOTICE = (
    "Generated evidence summary. Human verification and decision remain required. "
    "This report does not approve the change, confirm contract satisfaction, or authorise merge or publication."
)

REPOSITORY_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
SHA_PATTERN = re.compile(r"^[0-9a-fA-F]{7,64}$")
IDENTIFIER_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$")


class EvidenceValidationError(ValueError):
    """Raised when evidence-pack input does not satisfy the schema."""


class Classification(str, Enum):
    REPOSITORY_OBSERVED = "repository-observed"
    CONTRIBUTOR_REPORTED = "contributor-reported"
    DERIVED = "derived"
    PENDING = "pending"
    UNAVAILABLE = "unavailable"
    CONFLICTING = "conflicting"


class ReportStatus(str, Enum):
    COMPLETE = "complete"
    INCOMPLETE = "incomplete"
    CONFLICTING = "conflicting"
    STALE = "stale"


CLASSIFICATION_ORDER = {
    Classification.REPOSITORY_OBSERVED: 0,
    Classification.CONTRIBUTOR_REPORTED: 1,
    Classification.DERIVED: 2,
    Classification.PENDING: 3,
    Classification.UNAVAILABLE: 4,
    Classification.CONFLICTING: 5,
}

CLASSIFICATION_TITLES = {
    Classification.REPOSITORY_OBSERVED: "Repository-observed evidence",
    Classification.CONTRIBUTOR_REPORTED: "Contributor-reported assertions",
    Classification.DERIVED: "Derived evidence",
    Classification.PENDING: "Pending evidence",
    Classification.UNAVAILABLE: "Unavailable evidence",
    Classification.CONFLICTING: "Conflicting evidence",
}


@dataclass(frozen=True)
class Target:
    repository: str
    pull_request: int
    url: str
    linked_issue: int | None = None


@dataclass(frozen=True)
class CollectionWindow:
    started_at: str
    completed_at: str
    head_sha_start: str
    head_sha_end: str


@dataclass(frozen=True)
class EvidenceItem:
    identifier: str
    classification: Classification
    summary: str
    source_url: str | None
    source_timestamp: str | None
    derived_from: tuple[str, ...]
    details: Mapping[str, Any]


@dataclass(frozen=True)
class CollectionError:
    code: str
    message: str
    source_url: str | None


@dataclass(frozen=True)
class EvidenceReport:
    target: Target
    collection: CollectionWindow
    evidence: tuple[EvidenceItem, ...]
    errors: tuple[CollectionError, ...]

    @property
    def status(self) -> ReportStatus:
        if self.collection.head_sha_start != self.collection.head_sha_end:
            return ReportStatus.STALE
        if any(item.classification is Classification.CONFLICTING for item in self.evidence):
            return ReportStatus.CONFLICTING
        if (
            not self.evidence
            or self.errors
            or any(
                item.classification in {Classification.PENDING, Classification.UNAVAILABLE}
                for item in self.evidence
            )
        ):
            return ReportStatus.INCOMPLETE
        return ReportStatus.COMPLETE

    def sorted_evidence(self) -> tuple[EvidenceItem, ...]:
        return tuple(
            sorted(
                self.evidence,
                key=lambda item: (
                    CLASSIFICATION_ORDER[item.classification],
                    item.identifier,
                    item.source_url or "",
                ),
            )
        )

    def sorted_errors(self) -> tuple[CollectionError, ...]:
        return tuple(sorted(self.errors, key=lambda error: (error.code, error.message, error.source_url or "")))

    def to_mapping(self) -> dict[str, Any]:
        return {
            "schema_version": SCHEMA_VERSION,
            "status": self.status.value,
            "generated_notice": GENERATED_NOTICE,
            "human_decision_required": True,
            "target": {
                "repository": self.target.repository,
                "pull_request": self.target.pull_request,
                "url": self.target.url,
                **(
                    {"linked_issue": self.target.linked_issue}
                    if self.target.linked_issue is not None
                    else {}
                ),
            },
            "collection": {
                "started_at": self.collection.started_at,
                "completed_at": self.collection.completed_at,
                "head_sha_start": self.collection.head_sha_start,
                "head_sha_end": self.collection.head_sha_end,
                "head_stable": self.collection.head_sha_start == self.collection.head_sha_end,
            },
            "evidence": [
                {
                    "id": item.identifier,
                    "classification": item.classification.value,
                    "summary": item.summary,
                    **({"source_url": item.source_url} if item.source_url else {}),
                    **(
                        {"source_timestamp": item.source_timestamp}
                        if item.source_timestamp
                        else {}
                    ),
                    **(
                        {"derived_from": list(item.derived_from)}
                        if item.derived_from
                        else {}
                    ),
                    **({"details": _normalise_json(item.details)} if item.details else {}),
                }
                for item in self.sorted_evidence()
            ],
            "errors": [
                {
                    "code": error.code,
                    "message": error.message,
                    **({"source_url": error.source_url} if error.source_url else {}),
                }
                for error in self.sorted_errors()
            ],
        }

    def render_json(self) -> str:
        return json.dumps(self.to_mapping(), indent=2, sort_keys=True, ensure_ascii=False) + "\n"

    def render_markdown(self) -> str:
        lines = [
            "# IssueOps evidence report",
            "",
            f"> **Generated:** {GENERATED_NOTICE}",
            "",
            f"**Collection status:** `{self.status.value}`",
            "",
            "## Target",
            "",
            f"- Repository: `{self.target.repository}`",
            f"- Pull request: [#{self.target.pull_request}]({self.target.url})",
        ]
        if self.target.linked_issue is not None:
            lines.append(f"- Linked issue: `#{self.target.linked_issue}`")
        lines.extend(
            [
                f"- Collection started: `{self.collection.started_at}`",
                f"- Collection completed: `{self.collection.completed_at}`",
                f"- Head SHA at start: `{self.collection.head_sha_start}`",
                f"- Head SHA at end: `{self.collection.head_sha_end}`",
                "",
            ]
        )

        if self.status is ReportStatus.STALE:
            lines.extend(
                [
                    "## Circuit breaker",
                    "",
                    "The pull-request head changed during collection. This report is stale and must not be treated as complete.",
                    "",
                ]
            )

        grouped: dict[Classification, list[EvidenceItem]] = {
            classification: [] for classification in Classification
        }
        for item in self.sorted_evidence():
            grouped[item.classification].append(item)

        for classification in Classification:
            items = grouped[classification]
            if not items:
                continue
            lines.extend([f"## {CLASSIFICATION_TITLES[classification]}", ""])
            for item in items:
                source = f" ([source]({item.source_url}))" if item.source_url else ""
                lines.append(f"- **`{item.identifier}`** — {_single_line(item.summary)}{source}")
                if item.source_timestamp:
                    lines.append(f"  - Source timestamp: `{item.source_timestamp}`")
                if item.derived_from:
                    references = ", ".join(f"`{identifier}`" for identifier in item.derived_from)
                    lines.append(f"  - Derived from: {references}")
                if item.details:
                    details = json.dumps(
                        _normalise_json(item.details), sort_keys=True, ensure_ascii=False, separators=(",", ":")
                    )
                    lines.append(f"  - Details: `{details.replace('`', '\\`')}`")
            lines.append("")

        if self.errors:
            lines.extend(["## Collection errors", ""])
            for error in self.sorted_errors():
                source = f" ([source]({error.source_url}))" if error.source_url else ""
                lines.append(f"- **`{error.code}`** — {_single_line(error.message)}{source}")
            lines.append("")

        lines.extend(
            [
                "## Human decision boundary",
                "",
                "Human verification and decision remain required. This generated report does not decide readiness, evidence sufficiency, contract satisfaction, remediation, merge, publication or release.",
                "",
            ]
        )
        return "\n".join(lines)


def _normalise_json(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _normalise_json(value[key]) for key in sorted(value, key=str)}
    if isinstance(value, list):
        return [_normalise_json(item) for item in value]
    return value


def _single_line(value: str) -> str:
    return " ".join(value.split())


def _require_mapping(value: Any, path: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise EvidenceValidationError(f"{path} must be an object")
    return value


def _reject_unknown_keys(value: Mapping[str, Any], allowed: set[str], path: str) -> None:
    unknown = sorted(set(value) - allowed)
    if unknown:
        raise EvidenceValidationError(f"{path} contains unsupported fields: {', '.join(unknown)}")


def _require_string(value: Any, path: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise EvidenceValidationError(f"{path} must be a non-empty string")
    return value.strip()


def _optional_string(value: Any, path: str) -> str | None:
    if value is None:
        return None
    return _require_string(value, path)


def _validate_url(value: str, path: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise EvidenceValidationError(f"{path} must be an absolute http or https URL")
    return value


def _validate_timestamp(value: str, path: str) -> str:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise EvidenceValidationError(f"{path} must be an ISO-8601 timestamp") from exc
    return value


def _validate_sha(value: str, path: str) -> str:
    if not SHA_PATTERN.fullmatch(value):
        raise EvidenceValidationError(f"{path} must be a hexadecimal commit SHA")
    return value.lower()


def _validate_identifier(value: str, path: str) -> str:
    if not IDENTIFIER_PATTERN.fullmatch(value):
        raise EvidenceValidationError(
            f"{path} must start with an alphanumeric character and contain only alphanumerics, '.', '_', ':' or '-'"
        )
    return value


def parse_report(data: Mapping[str, Any]) -> EvidenceReport:
    root = _require_mapping(data, "root")
    _reject_unknown_keys(root, {"schema_version", "target", "collection", "evidence", "errors"}, "root")

    if root.get("schema_version") != SCHEMA_VERSION:
        raise EvidenceValidationError(f"schema_version must equal {SCHEMA_VERSION!r}")

    target_data = _require_mapping(root.get("target"), "target")
    _reject_unknown_keys(target_data, {"repository", "pull_request", "url", "linked_issue"}, "target")
    repository = _require_string(target_data.get("repository"), "target.repository")
    if not REPOSITORY_PATTERN.fullmatch(repository):
        raise EvidenceValidationError("target.repository must use owner/name form")
    pull_request = target_data.get("pull_request")
    if not isinstance(pull_request, int) or isinstance(pull_request, bool) or pull_request <= 0:
        raise EvidenceValidationError("target.pull_request must be a positive integer")
    target_url = _validate_url(_require_string(target_data.get("url"), "target.url"), "target.url")
    linked_issue = target_data.get("linked_issue")
    if linked_issue is not None and (
        not isinstance(linked_issue, int) or isinstance(linked_issue, bool) or linked_issue <= 0
    ):
        raise EvidenceValidationError("target.linked_issue must be a positive integer when provided")
    target = Target(repository, pull_request, target_url, linked_issue)

    collection_data = _require_mapping(root.get("collection"), "collection")
    _reject_unknown_keys(
        collection_data,
        {"started_at", "completed_at", "head_sha_start", "head_sha_end"},
        "collection",
    )
    collection = CollectionWindow(
        _validate_timestamp(
            _require_string(collection_data.get("started_at"), "collection.started_at"),
            "collection.started_at",
        ),
        _validate_timestamp(
            _require_string(collection_data.get("completed_at"), "collection.completed_at"),
            "collection.completed_at",
        ),
        _validate_sha(
            _require_string(collection_data.get("head_sha_start"), "collection.head_sha_start"),
            "collection.head_sha_start",
        ),
        _validate_sha(
            _require_string(collection_data.get("head_sha_end"), "collection.head_sha_end"),
            "collection.head_sha_end",
        ),
    )

    evidence_data = root.get("evidence")
    if not isinstance(evidence_data, list):
        raise EvidenceValidationError("evidence must be an array")
    if len(evidence_data) > MAX_EVIDENCE_ITEMS:
        raise EvidenceValidationError(f"evidence may contain at most {MAX_EVIDENCE_ITEMS} items")

    evidence: list[EvidenceItem] = []
    identifiers: set[str] = set()
    for index, raw_item in enumerate(evidence_data):
        path = f"evidence[{index}]"
        item_data = _require_mapping(raw_item, path)
        _reject_unknown_keys(
            item_data,
            {"id", "classification", "summary", "source_url", "source_timestamp", "derived_from", "details"},
            path,
        )
        identifier = _validate_identifier(_require_string(item_data.get("id"), f"{path}.id"), f"{path}.id")
        if identifier in identifiers:
            raise EvidenceValidationError(f"duplicate evidence id: {identifier}")
        identifiers.add(identifier)

        classification_value = _require_string(item_data.get("classification"), f"{path}.classification")
        try:
            classification = Classification(classification_value)
        except ValueError as exc:
            allowed = ", ".join(classification.value for classification in Classification)
            raise EvidenceValidationError(
                f"{path}.classification must be one of: {allowed}"
            ) from exc

        summary = _require_string(item_data.get("summary"), f"{path}.summary")
        source_url = _optional_string(item_data.get("source_url"), f"{path}.source_url")
        if classification is not Classification.DERIVED:
            if source_url is None:
                raise EvidenceValidationError(f"{path}.source_url is required for non-derived evidence")
            source_url = _validate_url(source_url, f"{path}.source_url")
        elif source_url is not None:
            source_url = _validate_url(source_url, f"{path}.source_url")

        source_timestamp = _optional_string(
            item_data.get("source_timestamp"), f"{path}.source_timestamp"
        )
        if source_timestamp is not None:
            source_timestamp = _validate_timestamp(source_timestamp, f"{path}.source_timestamp")

        raw_derived_from = item_data.get("derived_from", [])
        if not isinstance(raw_derived_from, list) or not all(
            isinstance(reference, str) and reference.strip() for reference in raw_derived_from
        ):
            raise EvidenceValidationError(f"{path}.derived_from must be an array of evidence IDs")
        derived_from = tuple(sorted({_validate_identifier(reference.strip(), f"{path}.derived_from") for reference in raw_derived_from}))
        if classification is Classification.DERIVED and not derived_from:
            raise EvidenceValidationError(f"{path}.derived_from is required for derived evidence")
        if classification is not Classification.DERIVED and derived_from:
            raise EvidenceValidationError(f"{path}.derived_from is only valid for derived evidence")

        details = item_data.get("details", {})
        if not isinstance(details, Mapping):
            raise EvidenceValidationError(f"{path}.details must be an object")
        details_size = len(json.dumps(details, sort_keys=True, ensure_ascii=False).encode("utf-8"))
        if details_size > MAX_DETAILS_BYTES:
            raise EvidenceValidationError(
                f"{path}.details exceeds the {MAX_DETAILS_BYTES}-byte limit"
            )

        evidence.append(
            EvidenceItem(
                identifier,
                classification,
                summary,
                source_url,
                source_timestamp,
                derived_from,
                details,
            )
        )

    for item in evidence:
        missing_references = sorted(set(item.derived_from) - identifiers)
        if missing_references:
            raise EvidenceValidationError(
                f"evidence item {item.identifier!r} references unknown evidence IDs: {', '.join(missing_references)}"
            )
        if item.identifier in item.derived_from:
            raise EvidenceValidationError(
                f"evidence item {item.identifier!r} may not derive from itself"
            )

    errors_data = root.get("errors", [])
    if not isinstance(errors_data, list):
        raise EvidenceValidationError("errors must be an array")
    if len(errors_data) > MAX_COLLECTION_ERRORS:
        raise EvidenceValidationError(f"errors may contain at most {MAX_COLLECTION_ERRORS} items")
    errors: list[CollectionError] = []
    for index, raw_error in enumerate(errors_data):
        path = f"errors[{index}]"
        error_data = _require_mapping(raw_error, path)
        _reject_unknown_keys(error_data, {"code", "message", "source_url"}, path)
        code = _validate_identifier(_require_string(error_data.get("code"), f"{path}.code"), f"{path}.code")
        message = _require_string(error_data.get("message"), f"{path}.message")
        source_url = _optional_string(error_data.get("source_url"), f"{path}.source_url")
        if source_url is not None:
            source_url = _validate_url(source_url, f"{path}.source_url")
        errors.append(CollectionError(code, message, source_url))

    return EvidenceReport(target, collection, tuple(evidence), tuple(errors))


def load_report(path: str) -> EvidenceReport:
    if path == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(path).read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise EvidenceValidationError(f"input is not valid JSON: {exc.msg}") from exc
    return parse_report(_require_mapping(data, "root"))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default="-", help="JSON input path, or '-' for stdin")
    parser.add_argument(
        "--format",
        choices=("json", "markdown"),
        default="markdown",
        help="output format",
    )
    args = parser.parse_args(argv)

    try:
        report = load_report(args.input)
    except (OSError, EvidenceValidationError) as exc:
        print(f"Evidence-pack validation failed: {exc}", file=sys.stderr)
        return 1

    output = report.render_json() if args.format == "json" else report.render_markdown()
    print(output, end="")
    return 0 if report.status is ReportStatus.COMPLETE else 2


if __name__ == "__main__":
    raise SystemExit(main())
