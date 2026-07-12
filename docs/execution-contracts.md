# Execution contracts

An execution contract is a GitHub issue written so that an agent or contributor can implement safely and a human can review meaningfully.

This stable page is now the entry point to focused IssueOps guidance. The underlying fields, readiness gates and authority model have not changed.

## Choose what you need

### Write or prepare the work

- [Write an executable issue contract](how-to/write-executable-issue.md)
- [Check readiness and dependencies](how-to/check-readiness-and-dependencies.md)
- [Prepare an implementation plan](how-to/prepare-implementation-plan.md)

### Check an exact rule or format

- [Execution-contract fields](reference/execution-contract-fields.md)
- [Readiness and dependency formats](reference/readiness-and-dependency-formats.md)
- [Implementation-plan format](reference/implementation-plan-format.md)

### Understand the model

- [Why the issue is the execution contract](explanation/execution-contract-model.md)

### Inspect an example

- [Example documentation-only execution contract](examples/execution-contract-example.md)

## What remains true

- The issue is the durable source of implementation intent.
- The issue must state the problem, expected outcome, scope, non-goals, acceptance criteria, validation evidence, risk and agent instructions.
- Dependencies and roadmap relationships are explicit when they govern the work.
- Readiness and dependency state are recorded before the implementation plan.
- The implementation plan is posted before branch creation.
- One feature branch contains one issue’s implementation.
- The pull request carries evidence that a human verifies against the issue.
- Evidence does not grant approval or merge authority.
- When material intent is missing, clarify the contract rather than guessing.

The complete lifecycle remains in the [IssueOps operating protocol](issueops-protocol.md).

## Compatibility note

Earlier versions of this page combined rationale, exact fields and task guidance. Stage 4 separated those reader needs while preserving this URL as the route into the current canonical pages.

Do not copy the old mixed structure into new documentation. Put exact requirements in Reference, task sequence in How-to and rationale in Explanation.
