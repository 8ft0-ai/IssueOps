# Stage 4 — Diátaxis documentation architecture

Status: completed.

Record type: contemporaneous.

Approved through [planning issue #93](https://github.com/8ft0-ai/IssueOps/issues/93) and formalised by [PR #95](https://github.com/8ft0-ai/IssueOps/pull/95) on 12 July 2026.

The exact approved roadmap before delivery and close-out is preserved at merge commit [`f22a0ec04eb16ad1f5c28ebe8b8f34d1618e4640`](https://github.com/8ft0-ai/IssueOps/blob/f22a0ec04eb16ad1f5c28ebe8b8f34d1618e4640/planning/roadmap/stage-04-diataxis-documentation-architecture.md). This completed status record summarises the approved intent and links actual delivery separately; it does not rewrite later findings as original plans.

Actual delivery and proof: [Stage 4 delivery record](../delivery/stage-04-diataxis-documentation-architecture.md).

## Problem statement

The approved roadmap identified that accurate IssueOps guidance was organised around internal process components and mixed learning, task, reference, explanation and historical needs. Readers had to understand the repository taxonomy before finding the right kind of help, and the canonical protocol had become a long path for small changes.

Stage 4 addressed documentation architecture rather than missing content.

## Outcome to prove

The approved outcome was to prove four explicit reader paths:

- **Tutorials** for guided learning;
- **How-to guides** for completing tasks;
- **Reference** for exact rules, formats and evidence requirements; and
- **Explanation** for concepts, decisions and trade-offs.

The stage also had to prove that project records remained outside the substantive tree, high-value URLs remained accessible, stable and experimental claims stayed accurate, and human approval and merge authority remained unchanged.

Close-out result: proved. The final decision is **Adopt**.

## Non-goals

The completed stage did not introduce:

- automatic agent execution, readiness decisions or lifecycle transitions;
- branch-protection, required-check, permission or repository-setting changes;
- auto-merge configuration changes;
- Stage 3 collector, evidence-schema or workflow changes;
- operational evidence-assistance implementation;
- application-code changes;
- wiki reorganisation;
- a new MkDocs theme or redirect plugin;
- movement of tests, fixtures, scripts, workflows, generated artefacts or subsystem material into `docs/`;
- a fifth `Project records` documentation mode; or
- speculative Stage 5 implementation work.

## Operating and autonomy boundary

Stage 4 changed documentation architecture only.

It preserved the issue as the execution contract, readiness and planning before branch creation, one issue-scoped branch, safe repository operations, change-specific validation, pull requests as evidence packs, grounded review, human approval and merge authority, and explicit post-merge verification.

Delegated batch authority permitted qualifying Stage 4 PRs to merge after all gates passed. It did not remove those gates or configure platform auto-merge.

## Target workflow or target state

The delivered repository state is:

```text
README.md                      -> repository overview and entry links
AGENTS.md                      -> agent operating rules

docs/
├── index.md                   -> documentation home
├── tutorials/                 -> guided learning
├── how-to/                    -> task procedures
├── reference/                 -> exact rules and formats
└── explanation/               -> rationale and trade-offs

planning/                      -> roadmap, delivery, evidence and graph records
tests/                         -> tests and fixtures
scripts/                       -> repository tooling
.github/                       -> workflows and GitHub configuration
```

Temporary compatibility pages remain under `docs/` only to preserve high-value paths and point readers to current guidance or immutable history. They are not a fifth mode or duplicate project records.

Canonical ownership is:

1. Reference owns normative facts.
2. How-to guides own task sequence.
3. Tutorials optimise for a reliable learning experience.
4. Explanation owns rationale and introduces no hidden requirements.
5. Examples are illustrative rather than normative.
6. Planning records own intent, delivery and historical evidence.
7. README and AGENTS remain concise entry and operating surfaces.

## Acceptance gates

Architecture and scope:

- [x] MkDocs presents explicit Tutorials, How-to, Reference and Explanation paths.
- [x] `docs/` contains user-facing Diátaxis content plus deliberate compatibility files.
- [x] Planning, delivery, test, script and workflow artefacts remain outside the substantive tree.
- [x] Root repository entry files retain their roles.
- [x] Every substantive user-facing page has one primary mode.
- [x] Project history remains accessible without a fifth documentation mode.

Reader journeys:

- [x] A first-time contributor can find and follow the 12-step tutorial without hidden chat context.
- [x] Tutorial steps expose visible expected outcomes and link to deeper modes.
- [x] Active contributors can directly find contract, readiness, plan, operation, validation, PR and remediation guidance.
- [x] Reviewers can directly find fields, evidence requirements, validation rules, recommendations, merge blockers and authority boundaries.
- [x] Maintainers can understand the thesis, planning/execution split, evidence/approval split, human authority and manual-first rationale without procedural reading.

Quality and compatibility:

- [x] Strict MkDocs builds passed throughout delivery.
- [x] Final representative site inspection checked 57 HTML pages and 3,076 internal links with zero missing targets.
- [x] Stable-versus-experimental claims remain accurate.
- [x] High-value URLs are preserved through labelled compatibility pages and immutable snapshots.
- [x] Documentation-currency and contradictory-guidance reviews passed.
- [x] No unsupported automation or governance claim was introduced.

Close-out:

- [x] Intended and actual delivery are recorded separately.
- [x] Issues, PRs, proof, limitations, compatibility decisions and deferred work are linked.
- [x] Final decision recorded: **Adopt**.
- [x] Issue #90 remains independently governed and shaping-only.

## Proposed implementation slices

The approved dependency order was delivered through:

1. architecture and front door — issue #97 / PR #105;
2. first tutorial — issue #98 / PR #106;
3. execution-contract guidance separation — issue #99 / PR #107;
4. PR evidence and review separation — issue #100 / PR #108;
5. safe-operation and validation separation — issue #101 / PR #109;
6. project-record boundary — issue #102 / PR #110;
7. canonical protocol simplification — issue #103 / PR #111; and
8. usability proof and close-out — issue #104 / close-out PR.

Detailed actual delivery belongs in the [delivery record](../delivery/stage-04-diataxis-documentation-architecture.md), not in this intent record.

## Risks and controls

The roadmap controls were applied as follows:

- cosmetic taxonomy risk was controlled through four recorded audience walkthroughs;
- safety loss through over-splitting was controlled by preserving the complete lifecycle map and canonical Reference owners;
- duplicated rules were controlled through explicit content ownership and compatibility pages;
- link breakage was controlled through incremental migration, strict builds, immutable snapshots and final generated-site inspection;
- project-record drift was controlled through `planning/evidence/index.md` and removal of a fifth substantive mode;
- broad rewrites were controlled through sequential issue-scoped PRs; and
- Stage 5 scope was controlled by keeping issue #90 shaping-only.

Remaining limitations are recorded in the delivery record rather than hidden here.

## Definition of done

Stage 4 is complete because:

- all approved implementation slices are merged;
- the four reader journeys pass representative repository-grounded walkthroughs;
- canonical source ownership and compatibility treatment are explicit;
- strict documentation and planning validation pass for close-out;
- actual delivery, limitations and preserved boundaries are recorded separately; and
- the final evidence-based decision is **Adopt**.

## Likely next decision boundary

Issue [#90](https://github.com/8ft0-ai/IssueOps/issues/90) may continue shaping a possible Stage 5 — Operational evidence assistance.

Stage 4 provides its documentation architecture dependency, but does not approve Stage 5, create an implementation backlog or change the proposed read-only, human-triggered and human-decision boundaries. Any future roadmap must be independently reviewed and approved.