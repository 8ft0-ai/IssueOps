# Execution contracts

An execution contract is a GitHub issue written so that an agent can implement safely and a human can review meaningfully. It is narrower than a product brief and more explicit than a task ticket.

The contract should tell Codex what problem to solve, which boundaries to respect, how the result will be judged and what evidence the pull request must provide. It should not rely on hidden context, chat history or assumptions that only the issue author understands.

## Why the issue is the contract

Agentic coding changes the risk profile of vague work. A human developer can often notice missing context, pause and ask clarifying questions. A coding agent may produce a plausible implementation before the missing intent is obvious.

For this repository, the issue is treated as the execution contract because it is visible, durable and reviewable. It can be checked before implementation starts, referenced from the branch and verified from the pull request.

## Required contract shape

A good execution contract includes:

| Section | Purpose |
| --- | --- |
| Problem | Explains why the change is needed. |
| Expected outcome | Describes the state that should exist after the work is complete. |
| Scope | Defines what the agent may change. |
| Non-goals | Defines what the agent must not change or infer. |
| Acceptance criteria | Makes success reviewable. |
| Validation evidence expected | States what the pull request should prove. |
| Change risk | Helps the reviewer apply the right level of scrutiny. |
| Agent instructions | Gives specific implementation guidance and constraints. |

The issue does not need to be long, but it does need to be executable. If the agent would need to invent product intent, architecture decisions or repository policy, the contract is not ready.

## Readiness check

Before implementation starts, the issue should be checked for readiness. The check asks whether:

- the expected outcome is clear;
- the boundaries are explicit;
- the acceptance criteria can be reviewed;
- the validation evidence is clear;
- the work is small enough to review safely; and
- there is enough context for Codex to act without guessing.

If the answer is no, clarify the issue before creating a branch.

## Relationship to Jira

Jira can still hold the broader planning context. It can explain why the work matters, how it relates to other work, which initiative it supports and how people are coordinating around it.

The GitHub issue has a different job. It should translate that planning context into a bounded repository change that an agent can execute and a reviewer can verify.

## Example

See the [example execution contract](examples/execution-contract-example.md) for a small documentation-only contract that shows the expected structure.
