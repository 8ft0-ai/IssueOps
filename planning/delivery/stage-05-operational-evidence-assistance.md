# Stage 5 — Operational evidence assistance

Status: completed.

## Original documented intent

The approved Stage 5 roadmap set out to turn the bounded Stage 3 evidence collector into an operationally useful normal-review aid without expanding its authority. The roadmap was approved through parent issue [#90](https://github.com/8ft0-ai/IssueOps/issues/90), formalised through issue [#155](https://github.com/8ft0-ai/IssueOps/issues/155) / PR [#156](https://github.com/8ft0-ai/IssueOps/pull/156), and is preserved exactly at merge commit [`1598667d61e836273415bd6d4e1e697041469096`](https://github.com/8ft0-ai/IssueOps/blob/1598667d61e836273415bd6d4e1e697041469096/planning/roadmap/stage-05-operational-evidence-assistance.md).

The intended minimum adaptations were:

- canonical non-closing execution-contract linkage;
- truthful read-only inline review-thread evidence, or explicit unavailable/incomplete representation under the retained permission ceiling;
- normal-review documentation under the adopted Stage 4 Diátaxis ownership model; and
- ordinary-work proof across at least three consecutive suitable implementation PRs before a separate evidence-based **Adopt**, **Adapt** or **Reject** decision.

The roadmap explicitly retained human-triggered invocation, read-only collection, human substantive review, separate human approval/merge authority and fail-closed mechanical completeness semantics.

## Retrospective interpretation

Not applicable. Stage 5 was planned and delivered contemporaneously. This delivery record separates actual results from the immutable approved roadmap rather than rewriting later findings into the original intent.

## What shipped

Stage 5 delivered the normal-review evidence-assistance model through five bounded slices:

1. **Roadmap formalisation** — issue [#155](https://github.com/8ft0-ai/IssueOps/issues/155) / PR [#156](https://github.com/8ft0-ai/IssueOps/pull/156).
2. **Canonical non-closing execution-contract linkage** — issue [#157](https://github.com/8ft0-ai/IssueOps/issues/157) / PR [#158](https://github.com/8ft0-ai/IssueOps/pull/158).
3. **Truthful read-only inline review-thread evidence** — issue [#159](https://github.com/8ft0-ai/IssueOps/issues/159) / PR [#160](https://github.com/8ft0-ai/IssueOps/pull/160).
4. **Normal reviewer workflow documentation** — issue [#161](https://github.com/8ft0-ai/IssueOps/issues/161) / PR [#162](https://github.com/8ft0-ai/IssueOps/pull/162).
5. **Ordinary-work proof and stage decision** — issue [#163](https://github.com/8ft0-ai/IssueOps/issues/163), using qualifying PRs [#167](https://github.com/8ft0-ai/IssueOps/pull/167), [#173](https://github.com/8ft0-ai/IssueOps/pull/173) and [#176](https://github.com/8ft0-ai/IssueOps/pull/176).

The previously completed [#141](https://github.com/8ft0-ai/IssueOps/issues/141) / [#144](https://github.com/8ft0-ai/IssueOps/issues/144) / PR [#152](https://github.com/8ft0-ai/IssueOps/pull/152) lineage supplied the exact deliberate `/collect-evidence` transport used by Stage 5; Stage 5 did not reopen or redesign that transport.

The adopted operating model is now:

```text
governing execution-contract issue
  -> ordinary PR declares canonical non-closing Issue #N linkage
  -> implementation and validation proceed normally
  -> authorised human/session deliberately requests /collect-evidence
  -> read-only collector gathers bounded repository-observed evidence
  -> pack reports complete/pending/unavailable/conflicting/error state with provenance
  -> human performs substantive contract, validation and risk review
  -> human separately decides approval and merge authority
```

## Linked issues and pull requests

Parent and close-out authority:

- Stage 5 parent and final owner decision: [#90](https://github.com/8ft0-ai/IssueOps/issues/90)
- Slice 5 ordinary-work proof: [#163](https://github.com/8ft0-ai/IssueOps/issues/163)
- final proof synthesis: #163 comment `5250300695`
- fresh independent proof-package review: #163 comment `5260611117`
- owner **Adopt** decision: #90 comment `5261343241`

Stage implementation:

- [#155](https://github.com/8ft0-ai/IssueOps/issues/155) / [PR #156](https://github.com/8ft0-ai/IssueOps/pull/156)
- [#157](https://github.com/8ft0-ai/IssueOps/issues/157) / [PR #158](https://github.com/8ft0-ai/IssueOps/pull/158)
- [#159](https://github.com/8ft0-ai/IssueOps/issues/159) / [PR #160](https://github.com/8ft0-ai/IssueOps/pull/160)
- [#161](https://github.com/8ft0-ai/IssueOps/issues/161) / [PR #162](https://github.com/8ft0-ai/IssueOps/pull/162)
- [#163](https://github.com/8ft0-ai/IssueOps/issues/163) — proof and close-out

Ordinary-work proof:

- [#166](https://github.com/8ft0-ai/IssueOps/issues/166) / [PR #167](https://github.com/8ft0-ai/IssueOps/pull/167) — qualifying position 1
- [#168](https://github.com/8ft0-ai/IssueOps/issues/168) / [PR #173](https://github.com/8ft0-ai/IssueOps/pull/173) — qualifying position 2
- [#175](https://github.com/8ft0-ai/IssueOps/issues/175) / [PR #176](https://github.com/8ft0-ai/IssueOps/pull/176) — qualifying position 3
- PRs [#165](https://github.com/8ft0-ai/IssueOps/pull/165), [#172](https://github.com/8ft0-ai/IssueOps/pull/172) and [#174](https://github.com/8ft0-ai/IssueOps/pull/174) — prospectively excluded from the qualifying sequence for lifecycle/authority reasons recorded in #163.

## Proof runs, checks and artefacts

The strongest ordinary-work proof snapshots were:

| Position | PR | Decision-relevant head | Request comment | Workflow run | Attempt | Result | Artifact | Independent review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | #167 | `cfc58623ddec0403452b624fda65c48bf10099b4` | `5233803230` | `31335523738` | 1 | success | `9044198947` | `4892656057` |
| 2 | #173 | `9c7d0719432604ccbafe483b1a9c65f3cf58d2c1` | `5245349417` | `31427268867` | 1 | success | `9077666717` | `4900599406` |
| 3 | #176 | `2683d3a043a8a44f7928a43c702d157b467622be` | `5248559483` | `31454688542` | 1 | success | `9087581658` | `4903280549` |

All three packs mechanically completed on the decision-relevant heads, represented canonical linkage truthfully and reported submitted-review state separately from inline review-thread state. The final snapshots contained zero inline review threads.

PR #173 also retained meaningful negative validation evidence: exact-pair run `31388150678` failed on trailing whitespace before remediation, while final exact-pair run `31388271889` succeeded. The failed run remained part of the review history rather than being erased to improve the Stage 5 proof.

Actions artifacts were short-lived supporting evidence. The durable proof is the issue/PR/request/run/review correlation recorded in GitHub and consolidated in the [Stage 5 close-out record](../closeout/stage-05-operational-evidence-assistance.md).

## Intended versus actual delivery

The implemented stage stayed close to the approved roadmap.

The canonical non-closing execution-contract declaration was delivered and used on ordinary PRs without requiring GitHub auto-closing keywords. Inline review-thread state became a separate truthful read-only evidence surface under the retained permission ceiling. The reviewer workflow was documented in the adopted How-to / Reference / Explanation ownership model.

The ordinary-work proof was deliberately not limited to three hand-picked successes. The natural sequence recorded exclusions before collection, retained a genuine validation failure/remediation history, and allowed ordinary PRs to proceed through substantive review without retrospective collection when prospective Stage 5 authority was absent.

No behavioural collector change was made inside Slice 5. No proof defect was opportunistically fixed under the close-out issue.

## Observed limitations and friction

The Stage 5 proof exposed or retained several limitations:

- Evidence artifacts used short retention and cannot serve as the sole durable audit record.
- All three qualifying final snapshots naturally had zero inline review threads, so the ordinary sequence proved truthful retrieval/representation but did not naturally exercise an unresolved-thread example.
- Adverse collector states such as stale, pending, unavailable, conflicting and retrieval-error were covered by implementation/repository validation rather than all occurring naturally in the three final proof snapshots.
- Pack value varies by PR complexity. On small one-file PRs, mechanical gathering is already cheap; the pack's strongest value is deterministic correlation, currentness and evidence-state consolidation.
- Lifecycle authority, issue semantics, exact diff meaning, validation adequacy, remediation history, risks and final recommendation remain manual review work.
- An `issue_comment` workflow run's root `head_sha` identifies the workflow execution context on `main`, not the target PR head. Reviewers must rely on the pack's separately resolved target-PR head for decision provenance.
- PR descriptions can be snapshots from an earlier lifecycle boundary; later authority must be reconciled from current issue/comment records rather than inferred from the body alone.

None of these limitations produced a false mechanical-completeness outcome, unauthorised collector mutation or material weakening of substantive review/merge authority during the accepted proof.

## Boundaries preserved

Stage 5 preserved the approved authority model:

- evidence collection remains deliberate and human-triggered;
- the collector remains read-only with respect to repository/lifecycle state;
- no automatic lifecycle transition is introduced;
- the collector makes no readiness, remediation, approval, merge, publication or deployment recommendation;
- mechanical completeness remains distinct from approval readiness;
- the governing issue remains the execution contract;
- substantive review remains human-led;
- approval and merge remain separate human decisions;
- no permission expansion was taken merely to improve evidence completeness;
- no auto-merge, repository-setting change or cross-repository rollout was authorised; and
- the separate #148/#149 PR-diff-validator lineage remained outside Stage 5 scope.

PR #176 remaining draft and unmerged at the Stage 5 decision boundary is direct evidence that a favourable proof position did not confer merge authority.

## Decisions and lessons

The repository owner recorded **Adopt** in #90 comment `5261343241` after accepting:

- the final Slice 5 synthesis and authority audit, #163 comment `5250300695`; and
- the fresh independent proof-package review, #163 comment `5260611117`, disposition **Decision-ready**.

The adopted conclusion is deliberately narrow: Stage 5 evidence assistance is useful enough for normal IssueOps review when it remains a human-triggered, read-only mechanical evidence aid. It is not a substitute for contract interpretation, substantive review, approval or merge authority.

The strongest operational lesson is that evidence consolidation and evidence judgement should stay separate. Deterministic collection can remove repeated mechanical work while the human remains responsible for meaning, adequacy and authority.

The sampling lesson is equally important: exclusions and negative evidence made the adoption proof stronger. Retrospective authority repair or favourable cherry-picking would have undermined the result.

## Implications for the next stage

No later stage is authorised by Stage 5 adoption.

Future planning may separately consider retained limitations or broader rollout only if a concrete problem justifies it. Any proposal for automatic invocation, expanded permissions, lifecycle automation, cross-repository adoption, auto-merge or additional reviewer authority must begin as a new governed planning question rather than being inferred from this **Adopt** decision.