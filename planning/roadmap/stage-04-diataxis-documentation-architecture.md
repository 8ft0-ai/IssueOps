# Stage 4 — Diátaxis documentation architecture

Status: approved.

Record type: contemporaneous.

Approved through [planning issue #93](https://github.com/8ft0-ai/IssueOps/issues/93) on 12 July 2026. The approved decision is to align the user-facing documentation incrementally with Diátaxis before operational evidence assistance. Issue #90 remains shaping-only for a possible Stage 5.

## Problem statement

IssueOps has a substantial and accurate canonical documentation set, but its current organisation follows repository concepts and process components rather than the distinct needs of readers.

The current navigation asks a reader to understand categories such as operating model, manual controls, examples, project record and validation before they can decide where to look. Several important pages also combine explanation, task guidance, precise rules, examples and historical evidence. That mixing increases the amount of material a contributor or reviewer must interpret and makes the canonical operating protocol a long path for a small change.

The problem is not that the documentation lacks content. The problem is that a first-time contributor, active contributor, reviewer and maintainer do not yet have clearly separated paths for learning, doing, checking exact rules and understanding the model.

Stage 4 will test whether a Diátaxis-aligned architecture improves those journeys without weakening IssueOps safety, duplicating canonical rules or turning the repository into a broad Markdown taxonomy exercise.

## Outcome to prove

Demonstrate that the user-facing documentation can be organised around four explicit reader needs:

- **Tutorials** for learning through a guided experience;
- **How-to guides** for completing a task;
- **Reference** for exact rules, formats and required evidence; and
- **Explanation** for understanding concepts, decisions and trade-offs.

The stage must prove that:

- a first-time contributor can complete one bounded documentation-only IssueOps journey without hidden chat context;
- an active contributor can find task guidance without reading the complete operating protocol;
- a reviewer can find exact contract, evidence, validation and merge rules directly;
- a maintainer or interested reader can understand the IssueOps model and authority boundaries without following a procedure;
- every user-facing page has one primary documentation mode;
- project and delivery records remain outside the substantive Diátaxis tree;
- current stable and experimental baseline claims remain accurate;
- existing useful content and high-value URLs are preserved or deliberately migrated; and
- all configured documentation builds and the final usability proof supports an explicit **Adopt**, **Adapt** or **Reject** decision.

## Goals

- Establish a durable documentation architecture based on reader need.
- Create one reliable first-time-contributor tutorial.
- Separate materially mixed explanation, procedure and reference content through bounded changes.
- Make normative rules easier to find and maintain from one canonical source.
- Reduce duplication in the operating protocol only after focused replacement pages exist.
- Keep planning, delivery history and implementation artefacts in their correct repository domains.
- Preserve existing IssueOps terminology, safety gates and authority boundaries.
- Validate the architecture through contributor, reviewer and maintainer walkthroughs.

## Non-goals

- No change to the IssueOps lifecycle, execution-contract model or authority model.
- No automatic agent execution, readiness decisions or lifecycle transitions.
- No branch-protection, required-check, permission or repository-setting change.
- No GitHub auto-merge configuration change.
- No Stage 3 collector, evidence schema or workflow change.
- No operational evidence-assistance implementation.
- No application-code change.
- No wiki reorganisation.
- No new MkDocs theme.
- No new MkDocs plugin solely to make the migration appear more complete.
- No repository-wide Markdown taxonomy exercise.
- No movement of tests, fixtures, scripts, workflows, generated artefacts or implementation-adjacent subsystem material into `docs/`.
- No fifth `Project records` category under `docs/`.
- No speculative Stage 5 execution work.

## Operating and authority boundary

Stage 4 changes documentation architecture only.

It preserves:

- the GitHub issue as the execution contract;
- readiness and implementation planning before branch creation;
- one feature branch per execution issue;
- safe repository-operation controls;
- validation matched to the changed behaviour;
- pull requests as evidence packs;
- human contract verification;
- human approval and merge authority;
- honest separation of pre-merge validation and post-merge verification;
- stable-versus-experimental capability distinctions; and
- separate planning or execution contracts for any future automation, authority or governance change.

Delegated delivery authority for this stage permits qualifying pull requests to merge after all required evidence and review gates pass. It does not remove those gates, create independent human review or authorise repository-setting changes.

## Hard repository location boundary

The intended repository shape is:

```text
README.md                      -> repository overview and entry links
AGENTS.md                      -> agent operating rules

docs/
├── index.md                   -> documentation home
├── tutorials/
├── how-to/
├── reference/
└── explanation/

planning/                      -> roadmap, delivery records, delivery graph and planning control surface
tests/                         -> tests and fixtures
scripts/                       -> repository tooling
.github/                       -> workflows and GitHub configuration
<subsystem>/                   -> subsystem-local implementation material where appropriate
```

A file belongs under `docs/` when its primary purpose is to teach, guide, describe exact behaviour or explain the user-facing IssueOps model.

The following remain outside the substantive Diátaxis content tree:

- `planning/`;
- roadmap specifications;
- delivery records, logs and graphs;
- tests and fixtures;
- scripts;
- generated artefacts;
- GitHub workflows;
- implementation-adjacent subsystem documentation;
- repository-management records; and
- historical evidence that is not current user-facing guidance.

Project records may be linked from the documentation where useful. They must not be duplicated into `docs/` or forced into a documentation mode.

Temporary compatibility files may remain under `docs/` during migration when they preserve a high-value URL and direct readers to new canonical pages. They are migration infrastructure, not a fifth content category.

## Target readers and journeys

### First-time contributor

```text
Home
  -> Tutorials
  -> Complete your first small IssueOps change
```

The tutorial teaches through a concrete, low-risk documentation change, minimises unnecessary choices, states expected outcomes and links to deeper material rather than becoming a complete reference manual.

### Active contributor or agent operator

```text
Home
  -> How-to guides
  -> choose a task
```

Task journeys include writing an execution contract, checking readiness and dependencies, preparing an implementation plan, performing a safe mutation, validating a change, preparing a pull-request evidence pack, reviewing against the contract, remediating findings, completing a delegated batch and publishing or verifying the documentation site.

### Reviewer

```text
Home
  -> Reference
  -> exact rule, format or blocker
```

Reference material includes lifecycle and gate definitions, execution-contract fields, readiness and plan formats, branch naming, lifecycle labels, phase permissions, safe-operation evidence, PR evidence requirements and templates, recommendation vocabulary, merge blockers, validation requirements and checklists.

### Maintainer or interested reader

```text
Home
  -> Explanation
  -> concept, rationale or trade-off
```

Explanation includes why the issue is the execution contract, why the PR is an evidence pack, why approval remains human, why the model begins manually, planning issues versus execution contracts, evidence completeness versus contract satisfaction, representative versus repository-native validation and canonical documentation versus project memory.

## Canonical-source and duplication rules

1. **Reference owns normative facts.** Exact fields, statuses, required gates, formats, classifications and decision vocabularies have one canonical reference location.
2. **How-to guides own task sequence.** They explain what to do and link to reference for exact rules instead of repeating full tables and templates.
3. **Tutorials optimise for learning.** They may repeat the minimum values and commands required for a reliable experience, but link to canonical reference and are reviewed when reference rules change.
4. **Explanation does not introduce hidden requirements.** It may discuss rationale and trade-offs, but must not be the only place where a mandatory rule is stated.
5. **Examples are illustrative, not normative.** They identify the reference rules they demonstrate.
6. **Project records describe intent or delivery.** They do not silently become the source of current operating rules.
7. **README and AGENTS point inward.** They remain concise repository entry and operating surfaces rather than duplicating the complete documentation set.
8. **Cross-domain links are preferred to relocation.** Planning, test and implementation artefacts remain where they belong and are linked when a documentation reader needs them.

## URL and migration policy

- Prefer incremental, navigation-first migration over a broad physical restructure.
- Preserve existing URLs in the architecture foundation and tutorial slices.
- When a page is split, retain the old path as a useful landing or temporary compatibility page that points to new canonical destinations.
- Preserve commonly linked headings where practical.
- Do not add a redirect plugin in the initial migration. A new dependency requires a separately justified execution contract and evidence that compatibility pages are no longer manageable.
- Move project records out of the substantive documentation tree only through explicit execution contracts that identify their canonical destination and compatibility treatment.
- Remove compatibility pages only after repository-link review, public-link consideration and a documented migration decision.
- Do not duplicate canonical project records to preserve a site path; use an appropriate repository link when the MkDocs site needs to refer to material outside `docs/`.

## Target documentation architecture

### Tutorials

- Complete your first small IssueOps documentation change.

Only one tutorial is required initially. Additional tutorials require a distinct learning journey that cannot be served by a how-to guide.

### How-to guides

Likely focused guides include:

- write an executable issue contract;
- check readiness and dependencies;
- prepare an implementation plan;
- perform a safe repository mutation;
- validate a documentation change;
- validate a workflow change;
- prepare a pull-request evidence pack;
- review a pull request against its contract;
- remediate review feedback;
- complete a delegated batch;
- publish or verify the documentation site; and
- collect an experimental evidence pack where that capability remains documented.

### Reference

Likely reference pages include:

- lifecycle and mandatory gates;
- execution-contract fields;
- readiness and dependency formats;
- implementation-plan format;
- branch naming and lifecycle labels;
- safe-operation phase permissions and evidence formats;
- PR evidence requirements and templates;
- review recommendation vocabulary and merge blockers;
- validation requirements by change type;
- documentation-currency checklist;
- workflow-change checklist;
- repository-native validation policy;
- `evidence-pack/v1` schema; and
- collector inputs, outputs, statuses and limitations where applicable.

### Explanation

Likely explanation pages include:

- why the issue is the execution contract;
- why a pull request is an evidence pack;
- why evidence completeness is not contract satisfaction;
- why approval and merge authority remain human;
- why IssueOps begins manually;
- planning issues versus execution contracts;
- delegated authority versus GitHub auto-merge;
- the relationship between Jira, GitHub Issues and pull requests; and
- canonical documentation versus project memory.

## Dependencies and sequencing

Stage 4 delivery begins only after this roadmap is merged and verified on `main`.

The intended dependency order is:

```text
roadmap approval
  -> architecture and front door
  -> first tutorial
  -> execution-contract guidance separation
  -> PR evidence and review guidance separation
  -> safe-operation and validation guidance separation
  -> project-record boundary cleanup
  -> canonical protocol simplification
  -> usability proof and close-out
```

Dependent migrations proceed sequentially from the latest `main`. An issue may run independently only when its contract explicitly shows that it does not depend on an unmerged content split or compatibility decision.

Issue #90 may continue as planning discussion, but it remains shaping-only for a possible Stage 5. It receives no implementation authority from this roadmap and must not be decomposed into execution work until independently approved.

## Proposed implementation slices

The final issue decomposition may combine or split these slices when repository inspection proves a smaller review boundary, but the complete outcome and dependencies must remain explicit.

1. **Establish the Diátaxis architecture and front door**
   - add the architecture and authoring rules;
   - establish the four reader pathways;
   - update MkDocs navigation;
   - classify existing pages by primary mode; and
   - preserve current content while the new structure is introduced.

2. **Add the first IssueOps tutorial**
   - create one guided contributor experience using a low-risk documentation-only scenario;
   - state expected outcomes and validation; and
   - test the tutorial as an end-to-end journey.

3. **Separate execution-contract guidance**
   - separate rationale, task guidance and exact field definitions;
   - separate readiness and planning procedures from reusable formats; and
   - preserve canonical terminology and compatibility entry paths.

4. **Separate PR evidence and review guidance**
   - distinguish evidence-pack explanation, preparation guidance, exact requirements and templates;
   - retain contract-verification and remediation behaviour; and
   - centralise recommendation vocabulary and merge blockers.

5. **Separate safe-operation and validation guidance**
   - distinguish task instructions from exact phase and evidence rules;
   - separate validation policy, procedures and checklists; and
   - keep publishing procedures separate from historical deployment evidence.

6. **Remove project records from the Diátaxis tree**
   - re-establish canonical homes for roadmap, release and delivery-history material;
   - update links without duplicating sources;
   - preserve high-value URLs where practical; and
   - document deliberate compatibility decisions.

7. **Simplify the canonical protocol**
   - reduce the operating protocol to the authoritative lifecycle and gate map;
   - link to focused how-to, reference and explanation pages;
   - remove duplication only after replacements exist; and
   - retain every mandatory safety and authority boundary.

8. **Validate usability and close Stage 4**
   - perform first-time-contributor, active-contributor, reviewer and maintainer walkthroughs;
   - fix material navigation or content-boundary problems through bounded issues;
   - record intended versus actual delivery; and
   - complete the **Adopt**, **Adapt** or **Reject** close-out decision.

## Acceptance and proof gates

### Architecture and scope

- [ ] MkDocs presents explicit Tutorials, How-to, Reference and Explanation paths.
- [ ] `docs/` contains only user-facing Diátaxis content plus deliberate temporary compatibility files.
- [ ] Planning, delivery, test, script, workflow and subsystem artefacts remain outside the substantive Diátaxis tree.
- [ ] Root repository entry files retain their intended roles.
- [ ] Every user-facing page has one primary documentation mode.
- [ ] Project history remains accessible without becoming a fifth documentation mode.

### First-time contributor

- [ ] A reader can identify the tutorial entry point from the documentation home.
- [ ] The reader can complete one small documentation-only IssueOps journey without hidden conversation context.
- [ ] Each tutorial step has a visible expected outcome.
- [ ] The tutorial links to deeper how-to, reference and explanation material rather than duplicating it.
- [ ] The tutorial relies only on implemented repository capabilities.

### Active contributor

- [ ] Task guidance is directly findable for contract writing, readiness, planning, safe mutation, validation, PR preparation and remediation.
- [ ] A contributor does not need to read the full operating protocol to find a task procedure.

### Reviewer

- [ ] Exact contract fields, evidence requirements, validation rules, recommendation vocabulary, merge blockers and authority boundaries are directly findable.
- [ ] Normative rules have one canonical reference location.

### Maintainer or interested reader

- [ ] The documentation explains the IssueOps thesis, planning/execution separation, evidence/approval separation, human authority and manual-first approach without requiring procedural reading.

### Quality and compatibility

- [ ] `mkdocs build --strict` passes for every slice and for final close-out.
- [ ] Internal links and navigation are reviewed after every structural change.
- [ ] Stable-versus-experimental baseline claims remain accurate.
- [ ] High-value existing URLs are preserved or deliberately migrated with recorded compatibility treatment.
- [ ] Documentation-currency and contradictory-guidance reviews pass.
- [ ] No unsupported automation or governance claim is introduced.

### Close-out decision

- [ ] Intended versus actual delivery is recorded separately.
- [ ] Merged issues, PRs, strongest proof, limitations, compatibility decisions and deferred work are linked.
- [ ] The final decision is recorded as **Adopt**, **Adapt** or **Reject**.
- [ ] Issue #90 is updated with any relevant documentation dependency but remains independently governed.

## Risks and controls

### Cosmetic taxonomy without better journeys

Control: require tutorial, task-findability, reviewer-reference and maintainer-understanding proof. Four directory names alone do not satisfy the stage.

### Safety guidance weakened by over-splitting

Control: preserve existing pages until replacements exist, centralise normative facts in reference and compare every split against the current authority boundaries.

### Canonical rules duplicated across modes

Control: assign normative facts to reference, task sequence to how-to, learning flow to tutorial and rationale to explanation. Link rather than repeat full definitions.

### Stable links break during physical migration

Control: migrate incrementally, preserve old paths as useful landing or compatibility pages and make URL treatment explicit in each execution contract.

### Project records are forced into the documentation tree

Control: maintain the hard location boundary, link to `planning/` or repository records and prohibit a fifth project-record mode.

### Historical evidence becomes current operating guidance

Control: keep delivery records separate, label compatibility pages clearly and ensure current normative rules resolve to focused reference pages.

### Broad rewrites become difficult to review

Control: use one feature branch per bounded execution issue, keep dependent migrations sequential and reject unrelated cleanup.

### Stage 4 silently changes governance or automation

Control: treat any policy or authority change as out of scope and require a separate planning or execution contract.

### Stage 5 begins before its authority is approved

Control: keep issue #90 shaping-only, record the sequencing note and do not create operational evidence-assistance implementation issues from this roadmap.

## Definition of done

Stage 4 is complete when:

- [ ] approved execution issues are complete or explicitly resolved;
- [ ] all four reader journeys are implemented and validated;
- [ ] the first tutorial has end-to-end evidence;
- [ ] materially mixed guidance has been separated or deliberately retained with rationale;
- [ ] project-record and compatibility decisions are recorded;
- [ ] the canonical protocol is simplified only after focused replacements exist;
- [ ] the complete documentation validation suite passes;
- [ ] contributor, reviewer and maintainer walkthroughs are recorded;
- [ ] limitations, deviations and deferred work are explicit;
- [ ] a completed Stage 4 delivery record exists;
- [ ] the delivery log is updated;
- [ ] the delivery graph is updated only if the causal project story changed;
- [ ] the roadmap status is updated to `completed`; and
- [ ] the final **Adopt**, **Adapt** or **Reject** decision is recorded without starting speculative Stage 5 implementation.

## Likely next decision boundary

The evidence from Stage 4 should allow the project to decide whether the Diátaxis architecture is adopted as the durable documentation model and whether issue #90 can be shaped against a clearer canonical documentation boundary as a possible Stage 5.

Stage 4 does not approve operational evidence assistance. That initiative requires its own reviewed roadmap, authority boundary, proof gates and execution contracts.