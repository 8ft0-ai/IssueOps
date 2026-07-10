# IssueOps

**Jira for human planning. GitHub Issues for agent execution. Pull requests for proof.**

IssueOps is an experiment in making agentic coding safer and easier to review by turning the GitHub issue into an execution contract. The issue defines the work. The branch contains the implementation. The pull request becomes the evidence pack that a human can verify before deciding whether to merge.

The repository starts deliberately small. Stage 1 established the manual workflow, while Stage 2 hardened it into the current operating protocol with clearer readiness, dependency, validation, remediation and evidence controls.

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

Start with the [IssueOps operating protocol](issueops-protocol.md). It is the canonical process overview from issue readiness through planning, implementation, validation, review, merge and post-merge verification.

For a small, low-risk change, use this path:

1. Confirm the issue is executable and record readiness and dependencies.
2. Post the implementation plan before creating the feature branch.
3. Use the [compact safe-operation evidence](tool-operations.md#compact-evidence-format) for routine mutations, or the full format when risk or ambiguity is higher.
4. Select validation through [change-type validation guidance](change-type-validation.md), preferring [repository-native validation](repository-native-validation.md).
5. Start the PR evidence pack from the relevant [compact PR evidence template](pr-evidence-templates.md), while retaining any full evidence required by the issue or risk level.
6. Complete [contract verification](contract-verification.md), remediate substantive feedback and record post-merge checks only when genuinely required.

The focused pages remain supporting references rather than separate process entry points:

- [Execution contracts](execution-contracts.md) for what belongs in an agent-ready issue.
- [Pull requests as evidence packs](pr-evidence-packs.md) for full review-evidence expectations.
- [Safe tool operations](tool-operations.md) for routine and higher-risk mutation checks.
- [PR review remediation](review-remediation.md) for handling feedback after review.
- [Examples](examples/README.md) for reference execution-contract and verification artefacts.

See the [Stage 2 contributor usability review](contributor-usability-review.md) for the walkthrough and the reasoning behind this front-door path.

## Canonical docs and project memory

This MkDocs site is the canonical public documentation surface. It should contain the curated project thesis, workflow, controls, examples, release notes and roadmap.

The GitHub wiki remains useful, but it has a different role. It is for project memory, working notes, broader research, draft material and reports that are not yet part of the canonical documentation set. The distinction is explained in [Site and wiki boundaries](site-vs-wiki.md).

## Current baseline

The first baseline is [Stage 1: Manual Execution-Contract IssueOps](releases/stage-1.md), released as `v0.1.0`. Stage 2 extends that baseline through the current manual operating protocol; it does not add automatic Codex execution, auto-merge, branch protection changes, required checks or application code.