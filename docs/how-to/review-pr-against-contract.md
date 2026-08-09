# Review a pull request against its contract

Use this guide to decide whether a pull request satisfies its execution-contract issue and is ready for approval.

For exact recommendation meanings and blockers, use [Review decisions and merge blockers](../reference/review-decisions-and-merge-blockers.md). For exact evidence-collection semantics, use [Pull-request evidence requirements](../reference/pr-evidence-requirements.md).

## 1. Read the authorising issue

Review the problem, expected outcome, scope, non-goals, acceptance criteria, validation expectations, risk and agent instructions. Include later clarifications, readiness evidence, the detailed implementation plan, the separate durable human approval of that plan, and any additional procedural authority required by the work.

Verify that required pre-implementation authority existed before the action it authorised. The human plan-approval record must clearly apply to the detailed plan and must predate branch creation or implementation mutation. A later record cannot be used to reconstruct missing authority retrospectively.

The PR is not reviewed as a standalone diff. The issue defines what the diff was allowed and expected to do.

## 2. Inspect the final repository change

Check:

- the final head SHA;
- changed files and complete diff;
- file contents and generated output;
- relevant tests, builds and workflow runs;
- PR conversation comments and submitted reviews;
- inline review threads; and
- repository policy or required checks.

Confirm that the pull request declares the governing issue in the canonical execution-contract form, records the required lifecycle-authority evidence, and that its evidence description represents the decision-relevant state.

## 3. Request evidence deliberately when authorised

When the current review/session grant explicitly permits evidence collection for this pull request, post exactly this PR comment:

```text
/collect-evidence
```

Do not request collection merely because the actor has repository write access or collaborator status. IssueOps procedural authority to request collection is separate from the repository workflow's GitHub platform-eligibility checks.

Use [Pull-request evidence requirements](../reference/pr-evidence-requirements.md#deliberate-evidence-collection) for the exact command, eligibility, request-identity, correlation, artifact and failure rules.

Collection is optional evidence assistance inside an authorised review flow. It is not the review decision and it does not advance the lifecycle automatically.

## 4. Correlate the collection result

For a comment-triggered request, reconstruct the repository-native chain:

```text
request comment ID
  -> workflow run ID
  -> run attempt / terminal conclusion
  -> run summary / evidence artifact
```

Treat a pending run as pending evidence, not as a successful result. Confirm that the correlated pack belongs to the pull request and exact decision-relevant head you are reviewing.

If the head, material validation state or material review state changes after collection, the earlier pack is a prior snapshot. When collection remains authorised and the changed state matters to the decision, deliberately request and correlate a new snapshot rather than silently treating the old one as current.

## 5. Verify evidence quality

Separate repository-observed facts from contributor assertions. Check that:

- required lifecycle-authority records are present, durable and temporally valid;
- completed validation actually ran;
- workflow evidence belongs to the final relevant head;
- unavailable validation is explicit;
- post-merge checks genuinely cannot run before merge;
- material remediation is reflected in the evidence pack; and
- no failing or contradictory evidence is omitted.

Interpret submitted review states and inline review-thread resolution as separate evidence surfaces. An `APPROVED` review, review count or absence of requested changes does not prove that inline review threads are resolved.

Treat stale, pending, unavailable, conflicting, retrieval-error or otherwise incomplete evidence as fail-closed mechanical evidence. Do not fill gaps by inference or convert an incomplete collection into a `complete` claim.

Evidence completeness is necessary input to review when the evidence surface is relied upon, but it is not the approval decision.

## 6. Verify contract satisfaction

Ask:

1. Did the PR deliver the expected outcome?
2. Did it satisfy each acceptance criterion?
3. Did it remain inside scope?
4. Did it respect every material non-goal?
5. Did validation match the changed behaviour and risk?
6. Does any correctness uncertainty remain?

When the result is useful but outside the issue, record a follow-up rather than approving scope drift.

## 7. Review authority and safety boundaries

Confirm that:

- the readiness, implementation plan and separate human plan approval form a durable pre-implementation authority chain;
- any additional procedural authority used by the work is recorded, or `N/A` is explicit where none was required; and
- the PR does not silently change human approval or merge authority, permissions or credentials, branch protection or required checks, lifecycle automation, production or publication behaviour, or stable versus experimental capability claims.

Missing or retrospective required pre-action authority is a material lifecycle defect. Do not treat technical correctness or passing validation as a substitute for that authority.

Any authorised change to authority-sensitive areas must be explicit in the issue and supported by matching validation.

The collector supplies bounded read-only evidence. It does not decide readiness, remediation, validation sufficiency, approval, merge, publication or deployment.

## 8. Classify findings

Classify each finding as:

- required fix;
- optional improvement;
- clarification needed; or
- out of scope.

Explain why a required fix blocks approval. Do not ask for optional or out-of-scope work as though it were a contract failure.

A missing required pre-implementation human authority record is not repaired by adding a later comment to the historical record. Classify the lifecycle defect honestly and route any follow-up through a separately authorised path rather than rewriting history.

## 9. Choose the recommendation and stop the review session

Use:

- `Approve` only when the contract is satisfied, required lifecycle authority is present and valid, and no review or pre-merge validation blocker remains;
- `Approve after minor fixes` when identified small changes must be completed and rechecked; or
- `Do not approve yet` when correctness, scope, lifecycle authority, validation, evidence or review state remains unresolved.

An agent-generated groundedness review may help orient the reviewer, but it is not independent human review and does not decide approval.

After the independent Review or evaluate session records its final recommendation durably, that reviewer model context is finished for merge purposes. Its next boundary is the human decision or another separately authorised role/session. Later human approval does not reopen or extend the independent-review session, and the same model conversation/context that performed the review must not invoke merge.

If remediation is required, perform it in a separate Deliver session and obtain any required fresh re-review before returning to the human decision boundary.

## 10. Confirm merge eligibility in a separate execution context

Implementation-plan approval is not merge authority. Even an approved implementation merges only when:

- repository policy is satisfied;
- required reviews and checks are complete;
- a durable GitHub-native human merge-authority record exists for the exact pull request, accepted head SHA and current accepted review state;
- the current head and material review state still match that authority immediately before merge; and
- any delegated-batch conditions are met.

If the current head or material review state has moved since the human decision, treat that authority as stale for merge purposes. Stop and obtain a fresh human decision tied to the new exact state before invoking merge.

The owner may merge directly or may authorise a separate non-review execution context to invoke merge. Do not route merge back through the completed independent-review session, and do not bypass branch protection or permissions.

## 11. Record post-merge verification

When legitimate post-merge verification remains, state:

- what must be checked;
- why it cannot run earlier;
- who will record it; and
- what happens if it fails.

After merge, verify the merged repository state rather than assuming the successful merge proves the deployment or published result.

## Common failure modes

- reviewing only the diff without reading the issue;
- treating the implementation plan as self-authorising;
- approving an implementation whose required human plan approval is missing or retrospective;
- requesting collection without IssueOps procedural authority;
- treating a pending collection run as successful evidence;
- relying on a collected pack after the decision-relevant head or material review state has changed;
- treating a submitted review as proof that inline review threads are resolved;
- treating a passing workflow as proof of contract satisfaction;
- approving stale evidence after remediation;
- allowing post-merge verification to replace available pre-merge validation;
- conflating an agent self-review with independent approval;
- continuing the independent reviewer model context into merge after later human approval; or
- invoking merge without durable exact-state human authority and an immediate current-state recheck.
