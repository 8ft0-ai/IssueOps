# Why evidence is not approval

IssueOps describes the pull request as an evidence pack because review needs more than a diff. The reviewer needs the authorising issue, the final scope, the validation record, the known limitations and the relationship between the implementation and the contract.

That evidence improves the decision. It does not make the decision automatically.

## The pull request connects implementation to intent

The issue states what was needed and what was forbidden. The branch contains the proposed implementation. The pull request gathers the evidence needed to compare them.

A useful evidence pack answers:

- What changed?
- What was deliberately excluded?
- Which acceptance criteria are satisfied?
- Which validation ran against the final state?
- What remains pending or can run only after merge?
- What risks, assumptions or caveats remain?

This makes review reproducible from the repository record rather than dependent on chat history or memory.

## Evidence presence and contract satisfaction are different

A pull request may contain complete evidence that shows the implementation is wrong, incomplete or outside scope. The evidence pack has still done its job: it made the mismatch visible.

A different pull request may appear to satisfy the issue but lack trustworthy validation or a current final-diff review. The implementation may be plausible, but approval would require guessing.

The human reviewer therefore asks two separate questions:

1. Is the evidence current, complete enough and trustworthy?
2. Does the final implementation satisfy the execution contract without exceeding it?

Neither answer can be replaced by a green status icon alone.

## Repository observations and assertions

Some evidence is observed directly from the repository: file contents, commits, diffs, workflow results, review threads and generated artefacts.

Other content is an assertion by the contributor or agent: why the change was made, what was excluded, which caveat matters and how the acceptance criteria were interpreted.

Assertions are useful, but they require review. An evidence pack should not make an inference look like a repository fact.

## Groundedness review

The pre-approval groundedness review asks whether the implementation did what was needed and only what was asked. It is a structured self-check that makes scope and evidence reasoning visible.

When an agent writes that review, it remains agent-generated analysis. It is not an independent human GitHub review, and it cannot grant itself approval or merge authority.

A human may use the analysis, verify it and make the decision.

## Human authority remains necessary

Approval includes judgement that cannot be reduced safely to evidence collection alone:

- whether the issue outcome was interpreted correctly;
- whether the residual risk is acceptable;
- whether a scope adaptation remained faithful to intent;
- whether post-merge verification is legitimately deferred; and
- whether the change should enter the stable branch now.

Repository-owner delegation may authorise an agent to continue through routine issue and merge operations after every gate passes. That delegation changes who performs the mechanics, not what qualifies as evidence or who owns the approval authority.

## Why post-merge verification exists

Some facts cannot be observed before merge, such as a production-only deployment or an environment setting applied after the branch enters `main`.

Recording those checks separately prevents two opposite errors:

- pretending that unavailable evidence already exists; and
- blocking a complete, validated implementation on a check that genuinely cannot run earlier.

Post-merge verification is not a general escape hatch. Any test or review that can determine correctness before merge remains pre-merge evidence.

## Why remediation must refresh the evidence pack

Review changes the proposed implementation. When remediation affects scope, validation, permissions, public claims, dependencies or residual risk, the earlier evidence pack may no longer describe the final head.

Updating the evidence is part of the fix because approval applies to the final state, not the original submission.

## Canonical requirements

This explanation introduces no hidden recommendation or blocker.

Use:

- [Pull-request evidence requirements](../reference/pr-evidence-requirements.md) for exact content;
- [PR evidence templates](../reference/pr-evidence-templates.md) for reusable formats;
- [Review decisions and merge blockers](../reference/review-decisions-and-merge-blockers.md) for the normative vocabulary; and
- [Review a pull request against its contract](../how-to/review-pr-against-contract.md) for the procedure.
