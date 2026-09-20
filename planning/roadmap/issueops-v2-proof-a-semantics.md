# IssueOps v2 Proof A — normative semantic specification

Status: delivering.

Record type: contemporaneous.

Governing execution contract: [#214](https://github.com/8ft0-ai/IssueOps/issues/214).

Parent architecture and proof programme: [#212](https://github.com/8ft0-ai/IssueOps/issues/212) and [IssueOps v2 — minimal authority protocol proof programme](issueops-v2.md).

IssueOps `v0.3.0` remains the current stable protocol. This specification defines the semantic model to be tested by later v2 proofs. It does not replace current operating guidance, grant execution authority, create operational capability or begin Proof B.

## Problem statement

The accepted v2 architecture is approved for proof, but later private-GitHub-Free, dogfood and external-pilot work must not invent unresolved lifecycle semantics while executing. Proof A therefore turns the architecture into one precise normative model while the current stable `v0.3.0` protocol remains authoritative for real IssueOps operations.

## Outcome to prove

Prove that one five-state / six-invariant semantic model can preserve every material stable-kernel safety property, resolve the architecture's open semantic choices needed by later proofs, and remain compatible with private GitHub Free without adding operational capability or a parallel lifecycle state store.

## Non-goals

Proof A does not:

- adopt v2 as the stable IssueOps protocol;
- replace `docs/issueops-protocol.md` or current public operating guidance;
- define the complete Proof B private-GitHub-Free operational profile;
- change workflows, repository settings, rulesets, branch protection or required checks/reviewers;
- create deployment, credential or generic execution transport;
- run IssueOps dogfood or an external pilot;
- introduce a lifecycle database, state manifest, queue or central service;
- publish a release/tag; or
- authorise later proof work merely because this specification is accepted.

## Operating and autonomy boundary

The current stable IssueOps protocol governs this proof's implementation, review and any eventual merge.

Within the v2 semantics defined here, deterministic mechanisms may establish exact canonical facts and currentness only when no new intent, risk acceptance, substantive judgement or authority is required. Human implementation authority and later consequence authority remain prospective, durable and separate. Independent substantive review remains a human-judgement qualification predicate.

No agent, workflow, check, role, technical capability or successful tool invocation may manufacture human authority.

## Target workflow or target state

The target semantic lifecycle is exactly:

```text
CONTRACT_READY
  -> IMPLEMENTATION_AUTHORISED
  -> CANDIDATE_QUALIFIED
  -> CONSEQUENCE_AUTHORISED
  -> OUTCOME_RECORDED
```

owned cross-cutting by:

```text
Intent
Identity
Authority
Assurance
Freshness
Outcome
```

The detailed normative rules below define the predicates, evidence, blockers, human/mechanical boundaries, staleness and permitted transition for each state.

These five names are semantic states, not once-only historical milestones. The ordinary first traversal is the forward sequence shown above. A later retry or recovery after a possibly-effective consequence attempt MAY re-enter an earlier applicable state only under the rules below. Re-entry MUST preserve the durable identity and outcome of every prior attempt, MUST re-establish every predicate made stale by the prior attempt or resulting state, and MUST NOT create a sixth lifecycle state or parallel lifecycle instance.

## Acceptance gates

- [ ] All six invariants have normative definitions.
- [ ] All five states define entry predicates, durable evidence, blockers, predicate classes, staleness and permitted next transition.
- [ ] Implementation and consequence authority remain prospective, durable, human and separate.
- [ ] Independent substantive review is exact-candidate-bound and cannot be self-satisfied by the authoring/remediation context.
- [ ] Candidate, base, scope, dependency, intent, review and deviation freshness rules fail closed when currentness is unknown.
- [ ] Consequence-authority evidence binding is minimal when unambiguous and explicit when ambiguity exists.
- [ ] `OUTCOME_RECORDED` cannot falsely represent successful verification.
- [ ] All ten stable-kernel properties are mapped with no intentional loss.
- [ ] The execution-deviation circuit breaker remains cross-cutting and equivalent or stronger.
- [ ] Exceptional/direct-main actions use the same semantic model without creating standing authority.
- [ ] GitHub-native records remain canonical and no parallel lifecycle state store is introduced.
- [ ] Private GitHub Free remains sufficient for protocol correctness without paid enforcement features.
- [ ] The specification introduces no operational capability and does not replace the stable protocol.

## Proposed implementation slices

Proof A itself is intentionally one bounded specification slice:

```text
canonical semantic specification
  -> exact-head repository validation
  -> completely fresh independent substantive semantic-specification review
  -> separate consequence authority if accepted
```

No Proof B implementation, dogfood, external pilot or speculative later-proof issue is part of this slice.

## Risks and controls

### Risk: semantic simplification silently removes a stable safety property

Control: the specification includes complete stable-kernel traceability and treats any lost or materially ambiguous property as a blocker.

### Risk: deterministic machinery manufactures judgement or authority

Control: predicate classification separates mechanical facts, human judgement and human authority; automation may establish only already-defined exact facts.

### Risk: consequence authority is under-bound

Control: exact candidate + named consequence + prospective human authority + immediate requalification is permitted only when one complete accepted evidence set is unambiguous; otherwise evidence identities must be bound explicitly or fresh authority obtained.

### Risk: outcome recording is mistaken for success

Control: outcome classification and verification completeness are separate; contract-required post-consequence verification cannot be bypassed by invocation or merge success.

### Risk: the exceptional path becomes a hidden fast path

Control: exceptional actions remain in the same five-state model, require prospective exact authority and must disclose when normal pre-effective candidate separation was unavailable.

### Risk: paid GitHub features become hidden correctness dependencies

Control: branch protection, rulesets, required checks/reviewers, protected environments, merge queues and Enterprise features remain optional hardening only.

## Definition of done

Proof A is complete only when:

- [ ] this semantic specification satisfies every acceptance gate above;
- [ ] repository-native planning/documentation validation is successful against the exact candidate;
- [ ] base-to-head scope remains within the approved Proof A paths;
- [ ] a completely fresh independent substantive semantic-specification review accepts the exact candidate;
- [ ] any review remediation is revalidated and freshly reviewed as required;
- [ ] any eventual merge occurs only under separate later human consequence authority; and
- [ ] completion does not automatically begin Proof B or adopt v2.

## Likely next decision boundary

If Proof A is accepted, the next separately governed question is whether to begin:

```text
V2 PROOF B — PRIVATE_GITHUB_FREE_PROFILE
```

Proof A acceptance provides semantic input to that decision but does not authorise Proof B implementation.

## 1. Normative interpretation

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD** and **MAY** are normative within this Proof A specification.

The v2 lifecycle has exactly five semantic states:

```text
CONTRACT_READY
IMPLEMENTATION_AUTHORISED
CANDIDATE_QUALIFIED
CONSEQUENCE_AUTHORISED
OUTCOME_RECORDED
```

and six cross-cutting invariants:

```text
Intent
Identity
Authority
Assurance
Freshness
Outcome
```

A state is a derived meaning over canonical repository evidence. It is not a mandatory label, file, database row, comment template or automation state.

A transition MAY be established mechanically only when all required facts are canonical, complete, exact, current and deterministic; no new intent, risk acceptance, substantive review judgement or human authority is required; the next action is already authorised; and failure stops safely.

Mechanical evaluation MUST NOT manufacture:

```text
intent
risk acceptance
substantive review judgement
implementation authority
consequence authority
```

Where a required predicate cannot be established, currentness is uncertain, evidence is contradictory, or accepted evidence identity is ambiguous, progression MUST fail closed.

## 2. Canonical evidence and state ownership

Canonical v2 evidence is derived from repository-native records, including as applicable:

```text
issues
issue/PR comments
pull requests
reviews
commits
exact commit and head SHAs
workflow/check records
merge/result records
release/publication/deployment records when the governing contract requires them
```

Compact evidence blocks, summaries, generated views and caches MAY improve usability, but they MUST remain non-authoritative and recomputable from canonical records.

The core protocol MUST NOT require a parallel:

```text
issueops-state.json
lifecycle database
programme manifest
central service
queue
generic execution engine
```

GitHub-native records own evidence and durable state. IssueOps owns lifecycle semantics, authority meanings, currentness rules and fail-closed behaviour. Execution, deployment, credential and host transport remain outside the core protocol.

## 3. Six invariants

### 3.1 Intent

There MUST be one identifiable durable governing record, or one unambiguous set of linked durable records, that defines the bounded outcome being pursued.

Intent is sufficiently bounded only when implementation and review can determine, without inventing material product, repository-policy or engineering intent:

- the problem or purpose;
- expected outcome;
- scope and important non-goals;
- reviewable success criteria;
- expected assurance appropriate to the change;
- material dependencies and ordering constraints; and
- the consequence boundary that later authority may permit.

Presentation MAY be compact. Routine implementation detail MAY remain implicit when repository conventions make it deterministic and non-material.

Intent MUST NOT remain implicit when omission would require later judgement about architecture, security, scope, authority, risk acceptance, validation sufficiency, destructive behaviour or consequence boundaries.

If two plausible interpretations would permit materially different implementation or consequence, Intent is ambiguous and progression MUST stop before the affected action.

The governing issue, approved planning/design record or another repository-native primary record is authoritative. Chat summaries, handovers and session grants are navigation or claims only until reconciled against current canonical records.

### 3.2 Identity

Every decision-relevant object or state MUST be identified precisely enough that the evidence and authority can be proven to apply to the thing acted upon.

Identity MAY include:

| Object | Minimum identity when material |
| --- | --- |
| repository | exact owner/repository |
| governing record | issue/record identity |
| implementation path | durable approved plan/record identity |
| candidate | repository + candidate object + exact immutable content identity |
| pull request | PR number + exact head SHA |
| base | exact base SHA when base state affects correctness, assurance or consequence |
| validation/check | run/check identity + exact candidate/state it assessed |
| substantive review | review/comment identity + exact candidate/state it assessed |
| authority | durable human authority record + exact state/consequence it permits |
| consequence attempt | attempt/operation identity + deterministic evidence of whether actuation could have crossed the consequence boundary when authority consumption or reuse depends on that fact |
| outcome | resulting merge commit/object/deployment/publication identity as applicable |

A mutable branch name, tag name, environment name or PR number alone MUST NOT be treated as exact candidate identity when its referenced content or state can move.

For normal repository work, the preferred candidate identity is:

```text
repository
+ pull request
+ exact head SHA
```

with base, assurance, review and target identities added whenever they affect the decision.

When more than one consequence attempt occurs under the same governing work, each possibly-effective attempt and its recorded outcome MUST have a distinct durable identity. A later retry or recovery MUST NOT overwrite, replace or relabel the identity or outcome classification of an earlier attempt; later evidence may change which resulting state is current, but historical attempt facts remain durable.

### 3.3 Authority

Technical capability, repository access, a green check, role name, approval-shaped UI state, absence of blockers or ability to invoke a tool is not authority.

v2 preserves two distinct human authority meanings.

#### IMPLEMENTATION_AUTHORITY

IMPLEMENTATION_AUTHORITY permits execution of one bounded proposed implementation path.

It MUST:

- be durable;
- be human;
- be prospective;
- apply to a CONTRACT_READY governing record;
- identify the approved execution path with enough precision for the risk;
- precede the implementation mutation it permits; and
- remain within the governing contract.

It does NOT authorise:

- merge or another later consequence;
- work outside the approved path;
- a material redesign discovered after approval;
- acceptance of validation/review findings; or
- replacement of the governing contract.

A material change to scope, architecture, files/areas, risk treatment, consequence boundary or validation model makes the earlier implementation authority stale for the changed work.

#### CONSEQUENCE_AUTHORITY

CONSEQUENCE_AUTHORITY permits one named later consequence against one exact qualified state.

It MUST:

- be durable;
- be human;
- be prospective;
- occur only after CANDIDATE_QUALIFIED has been established;
- identify the exact repository and governing contract;
- identify the exact candidate/state;
- name the permitted consequence; and
- remain current at the moment of actuation.

Implementation authority and consequence authority MUST remain separate human decisions. Earlier implementation authority MUST NOT be interpreted as later consequence authority.

CONSEQUENCE_AUTHORITY is single-use for one **possibly-effective actuation attempt**. It is consumed once actuation may have crossed the named consequence boundary.

A failed operation does **not** consume CONSEQUENCE_AUTHORITY only when positive deterministic evidence proves both that actuation never crossed that boundary and that no authoritative target state could have changed. Absence of an observed change is not sufficient proof of non-consumption.

If it is uncertain whether actuation crossed the consequence boundary, or if any authoritative side effect cannot be ruled out, the authority MUST be treated as consumed. A retry, recovery or follow-on actuation after consumed or uncertain authority requires fresh prospective CONSEQUENCE_AUTHORITY.

The same consequence-authority record MAY be reused after a proven pre-actuation/no-effect failure only when the exact candidate, target, named consequence and accepted assurance/review set remain current and an immediate deterministic requalification succeeds.

### 3.4 Assurance

Assurance is evidence that decision-relevant claims about the current state are sufficiently supported for the change and consequence.

Assurance MAY include:

```text
tests
builds
lint/static checks
documentation validation
planning validation
read-back
diff/scope verification
security analysis
representative/manual verification
repository/environment observations
substantive contract review
```

The assurance set MUST be proportional to the changed behaviour and risk. Change-specific evidence MAY vary, but these semantic properties remain mandatory whenever relevant:

- candidate identity is exact;
- implementation remains faithful to bounded intent;
- scope is controlled;
- required validation is current or truthfully classified;
- independent substantive review is current;
- unresolved material blockers are absent.

Evidence MUST identify the state it proves. Evidence against an older candidate MUST NOT be represented as current for a changed candidate unless the affected property can be deterministically proven unchanged.

Unavailable, pending or post-consequence evidence MUST be represented truthfully. A weaker fallback MUST NOT be described as equivalent to stronger evidence.

Green CI proves only the checks that actually ran against the identified state. It is never human implementation authority, consequence authority or substantive review judgement.

#### Independent substantive review

Independent substantive review is a HUMAN JUDGEMENT predicate within CANDIDATE_QUALIFIED.

A review relied upon as independent MUST:

- assess the governing contract and the actual exact candidate, not merely the shape of a diff;
- be performed from a context that did not author or remediate that candidate in the same review context;
- reach a substantive supported conclusion;
- remain bound to the exact state reviewed; and
- become stale when material candidate changes make its conclusion no longer prove the current candidate.

An authoring/remediation context MUST NOT self-qualify its own candidate by producing a review-shaped record.

Mechanical checks MAY establish review identity, exact-head binding and currentness. They MUST NOT manufacture the review judgement itself.

The independent review context relied upon for qualification MUST terminate its consequence-execution role after recording its conclusion; later human consequence authority does not turn that same review context into the consequence executor.

### 3.5 Freshness

Freshness is a continuously evaluated predicate that asks whether Intent, Identity, Authority and Assurance still apply to the state being acted upon.

Unknown freshness MUST fail closed.

At minimum:

| Change | Freshness effect |
| --- | --- |
| candidate head changes | prior exact-candidate qualification is stale until affected assurance/review are reconciled or rerun |
| validation targets older candidate | validation is not current for the new candidate unless deterministic unaffectedness is proven |
| review targets older materially changed candidate | review is stale |
| authority binds older candidate/state | authority is stale |
| governing intent or scope changes materially | affected implementation authority and downstream qualification are stale |
| proposed implementation path changes materially | implementation authority is stale for changed work |
| dependency changes materially | affected readiness/qualification/authority must be reconciled |
| new material review finding appears | candidate is not qualified until resolved and affected evidence refreshed |
| consequence target changes | consequence authority is stale unless exact applicability remains proven |
| execution deviation creates uncertainty | affected Authority, Assurance and Freshness evidence is stale or invalid until reconstructed |

#### Material base drift

Movement of a base branch does not automatically stale a candidate solely because another commit exists.

Base drift is material when it can affect any of:

```text
contract correctness
merge/apply result
validation assumptions
dependency state
security or authority boundary
conflict resolution
resulting consequence identity
```

If materiality can be proven absent deterministically, the prior candidate MAY remain current with respect to base drift.

If base-drift materiality cannot be established confidently, freshness is UNKNOWN and progression MUST stop.

### 3.6 Outcome

Outcome records what actually happened, not what was requested or what a tool reported before resulting state was verified.

The top-level outcome classification remains:

```text
EXPECTED
FAILED
PARTIAL
UNKNOWN
```

- **EXPECTED**: the named consequence produced the expected resulting state and all contract-required outcome evidence currently due is satisfied.
- **FAILED**: the consequence did not produce the required state, or required verification proves failure.
- **PARTIAL**: some expected consequence occurred but the required resulting state is incomplete, mixed or only partly satisfied.
- **UNKNOWN**: the actual resulting state or required verification cannot be established sufficiently.

Outcome identity MUST bind the actual attempt and resulting repository/object/environment identity where material.

Invocation success, an API 2xx response, command exit status or merge request submission is not sufficient by itself. Resulting state MUST be observed at the level required by the governing contract.

A failed operation with positive deterministic proof that no actuation crossed the consequence boundary and no authoritative target state could have changed is not a consequence attempt for lifecycle authority-consumption purposes. Otherwise, any possibly-effective or uncertain actuation MUST proceed to truthful outcome reconstruction, including `UNKNOWN` or `PARTIAL` when the effect cannot be established.

## 4. Five lifecycle states

### 4.1 CONTRACT_READY

#### Entry predicates

CONTRACT_READY holds only when:

- bounded durable Intent exists;
- scope and important non-goals are sufficient;
- success and evidence expectations are reviewable;
- material dependencies and action-relevant current state are reconciled;
- a safe execution starting point is identifiable when implementation requires one; and
- no unresolved material ambiguity requires new intent.

A separately named readiness comment is not semantically required when equivalent canonical evidence proves these predicates.

#### Required durable evidence

At minimum:

```text
governing record identity
bounded intent/scope
success/evidence expectations
dependency/current-state evidence
safe starting state when material
```

#### Blocking conditions

Missing material intent, unresolved dependency, unknown safe starting point, contradictory requirements or acceptance criteria that cannot be reviewed block CONTRACT_READY.

#### Predicate classification

- DETERMINISTIC / MECHANICAL: repository identity, dependency state, exact base existence, presence of required fields/records when their meaning is unambiguous.
- HUMAN JUDGEMENT: whether intent is sufficiently bounded, risk is represented honestly, acceptance criteria are reviewable and no material design choice is being hidden.
- HUMAN AUTHORITY: none merely to establish readiness.

#### Staleness

Material changes to governing intent, dependencies, current repository state or safe starting assumptions stale affected CONTRACT_READY evidence.

#### Permitted next transition

Only to IMPLEMENTATION_AUTHORISED after a proposed path exists and prospective durable human implementation authority is granted.

### 4.2 IMPLEMENTATION_AUTHORISED

#### Entry predicates

IMPLEMENTATION_AUTHORISED holds only when:

- CONTRACT_READY is current;
- the proposed execution path is explicit enough for the risk;
- material files/areas, design choices, exclusions, validation and consequence boundaries are visible;
- prospective durable human IMPLEMENTATION_AUTHORITY approves that path; and
- the authority predates implementation mutation.

The plan is proportional to risk. “Small change” MAY justify a compact plan, but MUST NOT justify omission of a material judgement.

#### Required durable evidence

```text
current CONTRACT_READY evidence
proposed implementation path
durable human implementation-authority record
approved safe starting state
```

#### Blocking conditions

No human approval, retrospective approval, vague plan that hides material design/risk, materially changed plan after approval, or stale safe base when applicability is uncertain.

#### Predicate classification

- DETERMINISTIC / MECHANICAL: exact plan/authority record existence, temporal ordering, safe-base identity and currentness where deterministic.
- HUMAN JUDGEMENT: sufficiency/proportionality of the proposed path and whether a change is material.
- HUMAN AUTHORITY: explicit implementation approval.

#### Staleness

Material change to contract, execution path, safe base, scope, risk, validation strategy or consequence boundary stales implementation authority to the extent affected.

#### Permitted next transition

Implementation may produce an exact candidate. The lifecycle reaches CANDIDATE_QUALIFIED only after all qualification predicates, including independent substantive review, hold.

### 4.3 CANDIDATE_QUALIFIED

#### Entry predicates

CANDIDATE_QUALIFIED holds only when:

- the candidate identity is exact;
- implementation remains faithful to current bounded Intent;
- scope is controlled;
- required exact-candidate Assurance is complete or truthfully classified;
- decision-relevant evidence is current;
- a current independent substantive review has assessed the exact candidate;
- no unresolved material review finding or other blocker remains; and
- any execution deviation affecting the candidate has completed its required resumption gate.

#### Required durable evidence

For normal PR work:

```text
repository
governing contract
PR
exact head SHA
material base identity where required
scope/diff evidence
validation/check evidence
independent substantive review identity
review conclusion
unresolved-blocker state
deviation/resumption evidence where applicable
```

#### Blocking conditions

Unknown candidate identity, scope drift, failed required assurance, misleading evidence, stale review, same-context self-review represented as independent, unresolved material finding, unresolved execution deviation or uncertain currentness.

#### Predicate classification

- DETERMINISTIC / MECHANICAL: candidate/head identity, diff/path set, check results, evidence exact-head binding, unresolved-thread/finding presence where canonically represented, currentness rules that require no judgement.
- HUMAN JUDGEMENT: contract fidelity, risk interpretation, substantive review, materiality of findings and whether evidence is sufficient where policy requires judgement.
- HUMAN AUTHORITY: none merely to qualify the candidate; reviewer judgement is not authority to perform the consequence.

#### Staleness

A candidate head change makes exact candidate qualification stale. Material base, dependency, intent, assurance or review-state changes stale the affected predicates. New material findings remove qualification until resolved and requalified.

#### Permitted next transition

Only to CONSEQUENCE_AUTHORISED after separate prospective durable human consequence authority for the exact qualified state.

When CANDIDATE_QUALIFIED is re-established after an OUTCOME_RECORDED attempt for retry or recovery of the same unchanged candidate, every qualification predicate affected by the prior attempt, resulting target state, dependency state or new finding MUST be re-established as current. Prior assurance or independent review MAY remain usable only when its applicability to the unchanged candidate and current decision can be deterministically proven; otherwise the affected evidence MUST be refreshed.

### 4.4 CONSEQUENCE_AUTHORISED

#### Entry predicates

CONSEQUENCE_AUTHORISED holds only when:

- CANDIDATE_QUALIFIED is current;
- the exact candidate/state is identified;
- the named consequence is explicit;
- prospective durable human CONSEQUENCE_AUTHORITY applies to that candidate and consequence;
- the complete accepted assurance/review set is either selected unambiguously from canonical records or explicitly bound by the authority; and
- immediate pre-action revalidation confirms currentness.

#### Minimum safe binding rule

The default minimum binding is:

```text
exact repository
+ governing contract
+ exact candidate/state
+ named consequence
+ prospective durable human consequence authority
+ immediate deterministic current requalification
```

This is sufficient only when the governing contract and canonical records select one complete accepted assurance/review set unambiguously.

If accepted review/check/evidence identity is ambiguous, incomplete or multiply selectable, deterministic requalification is insufficient. Before consequence:

```text
authority MUST explicitly bind the accepted evidence identities
OR
the ambiguity MUST be resolved and fresh human consequence authority obtained
```

This rule avoids mandatory repetition of evidence IDs when exact-candidate binding already selects them uniquely, without allowing ambiguity to be rounded up to authority.

#### Required durable evidence

```text
current CANDIDATE_QUALIFIED evidence
durable human consequence-authority record
exact candidate/state
named consequence
accepted evidence identity when ambiguity requires explicit binding
pre-action revalidation evidence
```

#### Blocking conditions

Changed candidate, stale review/validation, moved target, superseded authority, ambiguous accepted evidence set, new material blocker, unresolved deviation, inability to prove currentness, or an earlier operation whose authority-consumption state is uncertain.

#### Predicate classification

- DETERMINISTIC / MECHANICAL: exact candidate match, accepted evidence identity/currentness, target identity/currentness and check/review state where facts are canonical.
- HUMAN JUDGEMENT: whether a new fact materially changes qualification when not mechanically decidable.
- HUMAN AUTHORITY: explicit consequence decision.

#### Staleness

Any mismatch in exact candidate, named consequence or materially relevant accepted evidence/target state stales consequence authority. Unknown applicability fails closed.

#### Permitted next transition

On the first possibly-effective actuation attempt, the bounded CONSEQUENCE_AUTHORITY is consumed and the lifecycle proceeds through outcome reconstruction to OUTCOME_RECORDED.

If an operation fails before actuation with positive deterministic proof that the consequence boundary was never crossed and no authoritative target state could have changed, no consequence attempt has occurred for this purpose. The lifecycle MAY remain at CONSEQUENCE_AUTHORISED only after immediate deterministic requalification confirms that the exact candidate, target, accepted assurance/review set and named consequence remain current.

If non-consumption cannot be proven, the authority is treated as consumed, the actual outcome is reconstructed truthfully, and fresh prospective CONSEQUENCE_AUTHORITY is required before any retry or recovery actuation.

After a consumed or uncertain attempt reaches OUTCOME_RECORDED, a retry or recovery MUST NOT actuate directly from OUTCOME_RECORDED. For the same unchanged candidate, the lifecycle MUST first re-establish CANDIDATE_QUALIFIED against the current resulting state, then obtain fresh prospective CONSEQUENCE_AUTHORITY and re-enter CONSEQUENCE_AUTHORISED before the next actuation attempt. If recovery changes governing intent, the implementation path or the candidate, the lifecycle MUST instead return to the earliest state whose predicates were invalidated and satisfy all later predicates and human-authority requirements again before consequence.

### 4.5 OUTCOME_RECORDED

#### Entry predicates

OUTCOME_RECORDED holds when the consequence attempt has occurred and the currently knowable actual result is durably recorded with sufficient identity.

The state is deliberately not named OUTCOME_VERIFIED. Verification completeness is a predicate over the outcome, not a sixth lifecycle state.

Each possibly-effective actuation attempt closes one consequence-attempt cycle with its own durable OUTCOME_RECORDED evidence. A later retry or recovery creates a new attempt identity and, if possibly effective, a new outcome record. It MUST NOT overwrite or collapse the earlier attempt/outcome record.

#### Required durable evidence

As applicable:

```text
attempt identity
authorised consequence identity
actual result classification
resulting repository/object/environment identity
post-consequence verification requirement
verification evidence or truthful pending/failed/unavailable/unknown classification
```

#### Blocking conditions

The lifecycle MUST NOT represent successful completion when the actual result is unobserved, ambiguous or when contract-required post-consequence verification remains outstanding.

A consequence attempt may still be recorded with PARTIAL or UNKNOWN outcome while verification is incomplete.

#### Predicate classification

- DETERMINISTIC / MECHANICAL: resulting commit/object IDs, observed workflow/deployment status and verification facts where canonical and deterministic.
- HUMAN JUDGEMENT: interpretation of mixed evidence, residual risk and whether contract-required verification sufficiently proves the intended result.
- HUMAN AUTHORITY: none to record truthful outcome; any recovery, retry or follow-on actuation after consumed or uncertain consequence authority requires fresh prospective CONSEQUENCE_AUTHORITY.

#### Staleness

Outcome evidence becomes stale when the observed object/environment changes or later evidence shows the prior classification no longer describes the relevant resulting state. Historical attempt facts remain durable; their applicability to the current state may change.

#### Permitted next transition

No automatic next proof or initiative. Recovery, retry, follow-on implementation, adoption, release or another consequence requires the governing contract and authority appropriate to that new action.

For retry or recovery after a consumed or uncertain attempt:

- preserve the prior attempt and OUTCOME_RECORDED evidence;
- if the same exact candidate remains applicable, re-establish CANDIDATE_QUALIFIED against the current resulting state before seeking fresh consequence authority;
- if governing intent, implementation path or candidate changed, return to the earliest lifecycle state whose predicates were invalidated and satisfy the affected later states again;
- obtain fresh prospective CONSEQUENCE_AUTHORITY for the next possibly-effective actuation; and
- enter CONSEQUENCE_AUTHORISED with immediate current revalidation before actuating.

Only a positively proven pre-actuation/no-effect failure may remain at CONSEQUENCE_AUTHORISED with the existing unconsumed authority, subject to immediate deterministic current requalification.

## 5. Transition predicate summary

| Transition | Mechanical predicates may establish | Human judgement required | Human authority required |
| --- | --- | --- | --- |
| before CONTRACT_READY -> CONTRACT_READY | identity, dependency/current-state facts, exact safe base where deterministic | boundedness, material ambiguity, reviewability | no |
| CONTRACT_READY -> IMPLEMENTATION_AUTHORISED | plan/authority identity, temporal ordering, base currentness | proportional plan sufficiency, materiality | **yes: IMPLEMENTATION_AUTHORITY** |
| IMPLEMENTATION_AUTHORISED -> CANDIDATE_QUALIFIED | candidate identity, scope facts, checks/currentness | contract fidelity, substantive independent review, material findings | no consequence authority yet |
| CANDIDATE_QUALIFIED -> CONSEQUENCE_AUTHORISED | exact-state/evidence requalification | materiality when deterministic rules are insufficient | **yes: CONSEQUENCE_AUTHORITY** |
| CONSEQUENCE_AUTHORISED -> OUTCOME_RECORDED | actuation/attempt/result/object observations, including deterministic proof of pre-actuation failure where claimed | mixed/partial outcome interpretation where needed | no authority to record facts; consumed or uncertain authority requires fresh CONSEQUENCE_AUTHORITY before retry, while positively proven pre-actuation/no-effect failure may retain current authority after requalification |
| OUTCOME_RECORDED -> re-entry at earliest affected state for retry/recovery | prior-attempt identity, current candidate/target/dependency state, which predicates are demonstrably unchanged | materiality of changed state and sufficiency of retained assurance/review | no authority merely to reconstruct/requalify; any affected IMPLEMENTATION_AUTHORITY must be renewed where required, and fresh CONSEQUENCE_AUTHORITY is always required before a new possibly-effective retry |

## 6. Stable-kernel equivalence proof

| Current stable-kernel property | v2 invariant/state | Exact preservation mechanism | Semantic change |
| --- | --- | --- | --- |
| bounded issue contract | Intent + CONTRACT_READY | durable bounded governing record, scope/non-goals, reviewable outcome/evidence expectations | presentation generalised beyond mandatory issue-only syntax; no safety property removed |
| current-state reconciliation | Identity + Freshness + CONTRACT_READY | dependencies, action-relevant state and safe starting point must be current; unknown applicability fails closed | may be proven by equivalent durable evidence rather than a mandatory separate readiness comment |
| explicit proposed implementation path | Intent + IMPLEMENTATION_AUTHORISED | risk-proportionate path must expose material design, exclusions, validation and consequence boundaries before approval | presentation may be compact for low risk |
| durable human implementation authority | Authority + IMPLEMENTATION_AUTHORISED | prospective durable human approval binds current contract/path and predates mutation | unchanged in meaning |
| bounded candidate implementation | Intent + Identity + transition to CANDIDATE_QUALIFIED | implementation must stay inside contract and produce exact candidate identity | branch/setup mechanics become evidence rather than first-class state |
| exact-candidate validation/evidence | Identity + Assurance + Freshness + CANDIDATE_QUALIFIED | assurance is bound to exact candidate and stale evidence cannot qualify changed state | evidence set remains proportional rather than universal |
| substantive contract review | Assurance + Freshness + CANDIDATE_QUALIFIED | independent substantive exact-candidate review is mandatory; author/remediation context cannot self-qualify | review is a qualification predicate rather than separate lifecycle state |
| separate human merge/consequence authority | Authority + CONSEQUENCE_AUTHORISED | separate later prospective human decision binds exact qualified candidate and named consequence | **generalised** from merge to named bounded consequence; transport remains outside core |
| post-consequence verification | Outcome + Assurance + OUTCOME_RECORDED | contract-required verification remains mandatory; invocation/merge success cannot impersonate verification | verification completeness becomes an outcome predicate, not a separate state |
| execution-deviation circuit breaker | Authority + Assurance + Freshness cross-cutting rule | deviation suspends progression, stops normal writes, reconstructs state, stales affected evidence and requires evidenced resumption | remains cross-cutting; not a sixth state |

No stable-kernel property in this mapping is intentionally lost.

## 7. Execution-deviation circuit breaker

The circuit breaker is a cross-cutting rule over all five states.

An **execution deviation** is an unintended mutation, unplanned consequential side effect, or material uncertainty after actuation about authoritative state, scope, authority or decision-relevant evidence.

When triggered:

```text
suspend normal progression
-> stop normal mutation
-> permit only read-only investigation and minimum authorised containment/remediation
-> reconstruct and verify authoritative state
-> stale or invalidate affected Authority, Assurance and Freshness evidence
-> do not restore stale evidence merely because object state was restored
-> resume only through evidenced resumption
```

A failed tool call that changed no authoritative state, affected no evidence/authority and creates no material uncertainty need not become a formal deviation.

A contained **minor** deviation may resume without a new owner decision only when all of these are established:

- safe state is verified;
- authority, scope and dependencies remain valid;
- affected evidence is current or rerun;
- no security, permission, settings, production or merge impact occurred;
- no higher-impact consequence remains;
- a practical corrective control exists; and
- the resumption decision is durable.

A **material**, **critical**, unresolved or uncertain-severity deviation requires explicit human owner direction before normal mutation resumes. Uncertain severity MUST fail closed at the higher plausible boundary until evidence resolves it.

The deviation does not create a sixth normal lifecycle state because it interrupts and governs recovery from the state machine rather than representing a normal delivery meaning.

## 8. Exceptional hotfix/bootstrap/direct-main actions

Exceptional actions use the same five-state semantic model. They MUST NOT create a parallel fast-path lifecycle.

The normal immutable-candidate path remains preferred.

When a genuine authorised exceptional action cannot expose a separate immutable candidate before the change becomes effective, CANDIDATE_QUALIFIED MAY bind an **exception package** only if all of these are durable before actuation:

```text
exact repository
governing contract
exact pre-action state
complete bounded proposed mutation/content
selected operation or tool class
exception rationale
proportionate pre-action assurance
known limitation: candidate becomes effective as it is created
```

IMPLEMENTATION_AUTHORITY MUST prospectively permit the exceptional implementation path.

CONSEQUENCE_AUTHORITY MUST prospectively authorise that exact exception package and named direct consequence.

OUTCOME_RECORDED MUST bind the resulting commit/object/state and all mandatory post-action verification.

The record MUST explicitly state that normal immutable-candidate / later-consequence separation was technically unavailable. It MUST NOT represent the exceptional path as semantically identical to the normal PR path.

Exceptional capability, administrator access or precedent MUST NOT imply standing exceptional authority.

If a pre-effective candidate can be constructed safely, the normal candidate/consequence separation MUST be used instead.

## 9. Private GitHub Free correctness boundary

The core protocol MUST work for a private repository on GitHub Free without requiring paid enforcement features for correctness.

Therefore none of these may be normative prerequisites:

```text
branch protection
rulesets
required status checks
required reviewers
protected environments
merge queues
GitHub Enterprise features
```

A repository MAY use such controls as optional mechanical hardening.

Protocol correctness means that an IssueOps-conforming path:

- reconstructs canonical state;
- enforces semantic predicates before its own actuation;
- requires prospective human authority where required;
- fails closed on ambiguity/currentness failure; and
- records actual outcome.

It does not claim that GitHub Free mechanically prevents every privileged/manual bypass outside that conforming path.

GitHub Actions MAY provide assurance evidence but MUST NOT be required merely to mirror lifecycle states. Existing checks, read-back, manual evidence or other proportionate assurance may be sufficient.

## 10. Fail-closed rules

Progression MUST stop when any decision-critical condition is:

```text
missing
inaccessible
partial in a way that blocks the decision
stale
ambiguous
contradictory
bound to a different candidate/state
unsupported by the available evidence
dependent on new human judgement or authority not yet supplied
```

Examples:

```text
candidate head changed
-> requalify affected candidate assurance/review

review applies to old materially changed state
-> not CANDIDATE_QUALIFIED

validation applies to old affected state
-> not current

implementation authority names old or materially different plan
-> changed implementation not authorised

consequence authority names old candidate
-> consequence not authorised

accepted evidence set is ambiguous
-> explicitly bind accepted evidence or obtain fresh authority

base drift materiality unknown
-> freshness UNKNOWN; stop

actuation may have reached target / authority consumption uncertain
-> treat consequence authority as consumed
-> reconstruct outcome truthfully
-> preserve prior attempt/outcome identity
-> re-enter at earliest affected lifecycle state
-> same unchanged candidate must re-establish CANDIDATE_QUALIFIED
-> fresh CONSEQUENCE_AUTHORITY before retry
-> no retry actuation directly from OUTCOME_RECORDED

outcome cannot be proven
-> OUTCOME = UNKNOWN, never assumed success
```

Absence of a visible blocker is not authority.

## 11. Proof A boundary and later proofs

This specification resolves the semantic choices needed before operational proof:

- exact five-state ownership;
- six invariant meanings;
- implementation and consequence authority separation;
- independent substantive review;
- exact-candidate assurance;
- material base-drift handling;
- consequence-authority evidence binding;
- outcome/verification completeness;
- execution-deviation interruption/resumption; and
- exceptional direct-main representation.

It deliberately does **not**:

```text
adopt v2 as stable
replace docs/issueops-protocol.md
define the full private-GitHub-Free operational profile
change workflows or repository settings
create an IssueOps execution engine
define deployment or credential transport
run dogfood or an external pilot
publish a release/tag
begin Proof B automatically
```

The next proof after accepted Proof A is separately governed:

```text
V2 PROOF B — PRIVATE_GITHUB_FREE_PROFILE
```

Proof A acceptance itself grants no Proof B implementation or consequence authority.
