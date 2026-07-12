# Safe tool operations

Safe repository work requires a deliberate match between the current phase, intended mutation, selected tool, target and forbidden side effects.

This stable page now routes task procedure and exact operation rules to focused guidance. Permitted operations and the circuit breaker have not changed.

## Perform the task

- [Perform a safe repository mutation](how-to/perform-safe-repository-mutation.md)

## Check exact permissions and evidence

- [Operation permissions and evidence](reference/operation-permissions-and-evidence.md)

## What remains true

- The issue controls intent, the plan controls approach and the operation check controls actuation.
- Readiness, dependencies and implementation planning precede branch creation.
- Every mutation has one expected side effect and named forbidden effects.
- High-leverage operations require explicit issue scope and full evidence.
- Changed objects are fetched or read back after mutation.
- An unintended mutation activates the circuit breaker: stop normal writes, make only the minimum safe remediation, report it and require owner direction before continuing.
- Repository policy and human authority remain required for approval and merge.

The complete lifecycle remains in the [IssueOps operating protocol](issueops-protocol.md).

## Compatibility note

Earlier versions combined task sequence, evidence formats, phase permissions and the circuit breaker. Stage 4 separated those needs while preserving this URL as the safe-operation entry point.
