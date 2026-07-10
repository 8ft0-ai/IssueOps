# IssueOps

The Agent Does Not Need a Ticket. It Needs an Execution Contract.

This repository explores a practical operating model for agentic coding with Codex and similar coding agents.

Traditional IssueOps often treats the issue as a control record. This repository takes a narrower position: for agentic coding, the issue should become the execution contract between the human, the agent and the reviewer.

The issue defines the problem, expected outcome, scope, non-goals, acceptance criteria and required validation evidence. The implementation plan records the proposed execution path. The pull request becomes the evidence pack a human uses to decide whether the contract was fulfilled and whether the change stayed inside its boundaries.

## Current baseline

Stage 1 established the manual execution-contract model. Stage 2 hardened that foundation into the current operating protocol through dependency-aware readiness, safe tool-operation controls, change-specific validation, review remediation, compact evidence formats, bounded delegated batch mode, repository-native pull-request validation and published canonical documentation.

The core loop remains human-controlled:

```text
Issue = execution contract
Readiness check = contract and dependency check
Implementation plan = proposed execution path
Tool-operation check = safe actuation gate
Agent = contract-bound implementer
Validation check = evidence hygiene
Pull request = evidence pack
Human review = contract verification
Merge = human approval decision
```

Start with [`docs/issueops-protocol.md`](docs/issueops-protocol.md) for the canonical operating protocol, [`AGENTS.md`](AGENTS.md) for agent operating rules, [`docs/tool-operations.md`](docs/tool-operations.md) for safe repository operations, and [`docs/pr-evidence-templates.md`](docs/pr-evidence-templates.md) for compact evidence formats.

## Releases

- [`v0.1.0`](docs/releases/stage-1.md) — Stage 1 manual execution-contract IssueOps.
- [`v0.2.0` recommended baseline](docs/releases/stage-2.md) — Stage 2 published and hardened operating model.

Stage 2 remains deliberately bounded. It does not provide automatic agent execution, automatic lifecycle transitions, required status checks, branch protection changes, auto-merge or automatic publication. The documented lifecycle labels also remain advisory and were not created because repository-level label creation was unavailable through the connected tooling.
