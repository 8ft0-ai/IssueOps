# Example execution contract

This example shows the expected shape of a small issue contract for agent-assisted work.

It is intentionally documentation-only so the contract is easy to inspect. Real issues should use the same structure but replace the example content with the actual change request.

This page is illustrative. The canonical field definitions and conditional requirements are in [Execution-contract fields](../reference/execution-contract-fields.md).

## Problem

The repository has an agent operating guide, but new contributors may not immediately understand how to use the guide when preparing an agent task.

We need a short documentation addition that explains how to decide whether an issue is ready for implementation.

## Expected outcome

A contributor can read the documentation and understand the minimum information required before an agent should start implementation.

## Scope

- Add a short section to the agent operating guide explaining readiness.
- Mention that an agent should not infer missing product intent.
- Link back to the execution-contract workflow.

## Non-goals

- Do not add automation.
- Do not change the issue form.
- Do not change the pull request template.
- Do not create or enforce labels.
- Do not introduce application code.

## Acceptance criteria

- The new section explains what makes an issue ready for implementation.
- The section reinforces the execution-contract model.
- The change is documentation-only.
- The pull request records validation evidence and any caveats.

## Validation evidence expected

The pull request should confirm:

- the changed Markdown file was read back from the branch;
- links were reviewed manually; and
- no automation or application code was added.

## Change risk

Low.

This is a small documentation-only change.

## Agent instructions

Keep the change narrow. Do not redesign the workflow. Do not introduce future-stage concepts. If the existing documentation already covers the point clearly, say so in the pull request instead of duplicating content.

## How to use the example

- Compare its fields with the [canonical field reference](../reference/execution-contract-fields.md).
- Use [Write an executable issue contract](../how-to/write-executable-issue.md) for the task procedure.
- Run the [readiness and dependency check](../how-to/check-readiness-and-dependencies.md) before planning a branch.
