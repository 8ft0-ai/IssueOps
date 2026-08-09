# Prepare a pull-request evidence pack

Use this guide after implementation is complete enough to describe and validate, and before asking a human to approve the change.

For exact required sections, linkage rules and collection semantics, use [Pull-request evidence requirements](../reference/pr-evidence-requirements.md). For reusable bodies, use [PR evidence templates](../reference/pr-evidence-templates.md).

## 1. Refresh the issue and final branch state

Read:

- the execution-contract issue and later clarifications;
- readiness and dependency evidence;
- the detailed implementation-plan comment;
- the separate durable human approval of that plan;
- any additional procedural authority required for the work;
- the final changed-file list and diff;
- the current branch head;
- validation results and generated artefacts; and
- existing PR comments, reviews and threads when updating an open PR.

Verify that the human plan approval clearly applies to the detailed implementation plan and predates branch creation or implementation mutation. If required pre-action authority is missing or was created only retrospectively, record the lifecycle defect rather than filling the gap by inference.

The evidence pack must describe the current decision-relevant head, not an earlier implementation state.

## 2. Link the execution contract

Use the canonical IssueOps declaration:

```md
## Execution contract

Issue #<issue-number>
```

The issue remains the execution contract; the pull request identifies it without duplicating its contract content.

Add `Closes #N`, `Fixes #N` or `Resolves #N` separately only when merge should deliberately close that same issue. Closing keywords are GitHub lifecycle syntax, not the canonical IssueOps linkage.

Use [Pull-request evidence requirements](../reference/pr-evidence-requirements.md) for the exact canonical, legacy and conflict semantics. Link the parent stage or roadmap when it materially governs the slice.

Do not claim that a planning issue is being implemented directly when a separate execution contract authorised the branch.

## 3. Record lifecycle authority

Record the durable GitHub references for:

- readiness assessment;
- detailed implementation plan;
- human approval of that implementation plan; and
- any additional procedural authority required for the work, or explicit `N/A` when none is required.

The plan and its approval are separate records. Required authority must exist before the action it authorises; a later comment cannot be used to make an already-started implementation retrospectively compliant.

Additional procedural authority is conditional. For example, `/collect-evidence` remains optional and must be requested only when the governing issue/session separately authorises that repository mutation.

## 4. Describe changed and excluded work

State what changed and why. Then name the relevant non-goals and adjacent work deliberately excluded.

Compare the actual diff with the implementation plan. Record any material adaptation and why it remained inside the issue contract and approved execution path.

Do not hide unexpected files in a broad summary such as “miscellaneous cleanup”.

## 5. Map the result to acceptance criteria

Explain how the final repository state satisfies each material criterion. Point to files, generated output, tests or observations where useful.

When a criterion is not satisfied, do not present the PR as complete. Mark the gap and use `Do not approve yet`.

## 6. Record validation truthfully

Separate:

- pre-merge validation completed;
- validation not performed or still pending; and
- post-merge verification that cannot run earlier.

Tie workflow results and generated artefacts to the exact final head. Do not reuse a passing result from an earlier commit after remediation changes relevant files.

When local validation is unavailable, leave it unchecked and use the repository-native result only after it completes. Do not describe pending validation as a successful fallback.

## 7. Prepare for evidence-assisted review

When the current IssueOps session is explicitly authorised to request evidence collection for this pull request, it may deliberately post the exact `/collect-evidence` PR comment before the substantive review decision.

Do not treat repository write access or collaborator status as IssueOps authority to request collection. Use [Pull-request evidence requirements](../reference/pr-evidence-requirements.md#deliberate-evidence-collection) for the exact command, GitHub eligibility, request identity, correlation, artifact and failure semantics.

Before relying on a collected pack, make sure the pull request is at the decision-relevant head and that the validation and review state you expect to assess are present. Collection is a snapshot of repository state, not a lifecycle transition or approval action.

## 8. State risks, caveats and residual checks

Record assumptions, environmental limitations, compatibility decisions, deferred work and residual post-merge risk.

A caveat is not a substitute for fixing a known contract failure. When correctness depends on an unresolved fact, the PR remains blocked.

## 9. Perform the groundedness review

Answer:

1. Did we do what was needed?
2. Did we only do what was asked?

Then check issue alignment, lifecycle authority, scope control, validation evidence, risks and caveats. Use one final recommendation from the canonical vocabulary.

Do not recommend `Approve` when required pre-implementation authority is missing or retrospective, even if the implementation and technical validation are otherwise satisfactory.

State transparently when the review was generated by the implementation agent. It is useful evidence but not independent human review.

## 10. Record merge authorisation

Where delegated batch delivery applies, identify the repository-owner authorisation and its conditions. Do not imply that delegation overrides branch protection, required reviews, failing checks or unresolved material findings.

Implementation-plan approval is not merge authorisation. Merge remains a later decision after substantive review of the final state.

## 11. Open as a draft when work remains

Keep the PR as a draft while implementation, required validation, evidence updates or remediation is incomplete.

Mark it ready only when the evidence pack reflects the final head, required checks are not failing and the groundedness review can honestly recommend `Approve`.

## 12. Keep evidence current

After material remediation or another material head, validation or review-state change:

- read changed files back;
- rerun affected validation;
- update the PR body or post labelled remediation evidence;
- inspect comments, submitted reviews and inline review threads;
- treat any earlier collected evidence as a prior snapshot rather than silently carrying it forward;
- when collection is still authorised and the change affects the decision-relevant evidence, deliberately request and correlate a new `/collect-evidence` snapshot; and
- repeat the final groundedness review.

A new evidence request does not advance the lifecycle automatically. It only refreshes the mechanical evidence available to the reviewer.

## Common failure modes

- using a closing keyword as though it were the canonical IssueOps execution-contract declaration;
- omitting the separate human plan-approval record from the evidence pack;
- treating the implementation plan as self-authorising;
- using a retrospective comment to manufacture missing pre-action authority;
- requesting `/collect-evidence` merely because the actor has repository write access;
- summarising the intended plan instead of the final diff;
- marking checks complete because they are expected to pass;
- omitting deliberately excluded work;
- treating a generated report as approval;
- relying on a collected snapshot after material head, validation or review state has changed;
- retaining an `Approve` recommendation after material remediation without revalidation; or
- presenting delegated merge authority as permission to bypass repository policy.
