# Review a pull request against its contract

Use this guide to decide whether a pull request satisfies its execution-contract issue and is ready for approval.

For exact recommendation meanings and blockers, use [Review decisions and merge blockers](../reference/review-decisions-and-merge-blockers.md).

## 1. Read the authorising issue

Review the problem, expected outcome, scope, non-goals, acceptance criteria, validation expectations, risk and agent instructions. Include later clarifications, readiness evidence and the implementation plan.

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

Confirm that the evidence pack describes this final state.

## 3. Verify evidence quality

Separate repository-observed facts from contributor assertions. Check that:

- completed validation actually ran;
- workflow evidence belongs to the final relevant head;
- unavailable validation is explicit;
- post-merge checks genuinely cannot run before merge;
- material remediation is reflected in the evidence pack; and
- no failing or contradictory evidence is omitted.

Evidence completeness is necessary, but it is not the approval decision.

## 4. Verify contract satisfaction

Ask:

1. Did the PR deliver the expected outcome?
2. Did it satisfy each acceptance criterion?
3. Did it remain inside scope?
4. Did it respect every material non-goal?
5. Did validation match the changed behaviour and risk?
6. Does any correctness uncertainty remain?

When the result is useful but outside the issue, record a follow-up rather than approving scope drift.

## 5. Review authority and safety boundaries

Confirm that the PR does not silently change:

- human approval or merge authority;
- permissions or credentials;
- branch protection or required checks;
- lifecycle automation;
- production or publication behaviour; or
- stable versus experimental capability claims.

Any authorised change to those areas must be explicit in the issue and supported by matching validation.

## 6. Classify findings

Classify each finding as:

- required fix;
- optional improvement;
- clarification needed; or
- out of scope.

Explain why a required fix blocks approval. Do not ask for optional or out-of-scope work as though it were a contract failure.

## 7. Choose the recommendation and stop the review session

Use:

- `Approve` only when the contract is satisfied and no review or pre-merge validation blocker remains;
- `Approve after minor fixes` when identified small changes must be completed and rechecked; or
- `Do not approve yet` when correctness, scope, validation, evidence or review state remains unresolved.

An agent-generated groundedness review may help orient the reviewer, but it is not independent human review and does not decide approval.

After the independent Review or evaluate session records its final recommendation durably, that reviewer model context is finished for merge purposes. Its next boundary is the human decision or another separately authorised role/session. Later human approval does not reopen or extend the independent-review session, and the same model conversation/context that performed the review must not invoke merge.

If remediation is required, perform it in a separate Deliver session and obtain any required fresh re-review before returning to the human decision boundary.

## 8. Confirm merge eligibility in a separate execution context

Even an approved implementation merges only when:

- repository policy is satisfied;
- required reviews and checks are complete;
- a durable GitHub-native human merge-authority record exists for the exact pull request, accepted head SHA and current accepted review state;
- the current head and material review state still match that authority immediately before merge; and
- any delegated-batch conditions are met.

If the current head or material review state has moved since the human decision, treat that authority as stale for merge purposes. Stop and obtain a fresh human decision tied to the new exact state before invoking merge.

The owner may merge directly or may authorise a separate non-review execution context to invoke merge. Do not route merge back through the completed independent-review session, and do not bypass branch protection or permissions.

## 9. Record post-merge verification

When legitimate post-merge verification remains, state:

- what must be checked;
- why it cannot run earlier;
- who will record it; and
- what happens if it fails.

After merge, verify the merged repository state rather than assuming the successful merge proves the deployment or published result.

## Common failure modes

- reviewing only the diff without reading the issue;
- treating a passing workflow as proof of contract satisfaction;
- approving stale evidence after remediation;
- allowing post-merge verification to replace available pre-merge validation;
- conflating an agent self-review with independent approval;
- continuing the independent reviewer model context into merge after later human approval; or
- invoking merge without durable exact-state human authority and an immediate current-state recheck.
