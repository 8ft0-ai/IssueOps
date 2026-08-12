# Stage 5 — Operational evidence assistance

Status: completed.

Record type: contemporaneous.

Approved through planning issue [#90](https://github.com/8ft0-ai/IssueOps/issues/90) and formalised by issue [#155](https://github.com/8ft0-ai/IssueOps/issues/155) / PR [#156](https://github.com/8ft0-ai/IssueOps/pull/156) on 9 August 2026.

The exact approved roadmap before delivery and close-out is preserved at merge commit [`1598667d61e836273415bd6d4e1e697041469096`](https://github.com/8ft0-ai/IssueOps/blob/1598667d61e836273415bd6d4e1e697041469096/planning/roadmap/stage-05-operational-evidence-assistance.md). This completed status record summarises the approved intent and links actual delivery separately; it does not rewrite later findings as original plans.

Actual delivery and proof: [Stage 5 delivery record](../delivery/stage-05-operational-evidence-assistance.md) and [Stage 5 close-out record](../closeout/stage-05-operational-evidence-assistance.md).

Final owner decision: **Adopt**, issue #90 comment `5261343241`.

## Problem statement

The approved roadmap identified that Stage 3 had proved bounded, manually invoked, read-only evidence collection but had not proved normal-review adoption. Two evidence-completeness gaps remained material: execution-contract linkage depended on GitHub closing-keyword syntax, and inline review-thread resolution state was absent from the evidence pack.

The stage therefore addressed **normal-review usefulness and truthful evidence completeness**, not generic workflow invocation, review automation or lifecycle automation.

## Outcome to prove

The approved outcome was to prove that ordinary IssueOps review could use a deliberately requested, read-only evidence pack after two bounded completeness adaptations:

- one canonical repository-owned execution-contract declaration could identify exactly one governing same-repository issue without requiring automatic issue closure; and
- inline review-thread resolution state could be represented truthfully through bounded read-only collection, or explicitly represented as unavailable/incomplete if the retained permission boundary could not provide it.

The stage also had to prove ordinary-work usefulness, fail-closed completeness semantics and preservation of human substantive review and merge authority through at least three consecutive suitable ordinary implementation PRs.

Close-out result: proved. The final decision is **Adopt**.

## Non-goals

The completed stage did not introduce:

- automatic evidence collection on pull-request, review, push or schedule events;
- generic connector-to-workflow RPC or an arbitrary workflow dispatcher;
- readiness, remediation, approval, merge, publication or deployment recommendations by the collector;
- issue, PR, review, label, branch, commit, file, merge or repository-setting mutation by the collector;
- auto-merge or merge authority;
- permission expansion merely to improve evidence completeness;
- cross-repository or organisation-wide rollout;
- absorption of the separate #148/#149 PR-diff-validation capability;
- a second execution contract in the PR body; or
- an assumption that mechanical `complete` means approval readiness.

## Operating and autonomy boundary

Stage 5 adopted **evidence assistance only**.

The normal invocation remains the exact zero-argument PR comment:

```text
/collect-evidence
```

A current governing issue/session grant must separately authorise that deliberate request. Repository write capability alone does not confer IssueOps procedural authority.

The collector remains read-only with respect to repository and lifecycle state. Humans retain exclusive authority over issue readiness, plan approval, semantic contract satisfaction, review-finding interpretation, remediation, validation adequacy, risk acceptance, pull-request approval, merge, publication, deployment, repository settings and later stage decisions.

Mechanical collection completeness remains distinct from approval readiness.

## Target workflow or target state

The delivered normal-review state is:

```text
governing execution-contract issue
  -> ordinary PR declares canonical non-closing Issue #N linkage
  -> implementation + validation + substantive review proceed normally
  -> authorised human/session deliberately posts /collect-evidence
  -> collector resolves the request and decision-relevant PR head
  -> bounded read-only evidence is gathered with provenance
  -> pack exposes observed / contributor-reported / derived /
     pending / unavailable / conflicting state
  -> human verifies contract alignment, review findings, validation and risks
  -> human separately decides approval and merge authority
```

The canonical linkage and review-thread evidence surfaces are implemented and documented under the adopted Stage 4 How-to / Reference / Explanation ownership model.

## Acceptance gates

- [x] One canonical non-closing execution-contract linkage is implemented for ordinary IssueOps pull requests without depending solely on GitHub closing keywords.
- [x] The normal linkage case identifies exactly one governing same-repository issue, and ambiguous/multiple/conflicting declarations fail visibly rather than selecting silently.
- [x] The governing issue remains the execution contract; the pull-request declaration identifies it without duplicating issue content as a second contract.
- [x] Inline review-thread resolution state is collected read-only under the retained permission boundary, with truthful unavailable/incomplete semantics retained for inaccessible evidence.
- [x] Submitted review counts/states are not represented as proof that inline review work is resolved.
- [x] Existing evidence classifications, provenance, bounded pagination/error handling and stale-head detection remain intact.
- [x] Comment-triggered collection retains deterministic request-comment -> workflow-run -> attempt -> summary/artifact correlation.
- [x] Stale, pending, unavailable, conflicting and retrieval-error states remain fail-closed and cannot produce a false mechanical `complete` outcome.
- [x] The collector makes no issue, pull-request, review, label, branch, commit, file, merge or settings mutation.
- [x] Evidence completeness remains distinct from approval readiness and the collector makes no readiness, remediation, approval, merge, publication or deployment recommendation.
- [x] Normal-review procedures, exact rules and authority rationale are documented under the adopted Stage 4 How-to / Reference / Explanation ownership model.
- [x] Three consecutive suitable ordinary IssueOps implementation pull requests used the evidence path as part of real review work: PRs #167, #173 and #176.
- [x] Each qualifying proof records governing issue, exact decision-relevant head, request identity, run/attempt/result, artifact state, linkage, review-thread representation, incomplete/conflicting surfaces and remaining manual evidence gathering.
- [x] Counter-evidence was retained, including excluded PRs #165, #172 and #174 and the genuine failed validation/remediation history on PR #173.
- [x] Across the proof sequence there were zero false mechanical-completeness outcomes, zero unauthorised collector mutations and no material reduction in substantive human review quality or human merge authority.
- [x] Stage 5 closed with a distinct evidence-based owner decision: **Adopt**.

Detailed proof and limitations belong in the [close-out record](../closeout/stage-05-operational-evidence-assistance.md), not in this intent wrapper.

## Proposed implementation slices

The approved sequence was delivered through:

1. roadmap formalisation — issue #155 / PR #156;
2. canonical non-closing execution-contract linkage — issue #157 / PR #158;
3. truthful read-only review-thread evidence — issue #159 / PR #160;
4. normal evidence-assisted reviewer workflow documentation — issue #161 / PR #162; and
5. ordinary-work proof and close-out — issue #163.

The qualifying ordinary-work proof used PRs #167, #173 and #176. Detailed actual delivery and exclusion history belongs in the [delivery](../delivery/stage-05-operational-evidence-assistance.md) and [close-out](../closeout/stage-05-operational-evidence-assistance.md) records.

## Risks and controls

The roadmap controls were applied as follows:

- evidence-pack over-authority was controlled by preserving classifications, provenance and the mechanical-complete/approval-ready distinction;
- competing execution-contract truth was controlled by making the PR declaration identify the governing issue rather than duplicate it;
- linkage ambiguity/conflict was controlled through fail-visible semantics;
- review-thread completeness was separated from submitted-review state;
- permission expansion was avoided under the retained read-only boundary;
- lifecycle automation was excluded and deliberate human invocation retained;
- proof cherry-picking was controlled through prospective suitability decisions and consecutive suitable ordinary-work sampling;
- negative evidence was retained rather than repaired retrospectively; and
- Stage 5 remained separate from the completed execution-transport and PR-diff-validation lineages.

Remaining limitations are recorded in the delivery and close-out records rather than hidden here.

## Definition of done

Stage 5 is complete because:

- [x] the approved Stage 5 implementation slices were delivered and validated;
- [x] canonical non-closing execution-contract linkage was delivered and proved on ordinary work;
- [x] review-thread state is represented truthfully through bounded read-only collection with explicit incomplete/unavailable semantics retained;
- [x] retained evidence/provenance/stale/error controls remain validated;
- [x] Stage 4-aligned normal-review documentation is complete for the adopted behaviour;
- [x] three consecutive suitable ordinary implementation PRs supplied the approved proof and counter-evidence;
- [x] the authority audit found no weakening of human substantive review or merge authority and no unauthorised collector mutation;
- [x] limitations, deviations and cases of lower evidence-pack value are recorded honestly;
- [x] completed Stage 5 delivery and close-out records exist under `planning/`;
- [x] the final evidence-based owner decision is **Adopt**; and
- [x] the parent planning record can be reconciled to this completed terminal state after close-out merge.

## Likely next decision boundary

No later stage is currently approved.

Stage 5 adoption does not authorise automatic invocation, expanded permissions, cross-repository rollout, auto-merge or any other lifecycle automation. A future stage or adaptation requires a separately governed planning question grounded in a concrete observed problem.