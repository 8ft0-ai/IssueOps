# IssueOps

The Agent Does Not Need a Ticket. It Needs an Execution Contract.

This repository explores a practical operating model for agentic coding with Codex and similar coding agents.

Traditional IssueOps often treats the issue as a control record. This repository takes a narrower position: for agentic coding, the issue should become the execution contract between the human, the agent and the reviewer.

The issue defines the problem, expected outcome, scope, non-goals, acceptance criteria and required validation evidence. The implementation plan records the proposed execution path. The pull request becomes the evidence pack a human uses to decide whether the contract was fulfilled and whether the change stayed inside its boundaries.

## Current baseline

Stage 1 established the manual execution-contract model. Stage 2 hardened that foundation through dependency-aware readiness, safe tool-operation controls, change-specific validation, review remediation, compact evidence formats, bounded delegated batch mode, repository-native pull-request validation and published canonical documentation.

The current recommended stable baseline is `v0.3.0`. It consolidates the compatible operating model proved after `v0.2.0`: Stage 4's adopted Diátaxis documentation architecture, Stage 5's adopted human-triggered read-only evidence assistance, portable IssueOps bootstrap/adoption and adopted modular-session guidance.

The `/collect-evidence` execution bridge and repository-native PR-diff validation are bounded supporting mechanisms within that model; they do not create generic execution authority. The primary-record inspector and static GitHub Actions workflow auditor remain optional/advisory tools rather than lifecycle authorities.

Stage 3's `v0.3.0-alpha.1` release remains a historical experimental snapshot with an **Adapt** decision. The stable `v0.3.0` baseline reflects the later consolidated adopted operating model; it does not reclassify the Stage 3 alpha itself as stable.

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
- [`v0.2.0` Stage 2 baseline](docs/releases/stage-2.md)
- [`v0.3.0-alpha.1` Stage 3 experimental snapshot](docs/releases/stage-3-alpha.md)
- [`v0.3.0` recommended stable baseline](docs/releases/v0.3.0.md)

The stable baseline remains deliberately bounded. It does not provide generic workflow or command execution, automatic agent execution, automatic lifecycle transitions or readiness/approval decisions, required status checks or ruleset/branch-protection changes, auto-merge, automatic release publication, or broader repository-setting/merge-authority expansion.