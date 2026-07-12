# Example contract verification

This example shows how a reviewer can verify a pull request against an execution contract.

It is illustrative. The canonical procedure is [Review a pull request against its contract](../how-to/review-pr-against-contract.md), and the exact recommendation and blocker rules are in [Review decisions and merge blockers](../reference/review-decisions-and-merge-blockers.md).

## Linked execution contract

Example: `Stage 1.1: Dogfood the execution-contract workflow`

## Evidence-pack review

Repository-observed evidence:

- the final diff adds one execution-contract example and one verification example;
- discoverability links are present; and
- no workflow or application-code file changed.

Contributor assertions to verify:

- the examples represent the current manual workflow;
- no Stage 2 design was introduced; and
- documentation validation and link review were completed as stated.

## Acceptance-criteria check

| Acceptance criterion | Review result |
| --- | --- |
| At least one example execution contract is added. | Satisfied. |
| At least one example contract verification or evidence-pack review is added. | Satisfied. |
| Documentation refinements are small and justified by the dogfood run. | Satisfied if only discoverability links are added. |
| Manual workflow remains Stage 1 / Stage 1.1 only. | Satisfied if no automation or Stage 2 design is introduced. |
| PR evidence pack explains what was learned. | Satisfied if the PR body records the learning. |

## Contract-boundary check

The reviewer should confirm that the pull request did not drift into:

- automation;
- branch protection;
- label enforcement;
- application code;
- Stage 2 design; or
- unrelated documentation rewrites.

## Validation-evidence check

For this documentation-only change, inspect:

- changed files read back from the feature branch;
- Markdown and generated pages;
- internal links;
- strict MkDocs validation; and
- the absence of unrelated automation or application code.

The existence of those checks does not prove contract satisfaction. The reviewer still compares the result with the issue outcome, acceptance criteria and non-goals.

## Remaining uncertainty

This review does not prove the workflow is perfect. It proves only that the issue-scoped examples satisfy the stated contract with the recorded evidence. Friction discovered during delivery belongs in the pull request or a follow-up issue rather than an unrecorded scope expansion.

## Groundedness review

Did the PR do what was needed?

- Yes, when both examples and the intended discoverability links are present and validated.

Did the PR only do what was asked?

- Yes, when the diff remains documentation-only and excludes the listed future-stage work.

## Final recommendation

`Approve` only when the evidence is current, the examples are clear, the acceptance criteria are satisfied, the diff remains inside scope and no merge blocker remains.
