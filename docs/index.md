# IssueOps

**Jira for human planning. GitHub Issues for agent execution. Pull requests for proof.**

IssueOps is an experiment in making agentic coding safer and easier to review by turning the GitHub issue into an execution contract. The issue defines the work. The branch contains the implementation. The pull request carries the evidence pack that a human verifies before deciding whether to merge.

IssueOps has grown through five completed delivery stages. Stage 1 established the manual workflow, Stage 2 hardened it into a published operating protocol, Stage 3 tested read-only evidence-pack assistance as an experimental alpha capability and closed **Adapt**, Stage 4 adopted a Diátaxis-aligned documentation architecture, and Stage 5 adopted bounded human-triggered read-only evidence assistance for normal IssueOps review without changing human approval or merge authority.

Portable IssueOps bootstrap/adoption and modular-session guidance are also completed **Adopt** capabilities. They are cross-cutting operating capabilities rather than additional numbered delivery stages.

Current programme status is maintained in the [planning control surface](https://github.com/8ft0-ai/IssueOps/blob/main/planning/README.md) and [roadmap index](https://github.com/8ft0-ai/IssueOps/blob/main/planning/roadmap/index.md), rather than duplicated on this landing page.

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

The [IssueOps operating protocol](issueops-protocol.md) is the concise authoritative lifecycle and gate map. Focused How-to, Reference and Explanation pages own detailed procedures, exact formats and rationale.

## Project direction and history

Project records are not a fifth Diátaxis documentation mode. Their canonical repository homes are:

- [Planning control surface](https://github.com/8ft0-ai/IssueOps/blob/main/planning/README.md)
- [Roadmap index](https://github.com/8ft0-ai/IssueOps/blob/main/planning/roadmap/index.md)
- [Delivery records](https://github.com/8ft0-ai/IssueOps/blob/main/planning/delivery/index.md)
- [Historical evidence and compatibility decisions](https://github.com/8ft0-ai/IssueOps/blob/main/planning/evidence/index.md)

Existing public project-record URLs remain concise compatibility surfaces. The [documentation architecture](explanation/documentation-architecture.md) explains why these records are linked rather than duplicated into Tutorials, How-to, Reference or Explanation.

## Current baseline

The recommended stable baseline is [`v0.3.0`](releases/v0.3.0.md), a compatible successor to `v0.2.0`.

It carries forward the Stage 2 execution-contract foundation and reconciles the adopted Stage 4 documentation architecture, Stage 5 human-triggered read-only evidence assistance, portable bootstrap/adoption and modular-session guidance. The `/collect-evidence` bridge and repository-native PR-diff validation are bounded supporting mechanisms; the primary-record inspector and static workflow auditor remain optional/advisory aids.

[Stage 3 Alpha — Read-only Evidence-pack Assistance](releases/stage-3-alpha.md), `v0.3.0-alpha.1`, remains a historical experimental snapshot with an **Adapt** outcome. The stable `v0.3.0` recommendation reflects the later consolidated adopted model rather than reclassifying that alpha snapshot.

Human substantive review, approval and merge authority remain unchanged. The stable baseline does not authorise generic execution, lifecycle automation, required-check/ruleset changes, auto-merge, automated publication, or broader repository-setting or merge-authority expansion.