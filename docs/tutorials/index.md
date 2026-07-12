# Tutorials

Tutorials help a first-time contributor learn IssueOps by completing a controlled experience. They minimise choices, explain what should be visible after each step and link to reference material instead of trying to define every rule.

## Start here

[Complete your first small IssueOps change](first-issueops-change.md) guides one documentation-only exercise through:

```text
execution contract
  -> readiness and dependency check
  -> implementation plan
  -> feature branch
  -> bounded edit
  -> validation
  -> pull-request evidence
  -> human contract verification
  -> merge and post-merge verification
```

The tutorial uses a personal fork or authorised training repository so the full loop can be completed without adding exercise artefacts to the canonical project. It states the expected outcome at every major step and stops safely when permissions or validation are unavailable.

It teaches only capabilities already implemented in IssueOps. It does not introduce automatic execution, automatic review or automatic merge authority.

## After the tutorial

Repeat the planning tasks independently with:

- [Write an executable issue contract](../how-to/write-executable-issue.md);
- [Check readiness and dependencies](../how-to/check-readiness-and-dependencies.md); and
- [Prepare an implementation plan](../how-to/prepare-implementation-plan.md).

Repeat implementation and validation tasks with:

- [Perform a safe repository mutation](../how-to/perform-safe-repository-mutation.md);
- [Validate a documentation change](../how-to/validate-documentation-change.md); and
- [Validate a workflow change](../how-to/validate-workflow-change.md).

Repeat the pull-request tasks with:

- [Prepare a pull-request evidence pack](../how-to/prepare-pr-evidence-pack.md);
- [Review a pull request against its contract](../how-to/review-pr-against-contract.md); and
- [Remediate pull-request review feedback](../how-to/remediate-review-feedback.md).

Use [Reference](../reference/index.md) for exact fields, operation permissions, validation rules, evidence requirements, templates, decisions and blockers, and [Explanation](../explanation/index.md) for the reasoning behind the controls.
