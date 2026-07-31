# Handle an execution deviation

Use this guide after an IssueOps operation changes the wrong repository object, causes an unplanned side effect or creates uncertainty about authority, scope or evidence.

For exact thresholds, severity definitions, evidence fields, stale-evidence rules and resumption gates, use the canonical [Execution-deviation policy](../reference/execution-deviation-policy.md).

## 1. Stop normal mutation

Do not continue the planned issue flow.

Pause file changes, branch or issue transitions, pull-request operations, approvals and merges. Continue only:

- read-only investigation needed to understand the event; and
- the minimum authorised remediation needed to make the unintended state safe.

Do not use the incident as authority to tidy unrelated state or expand the execution contract.

## 2. Identify the intended and actual operation

Record:

- the workflow phase;
- the intended operation;
- the exact tool or command selected;
- the intended target and expected side effect;
- the actual object or state changed; and
- forbidden side effects that occurred or may have occurred.

Fetch the affected repository objects rather than relying on the tool response alone.

## 3. Contain the event

Choose the smallest authorised recovery action.

Examples include:

- delete an unintended empty branch;
- close an accidental issue or pull request;
- revert an unauthorised file commit;
- restore the approved file set;
- return a pull request to draft;
- invalidate an approval tied to an earlier head; or
- stop a release or deployment when the repository's operating procedure permits it.

Do not attempt a recovery operation whose effects or authority are unclear. Escalate instead.

## 4. Verify safe state

After containment, fetch and inspect the state that matters to the active execution:

- stable branch and expected head;
- issue state and execution-contract validity;
- feature branches and commits;
- changed files and diff;
- pull-request state and head;
- checks, reviews, threads and approvals; and
- settings, permissions, release, deployment or publication state when relevant.

A successful delete, close or revert response is not enough. Confirm that the expected state now exists and that forbidden state does not remain.

## 5. Decide whether a formal record is required

Apply the [meaningful-deviation threshold](../reference/execution-deviation-policy.md#meaningful-deviation-threshold).

A failed command with no authoritative side effect, no effect on evidence or authority and no repeated pattern may not require a formal repository record.

When the threshold is met, record the event on the active execution issue. Also update the pull request or close-out evidence when review or delivery interpretation is affected.

## 6. Record the evidence

Use the canonical record fields:

```text
Execution deviation

What happened:
<observed event and intended operation>

Impact:
<authoritative state or evidence affected>

Containment:
<minimum remediation and safe-state verification>

Cause:
<known cause, contributing factors or explicitly unknown>

Classification:
<minor, material or critical, with rationale>

Stale evidence:
<validation, review, approval or other evidence invalidated or confirmed current>

Remaining risk:
<none, bounded or unresolved>

Corrective control:
<control applied before resumption or escalation>

Resumption decision:
<resumed under the minor gate, awaiting owner direction or stopped>
```

Keep observed facts separate from inferred cause.

## 7. Classify severity

Use the normative [severity table](../reference/execution-deviation-policy.md#severity).

Consider:

- whether authoritative state changed;
- whether recovery is complete and confidently verified;
- whether authority or scope remains valid;
- whether validation, review or approval became stale;
- whether security, settings, permissions, merge or production state was involved; and
- whether recurrence shows that the current corrective control is ineffective.

When uncertain, use the higher plausible severity until the uncertainty is resolved.

## 8. Revalidate affected evidence

Use the [stale-evidence rules](../reference/execution-deviation-policy.md#stale-evidence-rules) to identify what must be refreshed.

Typical actions include:

- refresh readiness when the safe starting point changed;
- revise the implementation plan when recovery changes the approach;
- rerun tests or documentation builds after content restoration;
- reinspect review findings after remediation changes;
- refresh the pull-request evidence pack; and
- obtain new approval or exact-head authorisation after a head change.

Do not rerun unrelated validation merely to create activity. Rerun the evidence affected by the event and the recovery.

## 9. Apply a corrective control

Choose a practical control that changes the failing path before another mutation.

Examples:

- restrict the next permitted operation to one named tool and target;
- fetch and copy the exact issue, branch or head identifier immediately before the call;
- require a second operator or different environment after recurrence;
- separate recovery completion from resumption; or
- restart with a revised plan or execution contract.

Repeating the same operation with only a verbal promise to be careful is not sufficient after a repeated selection failure.

## 10. Resume or escalate

### Minor deviation

Resume only when every condition in the [minor-deviation resumption gate](../reference/execution-deviation-policy.md#minor-deviation-resumption-gate) is satisfied and the decision is recorded.

### Material or critical deviation

Do not resume normal mutation until explicit repository-owner direction records the accepted recovery state, residual risk, required revalidation and exact next permitted operation.

### Uncertain state

Treat uncertainty about state, authority, scope or evidence as a blocker. Do not classify an event as minor merely because the visible mutation appears small.

## 11. Decide whether follow-up work is warranted

Use the [follow-up issue criteria](../reference/execution-deviation-policy.md#follow-up-issue-criteria).

Create separate work only for an unresolved systemic problem, such as a missing control, recurring failure, tooling defect, unrecovered impact, security exposure or reusable cross-repository lesson.

Do not create a bug in the delivery repository when the repository behaved correctly and the failure was execution non-compliance.

## 12. Reflect the event in final review

Before approval, confirm that:

- containment and safe-state verification are complete;
- the severity and remaining risk are supported by evidence;
- affected validation, review and approval are current;
- the pull-request evidence pack discloses the event accurately;
- the final implementation still satisfies the issue; and
- the change still contains only the authorised scope.

An unresolved or inaccurately represented deviation blocks approval. A fully contained minor deviation may proceed when the final evidence remains trustworthy.

## Common failure modes

- continuing normal work because the accidental object was quickly removed;
- treating a successful remediation response as proof of safe state;
- classifying by the initiating command rather than observed impact;
- preserving approval after the head changed;
- creating a backlog issue for every harmless failed command;
- blaming the repository for an incorrect tool selection; or
- repeating the same failing execution path without a stronger control.