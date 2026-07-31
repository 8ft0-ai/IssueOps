# Portable IssueOps bootstrap and adoption

Status: completed.

Record type: contemporaneous.

Approved through [planning issue #115](https://github.com/8ft0-ai/IssueOps/issues/115) and formalised by [PR #116](https://github.com/8ft0-ai/IssueOps/pull/116) on 14 July 2026.

The exact approved roadmap before delivery and close-out is preserved at merge commit [`18c9bd6b37b4eb9219f3a5344a3bcd255520d54c`](https://github.com/8ft0-ai/IssueOps/blob/18c9bd6b37b4eb9219f3a5344a3bcd255520d54c/planning/roadmap/portable-issueops-bootstrap-and-adoption.md). This completed status record summarises the approved intent and links actual delivery separately; it does not rewrite later findings as original plans.

Actual delivery and proof: [Portable IssueOps bootstrap and adoption delivery record](../delivery/portable-issueops-bootstrap-and-adoption.md).

## Problem statement

The approved roadmap identified that IssueOps had a stable implemented manual operating model, but adoption in another repository depended on reconstructing its protocol, reference pages, templates and authority boundaries. Large prompts could compensate, but they were difficult to version, easy to drift and prone to hidden assumptions about the target repository.

A portable entry point also risked being mistaken for remote authority to create files, replace local conventions, enable automation or change repository controls before the target had established its own local execution contract.

The initiative therefore had to make the implemented manual baseline portable while preserving local repository authority, proportionality, validation and human review.

## Outcome to prove

The approved outcome was to prove that an unfamiliar or fresh-context agent could begin with a published, reproducibly pinned IssueOps bootstrap specification and an existing target repository and then:

1. inspect the target repository without mutation;
2. identify and preserve or deliberately adapt existing conventions;
3. select the lightest sufficient adoption posture;
4. create one local bootstrap execution-contract issue as the first write, unless a valid equivalent already existed;
5. deliver the bootstrap through readiness, planning, branch, validation, PR and human review controls;
6. introduce no unsupported automation, settings, permissions or authority changes;
7. deliver one subsequent genuine issue through the adopted process; and
8. support an evidence-based `Adopt`, `Adapt` or `Reject` close-out.

Close-out result: proved through `8ft0-ai/mri-fourier-lab`. The final decision is **Adopt**.

The formal pilot used:

- `IssueOps Bootstrap 0.1`;
- the pinned source at commit `fb2c42b1767d2baced01ee0539264bb80268beeb`;
- target repository `8ft0-ai/mri-fourier-lab`;
- stable branch `main`;
- verified starting commit `4cd7dda2630a1d8da4c7bc69c77e26050a71d648`; and
- exact target authority recorded on [issue #121](https://github.com/8ft0-ai/IssueOps/issues/121#issuecomment-5138524528).

## Non-goals

The completed initiative did not introduce:

- automatic agent execution or lifecycle transitions;
- a CLI, installer, generator, formal schema, GitHub App or launcher service;
- workflow, required-check, branch-protection, permission or repository-setting changes;
- auto-merge configuration;
- organisation-wide or cross-repository rollout;
- replacement of target conventions for naming symmetry;
- stage machinery as the default adoption posture;
- a release or publication change;
- implementation of issue #90 or issue #113; or
- external mutation beyond the exact authority recorded for the formal pilot.

The bootstrap phase did not change target application behaviour, application source, educational content, Fourier mathematics, MRI explanations, images, assets, dependencies, build tooling or Pages configuration.

The subsequent genuine issue changed application source only through its own separately scoped target issue after bootstrap merge verification.

## Operating and autonomy boundary

The delivered pre-contract sequence is:

```text
read-only assessment
  -> capability and convention map
  -> posture recommendation
  -> one locally authorised bootstrap issue
  -> normal local IssueOps lifecycle
```

The remote specification supplies a method and safety boundary. It does not grant unrestricted local authority.

The formal pilot preserved:

- the target issue as the first write;
- readiness and implementation planning before branch creation;
- one issue-scoped branch;
- explicit safe-operation checks;
- target-local scope, validation and evidence rules;
- final-head validation;
- draft PRs while evidence remained incomplete;
- groundedness review before approval; and
- per-PR human approval and merge authority.

No target auto-merge or delegated merge authority was granted. Same-session agent review was not described as independent human validation.

## Target workflow or target state

The delivered reusable workflow is:

```text
current or pinned BOOTSTRAP.md
  -> read-only repository assessment
  -> capability map and convention map
  -> lightest sufficient posture
  -> local bootstrap execution-contract issue
  -> readiness and implementation plan
  -> issue-scoped bootstrap branch and PR
  -> final-head validation and human review
  -> adopted manual IssueOps controls
  -> one subsequent genuine issue
  -> evidence-based Adopt / Adapt / Reject close-out
```

The formal target adopted the **Minimal manual adoption** posture through:

```text
AGENTS.md
.github/ISSUE_TEMPLATE/change.md
.github/pull_request_template.md
```

It did not copy the IssueOps protocol or install stage machinery.

The subsequent target issue used those surfaces to deliver bounded keyboard accessibility for the existing Fourier spectrum inspector.

### Adoption postures

The delivered posture model remains:

- **Already compatible** — map existing equivalents and permit no change when evidence supports it.
- **Minimal manual adoption** — add or adapt only the missing local manual controls.
- **Stage-capable adoption** — use only when dependent multi-issue planning, governance or proof genuinely requires it.

Capabilities, not mandatory filenames, govern the choice.

### Source ownership

Delivered source ownership remains:

- `BOOTSTRAP.md` — concise external entry point and safety boundary;
- `bootstrap/` — adaptable assessment, mapping and local-issue sources;
- `docs/how-to/adopt-issueops-in-an-existing-repository.md` — human adoption procedure;
- `docs/reference/issueops-bootstrap-requirements.md` — normative bootstrap inputs, postures, authority and evidence requirements; and
- `planning/` — approved intent, actual delivery, limitations and final decision.

### Versioning and reproducibility

The delivered model distinguishes:

1. the current mutable entry point at `main`;
2. the pinned commit URL used by each adoption; and
3. the specification identity `IssueOps Bootstrap 0.1`.

The formal target issue and PR recorded the exact pinned identity used.

### Evidence levels

The formal bootstrap path and subsequent genuine issue reached **Level 3 — fresh independent-agent walkthrough**.

Representative same-session checks from source-pack delivery remain separately labelled and are not substituted for the formal pilot. Human merge decisions remain separate from agent groundedness review.

## Acceptance gates

### Safety

- [x] The remote specification authorises only read-only assessment, posture proposal and one locally authorised bootstrap issue before the local lifecycle begins.
- [x] The first target-repository write was the local bootstrap issue.
- [x] No bootstrap workflow, settings, permission, branch-protection, required-check, auto-merge or application-code change occurred.
- [x] The subsequent application change used a separate genuine issue after bootstrap merge verification.
- [x] Human approval and merge authority remained explicit for both target PRs.

### Proportionality

- [x] The target received one justified posture: **Minimal manual adoption**.
- [x] Runtime, source, publication and validation conventions were mapped and preserved before new artefacts were proposed.
- [x] Every new bootstrap surface had one distinct local owner and tested need.
- [x] Minimal adoption did not install stage machinery.
- [x] Already-compatible and no-change remained valid alternatives and were rejected only through evidence.

### Portability and compatibility

- [x] The fresh execution began from the pinned bootstrap URL, target repository and exact authority.
- [x] It identified the local issue boundary without copying the complete protocol into the target.
- [x] It worked with the target's small dependency-free browser application and existing Pages layout.
- [x] Unsupported capabilities and unavailable validation were surfaced rather than simulated.
- [x] The target recorded the pinned bootstrap version actually used.

### Real use

- [x] The bootstrap PR was delivered through the target's adopted local lifecycle.
- [x] One subsequent genuine accessibility issue was delivered through the adopted process.
- [x] Available final-head validation was current and non-failing.
- [x] Unsupported mutations were zero.
- [x] Friction, wrong turns, deviations and limitations were recorded honestly.
- [x] Final decision recorded: **Adopt**.

### Source integrity

- [x] `BOOTSTRAP.md`, adaptable sources, How-to guidance, Reference requirements and planning records retain non-overlapping owners.
- [x] The portable pack exports only the implemented manual IssueOps baseline.
- [x] No capability from issue #90 or issue #113 is required or implied.
- [x] Mutable and pinned adoption paths are distinguished.

## Proposed implementation slices

The approved four slices were delivered:

1. **Baseline, bootstrap contract and source ownership** — issue #118 / PR #122.
2. **External entry point and adaptable bootstrap pack** — issue #119 / PR #123.
3. **Human adoption guidance and normative reference** — issue #120 / PR #124.
4. **External pilot, comparative proof and close-out** — issue #121, target issues #1 and #3, target PRs #2 and #4, and the IssueOps close-out PR.

Actual evidence, deviations and limitations belong in the [delivery record](../delivery/portable-issueops-bootstrap-and-adoption.md), not in this intent record.

## Risks and controls

The approved controls were applied as follows:

- remote-authority risk was controlled through read-only assessment and the first-local-issue rule;
- convention-displacement risk was controlled through capability and convention mapping;
- protocol-duplication risk was controlled through a concise entry point and three target-local surfaces rather than copied IssueOps documentation;
- planned-capability leakage was controlled by excluding issues #90 and #113;
- unplanned automation and authority change were controlled through explicit non-goals and per-write checks;
- excessive-process risk was controlled through **Minimal manual adoption** and rejection of stage machinery;
- false-independent-evidence risk was controlled through explicit Level 3 labels and separate human merge decisions;
- external mutation risk was controlled through an immutable target, branch, starting commit and authority record;
- mutable-link risk was controlled through the pinned source and specification identity; and
- hidden-context risk was controlled by governing execution through repository sources and durable issue and PR evidence.

Observed connector-selection errors and reaction mutations were contained, disclosed and classified under the execution-deviation policy. No material evidence or authority state remained changed.

Remaining limitations are recorded in the delivery record rather than hidden here.

## Definition of done

The initiative is complete because:

- [x] the approved source, entry-point and adoption-guidance issues are completed;
- [x] `BOOTSTRAP.md` and supporting artefacts exist only as approved;
- [x] human and normative documentation agree with the bootstrap surface;
- [x] no unsupported automation or authority expansion was introduced;
- [x] a pinned adoption path is documented;
- [x] a fresh independent-agent pilot completed read-only assessment and first-local-issue creation;
- [x] the bootstrap PR was delivered and human-approved in the target repository;
- [x] one subsequent genuine issue was delivered and human-approved through the adopted process;
- [x] intended and actual delivery are recorded separately;
- [x] limitations, friction and deviations are explicit;
- [x] a completed delivery record exists;
- [x] roadmap, delivery index, ledger and causal graph are reconciled through the close-out PR;
- [x] no target delivery PR remains open; and
- [x] final decision recorded: **Adopt**.

Issue #121 and parent issue #117 may close only after the IssueOps close-out PR is human-approved, merged and post-merge planning state is verified.

## Likely next decision boundary

The proven portable manual bootstrap may inform the independently governed [modular IssueOps session architecture](modular-issueops-session-architecture.md).

A later initiative may consider a thinner invocation or session launcher, reusable close-out formatting, better publication-surface discovery or stronger tool-action selection controls. Any such work must preserve:

- the local execution-contract handoff;
- capability-first and proportionate adoption;
- honest evidence levels;
- target-local validation and authority; and
- human approval and merge control.

This **Adopt** decision does not create lifecycle automation, automatic execution, auto-merge, repository-setting changes or implementation authority for issue #90 or issue #113.