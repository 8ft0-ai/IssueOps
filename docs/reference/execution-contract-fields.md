# Execution-contract fields

An execution contract is a GitHub issue that contains enough durable, reviewable intent for an agent or contributor to implement safely and for a human to verify the result.

This page is the canonical reference for the issue fields used by IssueOps.

## Core fields

Every execution contract should contain these fields.

| Field | Required content | Review question |
| --- | --- | --- |
| **Problem** | Why the change is needed and what current condition is unsatisfactory. | Is there a real, bounded problem rather than only a proposed solution? |
| **Expected outcome** | The observable state that should exist after the work is complete. | Can a reviewer recognise success? |
| **Scope** | Files, behaviours or areas the implementation may change. | Is the permitted change boundary explicit? |
| **Non-goals** | Work the contributor must not infer, add or redesign. | Are tempting adjacent changes excluded? |
| **Acceptance criteria** | Specific conditions used to judge completion. | Can each criterion be verified from the repository and evidence pack? |
| **Validation evidence expected** | Checks, observations and artefacts the pull request should provide. | Does validation match the changed behaviour and risk? |
| **Change risk** | The likely consequence of error and the scrutiny required. | Is the stated risk consistent with the scope? |
| **Agent instructions** | Repository-specific constraints, sequencing or implementation guidance. | Can an agent act without inventing product intent, policy or architecture? |

A field may be concise. It must still be explicit enough that implementation does not depend on private chat history, memory or unrecorded assumptions.

## Conditional fields

Add these fields when they materially govern the work.

| Field | Use when | Required content |
| --- | --- | --- |
| **Dependencies** | The issue depends on a prior issue, pull request, release, repository setting or environment state. | Required prior work, required state and the ordering constraint. |
| **Relationship to a roadmap or parent** | The issue is a delivery slice within an approved stage or initiative. | The governing roadmap or parent issue and how this slice contributes to it. |
| **Authority boundary** | Delegated delivery, production access, repository settings or other permissions could be misunderstood. | What is authorised and what remains human-controlled or separately governed. |
| **Post-merge verification** | Some evidence can exist only after merge, deployment or environment configuration. | The exact follow-up, owner and reason it cannot run before merge. |

Conditional fields clarify the contract; they do not create new authority. A roadmap relationship does not permit work outside the child issue, and delegated delivery does not remove validation or review gates.

## Quality tests

An execution contract is ready for a formal readiness check when:

- the expected outcome is unambiguous;
- scope and non-goals bound the change;
- acceptance criteria are observable;
- expected validation matches the change type;
- dependencies and safe ordering can be checked;
- risk is stated honestly;
- the contributor can proceed without inventing material intent; and
- the work is small enough to review safely.

The issue is not ready when the contributor would need to choose product direction, make an unapproved architecture decision, assume a dependency state or hide an unvalidated requirement inside the pull request.

## Minimal skeleton

```md
## Problem

...

## Expected outcome

...

## Scope

- ...

## Non-goals

- ...

## Acceptance criteria

- [ ] ...

## Validation evidence expected

- ...

## Change risk

...

## Agent instructions

...
```

Add conditional fields below this skeleton when ordering, roadmap authority or post-merge evidence matters.

## Related guidance

- [Write an executable issue contract](../how-to/write-executable-issue.md)
- [Check readiness and dependencies](../how-to/check-readiness-and-dependencies.md)
- [Readiness and dependency formats](readiness-and-dependency-formats.md)
- [Implementation-plan format](implementation-plan-format.md)
- [Why the issue is the execution contract](../explanation/execution-contract-model.md)
