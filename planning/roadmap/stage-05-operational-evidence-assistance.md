# Stage 5 — Operational evidence assistance

Status: approved.

Record type: contemporaneous.

Approved through planning issue [#90](https://github.com/8ft0-ai/IssueOps/issues/90) on 9 August 2026. The reviewed planning proposal is comment `5228818991`, the fresh independent Shape review is comment `5228889418` with recommendation **Approve**, and the owner approval/roadmap-formalisation decision is comment `5228920370`. Formalisation is governed by issue [#155](https://github.com/8ft0-ai/IssueOps/issues/155).

## Problem statement

Stage 3 delivered a bounded, manually invoked, read-only pull-request evidence collector and closed with decision **Adapt**. It proved deterministic evidence classification, provenance, stale-head detection, honest pending/final states, safe failure and preservation of human review and merge authority. It did not prove that the collector was ready for normal-review adoption.

The repository state has advanced since Stage 3 close-out. Issues [#141](https://github.com/8ft0-ai/IssueOps/issues/141) and [#144](https://github.com/8ft0-ai/IssueOps/issues/144), with merged PR [#152](https://github.com/8ft0-ai/IssueOps/pull/152), completed and verified a narrow execution bridge for the existing collector. An already-authorised IssueOps session can deliberately post the exact `/collect-evidence` command on an eligible pull request; the repository-owned workflow independently validates the GitHub-side request and invokes the existing read-only collection path. The original manual `workflow_dispatch` path remains available.

That completed transport materially reduces invocation friction, but transport success is not Stage 5 adoption. Stage 5 does not need to design a generic workflow dispatcher or reopen the #141/#144 bridge.

Two evidence-completeness gaps remain material for normal review:

1. **Execution-contract linkage still depends on GitHub closing-keyword syntax.** The current collector recognises a same-repository governing issue from `Closes`, `Fixes` or `Resolves` style references. Normal IssueOps close-and-reconcile work may deliberately keep the governing issue open through merge and post-merge verification, so auto-closing syntax is not a suitable sole evidence contract.
2. **Inline review-thread resolution state is absent.** The collector records pull-request conversation comments and submitted review states, but it does not represent whether inline review threads remain unresolved. Submitted-review counts are therefore not proof that inline review work is complete.

The remaining Stage 5 problem is consequently **normal-review usefulness and truthful evidence completeness**, not invocation transport. The stage must test whether the bounded collector becomes genuinely useful in ordinary IssueOps review after the minimum completeness adaptations, without turning evidence assistance into review, approval or lifecycle automation.

The separate [#148](https://github.com/8ft0-ai/IssueOps/issues/148) / [#149](https://github.com/8ft0-ai/IssueOps/issues/149) PR-diff-validation lineage remains outside Stage 5. Its repository-native execution patterns may be useful precedent where directly relevant, but Stage 5 must not absorb or redesign that capability.

## Outcome to prove

Demonstrate that IssueOps can use a deliberately requested, read-only evidence pack as a normal-review aid after two bounded completeness adaptations:

- an ordinary pull request can identify exactly one governing execution-contract issue through one canonical repository-owned declaration that does not itself require automatic issue closure; and
- inline review-thread resolution state is represented truthfully through bounded read-only collection where safely available, or explicitly reported as unavailable/incomplete where the retained permission boundary cannot provide it.

The resulting evidence path must preserve all existing evidence classifications and fail-closed behaviour while proving through ordinary work that it materially reduces repeated mechanical evidence gathering without weakening substantive human review.

The stage must also prove that:

- deliberate `/collect-evidence` invocation fits the normal IssueOps review workflow without becoming an automatic lifecycle transition;
- ambiguous or conflicting execution-contract declarations fail visibly rather than being silently selected;
- review submissions are never treated as a substitute for review-thread resolution state;
- missing, stale, pending, unavailable, conflicting or retrieval-error state cannot produce a misleading mechanical completeness claim;
- evidence completeness remains visibly distinct from approval readiness;
- the issue remains the execution contract rather than duplicating its content into the pull request;
- the collector makes no repository or lifecycle mutations and makes no readiness, remediation, approval, merge, publication or deployment recommendation;
- the normal-review documentation follows the adopted Stage 4 Diátaxis ownership model; and
- ordinary-PR proof supports a final evidence-based **Adopt**, **Adapt** or **Reject** decision rather than assuming adoption.

## Non-goals

- No reopening or reimplementation of completed Stage 3 work.
- No redesign of the completed #141/#144 `/collect-evidence` transport.
- No generic connector-to-workflow RPC or arbitrary workflow dispatcher.
- No arbitrary workflow names, refs, input maps, shell fragments or user-controlled execution parameters.
- No absorption or redesign of the separate #148/#149 PR-diff-validation capability.
- No automatic evidence collection on pull-request, review, push or schedule events.
- No readiness or implementation-plan approval decisions by the collector.
- No automated review-finding resolution or remediation classification.
- No issue, pull-request, review, label, branch, commit, file, merge or repository-setting mutation by the collector.
- No approval, merge, publication, deployment or release recommendation.
- No merge or auto-merge authority.
- No permission expansion merely to force review-thread collection to work.
- No cross-repository or organisation-wide rollout in this stage.
- No assumption that a mechanically complete evidence pack means the pull request is ready to approve.
- No Tutorial unless the implemented workflow later proves stable enough to justify a reliable guided learning journey.

## Operating and autonomy boundary

Stage 5 remains **evidence assistance only**.

### Deliberate invocation

The normal command path remains the exact zero-argument PR comment:

```text
/collect-evidence
```

Posting the command is a deliberate IssueOps action. A session may request it only when its current governing issue/session grant permits evidence collection for the pull request in scope. Repository collaborator status or connector write capability does not by itself grant IssueOps procedural authority.

The repository-owned workflow retains its independent GitHub platform-eligibility checks. The existing `workflow_dispatch` path remains a manual fallback. Stage 5 does not add scheduled or automatic lifecycle invocation.

### Read-only collection

The collector may read bounded GitHub-native evidence required for one pull request and may write generated reports only to its run-local output, Actions run summary and short-lived artifact surfaces already authorised by the existing implementation.

The Stage 5 evidence view may represent, where available and bounded:

- repository and pull-request identity;
- base and exact current head SHA;
- changed-file scope and statistics;
- canonical execution-contract issue identity and source;
- issue, readiness and implementation-plan records as source material rather than approval conclusions;
- pull-request conversation comments;
- submitted review states;
- inline review-thread resolution state or explicit unavailability;
- checks, workflows and jobs;
- contributor-reported validation evidence;
- stale-head state;
- pagination/API errors and incomplete state;
- request comment, workflow run, attempt and artifact correlation; and
- direct provenance links and source timestamps where available.

The evidence model continues to distinguish:

- **Repository-observed**;
- **Contributor-reported**;
- **Derived**;
- **Pending**;
- **Unavailable**; and
- **Conflicting**.

### Human authority retained

Humans retain exclusive authority over:

- issue readiness and implementation-plan approval;
- acceptance-criterion and execution-contract satisfaction;
- interpretation of review findings and whether they are substantively resolved;
- remediation classification;
- validation sufficiency;
- risk and caveat acceptance;
- pull-request approval;
- merge, publication, deployment or release;
- repository-setting changes; and
- the final Stage 5 Adopt/Adapt/Reject decision.

A generated `complete` state may describe mechanical collection completeness only. It must never mean `approve`, `ready to merge` or equivalent.

## Target workflow or target state

The intended normal-review workflow is:

```text
governing execution-contract issue
  -> bounded implementation PR declares that contract explicitly
  -> implementation + validation + substantive review proceed normally
  -> authorised reviewer/session deliberately posts /collect-evidence
  -> collector resolves the event-derived PR and current head
  -> collector gathers bounded repository-observed evidence
  -> evidence pack exposes observed / contributor-reported / derived /
     pending / unavailable / conflicting state with provenance
  -> human verifies contract alignment, review findings, validation and risks
  -> human decides whether approval, remediation or merge is authorised
```

Collection may be repeated when the pull-request head or material validation/review state changes. Repetition creates a new evidence snapshot; it is not a hidden lifecycle transition or automatic gate.

### Canonical non-closing execution-contract linkage

Stage 5 requires one repository-owned declaration for the normal case with these semantic properties:

- human-readable;
- deterministic enough for machine collection;
- exactly one governing same-repository issue in the normal case;
- independent of `Closes`, `Fixes` or `Resolves` semantics;
- compatible with keeping the governing issue open through merge and post-merge reconciliation;
- directly attributable to the pull-request body and governing issue; and
- fail-visible when multiple, ambiguous or conflicting declarations are present.

The final syntax and parser contract belong to the separately governed implementation slice. This roadmap does not freeze an implementation format beyond the approved semantic requirements.

Closing keywords may remain valid GitHub lifecycle syntax where deliberately wanted. If later implementation permits both explicit linkage and closing references, disagreement must be represented as conflict rather than guessed away.

### Truthful review-thread evidence

For normal-review usefulness, unresolved inline review work must not be silently invisible.

The preferred target is bounded read-only retrieval of review-thread resolution metadata sufficient to represent:

- total thread count;
- unresolved thread count;
- resolved thread count where available; and
- whether the surface was completely retrieved.

Current repository review tooling demonstrates that GitHub review-thread resolution metadata is technically retrievable through a read-only review-thread surface. That establishes feasibility only. It does **not** prove that the retained Actions `GITHUB_TOKEN` permission ceiling used by the collector can retrieve the same surface in the workflow environment.

The review-thread implementation slice must first validate the retained read-only permission boundary. If the required surface cannot be safely retrieved under that boundary, Stage 5 must represent review-thread state as **unavailable/incomplete** and return any proposed permission expansion for separate governance. It must not broaden authority incidentally.

Submitted review states remain useful evidence, but they must never be treated as proof that inline review threads are resolved.

### Documentation ownership

Any later user-facing documentation follows the adopted Stage 4 architecture:

- **How-to** owns the deliberate procedure for requesting and using an evidence pack during normal review;
- **Reference** owns exact linkage syntax, schema, evidence classifications, completeness states, invocation semantics, limits and failure modes;
- **Explanation** owns the read-only/human-authority rationale and trade-offs;
- **Tutorials** are added only if a stable guided journey is later justified; and
- `planning/` owns stage intent, proof, delivery and close-out records.

Compatibility pages may point to canonical content but must not become competing sources.

## Acceptance gates

- [ ] One canonical non-closing execution-contract linkage is implemented for ordinary IssueOps pull requests without depending solely on GitHub closing keywords.
- [ ] The normal linkage case identifies exactly one governing same-repository issue, and ambiguous/multiple/conflicting declarations fail visibly rather than selecting silently.
- [ ] The governing issue remains the execution contract; the pull-request declaration identifies it without duplicating issue content as a second contract.
- [ ] Inline review-thread resolution state is collected read-only under the retained permission boundary, or the surface is explicitly represented as unavailable/incomplete without unreviewed permission expansion.
- [ ] Submitted review counts/states are never represented as proof that inline review work is resolved.
- [ ] Existing evidence classifications, provenance, bounded pagination/error handling and stale-head detection remain intact.
- [ ] Comment-triggered collection retains deterministic request-comment -> workflow-run -> attempt -> summary/artifact correlation.
- [ ] Stale, pending, unavailable, conflicting and retrieval-error states remain fail-closed and cannot produce a false mechanical `complete` outcome.
- [ ] The collector makes no issue, pull-request, review, label, branch, commit, file, merge or settings mutation.
- [ ] Evidence completeness remains visibly distinct from approval readiness and the collector makes no readiness, remediation, approval, merge, publication or deployment recommendation.
- [ ] Normal-review procedures, exact rules and authority rationale are documented under the adopted Stage 4 How-to / Reference / Explanation ownership model.
- [ ] At least three consecutive suitable ordinary IssueOps implementation pull requests use the implemented evidence path as part of real review work rather than synthetic pilot-only ceremony.
- [ ] Each qualifying ordinary-PR proof records the governing issue, exact decision-relevant head, `/collect-evidence` request identity, run/attempt/result, artifact state, linkage result, review-thread representation, incomplete/conflicting surfaces and whether material mechanical evidence still had to be gathered outside the pack.
- [ ] The ordinary-PR proof records counter-evidence, including cases where the evidence pack adds little value, creates confusion or does not reduce manual mechanical gathering.
- [ ] Across the proof sequence there are zero false mechanical-completeness outcomes, zero unauthorised collector mutations and no material reduction in substantive human review quality or human merge authority.
- [ ] Stage 5 closes with an explicit evidence-based **Adopt**, **Adapt** or **Reject** decision rather than treating implementation completion as adoption.

## Proposed implementation slices

The approved Stage 5 sequence is deliberately small and ordered. Each later slice requires its own separately governed IssueOps issue, readiness assessment, detailed implementation plan, validation and review boundary.

1. **Formalise the approved Stage 5 roadmap** — issue [#155](https://github.com/8ft0-ai/IssueOps/issues/155). Create this contemporaneous roadmap and align the planning/public roadmap indexes. Make no collector behaviour change.
2. **Add canonical non-closing execution-contract linkage.** Align the pull-request declaration and collector linkage model around one canonical repository-owned contract identity, with deterministic conflict handling. Exact syntax and parser details belong to that issue.
3. **Add truthful review-thread evidence.** Retrieve bounded read-only thread-resolution state under the retained permission ceiling where feasible; otherwise surface unavailable/incomplete state and return any authority expansion to governance.
4. **Document the normal reviewer workflow.** Add the necessary How-to, Reference and Explanation updates under the Stage 4 architecture after the behaviour is stable enough to document accurately.
5. **Dogfood ordinary pull requests and close Stage 5.** Use at least three consecutive suitable ordinary implementation pull requests, retain positive and counter-evidence, perform an authority audit and conclude with **Adopt**, **Adapt** or **Reject**.

Listing these slices in the roadmap does not create their issues or grant execution authority.

## Risks and controls

### Risk: evidence pack looks more authoritative than it is

Control: preserve evidence classifications and provenance, retain explicit human-decision warnings, and keep mechanical completeness separate from approval readiness.

### Risk: canonical linkage becomes another source of truth

Control: the pull-request declaration identifies the governing GitHub issue; the issue remains the execution contract. Do not duplicate the issue's acceptance criteria or plan as a second authoritative contract.

### Risk: explicit linkage and GitHub closing syntax disagree

Control: later implementation must report conflict and fail the linkage surface closed rather than choosing one silently.

### Risk: review-thread retrieval requires broader authority

Control: validate the retained read-only workflow token first. If the surface is unavailable under that ceiling, report unavailable/incomplete and return any permission expansion for separate design and owner authority.

### Risk: submitted reviews are mistaken for resolved review work

Control: represent submitted review states separately from inline review-thread resolution state and never infer thread resolution from review counts.

### Risk: Stage 5 expands into review or lifecycle automation

Control: prohibit automatic invocation, readiness/remediation decisions, repository mutation, approval/merge recommendations and repository-setting changes. Any new authority requires separate shaping and approval.

### Risk: completed transport or PR-diff work is reopened

Control: treat #141/#144 as completed invocation transport and #148/#149 as a separate validator lineage. Reuse only bounded precedent; do not absorb their responsibilities into Stage 5.

### Risk: ordinary-PR proof becomes artificial ceremony

Control: use naturally occurring implementation pull requests rather than dummy pilot PRs, require consecutive suitable cases, measure remaining manual evidence gathering, and record counter-evidence when the pack adds little or no value.

### Risk: a successful implementation is treated as adoption

Control: require the ordinary-PR proof and a distinct close-out decision. Implementation completion alone cannot satisfy the Stage 5 adoption gate.

## Definition of done

The stage is complete when:

- [ ] the approved Stage 5 execution issues are complete or explicitly resolved;
- [ ] canonical non-closing execution-contract linkage has been delivered and proved on ordinary work, or any residual limitation is explicitly governed and recorded;
- [ ] review-thread state is represented truthfully through bounded collection or explicit unavailable/incomplete state, with any permission limitation recorded honestly;
- [ ] all retained evidence/provenance/stale/error controls remain validated;
- [ ] Stage 4-aligned normal-review documentation is complete for the behaviour actually adopted or retained;
- [ ] at least three consecutive suitable ordinary IssueOps implementation pull requests have supplied the approved adoption proof and counter-evidence;
- [ ] the authority audit confirms no weakening of human substantive review or merge authority and no unauthorised collector mutation;
- [ ] limitations, deviations and cases where the evidence pack was not useful are recorded honestly;
- [ ] a completed Stage 5 delivery/close-out record exists under `planning/`;
- [ ] the final Stage 5 decision is recorded as **Adopt**, **Adapt** or **Reject**; and
- [ ] issue #90 is reconciled only at that later terminal decision boundary, without speculative next-stage implementation.

## Likely next decision boundary

After the roadmap is accepted, the next separately governed execution question is the **canonical non-closing execution-contract linkage** slice.

That issue should choose and validate the smallest deterministic repository-owned declaration compatible with normal IssueOps close-and-reconcile work, align the pull-request template and collector only as required by that contract, preserve conflict/fail-closed semantics, and avoid beginning review-thread implementation in the same slice.

Approval of this roadmap does not itself create or authorise that issue. The owner retains the decision to start each later slice through the normal IssueOps lifecycle.
