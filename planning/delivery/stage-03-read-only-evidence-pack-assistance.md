# Stage 3 — Read-only evidence-pack assistance

Status: pending evidence.

Record type: contemporaneous.

This record is the dogfood and close-out surface for [issue #82](https://github.com/8ft0-ai/IssueOps/issues/82). It must not be changed to `completed` and must not record an adopt, adapt or reject decision until the required live collector runs and comparison evidence exist.

## Original documented intent

Stage 3 was shaped through [planning issue #75](https://github.com/8ft0-ai/IssueOps/issues/75) and recorded in `planning/roadmap/stage-03-read-only-evidence-pack-assistance.md`.

The approved outcome was to prove that a manually invoked, read-only capability could assemble a current, structured and provenance-linked evidence report for one pull request while:

- preserving the written issue and pull-request record as authority;
- separating repository-observed facts from contributor assertions;
- representing pending, unavailable, conflicting and stale evidence honestly;
- making no repository mutation or approval decision; and
- leaving evidence interpretation, merge and publication authority with a human.

The roadmap defined four ordered slices: formalise the roadmap, define the deterministic core, add manual GitHub integration, then dogfood, measure and close out.

## Retrospective interpretation

Not applicable yet. Stage 3 was planned contemporaneously and remains open while live proof is pending.

This record may later explain material differences between the approved roadmap and actual delivery, but it must not rewrite the original intent to match the outcome.

## What shipped

The first three ordered slices are merged:

### Approved roadmap

- [Issue #76](https://github.com/8ft0-ai/IssueOps/issues/76) and [PR #77](https://github.com/8ft0-ai/IssueOps/pull/77) recorded the approved Stage 3 roadmap and authority boundary.

### Deterministic evidence core

- [Issue #78](https://github.com/8ft0-ai/IssueOps/issues/78) and [PR #79](https://github.com/8ft0-ai/IssueOps/pull/79) added `evidence-pack/v1`, deterministic JSON and Markdown rendering, explicit evidence classifications, collection-state semantics, fail-closed validation, fixtures, tests and read-only CI.

### Manually invoked GitHub integration

- [Issue #80](https://github.com/8ft0-ai/IssueOps/issues/80) and [PR #81](https://github.com/8ft0-ai/IssueOps/pull/81) added a standard-library GitHub REST collector and a manual `workflow_dispatch` workflow for one pull request in the current repository.
- The workflow has read permissions for contents, pull requests, issues, checks and actions.
- Generated output is limited to the individual run summary and a seven-day JSON and Markdown artefact.
- The collector has no GitHub mutation method and makes no readiness, evidence-sufficiency, approval, merge or publication decision.

No adoption claim is made by this section. Delivery of an implementation path is not proof that the capability is useful enough to adopt.

## Linked issues and pull requests

- [Planning issue #75](https://github.com/8ft0-ai/IssueOps/issues/75) — selected and approved the bounded capability.
- [Issue #76](https://github.com/8ft0-ai/IssueOps/issues/76) / [PR #77](https://github.com/8ft0-ai/IssueOps/pull/77) — formalised the roadmap.
- [Issue #78](https://github.com/8ft0-ai/IssueOps/issues/78) / [PR #79](https://github.com/8ft0-ai/IssueOps/pull/79) — deterministic evidence core.
- [Issue #80](https://github.com/8ft0-ai/IssueOps/issues/80) / [PR #81](https://github.com/8ft0-ai/IssueOps/pull/81) — manually invoked read-only GitHub integration.
- [Issue #82](https://github.com/8ft0-ai/IssueOps/issues/82) — dogfood, measurement and close-out contract.
- Close-out pull request: pending creation from `feature/82-dogfood-and-close-stage-3`.

## Proof runs, checks and artefacts

### Existing implementation proof

Repository-native validation already proved the deterministic core and integration implementation:

- PR #79 evidence-pack workflow run `29144625519` and final-head reruns proved the schema, rendering, classification, provenance and non-complete exit behaviour.
- PR #81 collector workflow run `29145444610` proved fake-transport integration coverage, existing core compatibility and bytecode compilation.
- PR #81 planning workflow run `29145444585` passed planning, graph and freshness validation.
- PR #81 documentation workflow run `29145444592` passed strict MkDocs build and artefact upload while production deployment was skipped.
- An earlier PR #81 collector run `29145258244` exposed relative pagination-error provenance. The implementation was corrected to retain the absolute API page URL before approval.

### Required live dogfood — pending

The representative close-out pull request must be collected twice on the same head:

| Snapshot | Required state | Workflow run | Artefact | Report status | Inspection |
| --- | --- | --- | --- | --- | --- |
| Pending snapshot | At least one relevant PR workflow pending or incomplete | Pending | Pending | Expected `incomplete` when pending evidence exists | Pending |
| Final snapshot | Relevant PR workflows in final state | Pending | Pending | To be observed | Pending |

The record must capture the workflow-run URL and ID, artefact name and ID, target head SHA, report status and direct provenance links. A successful Actions run means only that collection and report production completed safely.

### Required report inspection — pending

For each live report, verify:

- [ ] the target repository, pull request, linked issue and head SHA are correct;
- [ ] repository-observed and contributor-reported evidence are separated;
- [ ] pending evidence is not inferred as success;
- [ ] final check and workflow conclusions are represented as observations rather than recommendations;
- [ ] changed-file scope and workflow sources have direct links;
- [ ] generated and human-decision warnings are prominent;
- [ ] no issue, pull-request, review, label, branch, file, merge or repository-setting mutation occurred; and
- [ ] the two reports show the validation-state change without rewriting the pull request.

## Manual versus assisted evidence assembly

Use the same required fields for both paths: issue contract, readiness and plan, PR metadata and body, changed files, head SHA, workflow/check state, reviews, caveats and source links.

| Measure | Manual path | Assisted path |
| --- | --- | --- |
| Steps performed | Pending measurement | Pending live collector runs |
| Bounded elapsed effort | Pending measurement | Pending live collector runs |
| Omitted fields | Pending comparison | Pending comparison |
| Incorrectly transcribed fields | Pending comparison | Pending comparison |
| Human interpretation still required | Pending observation | Pending observation |
| Review quality weakened | Pending decision | Pending decision |

The comparison must not invent precision. A bounded wall-clock observation or a clearly stated step-count comparison is acceptable when exact timing is unavailable.

## Safe-failure and recovery evidence

Repository-native tests currently cover:

- inaccessible or unresolved target failure before report construction;
- partial API failure after target resolution producing an incomplete report;
- excessive pagination producing a bounded collection error;
- conflicting same-repository issue references producing conflicting evidence;
- validly empty comments, reviews, checks and workflow runs;
- pending checks and jobs producing incomplete evidence;
- final failed checks remaining repository-observed facts;
- a moving head activating the stale-head circuit breaker; and
- local output limited to the specified report directory.

Live dogfood must confirm the default-branch workflow can run and produce retrievable artefacts. It need not reproduce every deterministic failure fixture through live destructive or artificial repository changes.

## Authority-boundary audit

### Preliminary implementation evidence

- [x] Collection trigger is manual only.
- [x] Workflow permissions are read-only: `contents`, `pull-requests`, `issues`, `checks` and `actions`.
- [x] The collector uses GitHub REST `GET` requests only.
- [x] Generated output is limited to the run summary and run artefact.
- [x] The collector has no issue, PR, review, label, branch, commit, file, merge, deployment, release or settings mutation method.
- [x] Collection status is distinct from approval, contract satisfaction and merge recommendation.
- [x] Human-decision warnings are part of the deterministic output.

### Live audit — pending

- [ ] run permissions match the declared workflow permissions;
- [ ] output appears only in the selected workflow run and artefact;
- [ ] the target issue and pull request remain unchanged by collection;
- [ ] no credential or sensitive log content appears in the report; and
- [ ] repeated collection creates separate run-scoped artefacts without duplicate repository actions.

## Intended versus actual delivery

Pending close-out evidence.

Known observations so far:

- The stage remained within the approved one-repository, one-pull-request, read-only boundary.
- Implementation was split into the approved ordered slices rather than combining schema, API integration and adoption proof.
- Repository-native testing exposed and corrected one provenance defect before live dogfood.
- Unresolved review-thread collection and workflow-log inspection remain outside scope as planned.

## Observed limitations and friction

Current known limitations:

- Live workflow dispatch must occur from an environment with Actions write authority; the connected toolset used for this close-out can inspect but not dispatch workflows.
- The collector does not include unresolved inline review-thread state.
- Workflow job collection is bounded to the newest twenty runs and page collection is bounded to twenty pages; exceeding a bound produces an incomplete report.
- A generated report reduces collection work but cannot decide whether evidence is sufficient or interpret the substantive quality of a change.
- Run artefacts are ephemeral and currently retained for seven days, so the durable delivery record must preserve the relevant identifiers and findings rather than depend on permanent artefact availability.

Additional friction and unintended consequences remain pending live use.

## Boundaries preserved

Stage 3 has not authorised:

- automatic pull-request or scheduled invocation;
- automatic issue readiness or implementation-plan approval;
- lifecycle transitions or label changes;
- remediation classification;
- approval or merge recommendations;
- auto-merge or repository-setting changes;
- autonomous publication or deployment decisions;
- cross-repository collection; or
- a broader agent-orchestration platform.

Written repository evidence remains canonical and human review remains required.

## Decisions and lessons

Decision: **pending live dogfood**.

No adopt, adapt or reject recommendation is valid until the two live reports, manual comparison and live authority audit are recorded.

Preliminary lessons:

- Separating evidence semantics from API collection made failure behaviour testable before granting live read access.
- Collection completeness and approval readiness must remain separate concepts.
- Provenance requirements should fail closed; the pagination-source defect found in PR #81 demonstrates why.
- A read-only capability can still create governance risk if generated output is mistaken for a decision, so warnings and classified evidence remain material controls.

## Implications for the next stage

Pending close-out decision.

No Stage 4 implementation issue or speculative automation backlog should be created from this record. If Stage 3 is adopted or adapted, the next activity is a planning question about whether evidence from broader use justifies advisory lifecycle visibility, bounded post-merge reporting or no further automation.