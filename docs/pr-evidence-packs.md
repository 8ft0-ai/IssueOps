# Pull requests as evidence packs

In this workflow, the pull request is the evidence pack. It should show how the issue contract was implemented, which boundaries were respected and what validation supports the change.

The reviewer should be able to compare the pull request with the issue contract without relying on chat history or memory.

## What to include

A useful evidence pack records:

- the linked issue contract;
- the change type or types;
- the files or documentation areas changed;
- the work deliberately left out;
- the acceptance criteria satisfied;
- the pre-merge validation performed;
- any validation not performed;
- any post-merge verification still required; and
- any assumptions, risks or caveats.

## Validation evidence

Validation evidence should be concrete and matched to the type of change. For documentation-only changes, this may include reading changed Markdown files back from the branch, checking internal links by inspection, reviewing the MkDocs navigation and confirming that the change did not introduce automation or application code.

For workflow, publishing, process-label and future application-code changes, use the [change-type validation guidance](change-type-validation.md) to select the relevant evidence. Validation should not be marked complete unless it was completed.

## Validation status

When a change has checks that can run before merge and checks that can only run after merge, separate them in the PR body.

Use this format:

```md
## Validation status

Pre-merge validation completed:

- [x] Files read back from branch
- [x] Local build/test completed
- [x] Scope checked against issue

Post-merge verification required:

- [ ] Workflow run observed
- [ ] Deployment URL checked
- [ ] Repository setting confirmed

Merge decision:

- Safe to merge with post-merge verification pending / do not merge yet.
```

Post-merge verification is acceptable only when the implementation is complete, available validation is not failing, the remaining check cannot run before merge or deployment and the PR states exactly what still needs to be verified.

Pending validation should block merge when it is needed to decide whether the issue contract was satisfied, when available validation is failing or when merging would make the evidence pack misleading.

## Remediation evidence

If review remediation changes the PR materially, the evidence pack should remain accurate.

Use the [PR review remediation protocol](review-remediation.md) to classify review feedback, apply required fixes, rerun validation and decide whether to reply inline, post a top-level summary or update the PR body.

## Scope evidence

The evidence pack should also record what did not change. This is especially important in the current manual baseline, where the workflow does not include automatic Codex execution, branch protection changes, auto-merge, required status checks for agent work, automatic post-merge verification or application code.

## Review hand-off

A clear evidence pack gives the human reviewer enough information to perform contract verification. The reviewer can then decide whether the pull request fulfilled the issue contract, stayed inside scope and has enough evidence to approve.
