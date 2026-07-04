# Example contract verification

This example shows how a reviewer can verify a pull request against an execution contract.

The review should not ask only whether the diff looks reasonable. It should ask whether the pull request fulfilled the contract and stayed inside its boundaries.

## Linked execution contract

Example: `Stage 1.1: Dogfood the execution-contract workflow`

## Evidence pack review

What changed:

- Added an example execution contract.
- Added an example contract verification review.
- Linked the examples from the workflow documentation.

What was deliberately excluded:

- No automation was added.
- No labels were created or enforced.
- No GitHub Actions workflow was added.
- No application code was added.
- No Stage 2 design was introduced.

## Acceptance criteria check

| Acceptance criterion | Review result |
| --- | --- |
| At least one example execution contract is added. | Satisfied. |
| At least one example contract verification or evidence-pack review is added. | Satisfied. |
| Documentation refinements are small and justified by the dogfood run. | Satisfied if only discoverability links are added. |
| Manual workflow remains Stage 1 / Stage 1.1 only. | Satisfied if no automation or Stage 2 design is introduced. |
| PR evidence pack explains what was learned. | Satisfied if the PR body records the learning. |

## Contract boundary check

The reviewer should check that the pull request did not drift into:

- automation;
- branch protection;
- label enforcement;
- application code;
- Stage 2 design; or
- unrelated documentation rewrites.

## Validation evidence check

For a documentation-only change, acceptable evidence includes:

- changed files read back from the feature branch;
- Markdown reviewed manually for clarity;
- internal links checked by inspection;
- explicit confirmation that no automation or application code was added.

## Remaining uncertainty

This kind of review does not prove the workflow is perfect. It only proves that the manual loop is usable for a small follow-up change. Any friction discovered during the run should be captured in the pull request rather than silently corrected outside the contract.

## Final recommendation

Approve if the examples are clear, the PR evidence pack is complete and the change remains inside the issue contract.
