# Evidence-pack schema

Stage 3 introduces an experimental, read-only evidence model for assembling pull-request review facts without transferring approval authority.

The current increment defines the deterministic core only. It does **not** connect to GitHub, collect live pull-request data, post comments, update a pull-request body, change lifecycle state, recommend merge or authorise publication.

## Authority boundary

The generated report is an input to human review. It may describe collection state as complete, incomplete, conflicting or stale, but those terms do not mean that:

- the issue is ready;
- the implementation plan is approved;
- the contract is satisfied;
- validation is sufficient;
- remediation is acceptable;
- the pull request should merge; or
- publication or release is approved.

Every rendered report states that human verification and decision remain required.

## Schema version

The initial schema identifier is:

```text
evidence-pack/v1
```

The core accepts one structured JSON document for one repository pull request. Unknown fields are rejected so that misspelled or unreviewed semantics do not silently enter the evidence model.

## Document shape

```json
{
  "schema_version": "evidence-pack/v1",
  "target": {
    "repository": "owner/repository",
    "pull_request": 123,
    "url": "https://github.com/owner/repository/pull/123",
    "linked_issue": 122
  },
  "collection": {
    "started_at": "2026-07-11T08:00:00Z",
    "completed_at": "2026-07-11T08:00:05Z",
    "head_sha_start": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "head_sha_end": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  },
  "evidence": [
    {
      "id": "workflow.validation",
      "classification": "repository-observed",
      "summary": "The validation workflow completed successfully.",
      "source_url": "https://github.com/owner/repository/actions/runs/1",
      "source_timestamp": "2026-07-11T08:00:03Z",
      "details": {
        "conclusion": "success"
      }
    }
  ],
  "errors": []
}
```

## Evidence classifications

Every material evidence item has a stable identifier, one classification and a concise summary.

| Classification | Meaning | Provenance rule |
| --- | --- | --- |
| `repository-observed` | Retrieved directly from repository state, such as a head SHA, changed-file count or workflow result | Requires an absolute source URL |
| `contributor-reported` | Stated in an issue, plan, pull-request body or comment but not independently proved by collection | Requires an absolute source URL |
| `derived` | Mechanically computed from other evidence items | Requires one or more valid `derived_from` item IDs |
| `pending` | A declared result has not reached a final state | Requires an absolute source URL |
| `unavailable` | A source or result could not be accessed or does not exist | Requires an absolute source URL identifying the attempted evidence surface |
| `conflicting` | Sources disagree or cannot be reconciled safely | Requires an absolute source URL |

A derived item may not reference itself or an unknown item. Non-derived items without provenance fail validation.

## Collection status

The core derives a collection status mechanically. Status precedence is:

```text
head changed            -> stale
conflicting item exists -> conflicting
pending/unavailable/error/empty evidence -> incomplete
otherwise               -> complete
```

`complete` means only that the supplied evidence document is structurally valid, the head SHA remained stable, and no pending, unavailable, conflicting or collection-error state was represented. It is not an approval decision.

## Stale-head circuit breaker

The collection input records the pull-request head SHA at the beginning and end. If they differ, the output status is `stale` and the Markdown report displays a circuit-breaker warning.

The core does not silently combine evidence from different pull-request heads.

## Deterministic output

Equivalent valid inputs produce stable output because the core:

- sorts evidence by classification and stable identifier;
- sorts collection errors by code and message;
- normalises structured detail keys;
- emits canonical indented JSON with sorted keys; and
- renders Markdown sections in a fixed classification order.

Execution timestamps and observed repository identifiers are inputs. The deterministic core does not invent them.

## Bounded details and errors

Each evidence item may include a small JSON object under `details`. The core limits the encoded details size to prevent an evidence report from becoming a log archive.

Collection errors contain:

```json
{
  "code": "api.pagination",
  "message": "A required page could not be retrieved.",
  "source_url": "https://api.github.com/repos/owner/repository/pulls/123/files"
}
```

Any collection error makes the report incomplete. Error messages must not include credentials or sensitive data.

## Local CLI

The core is a local standard-library command:

```bash
python scripts/evidence_pack.py input.json --format markdown
python scripts/evidence_pack.py input.json --format json
```

Use `-` or omit the input path to read JSON from standard input.

Exit codes are:

| Exit code | Meaning |
| --- | --- |
| `0` | Valid input with collection status `complete` |
| `2` | Valid input with collection status `incomplete`, `conflicting` or `stale` |
| `1` | Invalid JSON, schema violation or input read failure |

The command performs no network access and has no GitHub write path. Output is written to standard output only.

## Current limitation

The current core validates and renders supplied structured evidence. Live GitHub collection, pagination, least-privilege workflow invocation and run artefact production belong to a later bounded execution-contract issue and are not yet implemented.
