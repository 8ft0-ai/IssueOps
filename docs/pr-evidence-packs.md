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

Validation evidence should be concrete and matched to the type of change. For documentation-only changes, this may include reading changed Markdown files back from the branch, checking internal links by inspection, applying the [documentation currency checklist](documentation-currency.md), reviewing the MkDocs navigation and confirming that the change did not introduce automation or application code.

For workflow, publishing, process-label and future application-code changes, use the [change-type validation guidance](change-type-validation.md) to select the relevant evidence. Validation should not be marked complete unless it was completed.

## Documentation currency evidence

When documentation mentions releases, roadmap stages, PRs, issues, workflows, repository settings, labels, public site status or automation, record that the [documentation currency checklist](documentation-currency.md) was applied.

The PR should state whether the affected docs describe current, planned, pending or manual capabilities. Future automation should not be described as implemented unless it has actually been added and validated.

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

If review remediation changes the PR materially, the evidence pack must remain accurate.

A remediation is material when it changes validation evidence, security or permissions posture, dependency model, deployment behaviour, public documentation claims, files outside the original stated scope, assumptions, caveats or remaining checks.

For material remediation, either update the PR body or post a clearly labelled top-level remediation evidence comment. Minor typo or wording fixes can usually be handled with an inline reply if they do not change meaning, scope, validation or risk.

Use this format when a separate remediation evidence comment is clearer than rewriting the full PR body:

```md
## Remediation evidence

Review feedback addressed:

- Comment/thread:
- Change made:
- Validation rerun:
- Scope impact:

Final contract check:

- Did the PR still do what was needed?
- Did the PR still only do what was asked?
```

Use the [PR review remediation protocol](review-remediation.md) to classify review feedback, apply required fixes, rerun validation and decide whether to reply inline, post a top-level summary or update the PR body.

## Scope evidence

The evidence pack should also record what did not change. This is especially important in the current manual baseline, where the workflow does not include automatic Codex execution, branch protection changes, auto-merge, required status checks for agent work, automatic post-merge verification or application code.

## Review hand-off

A clear evidence pack gives the human reviewer enough information to perform contract verification. The reviewer can then decide whether the pull request fulfilled the issue contract, stayed inside scope and has enough evidence to approve.
