# IssueOps historical evidence index

This directory is the canonical navigation surface for historical project evidence that should remain accessible but is not current user-facing Tutorial, How-to, Reference or Explanation content.

Git history preserves the exact original records. Roadmap and delivery files provide maintained intent and outcome summaries. This index links those sources without copying them into the substantive documentation tree.

## Evidence boundary

```text
planning/roadmap/       -> intended outcomes and boundaries
planning/delivery/      -> what actually shipped and what proved it
planning/evidence/      -> curated links to immutable historical snapshots
GitHub history          -> exact source record, issues, PRs, commits and runs
docs/                   -> current user-facing guidance and compatibility URLs
```

Compatibility pages under `docs/` preserve high-value public paths. They are migration surfaces, not a fifth documentation mode and not canonical copies of project records.

## Pre-migration snapshot

The lossless snapshot for the records below is commit [`318d4b4f7c9490365033ff8363d42cd940d6b900`](https://github.com/8ft0-ai/IssueOps/tree/318d4b4f7c9490365033ff8363d42cd940d6b900), the verified `main` state immediately before Stage 4 project-record boundary changes.

## Roadmap

Current canonical intent:

- [Roadmap index](../roadmap/index.md)
- [Stage 4 — Diátaxis documentation architecture](../roadmap/stage-04-diataxis-documentation-architecture.md)

Immutable former public summary:

- [`docs/roadmap.md` at the pre-migration snapshot](https://github.com/8ft0-ai/IssueOps/blob/318d4b4f7c9490365033ff8363d42cd940d6b900/docs/roadmap.md)

Public compatibility path:

- [`docs/roadmap.md`](../../docs/roadmap.md)

## Stage 1 workflow snapshot

Maintained stage context:

- [Stage 1 retrospective roadmap](../roadmap/stage-01-manual-execution-contract-foundation.md)
- [Stage 1 delivery record](../delivery/stage-01-manual-execution-contract-foundation.md)

Immutable original workflow page:

- [`docs/issueops.md` at the pre-migration snapshot](https://github.com/8ft0-ai/IssueOps/blob/318d4b4f7c9490365033ff8363d42cd940d6b900/docs/issueops.md)

Public compatibility path:

- [`docs/issueops.md`](../../docs/issueops.md)

The current operating model is served by the user-facing [documentation home](../../docs/index.md) and [operating protocol](../../docs/issueops-protocol.md), not the Stage 1 snapshot.

## Stage 2 contributor-usability review

Maintained stage context:

- [Stage 2 retrospective roadmap](../roadmap/stage-02-operating-model-hardening.md)
- [Stage 2 delivery record](../delivery/stage-02-operating-model-hardening.md)

Immutable original walkthrough:

- [`docs/contributor-usability-review.md` at the pre-migration snapshot](https://github.com/8ft0-ai/IssueOps/blob/318d4b4f7c9490365033ff8363d42cd940d6b900/docs/contributor-usability-review.md)

Public compatibility path:

- [`docs/contributor-usability-review.md`](../../docs/contributor-usability-review.md)

The current first-time-contributor journey is the [first IssueOps tutorial](../../docs/tutorials/first-issueops-change.md).

## Release snapshots

### `v0.1.0` — Stage 1 manual baseline

- [Stage 1 delivery record](../delivery/stage-01-manual-execution-contract-foundation.md)
- [Immutable former release page](https://github.com/8ft0-ai/IssueOps/blob/318d4b4f7c9490365033ff8363d42cd940d6b900/docs/releases/stage-1.md)
- [Public compatibility path](../../docs/releases/stage-1.md)

### `v0.2.0` — recommended stable baseline

- [Stage 2 delivery record](../delivery/stage-02-operating-model-hardening.md)
- [Immutable former release page](https://github.com/8ft0-ai/IssueOps/blob/318d4b4f7c9490365033ff8363d42cd940d6b900/docs/releases/stage-2.md)
- [Public compatibility path](../../docs/releases/stage-2.md)

`v0.2.0` remains the recommended stable IssueOps operating baseline.

### Proposed `v0.3.0-alpha.1` — Stage 3 experimental snapshot

- [Stage 3 delivery record](../delivery/stage-03-read-only-evidence-pack-assistance.md)
- [Immutable former prerelease page](https://github.com/8ft0-ai/IssueOps/blob/318d4b4f7c9490365033ff8363d42cd940d6b900/docs/releases/stage-3-alpha.md)
- [Public compatibility path](../../docs/releases/stage-3-alpha.md)

Stage 3 closed with **Adapt**. The alpha remains experimental and does not replace the stable `v0.2.0` baseline or grant new approval, merge or automation authority.

## Publishing evidence

Current procedure:

- [Publish and verify the documentation site](../../docs/how-to/publish-and-verify-documentation-site.md)

Maintained delivery evidence:

- [Stage 2 delivery record](../delivery/stage-02-operating-model-hardening.md)
- GitHub Actions and Pages history linked from the detailed audit trail.

Immutable former mixed procedure/history page:

- [`docs/publishing.md` at the pre-migration snapshot](https://github.com/8ft0-ai/IssueOps/blob/318d4b4f7c9490365033ff8363d42cd940d6b900/docs/publishing.md)

## Compatibility decisions

| Former path | Treatment | Canonical destination |
| --- | --- | --- |
| `docs/roadmap.md` | concise compatibility page | `planning/roadmap/` plus this evidence index |
| `docs/issueops.md` | concise compatibility page | current Diátaxis guidance; immutable Stage 1 snapshot linked here |
| `docs/contributor-usability-review.md` | concise compatibility page | Stage 2 delivery record; immutable walkthrough linked here |
| `docs/releases/stage-1.md` | concise compatibility page | Stage 1 delivery record; immutable release snapshot linked here |
| `docs/releases/stage-2.md` | concise compatibility page | Stage 2 delivery record; immutable release snapshot linked here |
| `docs/releases/stage-3-alpha.md` | concise compatibility page | Stage 3 delivery record; immutable alpha snapshot linked here |
| `docs/publishing.md` | current-procedure compatibility page | publishing How-to; historical evidence linked here and in Stage 2 delivery |

No project record was duplicated into a Diátaxis mode. Removing a compatibility page requires a separate URL and external-link review.
