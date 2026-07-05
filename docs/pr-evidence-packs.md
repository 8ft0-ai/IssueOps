# Pull requests as evidence packs

In this workflow, the pull request is the evidence pack. It should show how the issue contract was implemented, which boundaries were respected and what validation supports the change.

The reviewer should be able to compare the pull request with the issue contract without relying on chat history or memory.

## What to include

A useful evidence pack records:

- the linked issue contract;
- the files or documentation areas changed;
- the work deliberately left out;
- the acceptance criteria satisfied;
- the validation performed;
- any validation still pending; and
- any assumptions, risks or caveats.

## Validation evidence

Validation evidence should be concrete. For documentation-only changes, this may include reading changed Markdown files back from the branch, checking internal links by inspection, reviewing the MkDocs navigation and confirming that the change did not introduce automation or application code.

For later code changes, the evidence should reflect the repository validation that actually ran. Validation should not be marked complete unless it was completed.

## Scope evidence

The evidence pack should also record what did not change. This is especially important in Stage 1, where the workflow remains manual and does not include automatic Codex execution, branch protection changes, auto-merge, GitHub Actions orchestration or application code.

## Review hand-off

A clear evidence pack gives the human reviewer enough information to perform contract verification. The reviewer can then decide whether the pull request fulfilled the issue contract, stayed inside scope and has enough evidence to approve.
