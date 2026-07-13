# Portable IssueOps bootstrap and adoption

Status: approved.

Record type: contemporaneous.

Approved through [planning issue #115](https://github.com/8ft0-ai/IssueOps/issues/115) on 14 July 2026. The initiative is deliberately unnumbered and is independently governed from issues [#90](https://github.com/8ft0-ai/IssueOps/issues/90) and [#113](https://github.com/8ft0-ai/IssueOps/issues/113).

The approved roadmap permits bounded delivery in `8ft0-ai/IssueOps`. It does not yet authorise mutation of an external pilot repository because the exact target repository, stable branch and external merge policy remain unresolved.

## Problem statement

IssueOps has a stable implemented manual operating model, but adoption in another existing repository currently depends on a repository owner or agent reconstructing the relevant protocol, reference pages, templates and authority boundaries. Large self-contained prompts can compensate for that, but they are difficult to version, easy to drift from current repository guidance and prone to hidden assumptions about the target repository.

A stable external bootstrap entry point is useful only if it does not become unchecked remote authority. A target repository must not treat a remote Markdown file as permission to create files, replace local conventions, enable automation, change settings or broaden agent authority before the repository has established its own local execution contract.

The initiative must therefore make the implemented manual baseline portable while preserving local repository authority, proportionality, validation and human review.

## Outcome to prove

Prove that an unfamiliar or fresh-context AI agent can begin with a published and reproducibly pinned IssueOps bootstrap specification plus an existing target repository and then:

1. inspect the target repository without mutation;
2. identify and preserve or deliberately adapt existing conventions;
3. select the lightest sufficient adoption posture;
4. create one local bootstrap execution-contract issue as the first write, unless a valid equivalent already exists;
5. deliver the bootstrap through that repository's normal readiness, planning, branch, validation, PR and review controls;
6. introduce no unsupported automation, settings, permissions or authority changes;
7. deliver one subsequent real issue through the adopted process; and
8. support an evidence-based Adopt, Adapt or Reject close-out.

The outcome is a safe, portable and proven adoption path, not merely the existence of `BOOTSTRAP.md`.

## Non-goals

This initiative does not authorise:

- implementation of issue #90 or issue #113;
- automatic agent execution or lifecycle transitions;
- a CLI, installer, generator, formal schema, GitHub App or launcher service;
- workflow, required-check, branch-protection, permission or repository-setting changes;
- auto-merge configuration;
- application-code changes;
- organisation-wide or cross-repository rollout;
- replacement of target-repository conventions merely for naming symmetry;
- stage machinery as the default adoption posture;
- external-repository mutation without exact target authority; or
- a release or publication change.

## Operating and autonomy boundary

Reading the remote bootstrap specification authorises only this pre-contract sequence:

```text
read-only assessment
  -> propose adoption posture and bounded local changes
  -> create one local bootstrap execution-contract issue
  -> normal local IssueOps lifecycle begins
```

Before a local execution contract exists and is ready, an agent may read repository instructions, templates, validation commands, branch and merge conventions, planning records and existing issues or pull requests. It may identify gaps, recommend a posture and prepare or create one local bootstrap issue only when the target repository owner has granted permission.

Before that local issue is ready and planned, the agent must not create or change files, create a branch or pull request, add automation, alter settings or permissions, change application code, replace existing conventions or treat the remote specification as delegated merge or publication authority.

The target repository's local issue, instructions, validation rules and human authority govern every mutation. The remote specification supplies a method and safety boundary; it does not grant unrestricted local authority.

Within `8ft0-ai/IssueOps`, the repository owner has approved bounded delegated delivery for the four roadmap slices. Every child issue still requires readiness, an implementation plan, one issue-scoped branch, scoped implementation, current validation, a PR evidence pack, groundedness review and a final recommendation of `Approve` before merge.

External pilot execution remains blocked until the owner records the exact target repository, stable branch, permitted scope, local instructions, validation and merge conventions, and external merge authority.

## Target workflow or target state

### Adoption workflow

```text
current or pinned BOOTSTRAP.md
  -> read-only repository assessment
  -> capability map and posture recommendation
  -> local bootstrap execution-contract issue
  -> readiness and implementation plan
  -> one issue-scoped bootstrap branch and PR
  -> target-repository validation and human review
  -> adopted manual IssueOps controls
  -> one subsequent real issue
  -> pilot evidence and Adopt / Adapt / Reject close-out
```

### Adoption postures

#### Already compatible

Use when the target repository already provides effective equivalents for executable issue contracts, branch discipline, validation, PR evidence and human merge controls. Map existing surfaces, identify only material gaps and permit a no-change outcome when the evidence supports it.

#### Minimal manual adoption

This is the default posture when material controls are missing but dependent stage planning is not justified. Introduce or adapt only the minimum local surfaces needed for issue contracts, agent rules, PR evidence, validation conventions and explicit human authority.

Required capabilities are not mandatory filenames. Existing `AGENTS.md`, contributor guidance, issue templates, PR templates and engineering documentation should be reused where they already own the needed information.

#### Stage-capable adoption

Use only when the target repository genuinely needs dependent multi-issue planning, cross-cutting governance or authority decisions, real end-to-end proof or an explicit adoption close-out. Stage machinery must not be installed merely because this source repository uses it.

### Source ownership

The approved source ownership is:

- `BOOTSTRAP.md` — concise external agent entry point, safety boundary, adoption postures, first-local-issue rule, version guidance and prohibited default mutations;
- `bootstrap/` — the smallest adaptable source pack needed for repository assessment, posture selection, local bootstrap issue creation and convention mapping;
- `docs/how-to/adopt-issueops-in-an-existing-repository.md` — the human task procedure for preparing, supervising and reviewing adoption;
- `docs/reference/issueops-bootstrap-requirements.md` — normative inputs, capability mapping, posture rules, authority boundary, evidence levels, version fields and acceptance requirements; and
- `planning/` — approved intent, delivery relationships, pilot evidence, actual delivery, limitations and final decision.

Implementation issues may consolidate source artefacts when doing so preserves distinct ownership and reduces unnecessary process or documentation volume.

### Versioning and reproducibility

The bootstrap must distinguish:

1. the current recommended mutable entry point at `https://github.com/8ft0-ai/IssueOps/blob/main/BOOTSTRAP.md`;
2. a pinned commit URL used by each adoption record for reproducibility; and
3. a specification identity, provisionally `IssueOps Bootstrap 0.1`, stating that it represents the completed Stage 2 manual baseline as organised through the adopted Stage 4 documentation architecture.

A later release tag may provide a friendlier pinned URL, but this roadmap does not require release creation.

### External pilot

The pilot must use another existing repository and a fresh-context agent or separate session without access to implementation reasoning or prior chat history. The agent receives only the pinned bootstrap URL, exact target repository, normal repository access and explicit local authority boundary.

The pilot must test read-only assessment, posture selection, preservation of local conventions, first-local-issue creation, bootstrap PR delivery, one subsequent real issue, absence of unsupported mutation, pinned reproducibility and honest friction recording.

IssueOps-repository delegated authority does not transfer to the pilot repository unless the owner explicitly grants equivalent authority there.

### Evidence levels

Use these labels accurately:

1. **Structural evidence** — required files, fields, links, headings or control surfaces exist.
2. **Representative walkthrough** — a constrained evaluator follows the path against current repository state.
3. **Fresh independent-agent walkthrough** — a fresh session or separate agent completes the scenario without implementation reasoning, prior chat context or hidden instructions.
4. **Observed human usability** — a human unfamiliar with the implementation completes the scenario.

The bootstrap path and subsequent real issue require at least Level 3 evidence. Same-session structured self-review must not be described as independent evidence.

## Acceptance gates

### Safety

- [ ] The remote specification authorises only read-only assessment, a posture proposal and creation of one local bootstrap issue before the normal local lifecycle begins.
- [ ] The first external-repository write is the local bootstrap issue or a documented valid equivalent.
- [ ] No workflow, settings, permission, branch-protection, required-check, auto-merge or application-code change occurs without separate local authority.
- [ ] Human approval and merge authority remain explicit.

### Proportionality

- [ ] The target repository receives one justified adoption posture.
- [ ] Existing conventions are mapped and reused before any new artefact is proposed.
- [ ] Every new surface has one distinct owner and a tested need.
- [ ] Minimal adoption does not install stage machinery.
- [ ] No-change is an acceptable already-compatible outcome.

### Portability and compatibility

- [ ] A fresh-context agent can begin from the pinned bootstrap URL and target repository alone.
- [ ] The agent identifies the required local issue boundary without an expanded launcher prompt.
- [ ] The process works with target-repository naming and layout differences.
- [ ] Conflicts and unsupported capabilities are surfaced rather than silently overwritten or simulated.
- [ ] The target repository records the pinned bootstrap version actually used.

### Real use

- [ ] The bootstrap PR is delivered through the target repository's local IssueOps lifecycle.
- [ ] One subsequent real issue is delivered through the adopted process.
- [ ] Required validation is current and no available validation is failing.
- [ ] Unsupported mutations are zero.
- [ ] Friction, deviations and limitations are recorded honestly.
- [ ] The final close-out records one decision: Adopt, Adapt or Reject.

### Source integrity

- [ ] `BOOTSTRAP.md`, adaptable sources, How-to guidance, Reference requirements and planning records have non-overlapping owners.
- [ ] The portable pack exports only the implemented manual IssueOps baseline.
- [ ] No capability from issue #90 or issue #113 is required or implied.
- [ ] Mutable and pinned adoption paths are distinguished.

## Proposed implementation slices

Delivery should use no more than four execution slices unless a later approved amendment provides evidence that another review boundary is necessary.

### Slice 1 — Baseline, bootstrap contract and source ownership

- confirm the exact implemented baseline exported by the bootstrap;
- define the normative capability map and local execution-contract requirements;
- resolve the smallest coherent adaptable source pack; and
- preserve a clear boundary between remote method and local authority.

### Slice 2 — External entry point and adaptable bootstrap pack

- create the concise root `BOOTSTRAP.md`;
- create only the adaptable assessment, posture and local-issue sources that have distinct tested need;
- include current and pinned version guidance; and
- add no workflow, installer, generator or schema.

### Slice 3 — Human adoption guidance and normative reference

- add the human How-to guide and normative Reference page under the adopted documentation architecture;
- align terminology, authority boundaries and version fields with the bootstrap sources;
- update only necessary navigation and entry links; and
- validate that no competing canonical protocol is created.

### Slice 4 — External pilot, comparative proof and close-out

- confirm separately governed target-repository authority;
- run the fresh independent-agent bootstrap path;
- deliver one subsequent real issue through the adopted process;
- record pinned reproducibility, friction, limitations and deviations;
- create the completed delivery record and reconcile planning surfaces; and
- decide Adopt, Adapt or Reject.

Slice 4 may be created as a blocked execution contract before target authority is supplied, but no external branch, PR, file or issue mutation may occur until that authority is complete.

## Risks and controls

### Risk: remote instructions become excessive authority

Control: restrict pre-contract authority to read-only assessment, posture proposal and one locally authorised bootstrap issue. Every other mutation follows the target repository's normal lifecycle.

### Risk: target-repository conventions are displaced

Control: assess capabilities rather than filenames, require convention mapping and permit already-compatible or no-change outcomes.

### Risk: the bootstrap duplicates the IssueOps protocol

Control: keep `BOOTSTRAP.md` concise, give normative detail one Reference owner and link to the canonical lifecycle rather than copying it.

### Risk: planned capabilities from #90 or #113 are imported

Control: state the completed Stage 2 manual baseline and Stage 4 documentation architecture as the only exported baseline; treat both issues as independent shaping work.

### Risk: unplanned automation or authority change

Control: prohibit workflows, installers, launchers, settings, permissions, auto-merge and application-code changes unless separately shaped and authorised.

### Risk: excessive templates and process

Control: use the lightest sufficient posture, require tested need for every new source surface and permit consolidation during bounded implementation.

### Risk: false independent-evaluation claims

Control: require evidence-level labels and at least Level 3 fresh independent-agent proof for both bootstrap and subsequent real issue.

### Risk: external pilot mutation without authority

Control: block all external writes until the exact repository, branch, scope, local rules and merge authority are recorded.

### Risk: mutable `main` links undermine reproducibility

Control: retain a current convenience URL and require the target repository to record an immutable commit URL and specification identity.

### Risk: hidden dependence on chat context

Control: constrain the pilot starting information to the pinned bootstrap URL, target repository and explicit local authority; record any additional instruction as a limitation.

## Definition of done

The initiative is complete when:

- [ ] the approved execution issues are completed or explicitly resolved;
- [ ] `BOOTSTRAP.md` and supporting artefacts exist only as approved;
- [ ] human and normative documentation agree with the bootstrap surface;
- [ ] no unsupported automation or authority expansion was introduced;
- [ ] a pinned adoption path is documented;
- [ ] a fresh-context external pilot completed read-only assessment and local issue creation;
- [ ] the bootstrap PR was delivered through the target repository's IssueOps lifecycle;
- [ ] one subsequent real issue was delivered through the adopted process;
- [ ] intended and actual delivery are recorded separately;
- [ ] limitations, friction and deviations are explicit;
- [ ] a completed delivery record exists;
- [ ] roadmap and delivery indexes are reconciled;
- [ ] parent and child issue states match actual delivery;
- [ ] no delivery PR remains open; and
- [ ] the final decision is Adopt, Adapt or Reject.

The initiative is not complete while the external target authority or required pilot proof remains unresolved.

## Likely next decision boundary

Evidence from this initiative may justify later consideration of automation or integration with a modular session architecture only if the manual portable bootstrap proves safe, proportionate and reproducible in a real external repository.

That later decision should ask which observed manual friction is worth addressing without weakening local execution-contract authority, validation, review or human merge control. This roadmap does not create or authorise that later work.
