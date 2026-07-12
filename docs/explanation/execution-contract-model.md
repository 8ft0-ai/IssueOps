# Why the issue is the execution contract

Agent-assisted implementation changes the cost of ambiguity. A human developer may notice missing context, pause and ask questions before changing the repository. An agent can produce a plausible implementation quickly, which means vague intent may become a polished but incorrect pull request before the gap is obvious.

IssueOps uses the GitHub issue as the execution contract because it is durable, visible beside the code and reviewable before implementation begins.

## The contract connects intent to evidence

The issue defines:

- the problem and expected outcome;
- the permitted and forbidden change boundary;
- the conditions used to judge completion;
- the evidence expected from validation; and
- the risk and implementation constraints.

The branch then contains one issue’s implementation, and the pull request can be checked against the same public contract. That creates a traceable line from intent to change to evidence to the human merge decision.

The issue is not a legal contract and it does not guarantee that the implementation is correct. “Contract” describes its operating role: it bounds execution and gives review a stable comparison point.

## Why a normal ticket is often insufficient

A conventional task may be adequate for a human team that shares product context, architecture knowledge and recent conversation. The same task may be unsafe for an agent when it says only:

> Update the docs for the new workflow.

The missing questions are material:

- Which workflow and which claims are current?
- Which pages may change?
- What must not change?
- Which evidence proves the result?
- Is the workflow stable, experimental or only proposed?
- Who retains approval and merge authority?

An execution contract makes those boundaries inspectable before the agent acts.

## Planning issues and execution contracts

Not every worthwhile idea is ready for implementation.

A **planning issue** exists to shape a decision. It may compare options, define an outcome to prove, resolve sequencing or decide to approve, adapt, defer or reject an initiative. Its output is a decision, roadmap or set of bounded execution issues.

An **execution-contract issue** exists to deliver one approved, reviewable repository change. It has explicit scope, non-goals, acceptance criteria, validation expectations and a safe dependency boundary.

The distinction prevents discussion from being mistaken for implementation authority. A planning issue may conclude that work should proceed, but a branch starts only from an execution contract after readiness, dependency and implementation-plan evidence are recorded.

## Relationship to Jira

Jira can remain the place for portfolio planning, prioritisation, cross-team coordination and broader product context.

The GitHub issue performs a narrower job close to the repository: it translates approved intent into one bounded change that an agent can execute and a reviewer can verify.

A useful flow is:

```text
Jira or planning issue
  -> reviewed decision and roadmap boundary
  -> GitHub execution-contract issue
  -> branch and implementation
  -> pull-request evidence pack
  -> human approval decision
```

The tools can differ. The important separation is between shaping intent and authorising bounded execution.

## Why readiness and planning are separate gates

A well-written issue can still be unsafe to start when a prerequisite has not merged or the base branch has changed.

Readiness tests whether the contract is executable now. The dependency check records the state that was actually observed. The implementation plan then proposes the path from that safe starting point.

Keeping the gates visible avoids two common failures:

- using a plan to invent missing issue intent; and
- creating a branch from an outdated or blocked state.

## Authority remains human

The issue authorises bounded implementation only to the extent stated by the repository owner and contract. It does not transfer approval or merge authority to the agent.

Evidence may show that checks passed and the diff matches the plan. A human still decides whether the contract is satisfied, whether residual risk is acceptable and whether the change should merge.

Delegated batch delivery can remove repeated confirmation between routine slices, but only after each issue and pull request passes its stated readiness, validation, review and merge gates.

## Canonical requirements

This explanation introduces no hidden mandatory field or decision rule.

Use:

- [Execution-contract fields](../reference/execution-contract-fields.md) for exact issue requirements;
- [Readiness and dependency formats](../reference/readiness-and-dependency-formats.md) for decision vocabulary and comment formats;
- [Implementation-plan format](../reference/implementation-plan-format.md) for the plan structure; and
- [Write an executable issue contract](../how-to/write-executable-issue.md) for the task procedure.
