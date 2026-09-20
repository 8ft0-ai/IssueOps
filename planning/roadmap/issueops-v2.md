# IssueOps v2 — minimal authority protocol proof programme

Status: completed.

Decision: **Reject**.

Record type: contemporaneous.

Approved for roadmap formalisation through issue [#212](https://github.com/8ft0-ai/IssueOps/issues/212), architecture review comment `5740096463`, owner roadmap-shaping authority `5740311763`, detailed roadmap-formalisation plan `5740321503`, and owner plan approval `5740326971`.

IssueOps `v0.3.0` remains the current stable protocol. “v2” is an architecture-generation name only; this roadmap does not declare a `v2.0.0` release or adopt v2 as stable.

## Problem statement

IssueOps `v0.3.0` has a strong human-governed execution-contract and exact-evidence model, but its operator-visible lifecycle is expressed as a comparatively large procedural sequence.

The accepted v2 architecture proposes that the same safety properties can be owned by six invariants:

```text
Intent
Identity
Authority
Assurance
Freshness
Outcome
```

and five semantic states:

```text
CONTRACT_READY
IMPLEMENTATION_AUTHORISED
CANDIDATE_QUALIFIED
CONSEQUENCE_AUTHORISED
OUTCOME_RECORDED
```

The programme question is:

> Can IssueOps prove that this five-state / six-invariant architecture preserves the current stable safety boundaries while materially reducing operator-visible machinery, and can it do so on a private GitHub Free repository without paid enforcement features?

Simplification is not treated as proven merely because the architecture has been accepted for proof.

## Outcome to prove

Produce enough durable evidence to decide whether the accepted #212 architecture should become the next stable IssueOps generation.

The proof must establish that:

1. the five states and six invariants cover the complete current stable kernel;
2. implementation authority and consequence authority remain prospective, human and separate;
3. substantive review remains independent and bound to the exact candidate;
4. assurance/currentness failures stop fail-closed;
5. execution-deviation recovery remains explicit and evidence-aware;
6. contract-required post-consequence verification cannot be bypassed by invocation success;
7. native GitHub records are sufficient canonical state/evidence without a parallel lifecycle store;
8. private GitHub Free is sufficient for protocol correctness without branch protection, rulesets, required reviews/checks, protected environments or merge queue;
9. the normal operator surface is materially smaller than `v0.3.0`; and
10. a genuine private-GitHub-Free proof succeeds before adoption.

The final programme decision is exactly one of:

```text
Adopt
Adapt
Reject
```

`Reject` is a valid evidence-backed completion outcome.

## Non-goals

This roadmap does not authorise or require:

- changing the current `v0.3.0` stable protocol merely because this roadmap is approved;
- publishing a release or tag;
- deciding the eventual release number before the adoption/versioning decision;
- automatic human judgement, authority, substantive review or risk acceptance;
- a generic shell or command execution capability;
- credential management;
- deployment transport;
- arbitrary live-system mutation;
- a central IssueOps service, queue or database;
- `issueops-state.json` or another canonical lifecycle manifest;
- paid GitHub plans or paid policy/enforcement features;
- Promptbook, Groundwork, Switchboard or another 8ft0 repository as a correctness dependency;
- workflow, ruleset, branch-protection, required-check or environment changes merely to support this programme;
- external-repository mutation without exact target-local authority;
- replacing current public operating documentation before a later adoption decision; or
- creating speculative follow-on implementation outside approved proof records.

## Operating and autonomy boundary

The programme remains governed by the current stable IssueOps protocol until a separately governed adoption/replacement decision changes that fact.

```text
approved v2 roadmap
  -> separately governed proof/decomposition records
  -> each proof record passes current stable IssueOps gates
  -> exact evidence
  -> independent substantive review where required
  -> comparative decision
  -> separate later adoption/protocol/release authority if warranted
```

Roadmap approval permits decomposition and shaping to begin. It does not self-authorise any child implementation, pilot, merge, repository-setting change, release or protocol replacement.

During proof, v2 dogfood is compatibility/shadow evidence unless a later separately governed record explicitly authorises a narrower experimental consequence.

Any external pilot repository retains its own authority. IssueOps roadmap or parent authority never transfers mutation authority into another repository.

## Target workflow or target state

The accepted semantic lifecycle is:

```text
CONTRACT_READY
  -> IMPLEMENTATION_AUTHORISED
  -> CANDIDATE_QUALIFIED
  -> CONSEQUENCE_AUTHORISED
  -> OUTCOME_RECORDED
```

with cross-cutting invariants:

```text
Intent
Identity
Authority
Assurance
Freshness
Outcome
```

The ordinary human authority surface should reduce to the two decisions that actually grant authority:

1. may this bounded proposed implementation path be executed?
2. may this exact qualified candidate perform the named consequence?

Other transitions may be mechanical only when their predicates are deterministic, exact, current, unambiguous, fail-closed and already covered by existing authority.

### Stable-kernel traceability

| Current stable-kernel distinction | v2 owner |
| --- | --- |
| bounded issue contract | `CONTRACT_READY` / Intent |
| current-state reconciliation | cross-cutting Identity + Freshness |
| explicit proposed implementation path | `IMPLEMENTATION_AUTHORISED` / Intent + Authority |
| durable prospective implementation authority | `IMPLEMENTATION_AUTHORISED` / Authority |
| bounded candidate implementation | transition to `CANDIDATE_QUALIFIED` / Intent + Identity |
| exact-candidate validation/evidence | `CANDIDATE_QUALIFIED` / Identity + Assurance + Freshness |
| independent substantive contract review | `CANDIDATE_QUALIFIED` / Assurance + Freshness |
| separate later merge/consequence authority | `CONSEQUENCE_AUTHORISED` / Authority |
| conditional post-consequence verification | `OUTCOME_RECORDED` / Outcome + Assurance |
| execution-deviation circuit breaker | cross-cutting protocol rule / Authority + Assurance + Freshness |

This table intentionally includes the post-consequence verification and execution-deviation rows omitted from the shorter mapping in the #212 architecture body and closes the non-blocking traceability finding from review comment `5740096463`.

## Acceptance gates

### Semantic and authority preservation

- [ ] All six invariants and five states are normatively specified.
- [ ] All ten stable-kernel distinctions in the traceability table remain preserved.
- [ ] Same-context authoring/remediation cannot satisfy independent substantive review.
- [ ] A changed candidate cannot reuse stale review, validation or consequence authority.
- [ ] Implementation authority remains prospective, durable and human.
- [ ] Consequence authority remains a separate later prospective human decision bound to the exact candidate and named consequence.
- [ ] Ambiguous evidence selection fails closed or requires explicit accepted evidence identities.

### Freshness, deviation and outcome

- [ ] Candidate/head/base/currentness rules are deterministic where possible and fail closed when materiality/currentness cannot be established.
- [ ] Execution deviations suspend normal progression, stop normal mutation, reconstruct authoritative state, stale affected evidence and use evidenced resumption semantics.
- [ ] The circuit breaker remains cross-cutting and does not become a sixth lifecycle state.
- [ ] `OUTCOME_RECORDED` is not equated with successful completion.
- [ ] Mandatory post-consequence verification remains mandatory whenever the governing contract declares it.

### Platform and evidence model

- [ ] The protocol works on a private GitHub Free repository without paid enforcement features.
- [ ] Paid controls remain optional hardening rather than correctness prerequisites.
- [ ] GitHub-native records remain canonical evidence/state.
- [ ] No mandatory parallel lifecycle database, state file, queue or generic execution engine is introduced.
- [ ] No other 8ft0 repository becomes a normative correctness dependency.
- [ ] Additional GitHub Actions use is proportional and no runner-heavy IssueOps lifecycle engine is required.

### Proof and simplification

- [ ] One real IssueOps dogfood proof completes without weakening `v0.3.0` authority.
- [ ] One genuine private-GitHub-Free external pilot completes under target-local authority.
- [ ] Representative stale/changed-candidate cases fail correctly.
- [ ] Operator-visible lifecycle concepts and required human authority decisions are measured against the current stable baseline.
- [ ] The resulting operating surface is materially smaller rather than merely renamed.
- [ ] A fresh substantive final comparison supports exactly `Adopt`, `Adapt` or `Reject`.

## Proposed implementation slices

The roadmap uses five conceptual proof slices. This roadmap does not create the child records; exact decomposition occurs only after roadmap approval is merged and separately governed.

### Slice 1 — Semantic specification and compatibility traceability

Specify and prove:

- the six invariants;
- five state predicates;
- exact identity semantics;
- minimum implementation-authority binding;
- candidate qualification;
- independent substantive review;
- consequence-authority binding;
- deterministic current requalification;
- freshness and base-drift fail-closed rules;
- outcome classifications;
- execution-deviation interruption/resumption; and
- direct-main/hotfix exceptional-path representation.

Resolve only the specification choices required before operational proof. Producing the specification does not itself change the stable protocol.

### Slice 2 — Private-GitHub-Free profile proof

Define and verify the exact minimum platform contract for a private GitHub Free repository.

The proof must distinguish:

```text
protocol correctness
from
optional mechanical hardening
```

and demonstrate that paid controls are not normative dependencies.

The profile should reuse repository validation where available and permit zero additional IssueOps-specific Action minutes where assurance can be established through existing checks, read-back or manual evidence.

### Slice 3 — IssueOps dogfood / compatibility proof

Exercise one real bounded IssueOps repository change against the v2 semantics while `v0.3.0` remains the governing stable protocol.

The proof must show that v2 can reconstruct the same authority/evidence outcome with fewer operator-visible lifecycle concepts without silently removing a stable boundary.

Include stale-candidate/currentness and independent-review behaviour where relevant.

### Slice 4 — Genuine private-Free external pilot

Prove one real bounded change in a private repository on GitHub Free with no paid enforcement assumed.

Before any target mutation, establish:

- exact target repository and safe base;
- target-local governing record and instructions;
- explicit target-local human authority;
- exact candidate identity;
- assurance/review expectations;
- consequence authority; and
- outcome/post-consequence evidence.

The pilot must test the v2 protocol itself rather than dependence on an 8ft0-specific orchestrator.

### Slice 5 — Comparative evidence and adoption decision

Compare v2 with the stable `v0.3.0` baseline.

At minimum compare:

- safety-property preservation;
- operator-visible lifecycle concepts;
- explicit human authority decisions;
- session/context handovers where reconstructable;
- evidence/currentness quality;
- stale-candidate rejection;
- independent-review preservation;
- execution-deviation handling;
- private-Free portability;
- additional GitHub Actions/minutes or other operational cost; and
- any new ambiguity or failure mode.

The final decision is exactly `Adopt`, `Adapt` or `Reject`.

That decision cannot publish a release or replace the stable protocol by itself.

## Risks and controls

### Risk: simplification only renames existing ceremony

Control: measure operator-visible concepts, decisions and handoffs and require material reduction while retaining all ten mapped safety distinctions.

### Risk: a safety property is silently deleted

Control: complete stable-kernel traceability is an acceptance gate. Any `LOST` or materially unsafe `AMBIGUOUS` mapping blocks adoption.

### Risk: paid GitHub features become hidden prerequisites

Control: private GitHub Free is the required proof profile; paid controls are optional hardening only.

### Risk: native evidence becomes a disguised parallel state store

Control: canonical state remains GitHub issues, comments, PRs, reviews, SHAs, checks/runs and outcome records. Derived summaries remain non-authoritative and recomputable.

### Risk: deterministic automation manufactures judgement or authority

Control: human implementation and consequence authority remain explicit and substantive review remains judgement-bearing and independent.

### Risk: dogfood changes the protocol before adoption

Control: `v0.3.0` remains governing during proof unless a separately governed experimental record explicitly says otherwise.

### Risk: an external pilot inherits IssueOps authority

Control: every target mutation requires target-local governing records and target-local human authority.

### Risk: v2 grows into an execution/deployment framework

Control: IssueOps owns protocol semantics only. Credential, host, deployment and generic execution transport remain outside the core.

## Definition of done

The original adoption-path completion gates below are preserved as the programme's documented intent. Because the programme reached an evidence-backed **Reject** decision at the mandatory compatibility boundary, the dogfood, external-pilot and later adoption-qualification gates became unnecessary for this rejected direction; they are intentionally not rewritten as passed.

The initiative is complete when:

- [ ] this roadmap is substantively reviewed, merged and indexed;
- [ ] each approved proof slice is complete or explicitly resolved under its own governed record;
- [ ] the complete stable-kernel mapping remains preserved;
- [ ] the private-GitHub-Free profile proof is complete;
- [ ] IssueOps dogfood evidence is complete;
- [ ] the genuine private-Free external pilot evidence is complete;
- [ ] limitations, negative evidence and execution deviations are recorded honestly;
- [ ] the comparative record reaches exactly `Adopt`, `Adapt` or `Reject`;
- [ ] a completed delivery record separates original intent from actual proof/delivery;
- [ ] the delivery log and graph are updated only where close-out rules require them; and
- [ ] any stable-protocol replacement, migration, release/version publication or follow-on implementation remains separately governed after the final decision.

## Close-out decision

The programme completed with an evidence-backed **Reject** decision.

The compatibility proof in issue [#218](https://github.com/8ft0-ai/IssueOps/issues/218) found a material C4 authority-semantic incompatibility against legitimate stable case #196. One bounded remediation cycle under issue [#219](https://github.com/8ft0-ai/IssueOps/issues/219) and PR [#220](https://github.com/8ft0-ai/IssueOps/pull/220) was implemented, reviewed and merged, but the fresh targeted re-proof recorded in comment `5752779607` still concluded `C4_NOT_COMPATIBLE`. Independent re-proof review `5752798842` approved that negative result, and owner close-out `5752832794` accepted it without rewriting historical evidence.

The owner then selected `REJECT_CURRENT_V2_DIRECTION` in issue [#221](https://github.com/8ft0-ai/IssueOps/issues/221), comment `5753118002`.

```text
Status: completed
Decision: Reject

stable protocol:
v0.3.0 retained

compatibility result:
C4_NOT_COMPATIBLE

historical #196:
legitimate stable-v0.3.0 behaviour
not compatible with the accepted v2 semantics

dogfood:
not required for rejected direction

external private-Free pilot:
not required for rejected direction

v2 adoption:
not authorised
```

Proof A and Proof B remain durable proof-programme artefacts and reusable design evidence. Their acceptance does not adopt the rejected architecture or replace the stable protocol. The unrun dogfood, external-pilot and later adoption-only proof requirements are not treated as passed; they became unnecessary once the owner accepted Reject as the programme outcome.

Any future IssueOps simplification effort requires a new separately governed architecture and roadmap rather than another semantic patch to this completed v2 lineage.

## Likely next decision boundary

After the proof programme, the repository owner should be able to answer:

> Does the evidence justify adopting the five-state / six-invariant architecture as the next stable IssueOps generation, adapting it through one bounded correction, or rejecting it in favour of the current stable model?

No release number, migration or stable-protocol replacement is implied before that decision and its own later authority.
