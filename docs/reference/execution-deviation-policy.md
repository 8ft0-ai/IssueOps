# Execution-deviation policy

This page is the canonical reference for identifying, recording, classifying and resolving IssueOps execution deviations. It owns the normative rules for stale evidence, resumption and escalation.

Use [Handle an execution deviation](../how-to/handle-execution-deviation.md) for the operating procedure and [Why execution deviations are evidence](../explanation/why-execution-deviations-are-evidence.md) for rationale.

## Core rule

When an operation changes the wrong repository object, causes an unplanned side effect or creates uncertainty about authority, scope, evidence or repository state:

1. stop normal mutation;
2. continue only the read-only investigation and minimum remediation needed to make the situation safe;
3. verify the resulting repository state;
4. record and classify the deviation when the threshold below is met;
5. invalidate or rerun affected evidence; and
6. resume only through the applicable resumption gate.

Restoring repository state does not erase the deviation and does not automatically restore evidence made stale by it.

## Meaningful-deviation threshold

A failed command or tool call that changes no authoritative state is not automatically a formal execution deviation.

Record a deviation when the event:

- changes or could reasonably have changed repository content or lifecycle state;
- crosses or creates uncertainty about an authority boundary;
- changes or creates uncertainty about approved scope;
- makes validation, review, approval or merge evidence potentially stale;
- affects repository integrity, security, permissions, settings or production state; or
- forms part of a repeated failure pattern whose recurrence changes the risk.

A harmless failed command may be mentioned in working notes without a formal deviation record when it has no repository side effect, does not affect evidence or authority and is not part of a repeated pattern.

## Authoritative state

Authoritative state includes, where relevant:

- issue, pull-request and review state;
- branches, commits, tags and files;
- approvals and exact-head authorisation;
- workflow runs and required checks;
- releases, deployments and published artefacts;
- repository settings, permissions and protection rules; and
- durable planning, validation and close-out evidence.

## Severity

Classify the event according to its observed impact and remaining uncertainty, not the apparent simplicity of the initiating action.

| Severity | Definition | Typical examples | Resumption authority |
| --- | --- | --- | --- |
| **Minor** | No authoritative content remains changed, the event is immediately and confidently reversible, authority and scope remain valid, and affected evidence is current or can be rerun without ambiguity. | An unintended empty branch or accidental issue is removed or closed; no commits, files, approvals or checks are affected. | May resume after all minor-deviation gates pass. |
| **Material** | Authoritative repository or evidence state changed but is recoverable, or the event creates meaningful uncertainty about scope, validation, review or approval. | Wrong-branch commit, accidental PR state change, stale approval, changed issue state or recoverable out-of-scope file mutation. | Explicit repository-owner direction is required before normal mutation resumes. |
| **Critical** | The event causes or may have caused unauthorised merge, data loss, security or permission exposure, irreversible mutation, production impact or repository state that cannot be confidently reconstructed. | Unauthorised merge, leaked secret, destructive settings change, unrecoverable history rewrite or uncertain production mutation. | Stop normal execution. Explicit owner direction and an incident-specific recovery decision are required. |

When severity is uncertain, use the higher plausible classification until evidence resolves the uncertainty.

Repeated minor deviations may be reclassified as material when recurrence shows that the corrective control is ineffective or the execution environment is not reliably safe.

## Required evidence record

A formal deviation record must contain:

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

Record facts separately from inference. Do not claim a root cause, complete restoration or absence of risk unless the repository evidence supports it.

## Evidence location

Record the deviation on the active execution issue whenever one exists.

Also surface it in:

- the pull-request evidence pack when review interpretation, validation or approval is affected;
- the pull-request discussion when remediation changes the final head or evidence state; and
- the post-merge or delivery close-out record when the event affects final delivery evidence.

Do not create a separate issue solely to duplicate a fully contained local record.

## Stale-evidence rules

A deviation invalidates evidence only to the extent that the evidence no longer proves the current state. When uncertain, treat the evidence as stale.

| Evidence | Stale when | Required action |
| --- | --- | --- |
| Safe starting point | The base branch or dependency state changed, or the branch was created from a different commit. | Refresh readiness or dependency evidence and record the new safe point. |
| Implementation plan | Recovery changes the permitted approach, files, sequence, assumptions or validation. | Update or replace the plan before normal implementation continues. |
| Validation | The validated content, configuration, environment or generated artefact changed, or its identity cannot be proved. | Rerun the affected validation against the restored final state. |
| Review finding disposition | Recovery changes the code or documentation that addressed the finding. | Reinspect the finding and refresh the response or resolution state. |
| Pull-request evidence pack | Scope, validation, caveats, remaining checks or final head changed. | Refresh the evidence pack before approval. |
| Approval or exact-head authorisation | The pull-request head changes after approval or the approved head cannot be established confidently. | Obtain new approval or exact-head authorisation for the final head. |
| Post-merge verification | The deployed, released or published object differs from the object previously observed. | Repeat the affected post-merge check. |

A successful rollback or object deletion proves containment only when the expected state is fetched and verified. It does not by itself prove that related evidence remains current.

## Minor-deviation resumption gate

Normal mutation may resume without a new owner decision only when all of these conditions are true:

- the deviation is classified as minor with evidence;
- the unintended state has been removed, closed, reverted or otherwise made safe;
- the expected stable branch, issue, branch, PR and changed-file state has been verified;
- authority, execution-contract scope and dependencies remain unchanged;
- affected evidence is confirmed current or has been rerun;
- no security, permission, settings, production or merge impact occurred;
- a practical corrective control is in place; and
- the resumption decision is recorded on the active issue.

Any failed condition or unresolved uncertainty blocks this gate.

## Material and critical resumption gates

Material and critical deviations require explicit repository-owner direction before normal mutation resumes.

The owner direction must identify, at minimum:

- whether the current execution contract remains valid;
- the accepted recovery state and residual risk;
- any evidence that must be rerun;
- whether a revised plan or new execution contract is required; and
- the exact next permitted mutation, if execution may continue.

Critical events may require repository-specific security, incident or recovery procedures outside IssueOps. IssueOps documentation does not replace those procedures.

## Corrective controls

A corrective control must address the observed failure mode. Examples include:

- constraining the next permitted tool to one named action;
- verifying the selected tool and target immediately before invocation;
- requiring exact issue, branch or head identifiers from fetched repository state;
- separating remediation from normal execution;
- changing execution environment or operator when recurrence shows the current path is unreliable; or
- narrowing or restarting the execution contract.

A verbal intention that does not change the failing execution path is not a sufficient corrective control after recurrence.

## Follow-up issue criteria

Create separate follow-up work only when the deviation reveals at least one unresolved condition:

- a missing or ambiguous protocol control;
- repeated failure despite an existing control;
- a connector, platform or repository-tooling defect;
- unrecovered repository impact;
- security, permission or production exposure;
- a justified need for preventive automation; or
- a reusable cross-repository lesson not already covered by canonical guidance.

The follow-up issue should describe the systemic problem and desired outcome. It should not be a second copy of the local deviation log.

## Failure-source classification

Classifying the source helps choose the correct follow-up work. It does not replace severity classification.

| Source | Meaning | Typical follow-up |
| --- | --- | --- |
| Repository defect | Repository code, configuration or documented behaviour is incorrect. | Product or repository bug issue. |
| Missing process control | IssueOps guidance lacks or ambiguously states a needed boundary. | Planning or documentation issue in IssueOps. |
| Connector or platform failure | The invoked operation behaved differently from its documented contract. | Tooling/platform defect with reproducible evidence. |
| Execution non-compliance | The operator or agent selected the wrong action, target or sequence despite an adequate rule. | Local deviation evidence; corrective execution control; follow-up only for recurrence or systemic prevention. |
| Harmless failed command | No authoritative state, authority or evidence was affected. | Usually no formal deviation or backlog item. |

## Merge and review effect

A deviation blocks approval or merge when:

- required recovery or owner direction is incomplete;
- repository state cannot be reconstructed confidently;
- affected validation, review or approval evidence remains stale;
- scope or authority is unresolved;
- a material finding remains open; or
- the pull-request evidence pack does not disclose the event accurately.

A fully contained minor deviation does not automatically block approval. The reviewer must still verify containment, current evidence and the groundedness of the final change.

## Relationship to safe operations

The [operation permissions and evidence](operation-permissions-and-evidence.md) reference defines which repository mutations are permitted in each lifecycle phase and triggers the circuit breaker. This page owns what happens after that circuit breaker is triggered.