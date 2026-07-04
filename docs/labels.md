# Manual label model

Stage 1 uses labels as manual state markers. Labels do not trigger automation yet.

The labels should describe the state of the execution contract, the agent work and the review evidence. Written issue and pull request content remains the source of truth.

| Label | Meaning |
| --- | --- |
| `contract/draft` | The issue contract exists but has not been checked. |
| `contract/needs-clarification` | The contract is not clear enough for agent implementation. |
| `contract/ready` | The contract is clear enough for Codex to implement. |
| `agent/codex` | Codex is the intended implementation agent. |
| `agent/in-progress` | Agent-assisted implementation has started. |
| `review/evidence-needed` | The pull request needs clearer evidence before review. |
| `review/human-required` | A human review decision is required. |
| `validation/pending` | Validation remains incomplete and must be recorded in the pull request. |
| `validation/complete` | Required validation for the current stage has been completed. |
| `scope/drift-risk` | The work may be moving outside the issue contract. |

These labels are intentionally lightweight. Later stages may attach automation to label changes, but Stage 1 keeps labels manual and advisory.
