# Manual label taxonomy

Stage 1 uses labels as a manual communication aid. Labels do not trigger automation yet. They help contributors understand the current state of an issue or pull request.

| Label | Meaning |
| --- | --- |
| `needs-triage` | New work that has not yet been assessed. |
| `needs-clarification` | Work that needs a clearer scope, acceptance criteria or validation expectation. |
| `ready-for-agent` | Work that has passed readiness review and can be implemented by Codex or another coding agent. |
| `agent-in-progress` | Work that has a posted implementation plan and an active feature branch. |
| `blocked` | Work that cannot continue until a decision, access requirement or failed check is resolved. |
| `needs-human-review` | Work that is ready for human review. |
| `validation-pending` | Work where some validation remains incomplete and is explicitly recorded in the pull request. |

In Stage 1, labels are advisory only. Written issue comments and pull request descriptions remain the source of truth.
