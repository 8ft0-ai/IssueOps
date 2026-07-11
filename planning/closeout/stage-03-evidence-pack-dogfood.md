# Stage 3 evidence-pack dogfood worklog

Status: pending evidence.

Record type: contemporaneous close-out worklog.

This worklog supports [Issue #82](https://github.com/8ft0-ai/IssueOps/issues/82), the prematurely merged [PR #83](https://github.com/8ft0-ai/IssueOps/pull/83), and recovery [Issue #84](https://github.com/8ft0-ai/IssueOps/issues/84).

The canonical `planning/delivery/` directory accepts completed delivery records only. A final Stage 3 delivery record must not be created there until the required live collector runs, comparison evidence and adoption decision exist.

## Current state

Stage 3 remains **delivering**. The first three ordered slices are merged, but representative live dogfood and the adopt/adapt/reject decision remain incomplete.

No roadmap, delivery-log or graph entry currently claims that Stage 3 is complete.

## Original documented intent

Stage 3 was shaped through [planning issue #75](https://github.com/8ft0-ai/IssueOps/issues/75) and the approved roadmap at `planning/roadmap/stage-03-read-only-evidence-pack-assistance.md`.

The intended outcome is to prove that a manually invoked, read-only capability can assemble a current, provenance-linked evidence report for one pull request while:

- preserving written repository evidence as the authority;
- separating repository-observed facts from contributor assertions;
- representing pending, unavailable, conflicting and stale evidence honestly;
- making no repository mutation or approval decision; and
- leaving interpretation, merge and publication authority with a human.

## Delivered implementation

The first three ordered slices are merged:

- [Issue #76](https://github.com/8ft0-ai/IssueOps/issues/76) / [PR #77](https://github.com/8ft0-ai/IssueOps/pull/77) — approved roadmap and authority boundary.
- [Issue #78](https://github.com/8ft0-ai/IssueOps/issues/78) / [PR #79](https://github.com/8ft0-ai/IssueOps/pull/79) — `evidence-pack/v1`, deterministic JSON and Markdown rendering, classifications, provenance validation and tests.
- [Issue #80](https://github.com/8ft0-ai/IssueOps/issues/80) / [PR #81](https://github.com/8ft0-ai/IssueOps/pull/81) — standard-library GitHub REST collector and manual `workflow_dispatch` for one pull request.

The collector has read-only permissions, uses GitHub REST `GET` requests, publishes only to the individual run summary and run artefact, and makes no readiness, sufficiency, approval, merge or publication decision.

Delivery of the implementation path is not proof that the capability should be adopted.

## Premature merge incident

PR #83 was intentionally a draft, pending-evidence close-out target. It was merged before:

- a pending-state collector run existed;
- a final-state collector run existed;
- generated artefacts were inspected;
- the assisted-versus-manual comparison was complete;
- the live authority audit was complete; or
- an adopt/adapt/reject decision was made.

Its body contained `Closes #82`, so GitHub also auto-closed Issue #82 despite incomplete acceptance criteria. Issue #82 was reopened on 11 July 2026.

### Why no revert was required

The merged change added only this worklog and explicitly retained `Status: pending evidence`. It did not:

- mark Stage 3 complete;
- create a completed delivery record;
- record an adoption decision;
- update the delivery log or graph; or
- authorise broader automation.

Reverting it would remove accurate evidence without restoring the missing review gate. Recovery therefore uses a new bounded issue and replacement draft PR rather than a revert.

## Recovery path

[Issue #84](https://github.com/8ft0-ai/IssueOps/issues/84) restores the open review and dogfood gate.

The replacement PR created from `feature/84-recover-stage-3-closeout` is the new representative target. Its number and stable head SHA will be recorded here before live collection.

The replacement PR must remain draft until both live reports are inspected and its pre-approval groundedness review no longer recommends `Do not approve yet`.

## Existing implementation proof

Repository-native checks already prove the deterministic core and bounded integration:

- PR #79 evidence workflow run `29144625519` and final-head reruns covered schema, rendering, classifications and non-complete exit behaviour.
- PR #81 collector workflow run `29145444610` passed collector integration tests, existing core tests and compilation.
- PR #81 planning workflow run `29145444585` passed planning, graph and freshness validation.
- PR #81 documentation workflow run `29145444592` passed strict MkDocs build and artefact upload; production deployment was skipped.
- Earlier PR #81 run `29145258244` exposed relative pagination-error provenance, which was fixed before approval.

## PR #83 observations

Initial PR #83 head: `ccb18f35b10f148aaed0b591b3471ab0c20ea680`.

- Documentation run `29145873760` passed.
- Planning run `29145873768` failed because a pending record was placed under `planning/delivery/`, where validation permits completed records only.
- The pending content was moved to `planning/closeout/` rather than fabricating completion.
- Corrected planning run `29145939973` passed planning, graph and freshness checks.
- Corrected documentation run `29145939972` passed strict build and artefact upload; production deployment was skipped.

The failure was a repository control working as designed.

## Manual evidence baseline

The bounded manual snapshot used seven source groups:

1. Issue #82 contract.
2. Readiness, plan and safe-operation comments.
3. PR metadata and evidence body.
4. Changed-file scope.
5. Workflow runs and conclusions.
6. Reviews and unresolved review threads.
7. Failure logs and validator source.

The observation ran from approximately `2026-07-11T08:17:16Z` to `2026-07-11T08:20:21Z`, about **3 minutes 5 seconds**, excluding implementation time.

The manual path found one changed file, no reviews or unresolved threads, the initial planning failure, its repository-rule cause and the corrected successful validation state. No bounded field omission or transcription error was identified, but multiple reads and human source interpretation were required.

## Required live dogfood

The replacement PR must be collected twice on the same stable head:

| Snapshot | Required workflow state | Collector run | Artefact | Report status | Inspection |
| --- | --- | --- | --- | --- | --- |
| Pending snapshot | At least one relevant PR workflow queued or running | Pending | Pending | Expected `incomplete` when pending evidence is present | Pending |
| Final snapshot | Relevant PR workflows completed | Pending | Pending | To be observed | Pending |

For each run, retain:

- workflow run URL and ID;
- artefact name and ID;
- target pull request and head SHA;
- report collection status; and
- direct provenance links.

A successful Actions run means only that collection and report production completed safely.

## Required report inspection

For both reports verify:

- [ ] repository, pull request, linked issue and head SHA are correct;
- [ ] repository-observed and contributor-reported evidence remain separated;
- [ ] pending evidence is not inferred as success;
- [ ] final conclusions remain observations rather than recommendations;
- [ ] changed-file and workflow sources have direct links;
- [ ] generated and human-decision warnings remain prominent;
- [ ] no issue, PR, review, label, branch, file, merge or setting mutation occurred; and
- [ ] the state transition is visible without rewriting the target PR.

## Manual versus assisted comparison

| Measure | Manual path | Assisted path |
| --- | --- | --- |
| Steps performed | Seven source groups plus interpretation | Pending live collector runs |
| Bounded elapsed effort | About 3 minutes 5 seconds | Pending |
| Omitted fields | None identified in bounded baseline | Pending |
| Incorrect transcription | None identified; reconciliation was manual | Pending |
| Human interpretation required | Yes | Pending |
| Review quality weakened | Not yet assessed | Pending |

The comparison must not invent precision. The generated report cannot replace substantive interpretation of validation or contract satisfaction.

## Safe-failure evidence

Repository-native tests cover:

- inaccessible target failure before report construction;
- partial API failure producing incomplete evidence;
- excessive pagination producing a bounded error;
- conflicting linked issues producing conflicting evidence;
- validly empty evidence surfaces;
- pending checks and jobs;
- final failed checks remaining observed facts;
- moving-head stale protection; and
- output limited to the selected local directory.

Live dogfood must still prove that the default-branch workflow produces retrievable run-scoped artefacts.

## Authority-boundary audit

Preliminary implementation evidence:

- [x] invocation is manual only;
- [x] permissions are read-only: contents, pull requests, issues, checks and actions;
- [x] the client uses REST `GET` requests only;
- [x] output is limited to run summary and artefact;
- [x] no GitHub mutation method exists in the collector;
- [x] collection status is distinct from approval and merge advice; and
- [x] human-decision warnings are rendered.

Live audit remains pending:

- [ ] actual run permissions match declarations;
- [ ] output appears only in run-scoped locations;
- [ ] target issue and PR remain unchanged by collection;
- [ ] no credential or sensitive log content appears; and
- [ ] repeated runs create separate artefacts without duplicate repository actions.

## Limitations and lessons

Current limitations:

- workflow dispatch requires an environment with Actions write authority;
- unresolved inline review-thread state is not collected;
- page and workflow-run collection are bounded and fail incomplete beyond limits;
- run artefacts are retained for seven days; and
- generated evidence cannot decide substantive sufficiency.

The premature merge adds a process lesson: a draft marker and `Do not approve yet` recommendation are advisory unless repository merge controls or human operating discipline enforce them. No repository-setting change is authorised by this recovery issue, but the incident must inform the final adoption decision.

## Decision

Decision: **pending live dogfood**.

No adopt, adapt or reject recommendation is valid until both live reports, the comparison and live authority audit are complete.

## Implications for the next stage

No Stage 4 issue or speculative automation backlog should be created from this worklog. Any next activity must begin as a new planning question after Stage 3 close-out.