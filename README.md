# IssueOps

The Agent Does Not Need a Ticket. It Needs an Execution Contract.

This repository explores a practical operating model for agentic coding with Codex.

Traditional IssueOps often treats the issue as a control record. This repository takes a narrower position: for agentic coding, the issue should become the execution contract between the human, the agent and the reviewer.

Codex does not need a vague ticket or an informal prompt. It needs a bounded contract that states the problem, expected outcome, scope, non-goals, acceptance criteria and validation evidence expected. The pull request then becomes the evidence pack a human uses to decide whether the contract was fulfilled and whether the change stayed inside its boundaries.

Stage 1 is deliberately manual. It establishes the language, templates, safety checks and review model before adding automation.

The core loop is:

```text
Issue = execution contract
Readiness check = contract check
Implementation plan = proposed execution path
Tool-operation check = safe actuation gate
Codex = contract-bound implementer
Validation check = evidence hygiene
Pull request = evidence pack
Human review = contract verification
Merge = human approval decision
```

Start with [`docs/issueops.md`](docs/issueops.md) for the workflow, [`AGENTS.md`](AGENTS.md) for agent operating rules, [`docs/tool-operations.md`](docs/tool-operations.md) for safe repository operations, [`docs/examples`](docs/examples/README.md) for examples and [`docs/labels.md`](docs/labels.md) for the manual label model.

The recommended first baseline release is [`v0.1.0`](docs/releases/stage-1.md): Stage 1 manual execution-contract IssueOps.
