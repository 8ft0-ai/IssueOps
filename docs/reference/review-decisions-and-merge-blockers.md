# Review decisions and merge blockers

Contract verification compares the final pull request with the execution-contract issue. This page is the canonical reference for review classifications, recommendation vocabulary and merge blockers.

## Review recommendation vocabulary

Use one final recommendation.

| Recommendation | Meaning | Merge state |
| --- | --- | --- |
| **Approve** | The contract is satisfied, the diff remains inside scope, required pre-merge validation passed, no material finding remains and residual post-merge risk is acceptable to the authorised human. | May qualify for merge when repository policy and authority also permit it. |
| **Approve after minor fixes** | The implementation is substantially correct, but small identified fixes or evidence updates are required before approval is final. | Do not merge until the fixes are present, affected validation is rerun and the final state is reviewed. |
| **Do not approve yet** | Correctness, contract satisfaction, scope, validation or review state is unresolved. | Do not merge. |

A recommendation is not merge authority. Repository permissions, branch protection, required reviews and owner authorisation still apply.

## Evidence and contract questions

A reviewer should answer separately:

1. Is the evidence present, current and trustworthy?
2. Does the implementation satisfy the issue contract?
3. Did the implementation stay inside the contract boundaries?
4. Is remaining risk explicit and acceptable?

A complete evidence pack can describe an implementation that does not satisfy the contract. Conversely, a plausible implementation without sufficient evidence cannot be approved safely.

## Merge blockers

Do not recommend approval or merge when any of these conditions applies:

- implementation is incomplete;
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
- branch protection or required review policy is not satisfied;
- merge authority has not been granted; or
- merging would conceal incomplete or misleading evidence.

## Acceptable post-merge verification

A PR may still receive `Approve` with a named post-merge check when all of the following are true:

- implementation is complete;
- the contract is satisfied based on available evidence;
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
- excuse unresolved material findings; or
- authorise work beyond the execution contract.

## Related guidance

- [Review a pull request against its contract](../how-to/review-pr-against-contract.md)
- [Remediate review feedback](../how-to/remediate-review-feedback.md)
- [Pull-request evidence requirements](pr-evidence-requirements.md)
- [Why evidence is not approval](../explanation/pr-evidence-and-approval.md)
