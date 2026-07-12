# IssueOps

The Agent Does Not Need a Ticket. It Needs an Execution Contract.

This repository explores a practical operating model for agentic coding with Codex and similar coding agents.

Traditional IssueOps often treats the issue as a control record. This repository takes a narrower position: for agentic coding, the issue should become the execution contract between the human, the agent and the reviewer.

The issue defines the problem, expected outcome, scope, non-goals, acceptance criteria and required validation evidence. The implementation plan records the proposed execution path. The pull request becomes the evidence pack a human uses to decide whether the contract was fulfilled and whether the change stayed inside its boundaries.

## Current baseline

Stage 1 established the manual execution-contract model. Stage 2 hardened that foundation into the current recommended stable operating protocol through dependency-aware readiness, safe tool-operation controls, change-specific validation, review remediation, compact evidence formats, bounded delegated batch mode, repository-native pull-request validation and published canonical documentation.

Stage 3 added an experimental, manually invoked and read-only pull-request evidence collector. It is retained for controlled evaluation with an **Adapt** decision and is not the recommended operational baseline.

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

## Start here

- [Documentation home](docs/index.md) — choose a Tutorial, How-to, Reference or Explanation path.
- [Complete your first small IssueOps change](docs/tutorials/first-issueops-change.md) — learn the complete loop through a guided documentation-only exercise.
- [How-to guides](docs/how-to/index.md) — complete a specific contributor or reviewer task.
- [Reference](docs/reference/index.md) — check exact rules, fields, formats and validation requirements.
- [Explanation](docs/explanation/index.md) — understand the model, authority boundaries and trade-offs.
- [Agent operating rules](AGENTS.md) — repository-specific instructions for coding agents.

## Project records and baselines

Project planning, delivery evidence and historical snapshots remain outside the substantive Diátaxis documentation tree:

- [Planning control surface](planning/README.md)
- [Roadmap index](planning/roadmap/index.md)
- [Delivery records](planning/delivery/index.md)
- [Historical evidence and compatibility decisions](planning/evidence/index.md)

Baseline compatibility pages remain available for public links:

- [`v0.1.0` Stage 1 baseline](docs/releases/stage-1.md)
- [`v0.2.0` recommended stable baseline](docs/releases/stage-2.md)
- [Proposed `v0.3.0-alpha.1` experimental snapshot](docs/releases/stage-3-alpha.md)

The stable baseline remains deliberately bounded. It does not provide automatic agent execution, automatic lifecycle transitions, required status checks, branch protection changes, auto-merge or automatic publication. The Stage 3 alpha does not expand those authority boundaries or represent routine operational adoption.