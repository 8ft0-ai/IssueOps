# Modular IssueOps session architecture

Status: approved.

Record type: contemporaneous.

Stage number: deliberately unassigned.

Authority: this roadmap approves only bounded decomposition and evidence-led pilots through separate execution contracts. It does not itself authorise modular prompt artefacts, automation, repository-setting changes, lifecycle mutation, approval or merge.

## Executive recommendation

IssueOps should develop and test a modular session architecture, but only as a manually assembled and evidence-tested Version 0.1. The initiative should not begin by creating a prompt generator, schema, workflow or second protocol.

The proposition to test is:

> A new or resumed session can reliably apply IssueOps through a stable kernel, a repository profile, one operating mode and a small initiative manifest, while using a much thinner launcher prompt and preserving the existing human-controlled execution contract.

The initiative is an approved cross-cutting roadmap because it changes how agents enter and apply the operating model, requires dependent design and pilot work, and needs an explicit evidence-based adoption decision. It remains deliberately unnumbered and independently governed from issue #90.

## Problem statement

The current large prompts have worked well. They have produced bounded issues, reviewable PRs, strong validation and defensible close-out decisions. The problem is not that the controls are wrong; it is that the controls are repeatedly embedded in each initiative prompt.

This creates several recurring weaknesses:

- the canonical IssueOps protocol is duplicated across prompts;
- prompts often read as clean-start instructions even when repository work is partially complete;
- review, planning, delivery and evaluation authority are mixed together;
- capability assumptions such as local checkout or native auto-merge are not always discovered first;
- the same evidence is repeated across issues, PRs and planning records;
- process and documentation volume can become disproportionate to the problem;
- representative self-review can be described too loosely as independent evaluation; and
- successful continuation depends too much on chat history rather than repository state.

The initiative should improve how IssueOps is invoked without creating a competing operating model.

## Target users and situations

The design should support:

1. a repository owner launching a new IssueOps review or delivery session;
2. an agent beginning work in an unfamiliar IssueOps-enabled repository;
3. a fresh session resuming an interrupted initiative;
4. a reviewer or evaluator operating without implementation context;
5. a repository adopting IssueOps while retaining its own validation and merge conventions; and
6. a bounded maintenance task that should not acquire unnecessary stage-level ceremony.

## Outcome to prove

The initiative succeeds only if it demonstrates that a session can:

- discover the repository's current authoritative state before creating anything;
- select the correct operating mode and delivery posture;
- find the local validation, branch, merge and authority rules;
- reconstruct an initiative from its GitHub issue and repository records rather than chat memory;
- resume from the first incomplete gate without duplicate issues, branches or PRs;
- preserve existing validation, review and human approval boundaries;
- use proportionate issue and evidence machinery;
- distinguish structural, representative, independent-agent and human evidence honestly; and
- close with an evidence-backed Adopt, Adapt or Reject decision.

The outcome is not the creation of a prompt catalogue. The outcome is reliable, restartable and proportionate IssueOps operation.

## Design principles

### 1. Repository state is authoritative

A launcher prompt may identify the initiative and desired mode, but issues, PRs, branches, workflow results, repository instructions and planning records determine what has actually happened.

### 2. Inspect and resume before creating

Every mode begins by classifying the initiative as:

```text
not started
partially planned or delivered
delivery complete but not closed
fully complete
```

The session resumes from the earliest incomplete authoritative gate and must not recreate valid existing artefacts.

### 3. One protocol, several modes

The modular architecture must reference and apply the canonical IssueOps protocol. It must not restate a subtly different protocol in each mode.

### 4. The lightest sufficient process

The session must choose among:

```text
no remediation
bounded correction
remediation stage
```

A stage pack is justified by cross-cutting ownership, governance, dependent delivery or end-to-end proof—not simply by the existence of several observations.

### 5. Evidence is named according to how it was obtained

Structured self-review is not independent-agent evidence. A rendered page existing is not proof that an unfamiliar reader can complete a task.

### 6. Information has one canonical owner

The issue owns intent and acceptance criteria. The PR owns changed scope and final validation. A reader-evidence record owns detailed walkthrough results. A delivery record owns stage-level synthesis. Other surfaces link rather than reproduce the complete evidence.

### 7. Manual composition before automation

The architecture must be proved through manually assembled prompt modules before any generator, schema or workflow is considered.

## Proposed architecture

### IssueOps kernel

The kernel contains repository-agnostic invariants:

- repository-state reconciliation;
- issue readiness and dependency checks;
- implementation planning;
- one-issue branch discipline;
- safe tool-operation expectations;
- change-specific validation;
- draft PR and evidence-pack expectations;
- review-remediation and stale-head handling;
- groundedness review;
- merge qualification;
- post-merge reconciliation; and
- honest stop, skip and limitation reporting.

The kernel should be concise and point to canonical detailed documentation rather than embedding every template and example.

### Repository profile

The profile records local facts and conventions:

- canonical repository and stable branch;
- agent instruction entry points;
- branch naming and merge method;
- validation commands and required checks;
- documentation and planning ownership;
- repository capabilities such as auto-merge;
- connector or local-checkout limitations;
- protected paths and authority boundaries; and
- expected cleanup behaviour.

The profile should describe the repository, not redefine IssueOps.

### Operating modes

Version 0.1 should use four modes:

1. **Review** — gather evidence, test current outcomes and classify findings; no implementation.
2. **Plan** — compare options, select posture, define decisions and produce the minimum backlog; no implementation before approval.
3. **Deliver** — execute approved issue contracts sequentially through the canonical loop.
4. **Evaluate and close** — repeat defined proof, record limitations, reconcile state and recommend Adopt, Adapt or Reject.

Evaluation and close-out should remain combined initially to keep the module set small. They may be separated later only if pilots show a real authority or usability benefit.

### Initiative manifest

The manifest contains only initiative-specific facts:

```yaml
initiative:
  planning_issue: 113
  mode: plan
  objective: prove a modular IssueOps session architecture
  posture: undecided

boundaries:
  included: []
  excluded: []
  authority: planning-only

delivery:
  max_implementation_issues: 4
  merge_policy: capability-aware

evidence:
  required_level: independent-agent
  scenarios: []

completion:
  decision: adopt-adapt-reject
```

The syntax is illustrative. Version 0.1 does not require a machine-readable schema.

### Thin launcher

The target launcher should be close to:

```text
Resume the initiative defined by issue #113 in planning mode.

Use the repository's IssueOps kernel and repository profile.
Reconcile current state before creating anything.
Continue from the first incomplete authoritative gate.
```

The launcher identifies work. It does not carry the complete operating model.

## Why the existing large prompts are not required

IssueOps still requires an invocation mechanism. An unfamiliar agent must be told which issue or initiative to perform and which operating mode applies. What IssueOps does not require is a collection of large, self-contained prompts that each reproduce the complete protocol.

The current model combines several responsibilities:

```text
invocation
+ complete protocol
+ repository conventions
+ operating mode
+ authority
+ completion rules
```

The proposed model separates them:

```text
thin launcher
  -> canonical IssueOps kernel
  -> repository profile
  -> selected operating mode
  -> initiative manifest or issue contract
```

The repository record remains authoritative throughout. The issue bounds the work, the profile supplies local conventions, the selected mode defines the session's responsibility, the branch contains implementation and the pull request carries evidence. The prompt starts the operation; it is not the source of truth for what has happened.

This distinction allows IssueOps to support three operating models without changing the protocol:

| Operating model | Invocation |
| --- | --- |
| Human-operated | A person follows the canonical protocol directly. |
| Agent-assisted | A thin launcher tells an agent what IssueOps work to resume. |
| Coordinated | An optional future coordinator supplies a bounded work grant that identifies the issue, mode, profile and authority. |

Existing large prompts remain useful as design evidence and comparative baselines while Version 0.1 is tested. They are not required as permanent duplicated protocol owners. No operational copy should be removed until the modular approach demonstrates at least equivalent reliability and is explicitly adopted.

## Delivery-posture gate

### No remediation

Use when there is no material correctness defect, primary task failure, ownership decision or governance change.

Expected result: record the review and stop without manufacturing implementation work.

### Bounded correction

Use when:

- existing architecture and ownership remain valid;
- no new cross-cutting reader or operating journey is required;
- no repository-wide governance or validator change is required; and
- the work fits within approximately one to three implementation PRs.

Expected result: normal execution-contract issues without a stage pack.

### Remediation stage

Use when any of the following applies:

- information architecture or canonical ownership changes;
- a new cross-cutting operating journey is introduced;
- repository-wide validation or governance changes;
- several dependent delivery slices are required;
- real end-to-end proof is needed; or
- a formal adoption decision is required.

Historical or review-record issues should not inflate the implementation-issue count.

## Evidence model

### Level 1 — Structural evidence

Files, pages, links, routes, headings or required fields exist.

### Level 2 — Representative walkthrough

A constrained evaluator follows the documented path against current rendered or repository output using a defined starting point and without relying on unstated project context.

### Level 3 — Independent-agent walkthrough

A fresh session or separate evaluation agent completes the scenario without access to implementation reasoning or prior chat history.

### Level 4 — Observed human usability

A human unfamiliar with the implementation completes the scenario.

Version 0.1 adoption should require at least Level 3 evidence for the interrupted-resume pilot. Level 2 evidence may support lower-risk bounded pilots but must be labelled accurately.

Each scenario should record:

- persona;
- exact task;
- permitted starting point;
- information withheld;
- expected outcome;
- authority boundary;
- pages or records consulted;
- transitions and wrong turns;
- final result;
- unresolved questions; and
- evaluator confidence.

## Prompt, process and documentation budgets

### Prompt budget

- initiative launchers should be materially shorter than current standalone prompts;
- invariant protocol text should not be copied into manifests or modes;
- a module should exist only when it owns a distinct responsibility.

### Process budget

Default maximums for the pilot stage:

```text
planning issues: 1
implementation issues: 4
canonical baseline evidence records: 1
canonical close-out evidence records: 1
temporary workflows: 0
repository-setting changes: 0
```

Exceeding a default requires explicit justification based on dependency, risk, validation ownership or rollback value.

### Documentation budget

Every new guide or reference page must support a tested need. Before acceptance, check whether it can be shortened, combined with existing guidance or replaced with a canonical link or compact decision table.

## Repository ownership options

### Option A — Put all modules under `docs/`

Advantages:

- easy to publish and discover;
- fits the adopted documentation architecture.

Disadvantages:

- operational source artefacts may become confused with user-facing guidance;
- risks turning documentation pages into executable control sources.

Assessment: suitable for explanations and how-to material, not necessarily the canonical module source.

### Option B — Use only `AGENTS.md` and planning records

Advantages:

- no new top-level source area;
- strong repository visibility.

Disadvantages:

- `AGENTS.md` would become too large;
- reusable modes and templates would be fragmented;
- planning records should not become current operating instructions.

Assessment: insufficient as the complete architecture.

### Option C — Add a dedicated source area

Candidate names:

```text
issueops/
.github/issueops/
prompts/
agent/
```

Provisional preference: a neutral top-level `issueops/` source area, with user-facing guidance in `docs/`, concise entry rules in `AGENTS.md`, and delivery evidence in `planning/`.

This remains a planning recommendation, not an approved path. The Version 0.1 decomposition should test whether a new source area is genuinely necessary before authorising it.

## Target workflow

```text
human identifies initiative issue and operating mode
  -> thin launcher starts a session
  -> session loads kernel and repository profile
  -> session reconciles repository state
  -> session reads the initiative manifest from the issue
  -> session selects or confirms delivery posture
  -> mode-specific work proceeds
  -> repository-native evidence is recorded canonically
  -> independent or accurately labelled evaluation runs
  -> human retains approval and merge authority
  -> delivery closes with Adopt, Adapt or Reject
```

## Proposed Version 0.1 artefacts

The smallest useful manual pack should contain:

```text
kernel.md
repository-profile.md
modes/review.md
modes/plan.md
modes/deliver.md
modes/evaluate-close.md
initiative-manifest-template.md
reader-evidence-template.md
run-scorecard-template.md
```

The roadmap should permit consolidation if decomposition shows that fewer artefacts are clearer. No generator or formal schema is part of Version 0.1.

## Pilot programme

### Pilot A — Bounded correction

Purpose: prove that the architecture avoids stage-level ceremony for a small one- or two-PR change.

Evidence:

- correct bounded posture selected;
- no unnecessary roadmap or parent stage created;
- required validation and scope controls retained;
- launcher and manifest materially shorter than the equivalent standalone prompt.

### Pilot B — Multi-issue remediation stage

Purpose: prove that the modular model retains dependency handling, evidence quality and formal close-out for cross-cutting work.

Evidence:

- coherent backlog and dependency order;
- one-issue, one-branch, one-PR discipline;
- current-head validation;
- no weakened review or approval gate;
- completed delivery record and adoption decision.

### Pilot C — Interrupted and resumed delivery

Purpose: prove that a fresh session can reconstruct state without hidden chat context.

Method:

- stop a pilot after at least one authoritative artefact exists but before initiative completion;
- start a fresh session with only the launcher and repository access;
- require it to identify the current state and earliest incomplete gate.

Evidence:

- zero duplicate issues, branches or PRs;
- no repeated completed work;
- correct dependency and PR-head state;
- successful continuation or an accurate stop condition.

Required evidence level: Level 3 independent-agent walkthrough.

### Pilot D — Planning-only boundary

Purpose: prove that the architecture recognises an issue with no implementation authority.

A future use of #90 could be considered only if #90's own planning process permits it. This roadmap must not assume or authorise that use.

Evidence:

- no branch, PR or execution issue created;
- planning choices and authority boundaries correctly identified;
- the session stops at the required human decision.

## Comparative scorecard

For each pilot record:

| Measure | Target direction |
| --- | --- |
| Launcher and initiative prompt length | at least 40% shorter than comparable standalone prompt |
| Duplicate repository artefacts | zero |
| Fresh-session resume | correct on first attempt |
| Human interventions | no increase caused by modularisation |
| Required validation | no loss |
| Scope drift | none material |
| Repeated governance evidence | materially reduced |
| Issue and PR count | proportionate to delivery posture |
| Evidence description | matches actual evidence level |
| Final close-out | defensible Adopt, Adapt or Reject |

Prompt length alone must not justify adoption. A shorter prompt that relies on hidden context or weakens safeguards fails.

## Acceptance gates

- [ ] **Architecture coherence:** kernel, profile, modes, manifest and launcher have non-overlapping responsibilities.
- [ ] **Canonical protocol preservation:** the modular pack applies the stable IssueOps protocol without creating a competing version.
- [ ] **State-reconciliation proof:** a fresh session resumes an interrupted initiative without duplicate artefacts or repeated completed work.
- [ ] **Proportionality proof:** a bounded correction remains bounded, while cross-cutting work receives appropriate stage controls.
- [ ] **Repository-capability proof:** merge, validation and local-tooling behaviour are discovered and handled without overclaiming.
- [ ] **Evidence honesty:** self-review, representative walkthrough and independent evaluation are labelled correctly.
- [ ] **Authority preservation:** no automatic lifecycle transition, approval, merge, publication or external mutation is introduced.
- [ ] **Comparative improvement:** launcher size and repeated governance text decrease without loss of scope or validation quality.
- [ ] **Repository ownership clarity:** canonical source locations and their documentation relationship are explicit.
- [ ] **Real pilot evidence:** the design is tested on bounded, multi-issue, resumed and planning-only scenarios, or deviations are explicitly approved and justified.

## Proposed implementation slices after roadmap approval

### Slice 1 — Baseline and rule decomposition

- preserve representative existing prompts as immutable evidence;
- classify each instruction into kernel, profile, mode, manifest or removable duplication;
- record current prompt lengths, intervention counts, artefact counts and observed limitations;
- resolve repository source ownership.

### Slice 2 — Manual Version 0.1 pack

- create the minimal modules;
- document manual assembly and launcher usage;
- add no generator, workflow or schema;
- validate internal consistency and canonical links.

### Slice 3 — Bounded and multi-issue pilots

- run Pilots A and B;
- record evidence in one canonical pilot record per run;
- adapt the modules only through explicit findings.

### Slice 4 — Resume and authority pilots

- run Pilots C and D with fresh-session evidence;
- verify no duplicate artefacts or unauthorised implementation;
- record capability and context limitations.

### Slice 5 — Comparative close-out

- compare all pilots with the baseline;
- document intended versus actual delivery;
- decide Adopt, Adapt or Reject;
- integrate into the recommended baseline only after Adopt;
- record the next decision boundary without creating speculative automation work.

The roadmap may combine slices when doing so reduces ceremony without losing independent reviewability.

## Risks and controls

### Risk: creating a second IssueOps protocol

Control: the kernel must reference and compress the canonical protocol, not silently redefine it. Any normative difference requires explicit protocol review.

### Risk: modularity creates assembly ambiguity

Control: each module has one responsibility, the manifest identifies the mode, and pilots test whether fresh sessions load the correct combination.

### Risk: repository-specific rules leak into the kernel

Control: classify every rule during decomposition and require local commands, paths, settings and merge conventions to remain in the repository profile.

### Risk: a thin launcher hides required context

Control: the resume pilot begins with only the launcher and repository access. Missing context is treated as a design failure, not supplied from chat memory.

### Risk: simplification produces weaker safeguards

Control: compare validation, authority, groundedness and close-out evidence with the successful standalone prompt baseline.

### Risk: process reduction becomes under-governance

Control: the posture gate preserves stage packs for cross-cutting governance, authority and end-to-end proof work.

### Risk: the initiative creates excessive new files

Control: apply the process and documentation budgets; consolidate modules when they do not own distinct responsibilities.

### Risk: evaluation is not independent

Control: require Level 3 evidence for the resume pilot and label lower-level evidence accurately.

### Risk: premature automation

Control: Version 0.1 is manual. Generator, schema and workflow work remain outside the initiative unless an Adopt decision creates a separately shaped next question.

### Risk: collision with #90 sequencing

Control: assign no stage number yet. Keep authority and outcomes separate. Any shared pilot must be independently authorised by both planning contexts.

## Definition of done

The candidate stage would be complete when:

- [ ] the roadmap has been reviewed and approved before execution issues are created;
- [ ] approved implementation issues are complete or explicitly resolved;
- [ ] the Version 0.1 manual architecture exists without unapproved automation;
- [ ] required pilots and comparative evidence are complete, or deviations are explicitly accepted;
- [ ] state resumption is proved at the required evidence level;
- [ ] no material scope, validation or human-authority regression remains;
- [ ] prompt, process and documentation budgets are assessed against actual delivery;
- [ ] limitations and deviations are recorded honestly;
- [ ] a completed delivery record separates intended from actual delivery;
- [ ] the delivery log and causal graph are updated only where warranted; and
- [ ] a final Adopt, Adapt or Reject decision is recorded.

## Likely next decision boundary

If **Adopt**, decide whether to:

- make the kernel and repository profile part of the recommended IssueOps baseline;
- add repository templates or issue-template support;
- define a lightweight manifest schema;
- create a prompt assembler or validator; or
- use the architecture in future initiatives such as operational evidence assistance.

Those are next-stage questions. They are not implementation authority for this proposal.

## Approved planning decisions

- The initiative remains unnumbered and independently governed from issue #90.
- Version 0.1 uses the four proposed operating modes. Evaluation and close-out remain combined unless pilot evidence demonstrates a material authority or usability problem.
- A neutral top-level `issueops/` source area is the provisional preference, but Slice 1 must first prove that existing repository surfaces cannot own the artefacts cleanly.
- The repository profile may be a compact file or a controlled assembly of existing sources. Slice 1 must establish one discoverable ownership model before pilot use.
- The pilot set must include a bounded correction, a multi-issue remediation stage, an interrupted-resume scenario and a planning-only boundary check. Real work should be used where practical; work must not be manufactured merely to satisfy the experiment.
- Level 3 independent-agent evidence is required for the interrupted-resume pilot. Level 2 evidence may support lower-risk pilots when labelled accurately. Human usability evidence remains desirable but is not a Version 0.1 adoption prerequisite.
- The proposed prompt, process and documentation budgets are approved as defaults. Any exception requires an explicit, evidence-backed justification.

## Roadmap approval

Issue #113 records the reviewed decision to formalise this roadmap. Approval authorises only the bounded implementation slices described here through separately reviewed execution contracts.

It does not authorise:

- automatic issue, branch, pull-request, review, merge or publication actions;
- a prompt generator, schema, GitHub Action or automatic launcher;
- repository-setting, permission or merge-authority changes;
- wholesale migration or removal of existing prompts;
- implementation of issue #90; or
- presentation of same-session self-review as independent evidence.

The architecture is adopted only after the pilots and comparative close-out support an evidence-backed **Adopt** decision. Until then, the current canonical IssueOps protocol and existing invocation practices remain the operational baseline.
