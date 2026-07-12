# IssueOps

**Jira for human planning. GitHub Issues for agent execution. Pull requests for proof.**

IssueOps is an experiment in making agentic coding safer and easier to review by turning the GitHub issue into an execution contract. The issue defines the work. The branch contains the implementation. The pull request carries the evidence pack that a human verifies before deciding whether to merge.

The repository starts deliberately small. Stage 1 established the manual workflow, Stage 2 hardened it into the current recommended operating protocol, and Stage 3 tested read-only evidence-pack assistance as an experimental alpha capability. Stage 4 is reorganising the user-facing documentation around distinct reader needs without changing the operating or authority model.

## Choose your path

### Learn IssueOps

Use [Tutorials](tutorials/index.md) when you want a controlled learning experience with expected outcomes at each step.

The full first-change tutorial is the next approved Stage 4 slice. Until it is published, the Tutorials page directs you to the current protocol and documentation-only example without presenting them as a completed tutorial.

### Complete a task

Use [How-to guides](how-to/index.md) when you need to perform a specific activity such as following the delivery loop, operating safely, validating a change, preparing review evidence or remediating feedback.

### Check an exact rule

Use [Reference](reference/index.md) for required contract fields, lifecycle rules, evidence formats, labels, validation requirements, checklists and schema definitions.

### Understand the model

Use [Explanation](explanation/index.md) for the IssueOps thesis, authority boundaries, delegated delivery, documentation architecture and the distinction between canonical guidance and project memory.

## The manual loop

```text
Issue = execution contract
Readiness check = contract check
Implementation plan = proposed execution path
Tool-operation check = safe actuation gate
Agent = contract-bound implementer
Validation check = evidence hygiene
Pull request = evidence pack
Human review = contract verification
Merge = human approval decision
```

The complete current lifecycle remains in the [IssueOps operating protocol](issueops-protocol.md). Stage 4 will progressively separate its detailed procedures, exact formats and explanation into focused pages while preserving the protocol as the authoritative lifecycle map.

## Project direction and history

Project records remain outside the substantive Tutorials, How-to, Reference and Explanation tree. They are still available when you need intent, delivery evidence or historical context:

- [Approved Stage 4 roadmap](https://github.com/8ft0-ai/IssueOps/blob/main/planning/roadmap/stage-04-diataxis-documentation-architecture.md)
- [Planning control surface](https://github.com/8ft0-ai/IssueOps/tree/main/planning)
- [Public roadmap compatibility page](roadmap.md)
- [Stage 1 release notes](releases/stage-1.md)
- [Stage 2 stable release notes](releases/stage-2.md)
- [Stage 3 experimental alpha notes](releases/stage-3-alpha.md)

The [documentation architecture](explanation/documentation-architecture.md) explains why project records are linked rather than treated as a fifth documentation mode.

## Current baseline

The recommended stable baseline is [Stage 2 — Published and Hardened IssueOps Operating Model](releases/stage-2.md), released as `v0.2.0`.

[Stage 3 Alpha — Read-only Evidence-pack Assistance](releases/stage-3-alpha.md), proposed as `v0.3.0-alpha.1`, is an experimental prerelease snapshot for controlled evaluation. It does not replace the stable baseline, establish routine operational adoption or expand human-controlled approval or merge authority.

Stage 4 changes documentation architecture only. It does not authorise automatic execution, lifecycle transitions, review decisions, merge authority, repository-setting changes or operational evidence-assistance implementation.
