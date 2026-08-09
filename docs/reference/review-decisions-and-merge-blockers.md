# Review decisions and merge blockers

Contract verification compares the final pull request with the execution-contract issue. This page is the canonical reference for review classifications, recommendation vocabulary and merge blockers.

## Review recommendation vocabulary

Use one final recommendation.

| Recommendation | Meaning | Merge state |
| --- | --- | --- |
| **Approve** | The contract is satisfied, required pre-implementation lifecycle authority is valid, the diff remains inside scope, required pre-merge validation passed, no material finding remains and residual post-merge risk is acceptable to the authorised human. | May qualify for merge when repository policy and later merge authority also permit it. |
| **Approve after minor fixes** | The implementation is substantially correct, but small identified fixes or evidence updates are required before approval is final. | Do not merge until the fixes are present, affected validation is rerun and the final state is reviewed. |
| **Do not approve yet** | Correctness, contract satisfaction, lifecycle authority, scope, validation or review state is unresolved. | Do not merge. |

A recommendation is not merge authority. Repository permissions, branch protection, required reviews and owner authorisation still apply.

## Pre-implementation lifecycle authority

The implementation plan is a proposed execution path, not self-authorising permission to begin work.

Before branch creation or implementation mutation, durable GitHub evidence must contain explicit human approval of the detailed implementation plan. That approval must clearly apply to the plan being executed and must predate the action it authorises.

A missing required human plan-approval record is a lifecycle and approval defect even when the resulting implementation is technically correct and validation passes. A later comment cannot retrospectively manufacture normal pre-action authority for work that has already begun. Do not recommend `Approve` while that required authority defect remains.

Additional procedural authority is conditional. When a governed action such as `/collect-evidence` is used, the action must have its own durable authority where the governing issue/session requires it. When no additional authority is required, `N/A` is valid.

This pre-implementation authority boundary is separate from the later human merge decision.

## Durable merge-authority provenance

Before merge is invoked, current durable GitHub evidence must contain an explicit human merge decision for the exact state being merged. At minimum, the authority record must identify:

```text
pull request
exact accepted head SHA
accepted independent review/recommendation or equivalent current review state
explicit human merge decision for that exact state
```

Chat-only approval that is first copied to GitHub after merge is not sufficient normal pre-action provenance for this boundary. Repository write access, connector capability, an `Approve` recommendation or a role label also does not create merge authority.

Immediately before merge, the merge executor must re-fetch and compare the current pull-request head and material review state with the durable authority record. If the head or material review state has changed, the prior human decision is **stale for merge purposes**. Stop and obtain a fresh human decision tied to the new exact state before invoking merge.

The human owner may merge directly or may explicitly authorise a separate non-review execution context to invoke merge. In either case, the independent Review or evaluate session must already have terminated after recording its final recommendation; later human approval does not reopen that reviewer model context.

## Evidence and contract questions

A reviewer should answer separately:

1. Is the evidence present, current and trustworthy?
2. Did the required pre-implementation lifecycle authority exist before the work it authorised?
3. Does the implementation satisfy the issue contract?
4. Did the implementation stay inside the contract boundaries?
5. Is remaining risk explicit and acceptable?

A complete evidence pack can describe an implementation that does not satisfy the contract. Conversely, a plausible implementation without sufficient evidence or required lifecycle authority cannot be approved safely.

## Review and merge blockers

Do not recommend approval or merge when any of these conditions applies:

- implementation is incomplete;
- required pre-implementation human plan approval is missing, retrospective or does not clearly apply to the executed plan;
- required additional procedural authority for an action taken under the governing work is missing;
- the expected outcome or acceptance criteria are not satisfied;
- the diff contains unexplained work outside scope;
- a stated non-goal was violated;
- required validation is failing;
- required validation is unavailable and correctness depends on it;
- the evidence pack is stale relative to the final head;
- a material review comment or required thread remains unresolved;
- remediation is incomplete or affected validation was not rerun;
- permissions, security, deployment or public claims remain uncertain;
- a post-merge check is being used to defer evidence that should exist before merge;
- the change weakens or ambiguously changes an authority boundary;
- branch protection or required review policy is not satisfied; or
- merging would conceal incomplete or misleading evidence.

## Merge-only authority blockers

An otherwise valid independent `Approve` recommendation may exist before human merge authority is granted. The recommendation does not satisfy this later boundary.

Do not invoke merge when:

- durable pre-action human merge authority for the exact current PR head and accepted review state is absent;
- the recorded human merge decision is stale because the head or material review state moved; or
- merge authority otherwise has not been granted.

These are merge blockers, not reasons to keep an otherwise contract-satisfying independent review from recording its recommendation. Human merge authority is established after the accepted review and before merge execution; it is separate from the earlier human approval that authorised implementation to begin.

## Acceptable post-merge verification

A PR may still receive `Approve` with a named post-merge check when all of the following are true:

- implementation is complete;
- the contract is satisfied based on available evidence;
- required pre-implementation lifecycle authority is valid;
- required pre-merge validation passed;
- no available check is failing;
- the remaining check genuinely cannot run before merge or deployment;
- the exact follow-up is recorded;
- residual risk is understood; and
- an authorised human accepts that risk.

Examples include checking a production-only Pages deployment or confirming a repository setting that becomes observable only after merge. A unit test, strict build or final-diff review that can run before merge is not post-merge verification.

## Review-feedback classifications

Classify each feedback item before remediation.

| Classification | Meaning | Action |
| --- | --- | --- |
| **Required fix** | A defect, missed criterion, inaccurate evidence, unsafe permission, broken link, failing validation or contract gap. | Fix before approval or provide evidence that the finding is invalid. |
| **Optional improvement** | Useful clarity or maintainability improvement not required by the issue. | Apply only when clearly safe and inside scope. |
| **Clarification needed** | The feedback is ambiguous or may change scope. | Resolve the question before editing. |
| **Out of scope** | The request exceeds the issue contract. | Do not implement without explicit scope expansion or a follow-up issue. |

When classification is uncertain, use `Clarification needed` rather than guessing.

## Delegated batch review

Repository-owner delegation may authorise routine merge after all gates pass. It does not:

- convert agent analysis into independent human review;
- override required reviews or branch protection;
- permit failing or unavailable required validation;
- excuse unresolved material findings;
- repair missing required pre-implementation lifecycle authority retrospectively;
- remove the requirement for durable exact-state merge authority; or
- authorise work beyond the execution contract.

## Related guidance

- [Review a pull request against its contract](../how-to/review-pr-against-contract.md)
- [Remediate review feedback](../how-to/remediate-review-feedback.md)
- [Pull-request evidence requirements](pr-evidence-requirements.md)
- [Why evidence is not approval](../explanation/pr-evidence-and-approval.md)
