# Stage 4 — Diátaxis documentation architecture

Status: completed.

## Original documented intent

Stage 4 was approved through [planning issue #93](https://github.com/8ft0-ai/IssueOps/issues/93) and formalised by [PR #95](https://github.com/8ft0-ai/IssueOps/pull/95). The exact approved roadmap is preserved at merge commit [`f22a0ec04eb16ad1f5c28ebe8b8f34d1618e4640`](https://github.com/8ft0-ai/IssueOps/blob/f22a0ec04eb16ad1f5c28ebe8b8f34d1618e4640/planning/roadmap/stage-04-diataxis-documentation-architecture.md).

The stage intended to organise user-facing documentation around four reader needs—Tutorials, How-to guides, Reference and Explanation—while keeping planning, delivery history, tests, scripts, workflows and implementation-adjacent material outside the substantive documentation tree. It also intended to preserve IssueOps lifecycle and human-authority boundaries, protect high-value URLs and prove the result through four representative reader journeys.

Parent delivery issue: [#96](https://github.com/8ft0-ai/IssueOps/issues/96).

## Retrospective interpretation

Not applicable. Stage 4 used a contemporaneous roadmap approved before implementation decomposition. This delivery record describes actual delivery and does not rewrite the original roadmap to make later findings appear planned.

## What shipped

Stage 4 delivered:

- a documentation home and MkDocs navigation with explicit Tutorials, How-to guides, Reference and Explanation paths;
- a complete first-time-contributor tutorial covering the manual IssueOps loop from issue creation through post-merge verification;
- focused How-to guides for contracts, readiness, planning, safe mutation, validation, publishing, PR evidence, review and remediation;
- canonical Reference pages for fields, formats, operation permissions, validation policies, evidence requirements, templates, review decisions and merge blockers;
- focused Explanation pages for the execution-contract model, evidence versus approval, repository-native validation and documentation architecture;
- concise compatibility entry pages for previously mixed or highly linked documentation paths;
- a canonical planning evidence index and explicit project-record boundary outside the substantive four-mode tree;
- preserved roadmap, workflow, usability-review and release URLs with immutable historical snapshots;
- a simplified operating protocol that retains the complete 12-step lifecycle, mandatory gates and human approval authority while linking to focused detail; and
- updated repository and documentation entry points that route readers by need rather than internal component taxonomy.

The stage changed documentation architecture only. It did not change IssueOps lifecycle, automation, validation, approval, merge or repository-setting behaviour.

## Linked issues and pull requests

Planning and roadmap:

- [#93 — Shape Diátaxis-aligned documentation architecture](https://github.com/8ft0-ai/IssueOps/issues/93)
- [#94 — Formalise the approved roadmap](https://github.com/8ft0-ai/IssueOps/issues/94) / [PR #95](https://github.com/8ft0-ai/IssueOps/pull/95)
- [#96 — Stage 4 parent issue](https://github.com/8ft0-ai/IssueOps/issues/96)

Delivery slices:

- [#97 — Architecture and front door](https://github.com/8ft0-ai/IssueOps/issues/97) / [PR #105](https://github.com/8ft0-ai/IssueOps/pull/105)
- [#98 — First IssueOps tutorial](https://github.com/8ft0-ai/IssueOps/issues/98) / [PR #106](https://github.com/8ft0-ai/IssueOps/pull/106)
- [#99 — Execution-contract guidance](https://github.com/8ft0-ai/IssueOps/issues/99) / [PR #107](https://github.com/8ft0-ai/IssueOps/pull/107)
- [#100 — PR evidence and review guidance](https://github.com/8ft0-ai/IssueOps/issues/100) / [PR #108](https://github.com/8ft0-ai/IssueOps/pull/108)
- [#101 — Safe-operation and validation guidance](https://github.com/8ft0-ai/IssueOps/issues/101) / [PR #109](https://github.com/8ft0-ai/IssueOps/pull/109)
- [#102 — Project-record boundary](https://github.com/8ft0-ai/IssueOps/issues/102) / [PR #110](https://github.com/8ft0-ai/IssueOps/pull/110)
- [#103 — Canonical protocol simplification](https://github.com/8ft0-ai/IssueOps/issues/103) / [PR #111](https://github.com/8ft0-ai/IssueOps/pull/111)
- [#104 — Usability proof and close-out](https://github.com/8ft0-ai/IssueOps/issues/104) / [PR #112](https://github.com/8ft0-ai/IssueOps/pull/112)

## Proof runs, checks and artefacts

The strongest user-facing proof before close-out was the final Stage 4 site artefact from PR #111:

- documentation workflow run `29186467967` completed successfully;
- `mkdocs build --strict` passed on final head `240c12caa0d5df788cd5a28eb4e08a32347b956b`;
- Pages artefact `8258157132` was generated and inspected;
- 57 generated HTML pages were inspected;
- 3,076 internal links were resolved with zero missing targets;
- the tutorial exposed 12 sequential steps and 14 visible expected outcomes;
- all required active-contributor task links were present;
- all required reviewer reference links and recommendation vocabulary were present;
- all required maintainer explanation links and concepts were present;
- the protocol retained all 12 lifecycle anchors and explicit human approval and merge authority; and
- all six high-value project-history compatibility pages remained available and labelled.

Project-record boundary proof included successful planning run `29186264357`, documentation run `29186264391` and inspected Pages artefact `8258089424` for PR #110.

[PR #112](https://github.com/8ft0-ai/IssueOps/pull/112) provides the final repository-native strict documentation build, planning validation, delivery-graph validation, graph regeneration and freshness evidence for the completed state.

## Intended versus actual delivery

The eight intended delivery slices were implemented in the planned dependency order. Actual delivery remained inside the roadmap boundary.

Material implementation decisions were:

- compatibility pages were retained instead of adding redirect infrastructure;
- exact former project-record pages were preserved through immutable Git links rather than duplicated under `docs/`;
- the project-record boundary introduced `planning/evidence/index.md` as a curated navigation surface;
- the operating protocol retained concise mandatory duplication where a lifecycle gate must remain visible without following a link; and
- usability proof used repository-grounded representative walkthroughs rather than claiming observed external-user research.

No new MkDocs theme or plugin was introduced. Tests, scripts, workflows, planning records and implementation artefacts remained in their original domains.

## Observed limitations and friction

- The four audience walkthroughs are representative repository-grounded tests, not observed external-user research.
- Compatibility pages remain under `docs/` as deliberate migration surfaces. Removing them requires a separate URL and external-link review.
- Some compatibility entries remain physically organised under a primary navigation mode even though their purpose is route preservation rather than new substantive content.
- The connected commit-workflow lookup exposes pull-request-triggered runs but not push-to-`main` Pages runs, so public post-merge deployment is not claimed unless directly observed through another available surface.
- The initiative used sequential connector commits because a local authenticated checkout was unavailable; repository-native CI remained the validation source of truth.

None of these limitations undermines the adopted information architecture or authority boundary.

## Boundaries preserved

Stage 4 preserved:

- the GitHub issue as the execution contract;
- readiness and implementation planning before branch creation;
- one feature branch per execution issue;
- safe repository-operation checks;
- validation matched to change type and risk;
- pull requests as evidence packs;
- explicit groundedness review;
- human approval and merge authority, including bounded owner delegation only after all gates pass;
- honest separation of pre-merge validation and post-merge verification;
- `v0.2.0` as the recommended stable baseline;
- Stage 3 and proposed `v0.3.0-alpha.1` as experimental with decision **Adapt**; and
- independent planning authority for any future operational evidence-assistance work.

No automatic agent execution, lifecycle transition, branch-protection, required-check, permission, repository-setting, evidence-schema or Stage 3 collector change was introduced.

## Decisions and lessons

Decision: **Adopt** the Diátaxis documentation architecture.

The evidence supports adoption because the four reader journeys are directly discoverable, the guided tutorial is complete, normative rules have focused Reference owners, task procedures are independently findable, conceptual material no longer requires procedural reading, project records remain outside the substantive tree and the lifecycle protocol retains every mandatory gate.

Lessons:

- Diátaxis is most useful as a content-ownership model, not merely four directory names.
- Navigation-first migration reduced link and review risk while focused pages were introduced incrementally.
- Compatibility surfaces can preserve URLs without remaining canonical content owners.
- A concise lifecycle map still needs limited mandatory duplication so safety gates remain visible.
- Final adoption should be based on reader journeys and ownership checks, not file placement alone.

## Implications for the next stage

Issue [#90](https://github.com/8ft0-ai/IssueOps/issues/90) remains shaping-only for a possible Stage 5 — Operational evidence assistance.

Any future roadmap or implementation from #90 should:

- place task procedures in How-to guides;
- place exact collector inputs, evidence states and limitations in Reference;
- place authority and trade-off reasoning in Explanation;
- add a Tutorial only when a reliable learning journey exists;
- keep delivery evidence and stage records under `planning/`; and
- preserve the read-only, human-triggered and human-decision boundaries unless separately shaped and approved.

Stage 4 does not approve Stage 5 or create an operational evidence-assistance backlog.