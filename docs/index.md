# IssueOps

**Jira for human planning. GitHub Issues for agent execution. Pull requests for proof.**

IssueOps is an experiment in making agentic coding safer and easier to review by turning the GitHub issue into an execution contract. The issue defines the work. The branch contains the implementation. The pull request carries the evidence pack that a human verifies before deciding whether to merge.

The repository starts deliberately small. Stage 1 established the manual workflow, Stage 2 hardened it into the current recommended operating protocol, and Stage 3 tested read-only evidence-pack assistance as an experimental alpha capability. Stage 4 is reorganising the user-facing documentation around distinct reader needs without changing the operating or authority model.

## Choose your path

### Learn IssueOps

Start with [Complete your first small IssueOps change](tutorials/first-issueops-change.md). It guides one documentation-only exercise from an executable issue through human-controlled merge and post-merge verification, with a visible expected outcome at every major step.

Use the [Tutorials](tutorials/index.md) landing page for the learning-path boundary and next steps.

### Complete a task

Use [How-to guides](how-to/index.md) when you need to perform a specific activity such as writing a contract, checking readiness, operating safely, validating a change, preparing review evidence or remediating feedback.

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

The complete current lifecycle remains in the [IssueOps operating protocol](issueops-protocol.md). Stage 4 will progressively reduce it to an authoritative lifecycle map after focused procedures and exact formats are established.

## Project direction and history

Project records are not a fifth Diátaxis documentation mode. Their canonical repository homes are:

- [Planning control surface](https://github.com/8ft0-ai/IssueOps/blob/main/planning/README.md)
- [Roadmap index](https://github.com/8ft0-ai/IssueOps/blob/main/planning/roadmap/index.md)
- [Delivery records](https://github.com/8ft0-ai/IssueOps/blob/main/planning/delivery/index.md)
- [Historical evidence and compatibility decisions](https://github.com/8ft0-ai/IssueOps/blob/main/planning/evidence/index.md)

Existing public project-record URLs remain concise compatibility surfaces. The [documentation architecture](explanation/documentation-architecture.md) explains why these records are linked rather than duplicated into Tutorials, How-to, Reference or Explanation.

## Current baseline

The recommended stable baseline is [Stage 2 — Published and Hardened IssueOps Operating Model](releases/stage-2.md), `v0.2.0`.

[Stage 3 Alpha — Read-only Evidence-pack Assistance](releases/stage-3-alpha.md), proposed as `v0.3.0-alpha.1`, is an experimental snapshot for controlled evaluation. It does not replace the stable baseline, establish routine operational adoption or expand human-controlled approval or merge authority.

Stage 4 changes documentation architecture only. It does not authorise automatic execution, lifecycle transitions, review decisions, merge authority, repository-setting changes or operational evidence-assistance implementation.