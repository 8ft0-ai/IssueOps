# Stage 3 evidence-pack dogfood worklog

Status: completed.

Record type: contemporaneous close-out worklog.

This worklog supports [Issue #82](https://github.com/8ft0-ai/IssueOps/issues/82), the prematurely merged [PR #83](https://github.com/8ft0-ai/IssueOps/pull/83), recovery [Issue #84](https://github.com/8ft0-ai/IssueOps/issues/84), and replacement dogfood [PR #85](https://github.com/8ft0-ai/IssueOps/pull/85).

## Current state

Stage 3 close-out evidence is complete. The decision is **Adapt**: retain the bounded read-only evidence-pack capability for controlled use, but address explicit execution-contract linkage and manual-dispatch friction before broader adoption.

No broader automation, lifecycle authority, merge authority or Stage 4 implementation is authorised by this decision.

## Original intent

Stage 3 was shaped through [planning issue #75](https://github.com/8ft0-ai/IssueOps/issues/75) and the approved roadmap at `planning/roadmap/stage-03-read-only-evidence-pack-assistance.md`.

The outcome to prove was that a manually invoked, read-only capability could assemble a current, provenance-linked report for one pull request while separating observations from assertions, representing incomplete state honestly, making no repository mutation or approval decision, and preserving human merge and publication authority.

## Delivered implementation

- [Issue #76](https://github.com/8ft0-ai/IssueOps/issues/76) / [PR #77](https://github.com/8ft0-ai/IssueOps/pull/77) — approved roadmap and authority boundary.
- [Issue #78](https://github.com/8ft0-ai/IssueOps/issues/78) / [PR #79](https://github.com/8ft0-ai/IssueOps/pull/79) — `evidence-pack/v1`, deterministic rendering, classifications, provenance validation and tests.
- [Issue #80](https://github.com/8ft0-ai/IssueOps/issues/80) / [PR #81](https://github.com/8ft0-ai/IssueOps/pull/81) — standard-library GitHub REST collector and manual `workflow_dispatch` for one pull request.
- [Issue #82](https://github.com/8ft0-ai/IssueOps/issues/82), [Issue #84](https://github.com/8ft0-ai/IssueOps/issues/84) and [PR #85](https://github.com/8ft0-ai/IssueOps/pull/85) — live dogfood, recovery, comparison, authority audit and close-out decision.

The collector uses read-only permissions and REST `GET` requests, publishes only to the workflow summary and run artefact, and makes no readiness, sufficiency, approval, merge or publication decision.

## Premature merge incident

PR #83 was a draft, pending-evidence target but was merged before the required live runs, artefact inspection, comparison, authority audit or decision. Its `Closes #82` wording also auto-closed Issue #82 despite incomplete criteria. Issue #82 was reopened on 11 July 2026.

No revert was required because PR #83 added only this worklog with `Status: pending evidence`; it did not mark Stage 3 complete, create a completed delivery record, record adoption, update the ledger or graph, or authorise broader automation. Recovery used Issue #84 and draft PR #85 to restore the open review gate.

This incident is material evidence that draft state and written recommendations remain advisory unless repository controls or human operating discipline enforce them.

## Stable live target

The qualifying reports targeted PR #85 at the same stable head:

`0d1d6c1a1ef063b9d422599efa400f5d2a9f1ab2`

The collector itself was dispatched from `main` at merge commit `b42458a65d2b69ef7b127d4f2011b17c77a3f9e9`.

## Live dogfood evidence

| Snapshot | Collector run | Artefact | Report status | Observed workflow state |
| --- | --- | --- | --- | --- |
| Pending | [29148889955](https://github.com/8ft0-ai/IssueOps/actions/runs/29148889955) | `evidence-pack-pr-85-29148889955`, ID `8247568476` | `incomplete` | Documentation workflow and MkDocs job were `in_progress` |
| Final | [29149028492](https://github.com/8ft0-ai/IssueOps/actions/runs/29149028492) | `evidence-pack-pr-85-29149028492`, ID `8247606971` | `complete` | Documentation and planning succeeded; Pages deployment was observed as `skipped` |

Both reports resolved PR #85, retained the same head SHA at collection start and end, contained no collection errors, preserved direct source links and displayed the generated-output and human-decision warnings.

Two earlier runs were useful rehearsals but are not the qualifying pair:

- run `29148249127` was dispatched from the old feature branch rather than `main`;
- run `29148787982` was a valid final-state snapshot but occurred before the qualifying pending snapshot.

## Report inspection

- [x] Repository, pull request and stable head SHA were correct.
- [x] Repository-observed evidence and contributor-reported PR-body assertions remained separate.
- [x] The pending report was `incomplete` and did not infer success.
- [x] The final report represented successful and skipped outcomes as observations, not recommendations.
- [x] Changed-file, check and workflow evidence retained direct provenance links.
- [x] Generated-output and human-decision warnings remained prominent.
- [x] The target PR and issues were not mutated by collection.
- [x] The state transition was visible without rewriting PR #85.
- [ ] The linked execution-contract issue was not identified in either report because PR #85 intentionally contained no closing keyword.

The missing issue linkage is the main substantive gap. The current collector discovers same-repository issue contracts only through GitHub closing-keyword syntax. The recovery PR deliberately omitted closing keywords to prevent another automatic issue closure, so the report omitted Issue #82 and Issue #84 rather than guessing. This is safe, but incomplete.

## Manual versus assisted comparison

| Measure | Manual path | Assisted path |
| --- | --- | --- |
| Steps | Seven source groups plus reconciliation and validator-source interpretation | One workflow dispatch and one generated JSON/Markdown artefact per snapshot, followed by human inspection |
| Bounded effort | About 3 minutes 5 seconds for the original bounded snapshot | Collector runtime was about 2.0 seconds for the pending report and 3.2 seconds for the final report; human interaction was not precisely timed |
| Omitted fields | None identified in the bounded manual baseline | Linked execution-contract issue omitted because no closing keyword was present; unresolved inline review threads remain outside the collector |
| Incorrect transcription | None identified | None identified; report fields were mechanically rendered from GitHub responses |
| Human interpretation | Required to explain validation and decide sufficiency | Still required to interpret contract alignment, skipped deployment, limitations and merge readiness |
| Review quality | Complete but assembled from multiple reads | Not weakened when used as an input to human review; insufficient as a replacement because contract linkage and unresolved-thread state may be absent |

The assisted path materially reduced repeated fact gathering and transcription, but the live exercise required manual choreography to capture a pending state and several attempts to select the correct workflow branch and timing. The report improves evidence navigation; it does not remove the need for review.

## Safe-failure evidence

Repository-native tests cover inaccessible targets, partial API failure, excessive pagination, conflicting issue links, validly empty surfaces, pending checks and jobs, failed checks as observations, moving-head stale protection and bounded local output. The live pending run additionally proved that in-progress validation produces an incomplete report rather than a success inference.

## Authority-boundary audit

- [x] Invocation remained manual.
- [x] Live run permissions were `actions: read`, `checks: read`, `contents: read`, `issues: read`, `metadata: read` and `pull-requests: read`.
- [x] The collector used GitHub REST `GET` requests only.
- [x] Output appeared only in the run summary and separate run-scoped artefacts.
- [x] PR #85, Issue #82 and Issue #84 remained unchanged by collection.
- [x] Logs redacted the token and no credential or sensitive payload was found in the inspected reports.
- [x] Repeated runs produced separate artefacts and no duplicate repository actions.
- [x] Collection status remained separate from readiness, sufficiency, approval, merge and publication decisions.

## Limitations and unintended consequences

- Issue linkage depends on closing-keyword syntax; a non-closing contract reference is not currently collected.
- Unresolved inline review-thread state is not collected.
- Pagination and workflow-run collection are bounded and fail incomplete beyond their limits.
- Artefacts are retained for seven days, so durable records must preserve identifiers and findings.
- Manual `workflow_dispatch` requires the operator to choose the correct workflow branch and coordinate timing when a pending snapshot is required.
- Draft state and `Do not approve yet` language did not prevent PR #83 from being merged.
- Generated evidence remains an aid to review and cannot decide substantive contract satisfaction.

## Decision

Decision: **Adapt**.

Retain the current capability for controlled, manually invoked, read-only use because it safely exposed a pending-to-final validation transition, reduced mechanical evidence assembly, preserved provenance and transferred no decision authority.

Before broader adoption, a separately planned change should address:

1. explicit execution-contract linkage that does not require an auto-closing keyword; and
2. simpler, less error-prone invocation and target selection.

This close-out does not authorise those changes, automatic invocation, lifecycle automation, merge authority, repository-setting changes or cross-repository rollout.

## Implications

Stage 3 is closed with an Adapt decision. Any next activity must begin as a new planning question about whether and how to improve contract linkage and invocation ergonomics, informed by broader-use evidence. No Stage 4 execution issue or speculative automation backlog is created here.
