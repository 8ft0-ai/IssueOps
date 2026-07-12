# Contract verification

Contract verification is the human review step that compares the final pull request with its execution-contract issue.

This stable page now routes review procedure and exact decision rules to focused guidance. Human approval and merge authority remain unchanged.

## Review the pull request

- [Review a pull request against its contract](how-to/review-pr-against-contract.md)
- [Remediate pull-request review feedback](how-to/remediate-review-feedback.md)

## Check exact decisions and blockers

- [Review decisions and merge blockers](reference/review-decisions-and-merge-blockers.md)
- [Pull-request evidence requirements](reference/pr-evidence-requirements.md)

## Understand the distinction

- [Why evidence is not approval](explanation/pr-evidence-and-approval.md)

## What remains true

The reviewer asks:

1. Did the pull request do what was needed?
2. Did the pull request only do what was asked?

The review considers issue alignment, acceptance criteria, non-goals, final scope, validation evidence, remaining checks, risks, caveats and unresolved review findings.

Use one final recommendation:

- `Approve`;
- `Approve after minor fixes`; or
- `Do not approve yet`.

Do not recommend approval when implementation is incomplete, required validation is failing or unavailable, scope has drifted, evidence is stale or a material finding remains unresolved.

An agent-generated groundedness review is evidence for the reviewer. It is not independent human review and does not grant approval or merge authority.

## Compatibility note

Earlier versions of this page combined procedure, blockers and recommendation definitions. Stage 4 separated those needs while preserving this URL as the contract-verification entry point.
