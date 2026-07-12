# PR review remediation

Review remediation is the controlled loop for addressing feedback without losing the execution contract, validation evidence or scope boundary.

This stable page now routes the task procedure, exact classifications and evidence format to focused guidance. The remediation behaviour has not changed.

## Remediate the pull request

- [Remediate pull-request review feedback](how-to/remediate-review-feedback.md)

## Check exact classifications and blockers

- [Review decisions and merge blockers](reference/review-decisions-and-merge-blockers.md)
- [Remediation evidence template](reference/pr-evidence-templates.md#remediation-evidence-template)

## Review the final result

- [Review a pull request against its contract](how-to/review-pr-against-contract.md)
- [Pull-request evidence requirements](reference/pr-evidence-requirements.md)

## What remains true

Classify every feedback item as:

- required fix;
- optional improvement;
- clarification needed; or
- out of scope.

Apply required fixes and only clearly safe, scoped optional improvements. Do not implement out-of-scope work without an explicit contract expansion or follow-up issue.

After remediation:

- read changed files back;
- compare the branch with `main`;
- rerun affected validation;
- reply to addressed findings;
- resolve threads only after the fix is present and checks are not failing;
- refresh material PR evidence; and
- repeat contract verification against the final head.

## Compatibility note

Earlier versions of this page combined the complete procedure, classifications, checklist and evidence template. Stage 4 separated those needs while preserving this URL as the remediation entry point.
