# Start or resume a bounded session

Use this guide to establish the verified starting gate for one new or resumed IssueOps session, identify one permitted next action and record the reconciliation outcome.

For the exact grant fields, role invariants, handover fields and claim statuses, use [Session grants, roles and handovers](../reference/session-grants-roles-and-handovers.md). This guide is not a copy-ready session launcher, role-specific prompt pack or replacement for the [IssueOps operating protocol](../issueops-protocol.md).

## 1. Read the session grant

Identify:

- the exact repository;
- the session role;
- the primary record;
- the bounded authority;
- the expected starting state; and
- the stop boundary.

Identify any applicable pinned source, expected branch or head, dependency, open finding, deviation, human decision or outstanding evidence.

If a material field or authority boundary is missing, stop and request a durable clarification. Do not infer authority from repository access or the role name.

## 2. Fetch current repository instructions and lifecycle rules

Read the repository's current agent and contributor instructions before acting.

Use the [IssueOps operating protocol](../issueops-protocol.md) as the lifecycle and mandatory-gate map. When external adoption is in scope, open the exact pinned `BOOTSTRAP.md` source named by the grant; the current [bootstrap entry point](https://github.com/8ft0-ai/IssueOps/blob/main/BOOTSTRAP.md) explains how to record a reproducible source. Do not substitute a copied summary for the current owners.

## 3. Fetch the primary record and relevant state

Read the primary issue, pull request or planning record and every later action-relevant comment.

Fetch the GitHub-native state that can affect the next action, including:

- stable branch and current commit;
- active branches and commits;
- pull requests and exact heads;
- checks and validation evidence;
- submitted reviews, conversation comments and inline threads;
- dependencies and human decisions; and
- execution-deviation records.

Keep the inspection proportionate to the role and primary record, but do not omit state that could invalidate authority, scope, validation, review or the stop boundary.

## 4. Verify the handover when resuming

For a resumed session, fetch the durable issue or pull-request handover.

Split compound statements into separate action-relevant claims. Verify the observed stable state, active branch or pull-request head, completed work, first incomplete gate, validation, findings, deviations, next action, required authority and known stale-risk.

Do not use private chat history to repair missing or conflicting evidence.

## 5. Reconcile expected state with current state

Classify each action-relevant grant or handover claim:

- **confirmed** when current canonical evidence supports it;
- **stale** when it may have been true but state has moved;
- **contradicted** when current evidence conflicts with it; or
- **unsupported** when sufficient canonical evidence cannot be found.

A mismatch is a result to record. Do not silently normalise it or continue from the most convenient interpretation.

## 6. Identify the earliest incomplete authorised gate

Use the canonical lifecycle and current evidence to find the first gate that is both incomplete and authorised for this role.

Do not skip an incomplete readiness, planning, validation, review, remediation, approval or post-merge requirement because a later artefact already exists. If the requested action belongs to another role or lacks authority, the correct result is a stop.

## 7. Check for duplicate or conflicting work

Before creating any issue, branch or pull request, search for an existing object that already represents the work.

- Resume or review a valid existing object rather than creating a duplicate.
- If an active branch or pull request conflicts with the primary record, stop mutation until the authoritative continuation path is clear.
- Treat a stale expected ref as evidence to reconcile, not permission to create a replacement automatically.

## 8. Select one next permitted action

Choose one bounded action supported by:

- the verified primary record;
- current repository state;
- the session role;
- explicit authority; and
- the identified lifecycle gate.

When no such action exists, identify the missing evidence, decision or authority and stop.

## 9. Record the reconciliation outcome

Post a durable comment on the relevant issue or pull request that records:

- the grant and handover references inspected;
- the stable state and active head observed;
- material confirmed, stale, contradicted and unsupported claims;
- duplicate or conflict checks;
- the earliest incomplete authorised gate;
- the one next permitted action, or the reason for stopping; and
- any authority, validation or human decision still required.

The comment records the receiver's verified conclusion. It does not replace the underlying issue, branch, pull request, checks or reviews.

## 10. Proceed or stop accurately

Proceed only with the selected action and only until the session's stop boundary.

Stop when:

- the primary authority is missing, superseded or contradictory;
- current state cannot be established;
- required validation or evidence is failing or unavailable beyond the permitted fallback;
- duplicate or conflicting work makes the continuation path ambiguous;
- the next action belongs to another role;
- a human decision is required; or
- the session has reached its stated boundary.

## Continue with the focused procedure

After reconciliation, use the existing task owner:

| Verified next gate | Continue with |
| --- | --- |
| Issue executability or dependency decision | [Check readiness and dependencies](check-readiness-and-dependencies.md) |
| Pre-branch execution plan | [Prepare an implementation plan](prepare-implementation-plan.md) |
| Repository mutation | [Perform a safe repository mutation](perform-safe-repository-mutation.md) |
| Execution deviation | [Handle an execution deviation](handle-execution-deviation.md) |
| Documentation validation | [Validate a documentation change](validate-documentation-change.md) |
| Pull-request evidence | [Prepare a pull-request evidence pack](prepare-pr-evidence-pack.md) |
| Independent pull-request review | [Review a pull request against its contract](review-pr-against-contract.md) |
| Review remediation | [Remediate pull-request review feedback](remediate-review-feedback.md) |
| Approval or merge decision | [IssueOps operating protocol](../issueops-protocol.md) and [Review decisions and merge blockers](../reference/review-decisions-and-merge-blockers.md) |
| Documentation post-merge verification | [Publish and verify the documentation site](publish-and-verify-documentation-site.md) |
| Validation fallback or post-merge status | [Validation status and fallback policy](../reference/validation-status-and-fallback-policy.md) |

This guide ends at reconciliation and routing. It does not duplicate those procedures or grant permission to perform them.
