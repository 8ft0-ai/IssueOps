# Stage 3 evidence-pack dogfood worklog

Status: pending evidence.

Record type: contemporaneous close-out worklog.

This worklog supports [Issue #82](https://github.com/8ft0-ai/IssueOps/issues/82), the prematurely merged [PR #83](https://github.com/8ft0-ai/IssueOps/pull/83), recovery [Issue #84](https://github.com/8ft0-ai/IssueOps/issues/84), and replacement dogfood [PR #85](https://github.com/8ft0-ai/IssueOps/pull/85).

The canonical `planning/delivery/` directory accepts completed records only. A final Stage 3 delivery record must not be created until the required live collector runs, comparison evidence and adoption decision exist.

## Current state

Stage 3 remains **delivering**. The deterministic core and manually invoked read-only collector are merged, but representative live dogfood and the adopt/adapt/reject decision remain incomplete.

No roadmap, delivery-log or graph entry claims Stage 3 is complete.

## Original intent

Stage 3 was shaped through [planning issue #75](https://github.com/8ft0-ai/IssueOps/issues/75) and the approved roadmap at `planning/roadmap/stage-03-read-only-evidence-pack-assistance.md`.

The outcome to prove is that a manually invoked, read-only capability can assemble a current, provenance-linked report for one pull request while separating observations from assertions, representing incomplete state honestly, making no repository mutation or approval decision, and preserving human merge and publication authority.

## Delivered implementation

- [Issue #76](https://github.com/8ft0-ai/IssueOps/issues/76) / [PR #77](https://github.com/8ft0-ai/IssueOps/pull/77) — approved roadmap and authority boundary.
- [Issue #78](https://github.com/8ft0-ai/IssueOps/issues/78) / [PR #79](https://github.com/8ft0-ai/IssueOps/pull/79) — `evidence-pack/v1`, deterministic rendering, classifications, provenance validation and tests.
- [Issue #80](https://github.com/8ft0-ai/IssueOps/issues/80) / [PR #81](https://github.com/8ft0-ai/IssueOps/pull/81) — standard-library GitHub REST collector and manual `workflow_dispatch` for one pull request.

The collector uses read-only permissions and REST `GET` requests, publishes only to the run summary and artefact, and makes no readiness, sufficiency, approval, merge or publication decision.

Implementation is not adoption proof.

## Premature merge incident

PR #83 was a draft, pending-evidence target but was merged before:

- pending-state and final-state collector runs;
- artefact inspection;
- assisted-versus-manual comparison;
- live authority audit; and
- adopt/adapt/reject decision.

Its `Closes #82` wording also auto-closed Issue #82 despite incomplete criteria. Issue #82 was reopened on 11 July 2026.

### Why no revert was required

PR #83 added only this worklog with `Status: pending evidence`. It did not mark Stage 3 complete, create a completed delivery record, record adoption, update the delivery log or graph, or authorise broader automation.

A revert would remove accurate evidence without restoring the review gate. Recovery therefore uses Issue #84 and draft PR #85.

## Replacement gate

[PR #85](https://github.com/8ft0-ai/IssueOps/pull/85) is the replacement open dogfood target. It intentionally contains no closing keyword for Issue #82 or #84.

The exact stable head SHA used for both live runs is recorded in PR #85's evidence body and Issue #84 immediately before dispatch. The branch must not change between the two collector runs.

PR #85 must remain draft until both reports are inspected and its groundedness review no longer recommends `Do not approve yet`.

## Existing implementation proof

- PR #79 workflow run `29144625519` and final-head reruns covered schema, rendering, classifications and non-complete exit behaviour.
- PR #81 collector run `29145444610` passed collector integration tests, core tests and compilation.
- PR #81 planning run `29145444585` passed planning, graph and freshness validation.
- PR #81 documentation run `29145444592` passed strict build and artefact upload; production deployment was skipped.
- Earlier PR #81 run `29145258244` exposed relative pagination-error provenance, fixed before approval.

## PR #83 validation observations

Initial head: `ccb18f35b10f148aaed0b591b3471ab0c20ea680`.

- Documentation run `29145873760` passed.
- Planning run `29145873768` failed because a pending record was placed under `planning/delivery/`, which accepts completed records only.
- Pending content was moved to `planning/closeout/` rather than fabricating completion.
- Corrected planning run `29145939973` passed planning, graph and freshness checks.
- Corrected documentation run `29145939972` passed strict build and artefact upload; production deployment was skipped.

The initial failure was a repository control working as designed.

## Manual evidence baseline

The bounded manual snapshot used seven source groups: issue contract; readiness and plan comments; PR metadata/body; changed files; workflow state; reviews/threads; and failure logs plus validator source.

The observation ran from approximately `2026-07-11T08:17:16Z` to `2026-07-11T08:20:21Z`, about **3 minutes 5 seconds**, excluding implementation time.

It found one changed file, no reviews or unresolved threads, the initial planning failure, its repository-rule cause and the corrected successful state. No bounded omission or transcription error was identified, but multiple reads and human interpretation were required.

## Required live dogfood

PR #85 must be collected twice on the same head:

| Snapshot | Required workflow state | Collector run | Artefact | Report status | Inspection |
| --- | --- | --- | --- | --- | --- |
| Pending | A relevant PR workflow queued or running | Pending | Pending | Expected `incomplete` when pending evidence exists | Pending |
| Final | Relevant PR workflows completed | Pending | Pending | To be observed | Pending |

Retain each run URL/ID, artefact name/ID, target head SHA, report status and direct provenance links. Successful workflow execution means only that collection and report production completed safely.

## Report inspection

For both reports verify:

- [ ] repository, PR, linked issue and head SHA are correct;
- [ ] observed and contributor-reported evidence are separated;
- [ ] pending evidence is not inferred as success;
- [ ] final conclusions remain observations, not recommendations;
- [ ] changed-file and workflow sources have direct links;
- [ ] human-decision warnings remain prominent;
- [ ] no repository mutation occurred; and
- [ ] the state transition is visible without rewriting PR #85.

## Manual versus assisted comparison

| Measure | Manual | Assisted |
| --- | --- | --- |
| Steps | Seven source groups plus interpretation | Pending |
| Bounded effort | About 3 minutes 5 seconds | Pending |
| Omitted fields | None identified | Pending |
| Incorrect transcription | None identified | Pending |
| Human interpretation | Required | Pending |
| Review quality weakened | Not assessed | Pending |

The generated report cannot replace substantive interpretation of validation or contract satisfaction.

## Safe-failure evidence

Tests cover inaccessible targets, partial API failure, excessive pagination, conflicting issue links, validly empty surfaces, pending checks/jobs, failed checks as observations, moving-head stale protection and bounded local output.

Live dogfood must still prove that the default-branch workflow produces retrievable run-scoped artefacts.

## Authority-boundary audit

Preliminary evidence:

- [x] manual invocation only;
- [x] read-only contents, pull-request, issue, check and action permissions;
- [x] REST `GET` requests only;
- [x] output limited to run summary and artefact;
- [x] no GitHub mutation method;
- [x] collection status separate from approval advice; and
- [x] human-decision warnings rendered.

Live audit:

- [ ] actual run permissions match declarations;
- [ ] output appears only in run-scoped locations;
- [ ] target issue and PR remain unchanged;
- [ ] no credentials or sensitive logs appear; and
- [ ] repeated runs create separate artefacts without duplicate repository actions.

## Limitations and lessons

Current limitations include environment-specific dispatch authority, no unresolved inline-thread collection, bounded pagination/run collection, seven-day artefact retention and continued need for human judgement.

The premature merge demonstrates that draft status and `Do not approve yet` are advisory unless merge controls or human discipline enforce them. No repository-setting change is authorised here, but this must inform the final decision.

## Decision

Decision: **pending live dogfood**.

No adopt, adapt or reject recommendation is valid until both reports, the comparison and live authority audit are complete.

## Implications

No Stage 4 issue or speculative automation backlog should be created. Any next activity must begin as a planning question after Stage 3 close-out.