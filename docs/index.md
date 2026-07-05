# IssueOps

**Jira for human planning. GitHub Issues for agent execution. Pull requests for proof.**

IssueOps is an experiment in making agentic coding safer and easier to review by turning the GitHub issue into an execution contract. The issue defines the work. The branch contains the implementation. The pull request becomes the evidence pack that a human can verify before deciding whether to merge.

The repository starts deliberately small. Stage 1 is a manual workflow for using Codex and similar coding agents inside a repository without pretending that automation is already in place. The point is to prove the language, boundaries and review evidence before adding orchestration.

## The thesis

Jira remains useful for human planning, prioritisation and portfolio context. It is where teams can discuss the broader problem, sequencing, dependencies and delivery intent.

GitHub Issues are better suited to the agent execution contract. A coding agent needs a bounded, reviewable instruction that says what to change, what not to change, how success will be assessed and what validation evidence is expected.

Pull requests provide proof. A good pull request should not simply describe the diff. It should show whether the issue contract was fulfilled, whether the change stayed inside scope and what evidence supports the result.

## The manual loop

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

## Where to start

Start with the [Stage 1 workflow](issueops.md) to understand the manual operating model.

Then read:

- [Execution contracts](execution-contracts.md) for what belongs in an agent-ready issue.
- [Pull requests as evidence packs](pr-evidence-packs.md) for how review evidence should be presented.
- [Contract verification](contract-verification.md) for the pre-approval review model.
- [Safe tool operations](tool-operations.md) for the manual check before repository mutations.
- [Examples](examples/README.md) for reference execution-contract and verification artefacts.

## Canonical docs and project memory

This MkDocs site is the canonical public documentation surface. It should contain the curated project thesis, workflow, controls, examples, release notes and roadmap.

The GitHub wiki remains useful, but it has a different role. It is for project memory, working notes, broader research, draft material and reports that are not yet part of the canonical documentation set. The distinction is explained in [Site and wiki boundaries](site-vs-wiki.md).

## Current baseline

The first baseline is [Stage 1: Manual Execution-Contract IssueOps](releases/stage-1.md), released as `v0.1.0`. It defines the manual workflow and explicit exclusions.

Stage 1 does not add automatic Codex execution, auto-merge, branch protection changes, required checks, GitHub Actions orchestration or application code.
