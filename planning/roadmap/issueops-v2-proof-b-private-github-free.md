# IssueOps v2 Proof B — private GitHub Free operating profile

Status: delivering.

Record type: contemporaneous.

Governing execution contract: [#216](https://github.com/8ft0-ai/IssueOps/issues/216).

Parent architecture and proof programme: [#212](https://github.com/8ft0-ai/IssueOps/issues/212), [IssueOps v2 — minimal authority protocol proof programme](issueops-v2.md), and [IssueOps v2 Proof A — normative semantic specification](issueops-v2-proof-a-semantics.md).

IssueOps `v0.3.0` remains the current stable protocol. This Proof B record defines the minimum private-GitHub-Free operating profile for the already accepted Proof A semantics. It does not replace current operating guidance, change repository enforcement, begin dogfood or an external pilot, or adopt v2 as stable.

## Problem statement

Proof A establishes the normative IssueOps v2 semantics, but it deliberately stops before defining the concrete minimum platform/evidence profile needed to realise those semantics on a private GitHub Free repository.

The portability requirement is stronger than merely showing that the current IssueOps repository can execute the flow. Current IssueOps is public and currently has repository-specific ruleset hardening. A private GitHub Free proof profile must remain correct even when paid or public-repository-only enforcement surfaces are unavailable.

The question for Proof B is therefore:

> What is the minimum private-GitHub-Free capability and evidence model that can realise the accepted five-state / six-invariant semantics faithfully, while keeping platform enforcement optional?

The core distinction is:

```text
PROTOCOL CORRECTNESS
!=
PLATFORM ENFORCEMENT
```

## Outcome to prove

Prove that the accepted IssueOps v2 semantics can be realised on a private GitHub Free repository using ordinary GitHub-native records and exact-state checks, without requiring paid enforcement features for correctness.

The profile must show that:

1. bounded intent can be durably represented;
2. implementation authority can be prospective and durable;
3. an exact candidate can be identified without branch protection;
4. assurance can be proportional and exact-candidate-bound;
5. independent substantive review remains a semantic requirement even when GitHub does not enforce required reviewers;
6. freshness/currentness can be re-established immediately before consequence;
7. consequence authority can remain a separate later human decision;
8. actual outcomes and required post-consequence verification can be recorded truthfully;
9. execution deviations still stop normal progression and stale affected evidence; and
10. optional paid enforcement can strengthen the path without becoming a hidden correctness dependency.

## Non-goals

Proof B does not:

- adopt v2 as the stable IssueOps protocol;
- replace `docs/issueops-protocol.md` or current stable guidance;
- change the Proof A state machine, authority model, retry semantics or exceptional-path semantics;
- change workflows, repository settings, rulesets, branch protection, required checks/reviewers or environments;
- create an IssueOps-specific lifecycle workflow merely to mirror semantic states;
- require GitHub Actions when assurance can be established without it;
- create a lifecycle database, state manifest, queue or central service;
- create a generic execution engine;
- begin Proof C / IssueOps dogfood;
- run the genuine private-Free external pilot;
- mutate another repository;
- introduce Promptbook or Groundwork as correctness dependencies;
- publish a release/tag; or
- claim that GitHub Free mechanically prevents every privileged/manual bypass.

## Operating and autonomy boundary

The current stable IssueOps protocol governs implementation, validation, review and any later merge of this Proof B record.

Proof B classifies controls into exactly three categories:

```text
NORMATIVE SEMANTIC REQUIREMENT
MINIMUM PRIVATE-FREE EVIDENCE MECHANISM
OPTIONAL GITHUB ENFORCEMENT
```

A **normative semantic requirement** is owned by Proof A and cannot be removed by platform limitations.

A **minimum private-Free evidence mechanism** is a GitHub-native record or exact observation sufficient to prove the semantic predicate without paid enforcement.

**Optional GitHub enforcement** may mechanically block non-conforming actions, but its absence does not weaken the semantic requirement. Where optional enforcement is unavailable, the IssueOps-conforming execution path must perform the equivalent precondition checks itself and fail closed.

No workflow, role, connector, technical capability, repository write permission or successful command may manufacture human authority.

IssueOps assurance applies to actions executed through a conforming IssueOps path:

```text
manual technical ability to bypass IssueOps
!=
IssueOps authority to bypass IssueOps
```

A direct/manual mutation outside that path is outside the assured lifecycle unless it was prospectively authorised as an exceptional action or reconciled through the execution-deviation process.

## Target workflow or target state

The profile realises exactly the Proof A lifecycle:

```text
CONTRACT_READY
  -> IMPLEMENTATION_AUTHORISED
  -> CANDIDATE_QUALIFIED
  -> CONSEQUENCE_AUTHORISED
  -> OUTCOME_RECORDED
```

owned by:

```text
Intent
Identity
Authority
Assurance
Freshness
Outcome
```

The ordinary minimum operating path is:

```text
CONTRACT_READY
  durable bounded issue or equivalent repository-native governing record
  + current dependency / action-relevant state

IMPLEMENTATION_AUTHORISED
  sufficient proposed execution path
  + prospective durable human implementation authority

CANDIDATE_QUALIFIED
  PR + exact head SHA
  + proportionate exact-candidate assurance
  + current independent substantive review
  + no unresolved material blocker

CONSEQUENCE_AUTHORISED
  exact qualified candidate
  + named consequence
  + later prospective durable human authority
  + immediate deterministic current requalification

OUTCOME_RECORDED
  actual consequence-attempt/result identity
  + resulting object/state
  + contract-required post-consequence verification status
```

This is a semantic profile, not a requirement to recreate the current twelve-step stable presentation.

### Minimum private-GitHub-Free profile matrix

| v2 semantic property | Minimum private-GitHub-Free capability | Required durable evidence | Fail-closed condition | Optional stronger GitHub enforcement |
| --- | --- | --- | --- | --- |
| **Intent** | Issues and issue comments, or an equivalent durable repository-native governing record | Bounded outcome, scope/non-goals, success/evidence expectations and governing-record identity | Governing intent is missing, inaccessible, contradictory or materially ambiguous | Issue forms, Projects policy or repository conventions |
| **Identity** | Repository metadata, issue/PR objects, commits/SHAs and canonical GitHub object identities | Exact repository/object identity, governing record, candidate head SHA, material base SHA when relevant, review/check/authority/outcome identities | Exact state cannot be established or mutable locator is being used where immutable identity is required | Rules that restrict branch movement or destructive ref operations |
| **Implementation Authority** | Durable issue/PR comment or equivalent GitHub-native human record | Proposed execution-path identity plus prospective human approval tied to the current contract/path and preceding implementation mutation | Approval absent, retrospective, ambiguous, stale or bound to a materially different path | None required; organisation policy may add approval tooling |
| **Candidate** | Pull request plus commit history | Exact repository + PR + exact head SHA; material base identity when decision-relevant | PR/head cannot be established exactly or head changed without requalification | Branch protection, rulesets, required PR path |
| **Assurance** | Commit/PR read-back, diffs, tests, static/manual evidence and optional workflow/check records | Change-appropriate evidence tied to the exact candidate and truthfully classified | Required assurance is missing, failing, stale, inaccessible or applies to another state | Required status checks, merge queue or policy-enforced CI |
| **Independent Review** | Durable PR review or PR-native review record | Exact candidate/head reviewed, substantive conclusion, independent review context and currentness | Review is self-review/remediation context, stale, materially contradicted or not bound to the exact candidate | Required reviewers, CODEOWNERS enforcement, branch-protection review rules |
| **Freshness** | Read access to action-relevant current GitHub state | Immediate pre-action re-fetch of candidate, base/dependencies, assurance, review, authority, target and material blockers | Any decision-critical fact is stale, ambiguous, partial, contradictory or inaccessible | Dismiss-stale-review policies, required up-to-date branch, merge queue |
| **Consequence Authority** | Durable owner/human GitHub-native record plus current-state reads | Exact repository, governing contract, exact candidate/state, named consequence, prospective human authority and immediate requalification; explicit evidence IDs when accepted evidence is ambiguous | Authority names old state/consequence, accepted evidence is ambiguous, or currentness cannot be proved | Protected branches, required reviews/checks, environment approval for separately governed deployment consequences |
| **Outcome** | PR/merge/result object reads and durable issue/PR records | Attempt identity, authorised consequence identity, actual result classification, resulting commit/object/state | Result cannot be observed confidently or invocation success is being substituted for actual outcome | Merge queue/result automation, deployment status policy |
| **Post-consequence Verification** | Read access to the resulting repository/object/environment state relevant to the contract | Named verification requirement, exact observed resulting identity and PASS/FAIL/PENDING/UNAVAILABLE/UNKNOWN status as applicable | Contract-required verification is absent or falsely represented as complete | Environments, deployment protection, required deployment checks |
| **Execution Deviation** | Durable issue/PR comments plus repository-state reads | Deviation facts, containment, resulting-state verification, stale-evidence classification, corrective control and required resumption authority | Normal writes continue while authoritative state, scope, authority or evidence is uncertain | Rulesets/protection may reduce some mutation paths but do not replace the circuit breaker |
| **Exceptional Path** | Durable governing/authority records and exact pre/post action state | Exact exception package from Proof A, prospective implementation and consequence authority, proportionate assurance, resulting identity and post-action verification | Normal immutable candidate was available but bypassed without authority, exception package incomplete, or resulting state uncertain | Administrator/hotfix controls or protected-branch bypass policies |

### Platform capability boundary

Current GitHub documentation confirms the intended minimum boundary:

- GitHub Free supports unlimited private repositories with a limited private-repository feature set. See [About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories).
- Protected branches are available for public repositories on GitHub Free, while private-repository protected branches require GitHub Pro, Team, Enterprise Cloud or Enterprise Server. See [Managing protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches).
- Repository rulesets are available for public repositories on GitHub Free, while private-repository rulesets require GitHub Pro, Team or Enterprise Cloud. See [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).
- Environments and their private-repository access/protection are not a GitHub Free private-repository baseline. See [Managing environments for deployment](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments).
- GitHub Actions is available across GitHub products; private repositories receive plan-dependent included minutes/storage and may incur usage charges beyond that allowance. See [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions).

Therefore none of these may be normative Proof B correctness prerequisites:

```text
branch protection
rulesets
required status checks
required reviewers
protected environments
merge queue
Enterprise-only policy controls
```

GitHub Actions MAY provide assurance evidence, but the profile does not require an IssueOps-specific hosted-runner workflow. A repository whose change can be qualified through existing validation, read-back, diff/static inspection and appropriate manual evidence may require zero additional IssueOps-specific Action minutes.

### Current IssueOps hardening is not the minimum profile

Current IssueOps is a **public** repository. Repository-native observation during Proof B readiness found these active `main` rulesets:

```text
ruleset 18527731 — main
  deletion protection
  non-fast-forward protection
  no bypass actors

ruleset 20885188 — main-pr-required
  pull-request rule
  required approving review count: 0
  owner bypass present
```

These controls are repository-specific hardening only. They do not prove the private-GitHub-Free baseline and are not required by this profile.

The connected GitHub integration could not read the branch-protection endpoint because that endpoint required repository Administration(read) capability unavailable to the integration. Proof B therefore records branch-protection configuration as:

```text
NOT_OBSERVED
```

It does not infer that branch protection is absent.

### Intent and governing record

The minimum normal representation is:

```text
GitHub issue
+ durable issue comments where clarification or later authority is required
```

An equivalent repository-native governing record MAY replace the issue only when it provides the same durable bounded intent, identity and reviewability.

Projects, issue forms and paid project features are not required.

### Exact identity

The profile separates immutable decision identity from mutable navigation:

- repository identity: the canonical GitHub repository object; use its stable repository identifier when exposed and retain `owner/name` as the current human-readable locator;
- governing issue/record: repository-local issue/record identity;
- candidate: exact commit SHA, normally reached through one PR;
- base: exact base commit SHA when base state materially affects correctness, merge result or review;
- assurance: exact workflow/check/run identity where such evidence is used, or exact durable manual/read-back evidence record;
- review: review/PR record identity plus exact candidate/head assessed;
- authority: durable issue/PR comment or equivalent record identity;
- attempt: durable consequence-attempt identity when more than one attempt can occur; and
- outcome: exact merge/resulting commit or other resulting object identity.

A branch name, PR number without its current head, label, workflow name or moving default branch is not sufficient exact identity when the decision requires exact state.

### Implementation authority

The minimum normal representation is:

```text
governing issue/record
+ sufficient proposed execution-path record
+ later durable human approval of that path
```

The authority must be prospective and precede implementation mutation.

The plan may be compact for low-risk work, but material choices, exclusions, validation and consequence boundaries must remain visible when they matter.

No `issueops-state.json`, authority database or external lifecycle control plane is introduced.

### Candidate

The preferred normal candidate representation is:

```text
exact repository
PR number/object
exact head SHA
```

The PR is the primary evidence container. A branch name may locate work but does not qualify the candidate.

Branch protection is optional hardening and is not required to establish exact candidate identity.

### Assurance

Assurance is selected proportionately to the change and may include:

```text
existing workflow/check run identities and results
repository-native test/build/lint results
changed-file read-back
base-to-head diff and scope comparison
static inspection
manual or representative verification
other durable exact-candidate evidence
```

When GitHub Actions is used:

```text
workflow/check result
= assurance evidence

required-status-check enforcement
= optional GitHub enforcement
```

No check may be represented as complete unless it actually ran or its durable evidence actually exists for the decision-relevant state.

### Independent substantive review

Independent substantive review remains **HUMAN JUDGEMENT** under Proof A.

The minimum durable record must:

- identify the exact candidate/head reviewed;
- record a substantive contract/scope/evidence conclusion;
- come from a genuinely independent Review/evaluate context that did not author or remediate that candidate in the same context;
- remain current for the exact candidate; and
- become stale to the extent later changes invalidate its conclusion.

A formal GitHub `APPROVED` state is useful when available but is not the semantic requirement. Conversely, a review-shaped record is not sufficient merely because it exists.

Private GitHub Free does not need required-review enforcement to preserve the semantic review boundary.

### Freshness

Freshness is derived from canonical records; it is not stored as an independent state object.

Immediately before a consequence, the conforming executor must re-fetch and establish current:

```text
repository / target identity
governing contract
candidate exact head/state
material base and dependencies
accepted assurance
independent review
consequence-authority record
named consequence
unresolved material finding state
execution-deviation / resumption state
```

If evidence is missing, partial, stale, ambiguous, contradictory or inaccessible in a way that blocks the decision, progression stops.

Candidate-head change always requires requalification of affected assurance/review/currentness. Material base/dependency change requires requalification. Unknown materiality fails closed.

### Consequence authority

The minimum binding remains exactly the Proof A rule:

```text
exact repository
+ governing contract
+ exact candidate/state
+ named consequence
+ prospective durable human consequence authority
+ immediate deterministic current requalification
```

This minimum is sufficient only when canonical records select one complete accepted assurance/review set unambiguously.

If accepted evidence identity is ambiguous, incomplete or multiply selectable:

```text
authority MUST explicitly bind the accepted evidence identities
OR
the ambiguity MUST be resolved and fresh human consequence authority obtained
```

Repository write permission and the technical ability to invoke Merge are capability, not authority.

### Outcome and consequence-attempt identity

A merge consequence records, as applicable:

```text
attempt identity
authorised PR/head/consequence
merge attempted/completed state
resulting commit identity
current PR/repository state
EXPECTED / FAILED / PARTIAL / UNKNOWN classification
post-consequence verification obligation and status
```

Successful invocation alone does not establish successful completion.

Proof A retry semantics remain unchanged:

- a possibly-effective actuation consumes consequence authority;
- uncertain authority consumption fails closed as consumed;
- each possibly-effective attempt receives its own durable outcome evidence;
- prior attempt/outcome evidence is preserved;
- retry cannot actuate directly from `OUTCOME_RECORDED`;
- an unchanged candidate must re-establish `CANDIDATE_QUALIFIED`, then obtain fresh prospective `CONSEQUENCE_AUTHORITY` before another possibly-effective actuation; and
- only positively proven pre-actuation/no-effect failure may retain unconsumed authority, subject to immediate deterministic requalification.

### Post-consequence verification

When the governing contract declares post-consequence verification mandatory, the profile requires a durable observation of the named resulting state/object tied to its exact identity.

Verification may truthfully be:

```text
PASS
FAIL
PENDING
UNAVAILABLE
UNKNOWN
```

A pending, failed, unavailable or unknown check cannot be collapsed into successful completion.

Protected environments or deployment gates may harden a separately governed deployment path but are not required merely to represent the verification obligation.

### Execution-deviation circuit breaker

The Proof A circuit breaker remains fully effective without paid enforcement:

```text
unexpected/unintended mutation or material uncertainty
-> stop normal writes
-> permit only read-only investigation and minimum authorised containment/remediation
-> reconstruct authoritative state
-> stale affected Authority / Assurance / Freshness evidence
-> record deviation and resumption evidence where required
-> resume only under the required evidenced resumption authority
```

Rulesets, protected branches and required checks may reduce some accidental mutation paths, but they do not replace the circuit breaker.

### Exceptional path

A legitimate hotfix/bootstrap/direct-main exception uses the same five-state semantics.

When a separate pre-effective immutable candidate is genuinely unavailable, the Proof A exception package remains required:

```text
exact repository
governing contract
exact pre-action state
complete bounded proposed mutation/content
selected operation/tool class
exception rationale
proportionate pre-action assurance
known limitation: candidate becomes effective as it is created
```

Implementation authority and consequence authority remain prospective and action-specific. The resulting commit/object/state and mandatory post-action verification are recorded.

Exceptional capability, administrator access or precedent never creates standing exceptional authority.

### Native evidence reference composition

The following is an example evidence composition, not a new mandatory manifest or schema:

```text
Contract:
  issue #N

Implementation authority:
  issue comment <id>

Candidate:
  PR #M
  head <sha>

Assurance:
  run/check <id> / result, if used
  read-back / diff / manual evidence as applicable

Independent review:
  review or durable PR record <id>
  applies to <sha>

Consequence authority:
  durable owner record <id>
  binds exact candidate / consequence

Outcome:
  attempt <identity>
  resulting commit/object <identity>
  EXPECTED / FAILED / PARTIAL / UNKNOWN

Post-consequence verification:
  durable exact-state observation / status
```

The canonical state remains the native GitHub records themselves.

### Proof A stable-kernel preservation check

| Stable-kernel property | Private-Free profile preservation |
| --- | --- |
| bounded issue contract | Durable issue or equivalent governing record under Intent |
| current-state reconciliation | Immediate canonical reads under Identity + Freshness |
| explicit proposed implementation path | Durable path record before implementation authority |
| durable human implementation authority | Prospective durable owner/human GitHub-native record |
| bounded candidate implementation | PR + exact head plus contract/scope fidelity |
| exact-candidate validation/evidence | Proportionate exact-candidate assurance; Actions optional |
| substantive contract review | Exact-candidate independent human review; required-review enforcement optional |
| separate human merge/consequence authority | Later prospective durable authority using Proof A binding |
| post-consequence verification | Contract-derived obligation recorded under Outcome + Assurance |
| execution-deviation circuit breaker | Protocol-level stop/reconstruct/stale/resume behaviour independent of paid enforcement |

No Proof A stable-kernel property is intentionally removed by the private-Free profile.

## Acceptance gates

- [ ] The profile faithfully realises the accepted Proof A semantics without semantic redesign.
- [ ] All six invariants are represented.
- [ ] All five semantic states are represented.
- [ ] All ten Proof A stable-kernel properties remain preserved.
- [ ] The required 12-row profile matrix is complete.
- [ ] Private GitHub Free compatibility is explicit.
- [ ] No paid GitHub feature is normative for correctness.
- [ ] Evidence and enforcement are distinguished consistently.
- [ ] GitHub Actions is optional assurance infrastructure, not a mandatory lifecycle engine.
- [ ] Independent substantive review remains semantic, independent, exact-candidate-bound and stale-on-change.
- [ ] Implementation and consequence authority remain prospective, human and separate.
- [ ] Consequence-authority ambiguity uses the Proof A explicit-binding/fresh-authority fallback.
- [ ] Immediate pre-action currentness/requalification is explicit.
- [ ] Outcome and contract-required post-consequence verification remain truthful.
- [ ] Proof A authority-consumption/retry semantics remain unchanged.
- [ ] Execution-deviation circuit breaker remains effective without paid enforcement.
- [ ] Exceptional path remains bounded and uses the same five-state model.
- [ ] Current IssueOps rulesets are classified only as repository-specific hardening.
- [ ] Unobservable branch-protection state is recorded as `NOT_OBSERVED`, not inferred.
- [ ] No mandatory parallel state store, generic execution engine, new workflow/settings mutation or later-proof work is introduced.
- [ ] One exact final candidate is validated and ready for completely fresh independent substantive private-GitHub-Free profile review.

## Proposed implementation slices

Proof B is intentionally one bounded profile/specification slice:

```text
private-GitHub-Free profile
  -> exact-head repository validation
  -> completely fresh independent substantive profile review
  -> separate consequence authority if accepted
```

No Proof C/dogfood, external pilot or adoption work is part of this slice.

## Risks and controls

### Risk: current IssueOps hardening is mistaken for the portable minimum

Control: current IssueOps is explicitly identified as public; its observed rulesets are classified as repository-specific hardening only, and inaccessible branch-protection state is `NOT_OBSERVED`.

### Risk: paid GitHub features become hidden correctness dependencies

Control: the profile matrix separates semantic requirements, minimum evidence mechanisms and optional enforcement. Private rulesets/protected branches/environments are excluded from the minimum profile.

### Risk: a missing enforcement feature weakens authority semantics

Control: human implementation and consequence authority remain durable semantic predicates. The conforming executor revalidates exact current state before actuation and fails closed when proof is incomplete.

### Risk: CI becomes a lifecycle engine

Control: Actions is optional assurance evidence. No IssueOps-specific state-mirroring workflow is required, and zero additional IssueOps-specific Action minutes is a valid posture when other assurance is sufficient.

### Risk: independent review is reduced to a GitHub setting

Control: independence remains a substantive human-judgement property. Required-review enforcement may harden the path but cannot substitute for semantic independence.

### Risk: direct/manual capability is treated as protocol authority

Control: the profile states explicitly that technical bypass capability is not IssueOps authority; non-conforming direct mutation is outside the assured lifecycle unless prospectively exceptional or reconciled as a deviation.

### Risk: profile work invents new v2 semantics

Control: Proof A is normative. Any profile conflict with Proof A is a Proof B defect, not authority to redesign the semantic model.

## Definition of done

Proof B is complete only when:

- [ ] the profile satisfies every acceptance gate above;
- [ ] platform capability claims are refreshed against authoritative GitHub documentation;
- [ ] repository-native planning/documentation validation is successful against the exact candidate where applicable;
- [ ] base-to-head scope remains exactly within the approved Proof B paths;
- [ ] a completely fresh independent substantive private-GitHub-Free profile review accepts the exact candidate;
- [ ] any remediation is revalidated and freshly reviewed as required;
- [ ] any eventual merge occurs only under separate later human consequence authority;
- [ ] merged-state read-back records the actual outcome truthfully; and
- [ ] completion does not automatically begin Proof C, the external pilot or v2 adoption.

## Likely next decision boundary

If Proof B is accepted, the next separately governed roadmap question is whether to begin the IssueOps dogfood / compatibility proof:

```text
V2 PROOF C — ISSUEOPS_DOGFOOD_COMPATIBILITY
```

Proof B acceptance supplies a platform/evidence profile to later proofs. It does not itself authorise dogfood, external pilot activity, stable-protocol replacement, migration, release or adoption.
