# Modular IssueOps session architecture

Status: approved.

Record type: contemporaneous, adapted after portable-bootstrap proof.

Stage number: deliberately unassigned.

Authority: this roadmap approves only bounded decomposition and evidence-led pilots through separate execution contracts. It does not itself authorise session artefacts, pilot mutations, automation, repository-setting changes, lifecycle mutation, approval or merge.

## Executive recommendation

IssueOps should develop and test a small manual session architecture focused on invocation, role assignment, repository-state reconciliation and durable handover.

The proposition to test is:

> A new or resumed session can begin from a compact, explicit work grant, independently reconstruct current GitHub state, operate within one bounded role and leave a durable handover without duplicating the portable bootstrap, canonical protocol or repository-local execution contract.

The target Version 0.1 is:

```text
thin session grant
  -> repository-native state reconciliation
  -> role-specific work
  -> durable handover or evidence record
```

This is an adaptation of the originally approved roadmap. The earlier kernel, repository-profile, operating-mode, initiative-manifest and launcher model was reasonable before the portable bootstrap had been completed and proved. `IssueOps Bootstrap 0.1` now provides adopted owners for external entry, repository assessment, convention mapping, posture selection and the first-local-issue authority handoff. The canonical protocol and target repository continue to own execution after that handoff.

The remaining initiative must therefore add only what is still missing between sessions. It must not package the existing lifecycle into a second kernel or require copied repository facts in a mandatory profile.

## Adaptation basis

The completed [Portable IssueOps bootstrap and adoption](portable-issueops-bootstrap-and-adoption.md) initiative closed with **Adopt** after Level 3 fresh independent-agent proof in `8ft0-ai/mri-fourier-lab`.

That proof established that a fresh agent can begin from a pinned [bootstrap entry point](../../BOOTSTRAP.md), assess an unfamiliar repository without mutation, map local capabilities and conventions, select the lightest sufficient posture, create the first locally governed issue and then use the repository-local lifecycle for both bootstrap delivery and a subsequent genuine issue.

The completed bootstrap now owns:

- portable external entry and source identity;
- read-only repository assessment before local authority exists;
- capability and convention mapping;
- already-compatible, minimal-manual and stage-capable posture selection;
- the first-local-issue authority handoff;
- prohibited default mutations; and
- transition into the target repository's local IssueOps lifecycle.

The [IssueOps operating protocol](../../docs/issueops-protocol.md) and focused Reference documentation already own:

- execution-contract requirements;
- readiness and dependency decisions;
- implementation planning;
- issue-scoped branching;
- safe repository mutations;
- validation status and fallback rules;
- pull-request evidence;
- review, remediation and merge blockers;
- deviation handling; and
- human approval and merge authority.

The modular-session initiative must consume these owners. It must not restate them as a new `kernel.md`, duplicate repository-local facts in a mandatory profile or create a parallel manifest that competes with the GitHub issue.

## Problem statement

Large self-contained prompts have worked, but they repeatedly combine several responsibilities:

```text
invocation
+ protocol
+ repository facts
+ session role
+ initiative state
+ authority
+ completion rules
```

The bootstrap and canonical protocol now remove the need to carry the complete operating model in every prompt. A smaller operational problem remains:

- a new session needs an explicit role and authority boundary;
- a resumed session needs to know which durable records to inspect;
- an outgoing session needs a reviewable way to state what happened and what did not;
- a receiving session must detect stale, partial or untrusted handover claims;
- planning, delivery, review and close-out responsibilities must not overlap silently;
- repository changes between sessions must be discovered before action;
- duplicate work and conflicting branches must be avoided using GitHub-native state; and
- continuation must not depend on private chat history.

The initiative should solve these transition and responsibility problems without creating a second IssueOps operating model.

## Target users and situations

The design should support:

1. a repository owner starting a bounded planning, delivery, review or close-out session;
2. a fresh agent resuming work after a previous session stopped;
3. an independent reviewer operating without implementation reasoning;
4. a delivery session receiving an approved issue and current repository state;
5. a close-out session reconciling completed delivery without rewriting original intent; and
6. a session that must stop safely because authority, validation or current state cannot be established.

External adoption remains governed by `IssueOps Bootstrap 0.1`. The modular-session architecture begins only after the relevant repository, role and primary durable record can be identified.

## Outcome to prove

The initiative succeeds only if it demonstrates that a session can:

- begin from a compact session grant rather than a large duplicated protocol prompt;
- identify the exact repository, role, primary record and authority boundary;
- independently reconstruct current state from GitHub before mutation;
- distinguish completed, incomplete, stale and contradicted prior claims;
- resume from the earliest incomplete authorised gate without duplicate issues, branches or pull requests;
- operate within one non-overlapping role;
- preserve repository-local validation, review and human approval;
- leave a durable handover that another fresh session can verify;
- stop accurately when authority, evidence or current state is insufficient; and
- close with an evidence-backed `Adopt`, `Adapt` or `Reject` decision.

The outcome is not a prompt catalogue or orchestration platform. It is reliable, role-bounded movement between sessions.

## Design principles

### 1. GitHub state is authoritative

Issues, comments, branches, commits, pull requests, checks, reviews, repository instructions and planning records determine what has happened.

A launcher or handover may point to those records. It cannot override or replace them.

### 2. Use the bootstrap and protocol; do not repackage them

The portable bootstrap owns external assessment and local-authority handoff. The canonical protocol owns the local implementation lifecycle.

No second kernel is required for Version 0.1. A short role instruction may link to the canonical owners, but it must not copy their complete rules.

### 3. The issue remains the manifest

The planning or execution issue owns objective, scope, non-goals, acceptance, validation expectations and authority.

A separate initiative manifest is not required unless pilot evidence shows that the issue cannot provide a necessary, durable and discoverable field. Convenience alone is insufficient justification.

### 4. Discover repository facts rather than copy them

A session must inspect current repository instructions, workflows, templates, branch state, checks and merge policy.

A mandatory repository-profile file is not part of Version 0.1. A derived summary may be used as non-authoritative evidence when it reduces repeated inspection, but current repository state always wins.

### 5. One role per session

Each session receives one primary role. A session may report that another role is required, but it must not silently grant that role to itself.

### 6. Handover claims are untrusted until verified

A handover is a structured claim set and navigation aid. The receiving session must fetch the referenced objects, verify heads and statuses, inspect unresolved findings and reject or narrow stale instructions.

### 7. Manual proof before automation

Version 0.1 uses manually composed session grants and handovers. No generator, schema, workflow, service or coordinator is justified until manual pilots identify a specific repeated failure that cannot be solved proportionately.

### 8. Information has one canonical owner

The issue owns intent and authority. The branch owns implementation. The pull request owns changed scope and final-head evidence. Review records findings and decisions. A handover links these owners and records transition state; it does not duplicate their complete contents.

## Proposed architecture

### Thin session grant

A session grant supplies only the external facts needed to start the correct investigation.

Minimum fields:

```text
Repository: <owner/repository>
Role: <shape | deliver | review-or-evaluate | close-and-reconcile>
Primary record: <issue, pull request or planning record>
Authority: <permitted reads, comments and mutations>
Expected starting state: <branch, head, gate or explicit unknown>
Pinned external source: <optional immutable bootstrap or protocol source>
Stop boundary: <decision or condition that ends the session>
```

Example:

```text
Repository: 8ft0-ai/IssueOps
Role: review-or-evaluate
Primary record: PR #123
Authority: read current repository and post review findings only
Expected starting state: implementation complete; independently verify the exact head
Pinned external source: none; use repository-local instructions
Stop boundary: final review recommendation; do not merge
```

The session grant does not prove that the expected state is true. It identifies what must be verified.

### Repository-native state reconciliation

Before mutation, every role performs a bounded reconciliation appropriate to its primary record.

Required questions:

1. Does the exact repository and primary record exist?
2. What local instructions and authority rules apply?
3. Is the primary record open, closed, merged, superseded or otherwise complete?
4. Which branches, commits, pull requests, checks, reviews and dependencies currently exist?
5. Does the expected starting state match current GitHub state?
6. Which gate is the earliest incomplete authorised gate?
7. Would the proposed next action duplicate or conflict with existing work?
8. Has repository state changed in a way that invalidates the grant, handover, plan, validation, review or approval?

The session records one reconciliation outcome:

```text
ready at stated gate
ready at a different verified gate
already complete
blocked or clarification required
stale or contradictory handover
unauthorised for requested action
```

A mismatch is evidence. It must not be repaired by assuming the handover was probably correct.

### Session roles

#### Shape

Purpose:

- understand a problem;
- review evidence;
- compare options;
- define decisions, boundaries and proof; and
- recommend whether work should proceed.

May:

- read repository state;
- comment on the planning issue;
- prepare a roadmap or backlog proposal only when separately authorised.

Must not:

- implement product or repository changes;
- create execution issues, branches or pull requests without approved planning authority;
- represent a proposal as an approved execution contract.

#### Deliver

Purpose:

- implement one ready execution contract through the repository-local IssueOps lifecycle.

May:

- post readiness and implementation planning;
- create the approved issue-scoped branch;
- implement, validate, prepare the pull-request evidence pack and remediate in-scope findings.

Must not:

- invent missing intent;
- absorb another issue or future stage;
- approve or merge unless explicit bounded local authority separately permits it.

#### Review or evaluate

Purpose:

- independently compare current repository state with the governing contract or proof scenario.

May:

- inspect the exact final head, evidence, checks, comments and unresolved review state;
- post findings and one supported recommendation.

Must not:

- rely on implementation reasoning unavailable in durable records;
- remediate findings in the same independent review role;
- describe same-session self-review as independent evidence;
- continue into merge execution after its final recommendation; later human approval does not reopen or extend that reviewer model context;
- invoke merge from the same model conversation/context; merge execution occurs outside the independent reviewer session under separately established human authority.

#### Close and reconcile

Purpose:

- verify completed delivery, record intended versus actual outcomes, reconcile planning state and recommend `Adopt`, `Adapt` or `Reject` where required.

May:

- read merged state and post-merge evidence;
- update approved delivery and roadmap records through a separate execution contract;
- identify the next decision boundary.

Must not:

- rewrite original intent to match later discoveries;
- mark unavailable evidence complete;
- start the next initiative merely because the current one closed.

### Durable handover contract

Use a durable handover only when another session has a real continuation need. Do not create one merely to duplicate an already complete issue or pull request.

Minimum fields:

```text
Handover identity: <version or immutable comment/file reference>
Outgoing role: <role>
Primary record: <issue, pull request or planning record>
Repository state observed: <stable branch and commit>
Active branch or PR head: <exact ref and SHA, or none>
Completed work: <claims with durable links>
Incomplete work: <first incomplete gate and remaining checks>
Validation state: <completed, failing, pending, unavailable and post-merge>
Open findings or dependencies: <durable links and status>
Execution deviations: <none or durable records>
Next permitted action: <one bounded action>
Required authority: <owner, reviewer or merge decision>
Known stale-risk: <state that must be refreshed>
```

A handover must link to canonical owners rather than reproduce full issue, PR or validation content.

The receiving session must:

1. fetch the handover and primary record;
2. fetch the referenced branch, head, checks, reviews and dependencies;
3. compare current state with every action-relevant handover claim;
4. identify stale, missing or contradictory evidence;
5. record the verified starting gate; and
6. continue only within the new session grant.

### Ownership and state boundaries

| Concern | Authoritative owner | Session-layer responsibility |
| --- | --- | --- |
| External adoption method | `BOOTSTRAP.md` and `bootstrap/` | Point to a pinned source when required. |
| Repository conventions | Current target repository | Discover and cite; do not replace with a mandatory copied profile. |
| Intent, scope and authority | GitHub issue or approved planning record | Identify the primary record and verify it is current. |
| Implementation | Issue-scoped branch | Identify the exact branch and head. |
| Validation and changed scope | Pull request and checks | Verify final-head evidence and pending state. |
| Review findings and decision | Review records and threads | Link unresolved findings and preserve role separation. |
| Deviations | Active issue, PR and close-out record as applicable | Surface action-relevant deviations and stale evidence. |
| Approval and merge | Human or explicit bounded local delegation | Never infer authority from access or handover text. |
| Session transition | Durable handover comment or approved repository record | State verified transition facts without becoming a parallel lifecycle database. |

All authoritative operational state remains in GitHub. External databases, queues, local state stores and hidden coordination services are not required for correctness.

## Failure and change handling

### Session cannot complete its role

Record:

- the verified current state;
- the exact incomplete gate;
- what was attempted;
- why continuation is unsafe or unavailable;
- validation or evidence state;
- the next permitted action; and
- the authority required.

Do not broaden the role or manufacture completion.

### Validation is unavailable

Use the canonical validation-status and fallback rules. A handover must distinguish:

```text
completed
failing
pending local validation
pending environment-specific validation
post-merge verification
not performed or unavailable
```

A receiving session must not convert pending or unavailable evidence into passed evidence.

### Repository state changes between sessions

Refresh the safe starting point, branch head, checks, reviews, dependencies and approvals. Treat any affected plan, validation, review or approval as stale according to the canonical policy.

If the requested action is no longer valid, record a different verified gate or stop.

### Handover is stale, partial or contradictory

Do not repair it from chat history. Use current GitHub state and identify:

- which claim is stale or unsupported;
- which canonical record controls;
- whether work can continue at a narrower gate; and
- whether owner clarification is required.

### Duplicate or conflicting work exists

Check for an existing issue, branch and pull request before creation. If a valid object exists, resume or review it rather than creating a duplicate.

If two active branches or claims conflict, stop mutation until the authoritative execution contract and safe continuation path are clear.

### Execution deviation occurs

Apply the canonical execution-deviation policy. Handover records must identify any deviation that affects authority, scope, validation, review, approval or current state.

A receiving session must verify containment and resumption authority rather than trusting the word `resolved`.

## Prompt, process and documentation budgets

### Prompt budget

- session grants contain only start facts, role, authority and stop boundary;
- protocol text is linked, not copied;
- repository facts are discovered from current sources;
- handovers contain transition facts, not duplicated evidence packs.

A target of shorter prompts remains useful, but prompt length alone does not justify adoption.

### Process budget

Default pilot maximums:

```text
planning issues: 1
implementation issues for session artefacts: 2
pilot execution issues: use real work where separately authorised
canonical baseline evidence records: 1
canonical close-out evidence records: 1
temporary workflows: 0
repository-setting changes: 0
```

Any exception requires explicit evidence that the lighter structure cannot prove the outcome.

### Documentation budget

Version 0.1 should create only artefacts with one distinct tested need. Contract definition, examples and scorecard material should be consolidated where possible.

No dedicated top-level source area is approved by default. Source location must follow demonstrated ownership and the adopted documentation architecture.

## Repository ownership options

### Existing repository surfaces first

Potential owners include:

- a focused Reference page for exact session-grant and handover fields;
- a How-to guide for starting or resuming a session;
- repository-local issue comments or planning records for real handovers; and
- existing examples for non-normative illustrations.

This is the preferred starting hypothesis because it avoids a new operational source tree.

### Dedicated source area only after evidence

A dedicated `issueops/`, `.github/issueops/`, `prompts/` or similar area may be considered only if pilots prove that existing documentation and repository records cannot provide discoverable, non-conflicting ownership.

Filename symmetry or future automation is not sufficient justification.

## Target workflow or target state

```text
human or authorised coordinator identifies repository, role and primary record
  -> thin session grant starts a fresh session
  -> session loads repository-local instructions and canonical linked guidance
  -> session reconciles current GitHub state
  -> session records the verified starting gate
  -> role-specific work proceeds under repository-local authority
  -> canonical issue, branch, PR, review and validation records are updated
  -> session completes its role or records an accurate stop
  -> durable handover is created only when another session must continue
  -> receiving session independently verifies the handover
  -> human approval and merge authority remain explicit
  -> initiative closes with evidence-backed Adopt, Adapt or Reject
```

## Proposed Version 0.1 artefacts

Version 0.1 should prove the model with the smallest coherent manual material. Candidate capabilities are:

1. one compact normative definition of session-grant fields;
2. one compact normative definition of durable-handover fields and verification rules;
3. concise role boundaries for Shape, Deliver, Review or evaluate, and Close and reconcile;
4. one manually assembled example covering an interrupted and resumed session; and
5. one comparative pilot scorecard.

The implementation decomposition may consolidate these into fewer artefacts. It must not pre-commit to:

```text
kernel.md
repository-profile.md
initiative-manifest-template.md
a nine-file mode pack
a top-level issueops/ directory
```

The GitHub issue remains the manifest unless real pilot evidence demonstrates a missing capability.

## Pilot programme

Pilot work requires its own execution contract and must use real repository work where practical.

### Pilot A — Planning-only boundary

Purpose: prove that a Shape session recognises planning authority and stops before implementation.

Evidence:

- correct primary planning record identified;
- no implementation issue, branch or pull request created without approval;
- decisions requiring owner input are explicit;
- session ends at the authorised boundary.

### Pilot B — Interrupted delivery and fresh-session resume

Purpose: prove that a fresh Deliver session can verify a handover and continue from the earliest incomplete gate.

Method:

- stop a real bounded delivery after at least one durable object exists;
- create a durable handover under the outgoing role;
- start a fresh session with only the session grant, handover and repository access.

Evidence:

- exact current branch and PR head identified;
- zero duplicate issues, branches or pull requests;
- no repeated completed work;
- stale or changed state detected correctly;
- validation remains honestly classified;
- continuation succeeds or stops accurately.

Required evidence level: Level 3 fresh independent-agent walkthrough.

### Pilot C — Independent review role separation

Purpose: prove that a Review or evaluate session can inspect current evidence without implementation reasoning and does not remediate or merge under its review grant.

Evidence:

- exact contract and final head verified;
- unresolved comments and checks considered;
- self-review is not described as independent evidence;
- one supported review recommendation is recorded;
- no implementation or merge mutation occurs.

Required evidence level: Level 3 where independence is claimed.

### Pilot D — Bounded end-to-end handover

Purpose: prove that a real initiative can move through at least two different roles using durable GitHub records without hidden chat context.

Evidence:

- grants and handovers remain compact;
- each role begins with current-state reconciliation;
- authority boundaries do not overlap silently;
- no validation or approval gate is weakened;
- handover duplication remains lower than the standalone-prompt baseline; and
- close-out records intended versus actual delivery honestly.

This pilot must not manufacture repository work merely to exercise the architecture.

## Comparative scorecard

| Measure | Target direction |
| --- | --- |
| Duplicated protocol text | materially reduced |
| Duplicated repository facts | zero authoritative copies |
| Hidden chat context required | none |
| Duplicate issues, branches or PRs | zero |
| Fresh-session starting gate | correct on first attempt |
| Stale handover detection | all action-relevant mismatches surfaced |
| Role-boundary violations | zero |
| Unauthorised mutations | zero |
| Required validation | no loss |
| Scope drift | none material |
| Human interventions | no increase caused by modularisation |
| Handover size | limited to transition facts and links |
| Evidence description | matches actual evidence level |
| Final close-out | defensible Adopt, Adapt or Reject |

A shorter grant or handover that relies on hidden context, copies stale repository facts or weakens safeguards fails.

## Acceptance gates

- [ ] **Dependency clarity:** bootstrap, protocol and repository-local owners remain authoritative and are not duplicated.
- [ ] **Session-grant coherence:** a compact grant identifies repository, role, primary record, authority, expected state and stop boundary.
- [ ] **Role separation:** Shape, Deliver, Review or evaluate, and Close and reconcile have non-overlapping responsibilities.
- [ ] **State-reconciliation proof:** every pilot begins from current GitHub evidence rather than handover trust.
- [ ] **Handover verification proof:** a fresh session verifies an interrupted initiative without duplicate objects or repeated completed work.
- [ ] **Planning-boundary proof:** planning-only authority produces no implementation mutation.
- [ ] **Independent-review proof:** claimed independent review excludes implementation reasoning and remediation authority.
- [ ] **Failure honesty:** incomplete work, unavailable validation, stale evidence and changed state are represented accurately.
- [ ] **Authority preservation:** no automatic lifecycle transition, approval, merge, publication or external hidden state is introduced.
- [ ] **Comparative improvement:** repeated prompt and handover content decreases without loss of scope, validation or review quality.
- [ ] **Repository ownership clarity:** every new artefact has one distinct owner and no competing protocol role.
- [ ] **Real pilot evidence:** work is not manufactured merely to satisfy the experiment.

## Proposed implementation slices

### Slice 1 — Contract definition and source ownership

- preserve representative standalone prompts and completed handovers as baseline evidence;
- classify remaining instructions into session grant, role boundary, handover transition fact or removable duplication;
- map each proposed rule to bootstrap, protocol, repository-local or session-layer ownership;
- decide the smallest source locations under the adopted documentation architecture;
- create no pilot or operational automation.

### Slice 2 — Minimal manual Version 0.1 material

- create the smallest approved session-grant, role-boundary and handover guidance;
- consolidate artefacts where one owner is sufficient;
- include state-reconciliation and stale-handover checks;
- add no kernel, mandatory repository profile, separate manifest schema, generator or workflow;
- validate internal consistency and canonical links.

### Slice 3 — Role and resume pilots

- run separately authorised planning-boundary, interrupted-resume, independent-review and bounded handover pilots;
- use real work where practical;
- record one canonical evidence record per pilot or a justified consolidated record;
- adapt only through explicit findings.

### Slice 4 — Comparative close-out

- compare actual grants, handovers, interventions, artefact counts and outcomes with the baseline;
- document intended versus actual delivery;
- decide `Adopt`, `Adapt` or `Reject`;
- integrate into the recommended baseline only after `Adopt`;
- record the next decision boundary without creating speculative automation work.

Slices may be combined when doing so reduces ceremony without weakening reviewability or independent proof.

## Risks and controls

### Risk: recreating a second IssueOps protocol

Control: session material links to the bootstrap and canonical protocol and owns only role and transition responsibilities.

### Risk: a repository profile becomes stale authority

Control: Version 0.1 requires current repository discovery and does not require a mandatory profile. Any summary is explicitly derived and non-authoritative.

### Risk: the handover becomes a parallel state database

Control: handovers contain transition facts and links only. Issues, branches, pull requests, checks, reviews and planning records remain canonical.

### Risk: a separate manifest competes with the issue

Control: the issue remains the manifest unless pilot evidence proves a specific missing durable field.

### Risk: thin grants hide required context

Control: pilots begin with only the grant, durable records and repository access. Missing information is treated as a design failure or stop condition, not supplied from private chat memory.

### Risk: sessions grant themselves additional roles

Control: each grant names one role and authority. Role changes require a new explicit grant or repository-owner direction.

### Risk: stale handovers cause duplicate or unsafe work

Control: receiving sessions verify current object identity, heads, checks, reviews, dependencies and authority before mutation.

### Risk: simplification weakens validation or human authority

Control: compare final-head validation, review evidence, approval and merge boundaries with the current protocol baseline.

### Risk: pilots manufacture work

Control: use real bounded work where practical and permit an accurate stop when no suitable pilot exists.

### Risk: premature automation

Control: Version 0.1 is manual. Automation is a separately shaped future question only after an evidence-backed Adopt decision.

### Risk: collision with issue #90

Control: issue #90 remains independently governed. Shared evidence requires separate authority from both contexts and does not merge their outcomes.

## Definition of done

The initiative is complete when:

- [ ] this adapted roadmap has been reviewed and approved before implementation issues are created;
- [ ] approved implementation issues are complete or explicitly resolved;
- [ ] the minimal manual session architecture exists without duplicated protocol or repository authority;
- [ ] required pilots and comparative evidence are complete, or deviations are explicitly accepted;
- [ ] interrupted resume and independent review are proved at the required evidence level;
- [ ] no material scope, validation, handover or human-authority regression remains;
- [ ] prompt, process and documentation budgets are assessed against actual delivery;
- [ ] limitations, stale-state findings and deviations are recorded honestly;
- [ ] a completed delivery record separates intended from actual delivery;
- [ ] roadmap, delivery relationships and indexes are reconciled only where warranted; and
- [ ] a final `Adopt`, `Adapt` or `Reject` decision is recorded.

## Likely next decision boundary

If **Adopt**, separately decide whether evidence justifies:

- recommending standard session-grant and handover templates;
- adding repository template support;
- defining a lightweight machine-readable representation;
- creating a prompt assembler or validator;
- introducing a coordinator that issues bounded grants; or
- using the architecture alongside future operational evidence assistance.

Those are next-stage questions. They are not implementation authority for this roadmap.

## Approved planning decisions

- The initiative remains unnumbered and independently governed from issue #90.
- The portable bootstrap and canonical protocol are completed dependencies, not components to be duplicated.
- Version 0.1 focuses on session grants, current-state reconciliation, role boundaries and durable handovers.
- The GitHub issue remains the manifest unless pilot evidence proves a specific missing capability.
- A mandatory repository profile and second kernel are not part of Version 0.1.
- Initial roles are Shape, Deliver, Review or evaluate, and Close and reconcile.
- Every receiving session independently verifies action-relevant handover claims.
- Existing repository surfaces are preferred over a new top-level source area.
- The required proof set prioritises planning boundaries, interrupted resume, independent review and one real bounded handover journey.
- Level 3 fresh independent-agent evidence is required for interrupted resume and any claimed independent review.
- Existing prompts remain comparative evidence until an explicit Adopt decision supports replacement.
- Automation, schemas and hosted coordination remain outside Version 0.1.

## Operating and autonomy boundary

Issue #113 records the original planning decision. Issue #131 authorises this post-bootstrap roadmap adaptation only.

Future roadmap implementation requires separately reviewed execution contracts. Each pilot requires its own exact repository, primary record, role, authority, safe starting state, validation and stop boundary.

The session architecture does not grant target-repository mutation authority. Repository-local issues, instructions, validation rules, review requirements and human authority govern every mutation.

Human approval and merge authority remain explicit unless the repository owner separately grants bounded delegation after all readiness, validation, groundedness and merge-qualification gates pass.

## Non-goals

This roadmap does not authorise:

- a second IssueOps kernel or copied canonical protocol;
- a mandatory repository-profile file;
- a separate initiative-manifest schema;
- a fixed nine-file prompt pack;
- a top-level `issueops/` source area;
- automatic issue, branch, pull-request, review, merge or publication actions;
- automatic issue claiming or session allocation;
- a prompt generator, formal schema, GitHub Action, CLI, service, database, queue, GitHub App or hosted launcher;
- repository-setting, permission, required-check, branch-protection or merge-authority changes;
- wholesale migration or removal of existing prompts;
- implementation of issue #90;
- use of non-GitHub authoritative operational state; or
- presentation of same-session self-review as independent evidence.

The architecture is adopted only after the pilots and comparative close-out support an evidence-backed **Adopt** decision. Until then, the portable bootstrap, canonical protocol and existing invocation practices remain the operational baseline.
