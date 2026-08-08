# Session grants, roles and handovers

This page is the canonical Reference for the Version 0.1 bounded-session transition contract.

It defines the facts that may invoke one session, the responsibility boundary for that session, the minimum durable handover fields and the receiving-session verification rules. It does not replace the [IssueOps operating protocol](../issueops-protocol.md), the repository's current instructions, the governing issue or planning record, or current GitHub state.

A session grant and a handover are claims and navigation aids. They do not prove current repository state and do not create authority beyond the cited governing record.

## Source of truth and authority

Before relying on a grant or handover:

- fetch and confirm the exact repository identity;
- read the current repository instructions and the named primary record;
- treat current issues, comments, branches, commits, pull requests, checks, reviews and planning records as authoritative for their respective facts; and
- stop accurately when the required authority or evidence cannot be established.

The named issue, pull request or approved planning record remains the primary authority owner. Current repository instructions and GitHub-native records override stale summaries.

Repository access does not imply permission to mutate, approval authority, independent-review status or merge authority. A role label also does not provide any of those authorities.

## Session-grant fields

A session grant supplies the minimum invocation facts needed to investigate the correct repository state. The expected starting state is deliberately unverified until reconciliation.

### Required fields

| Field | Required content |
| --- | --- |
| **Repository identity** | The exact `owner/repository` to fetch and confirm. |
| **Primary record** | The governing issue, pull request or approved planning record. |
| **Bounded authority** | The reads, comments, mutations or decisions explicitly permitted by the primary record and human authority. |
| **Expected starting state** | The branch, commit, pull-request head, lifecycle gate or explicit unknown that the session is expected to find. |
| **Session role** | Exactly one of Shape, Deliver, Review or evaluate, or Close and reconcile. |
| **Stop boundary** | The decision, completed action or condition that ends the session. |

### Conditional fields

Include these fields when they materially affect the session:

| Field | Use when |
| --- | --- |
| **Pinned external source** | A reproducible bootstrap, protocol or other external source must be used. |
| **Expected branch, pull request or head** | Correct continuation depends on an exact ref, pull request or commit. |
| **Dependencies or open findings** | Another record, review finding, release or environment state controls the next action. |
| **Execution-deviation records** | A deviation may affect authority, scope, validation, review, approval or current state. |
| **Required human decision** | Owner clarification, approval, merge or another explicit decision remains outstanding. |
| **Outstanding post-merge or environment-specific evidence** | A required check cannot be completed in the current pre-merge environment. |

Omitting an applicable conditional field does not remove the underlying dependency or authority boundary. The receiving session must still discover it from current repository state.

## Role invariants

A role constrains responsibility. It never grants authority by itself. Moving to another role requires a fresh explicit grant.

| Role | Primary responsibility | Prohibitions |
| --- | --- | --- |
| **Shape** | Analyse the problem, inspect evidence, compare options and prepare bounded decisions or recommendations. | Do not implement repository changes, create unapproved execution work or represent a proposal as approved authority. |
| **Deliver** | Implement one ready execution contract and prepare current validation and pull-request evidence. | Do not invent missing intent, absorb adjacent work, approve the implementation or infer merge authority. |
| **Review or evaluate** | Independently assess current durable evidence against the governing contract or proof question and record one supported conclusion. | Do not remediate findings in the same independent role or represent same-role self-review as independent evidence. After recording the final supported conclusion, the Review or evaluate session terminates for merge purposes; later human approval does not reopen that model context, and the same model conversation/context must not invoke merge. |
| **Close and reconcile** | Verify completed outcomes, compare intended and actual delivery, reconcile authorised planning or close-out state and identify the next decision boundary. | Do not rewrite original intent, mark unavailable evidence complete or silently begin the next initiative. |

Every role remains subordinate to the [canonical lifecycle and authority boundary](../issueops-protocol.md).

## Durable-handover fields

Use a durable handover only when another session has a genuine continuation need. Real handovers remain GitHub issue or pull-request comments by default.

An exceptional repository-file handover location remains unresolved. This contract does not establish a file convention. Any such convention requires separate evidence, review and authority.

A handover must contain:

| Field | Required content |
| --- | --- |
| **Handover identity** | A durable comment reference or other immutable handover identity. |
| **Outgoing role** | The role performed by the outgoing session. |
| **Primary record** | The governing issue, pull request or planning record. |
| **Stable state observed** | The stable branch and exact commit observed. |
| **Active branch or pull-request head** | The exact active ref and commit, or `none`. |
| **Completed claims** | Action-relevant completed work with durable links to canonical evidence. |
| **First incomplete gate and work** | The earliest incomplete authorised lifecycle gate and the remaining work. |
| **Validation state** | Passed, failing, pending local validation, pending environment-specific validation, post-merge, not performed or unavailable, tied to the relevant head. |
| **Open findings or dependencies** | Durable links and current status for action-relevant findings or dependencies. |
| **Execution deviations** | Durable deviation records and their known containment or resumption state, or `none`. |
| **Next permitted action** | One bounded action supported by the observed state and authority. |
| **Required authority or human decision** | The exact owner, reviewer, approval, merge or clarification decision still required. |
| **Known stale-risk** | Any branch, head, check, review, dependency or approval that must be refreshed. |

A handover links canonical owners; it does not reproduce the complete issue, pull-request evidence pack or lifecycle. Do not create a handover merely to restate already-complete work.

## Claim statuses

The receiving session classifies each action-relevant grant or handover claim separately.

| Status | Meaning |
| --- | --- |
| **Confirmed** | Current canonical evidence supports the claim. |
| **Stale** | The claim may have been true when recorded, but current state has moved. |
| **Contradicted** | Current canonical evidence conflicts with the claim. |
| **Unsupported** | No sufficient canonical evidence was found. |

Split compound statements into independently verifiable claims. A partly correct statement must not hide a stale, contradicted or unsupported component.

Status is evaluated against current canonical evidence, not frozen at first receipt. A previously **Confirmed** action-relevant observation becomes **Stale** when later state supersedes it. Use **Contradicted** when current canonical evidence conflicts with the claim rather than merely showing normal subsequent state movement, and **Unsupported** when sufficient canonical evidence cannot be established. Do not silently replace a stale observation with a newer fact without recording the status transition.

## Receiving-session verification

Before action, the receiving session must:

1. fetch current repository instructions and the primary record;
2. fetch action-relevant branches, commits, pull requests, checks, reviews, threads, dependencies and execution deviations;
3. compare every action-relevant grant and handover claim with current canonical evidence;
4. revisit previously recorded action-relevant observations whenever current state has moved and explicitly record any transition, including **Confirmed** to **Stale**, before selecting the next action;
5. classify each current mismatch as stale, contradicted or unsupported rather than repairing it from private chat history;
6. identify the earliest incomplete authorised lifecycle gate;
7. check for duplicate or conflicting issues, branches and pull requests;
8. record the reconciliation outcome durably on the relevant issue or pull request; and
9. continue only within the new session grant, verified repository state and explicit authority.

A mismatch may permit narrower continuation, but only when the governing record and current evidence support that action. Otherwise stop and state the missing evidence, decision or authority.

Receiving verification does not confer mutation, approval, independent-review or merge authority.

## Related canonical guidance

Use the focused owner for the next task rather than extending this transition contract:

- [Execution-contract fields](execution-contract-fields.md)
- [Readiness and dependency formats](readiness-and-dependency-formats.md)
- [Implementation-plan format](implementation-plan-format.md)
- [Operation permissions and evidence](operation-permissions-and-evidence.md)
- [Execution-deviation policy](execution-deviation-policy.md)
- [Validation status and fallback policy](validation-status-and-fallback-policy.md)
- [Pull-request evidence requirements](pr-evidence-requirements.md)
- [Review decisions and merge blockers](review-decisions-and-merge-blockers.md)
