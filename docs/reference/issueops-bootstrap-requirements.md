# IssueOps bootstrap requirements

This page is the canonical reference for portable IssueOps bootstrap inputs, authority, posture selection, capability mapping, version identity, evidence levels and acceptance requirements.

Use the root [bootstrap entry point](https://github.com/8ft0-ai/IssueOps/blob/main/BOOTSTRAP.md) to start an agent assessment and [Adopt IssueOps in an existing repository](../how-to/adopt-issueops-in-an-existing-repository.md) for the repository-owner procedure. The detailed implementation lifecycle remains owned by the [IssueOps operating protocol](../issueops-protocol.md).

## Specification identity

| Field | Required value |
| --- | --- |
| Specification | `IssueOps Bootstrap 0.1` |
| Implemented baseline | Completed Stage 2 manual IssueOps operating model |
| Documentation organisation | Adopted Stage 4 Diátaxis documentation architecture |
| Current entry point | `https://github.com/8ft0-ai/IssueOps/blob/main/BOOTSTRAP.md` |
| Pinned entry point | `https://github.com/8ft0-ai/IssueOps/blob/<commit-sha>/BOOTSTRAP.md` |

The bootstrap does not include planned operational evidence assistance from issue #90 or planned modular session architecture from issue #113.

A target repository must record the exact pinned entry point it used. The mutable `main` URL may identify the current recommendation but is not reproducible adoption evidence.

## Required starting inputs

Assessment requires:

- exact target repository;
- stable or default branch;
- repository owner or maintainer granting authority;
- explicit permission for read-only assessment;
- explicit decision on whether one local bootstrap issue may be created;
- target-repository agent and contributor instructions;
- known protected paths, sensitive data or operational restrictions; and
- the pinned bootstrap URL.

If the repository, branch or authority is unclear, the assessment decision is `Clarification required` and no target-repository access or mutation should proceed beyond what is explicitly permitted.

## Instruction and authority precedence

Apply sources in this order:

1. target-repository owner authority and repository policies;
2. target-repository agent and contributor instructions;
3. the locally approved bootstrap execution contract, within those higher-level constraints;
4. existing local issue, validation, review and merge conventions not explicitly adapted by that contract; and
5. the remote IssueOps bootstrap method.

The remote bootstrap does not override local authority. A local execution contract may authorise a bounded adaptation of an existing convention but cannot override protected policy, owner authority or scope outside the issue.

## Permission phases

| Phase | Permitted operations | Prohibited operations |
| --- | --- | --- |
| Before assessment authority | None. | Repository access or mutation not explicitly authorised. |
| Read-only assessment | Read instructions, templates, validation, branches, issues, pull requests, planning records and observable repository policy within the granted scope. Prepare assessment and proposed issue text. | Issue creation, file changes, branch creation, pull-request creation, settings, permissions, workflow or application changes. |
| Issue-creation handoff | Create one local bootstrap issue only when the owner explicitly permits it, or identify a valid existing equivalent. | Any file, branch or pull-request mutation; approval or merge claims. |
| Local issue setup | Read the issue and comments, check readiness and dependencies, identify the safe starting state and post the implementation plan. | Branch creation before readiness and planning are complete; file or pull-request changes. |
| Local implementation | Create one issue-scoped branch, implement only the local contract, read changed files and validate. | Work outside the issue; unsupported automation, authority or settings changes; merge. |
| Pull-request review | Open the pull request as the evidence pack, remediate in-scope findings and refresh final-head evidence. | Misstating pending validation, resolving unfixed findings or adding unapproved scope. |
| Merge and post-merge | Merge only under local policy and authority after all gates pass; complete named post-merge checks. | Merge with blockers, stale evidence, unclear authority or failing required validation. |

Repository access is not equivalent to authority for any write.

## Adoption postures

Select exactly one posture from repository evidence.

| Posture | Required conditions | Expected change boundary |
| --- | --- | --- |
| **Already compatible** | Effective local equivalents exist for the required manual controls. Naming and layout may differ. | Preserve local owners. Apply only material bounded corrections. A no-change outcome is valid. |
| **Minimal manual adoption** | One or more required controls are materially missing or incomplete, but dependent stage planning is not justified. | Default posture. Adapt or add the fewest surfaces needed for executable issues, readiness, planning, scoped branches, safe mutation, validation, PR evidence and human authority. |
| **Stage-capable adoption** | The repository genuinely needs dependent multi-issue delivery, cross-cutting governance or authority decisions, end-to-end proof or a formal close-out. | Retain minimal-manual controls and add only justified planning, dependency and delivery-record surfaces. |

A heavier posture must explain why the lighter posture cannot produce the required outcome. Source-repository symmetry is not sufficient justification.

## Required manual capabilities

The selected posture must provide locally owned equivalents for all applicable capabilities.

| Capability | Required outcome |
| --- | --- |
| Execution contract | One issue or equivalent durable work item contains enough outcome, scope, non-goals, acceptance, validation, risk and instructions to implement without hidden intent. |
| Readiness and dependency evidence | Executability, dependencies and a safe starting point are recorded before branch creation. |
| Implementation plan | Proposed branch, files or areas, sequence, validation, assumptions, caveats and exclusions are visible before mutation. |
| Issue-scoped branch | One change is isolated from a known safe base and does not mix unrelated issues. |
| Safe mutation | Phase, intended operation, target, expected side effect and forbidden side effects are considered before writes. |
| Change-specific validation | Evidence matches changed behaviour and risk, identifies the final state and distinguishes completed, pending and post-merge checks honestly. |
| Pull-request evidence | The pull request records contract, changed scope, exclusions, acceptance evidence, validation, caveats, groundedness and recommendation. |
| Contract and scope review | Review answers both whether the change did what was needed and whether it did only what was asked. |
| Human authority | Approval and merge remain human-controlled unless the local owner explicitly grants bounded delegation after all gates pass. |
| Dependent planning | Required only for Stage-capable adoption and owned separately from actual delivery evidence. |

The [repository assessment form](https://github.com/8ft0-ai/IssueOps/blob/main/bootstrap/repository-assessment.md) records the capability evidence and gaps.

## Convention treatments

Each local surface receives one treatment:

- **Preserve** — clear and compatible existing owner.
- **Adapt** — existing owner remains canonical but requires a bounded correction.
- **Add** — no compatible owner exists and a new surface has a tested need.
- **Not needed** — not required for the selected posture.

`Add` requires evidence that no smaller adaptation can satisfy the same criterion. Use the [convention-mapping guidance](https://github.com/8ft0-ai/IssueOps/blob/main/bootstrap/convention-mapping.md).

Equivalent local terminology is valid. IssueOps filenames and labels are not mandatory.

## Bootstrap source ownership

| Surface | Normative responsibility |
| --- | --- |
| Root `BOOTSTRAP.md` | External agent entry point, pre-contract authority boundary, posture path, first-local-issue rule, prohibited defaults and version links. |
| `bootstrap/` | Adaptable assessment, mapping and local execution-contract source material. |
| Adoption How-to | Repository-owner procedure and sequence. |
| This Reference page | Exact bootstrap inputs, permissions, capabilities, posture criteria, version fields, evidence levels and acceptance gates. |
| IssueOps operating protocol and focused Reference pages | Detailed lifecycle, execution-contract, readiness, operation, validation, PR evidence and merge rules. |
| `planning/` | Roadmap intent, delivery evidence, pilot results, limitations and final Adopt, Adapt or Reject decision. |

A surface must not become a competing canonical protocol or duplicate complete content from another owner.

## Local bootstrap issue requirements

The first local bootstrap execution contract must contain:

### Bootstrap identity

- `IssueOps Bootstrap 0.1`;
- current entry point;
- pinned entry point; and
- assessment record or equivalent evidence.

### Core execution-contract fields

- problem;
- expected outcome;
- selected posture and evidence;
- existing conventions to preserve;
- exact scope;
- non-goals;
- observable acceptance criteria;
- validation evidence expected;
- change risk; and
- agent instructions.

### Conditional fields

- parent or roadmap relationship when Stage-capable adoption applies;
- dependencies and safe starting state;
- authority boundary and local merge policy; and
- post-merge verification when evidence genuinely cannot exist before merge.

### Proof continuation

- the rule for selecting one subsequent real issue;
- required evidence from that issue; and
- its authority boundary.

Use the adaptable [local bootstrap issue template](https://github.com/8ft0-ai/IssueOps/blob/main/bootstrap/bootstrap-issue-template.md).

Creating the issue requires explicit target-repository owner permission. The remote specification does not grant it.

## Prohibited default mutations

Portable bootstrap does not authorise by default:

- workflows or automatic lifecycle transitions;
- CLIs, installers, generators, formal schemas, bots, apps or launchers;
- repository settings or permissions;
- required-check or branch-protection changes;
- auto-merge configuration;
- new labels as a prerequisite;
- application-code changes;
- organisation-wide rollout;
- publication or release changes; or
- a copied IssueOps protocol that can drift from its source.

A repository may consider one of these changes only through a separate local execution contract with explicit scope, authority, validation and review. It must not be hidden inside a documentation bootstrap.

## Version fields

Each adoption record should contain:

| Field | Meaning |
| --- | --- |
| `specification` | `IssueOps Bootstrap 0.1` |
| `current_url` | Mutable current recommendation on `main` |
| `pinned_url` | Immutable commit URL actually used |
| `source_commit` | Full IssueOps commit SHA |
| `target_repository` | Exact owner and repository |
| `target_base` | Stable branch or starting commit |
| `assessment_date` | Date the repository state was assessed |
| `selected_posture` | Already compatible, Minimal manual adoption or Stage-capable adoption |

Later bootstrap versions must state material compatibility changes. A target repository should not silently update its recorded adoption source when `main` changes.

## Validation requirements

### Assessment

Required:

- all relevant local instruction and convention surfaces identified;
- capability statuses supported by paths, commands or observable repository evidence;
- one posture selected with lighter and heavier alternatives addressed;
- proposed changes bounded or no-change stated explicitly;
- authority, conflict and unsupported-capability limitations recorded; and
- complete proposed local issue text when issue creation is requested.

### Bootstrap pull request

Required:

- changed files read back;
- final diff compared with the local issue;
- existing local conventions checked for preservation or explicit adaptation;
- repository-native validation completed where available;
- final head identified;
- prohibited default mutations checked;
- evidence pack current; and
- groundedness review completed.

### Subsequent real issue

Required:

- a real, bounded repository need rather than work manufactured only for the pilot;
- local execution-contract fields used;
- readiness and implementation planning before branching;
- one issue-scoped branch;
- change-specific final-head validation;
- pull-request evidence and contract review; and
- merge under local policy and authority.

## Evidence levels

| Level | Name | Definition |
| --- | --- | --- |
| 1 | **Structural evidence** | Required files, fields, links, headings or local control surfaces exist. |
| 2 | **Representative walkthrough** | A constrained evaluator follows the documented path against current or defined representative repository state. |
| 3 | **Fresh independent-agent walkthrough** | A fresh session or separate agent completes the scenario without implementation reasoning, prior chat history or hidden instructions. |
| 4 | **Observed human usability** | A human unfamiliar with the implementation completes the scenario. |

Same-session structured review is not Level 3. Generated artefacts and templates are not evidence that an unfamiliar agent or human can use them successfully.

Formal adoption of Version 0.1 requires at least Level 3 evidence for:

1. the external bootstrap assessment, local issue and bootstrap pull-request path; and
2. one subsequent real issue delivered through the adopted process.

Level 4 is valuable but not required for Version 0.1.

## External proof requirements

A fresh independent-agent pilot must receive only:

- the pinned `BOOTSTRAP.md` URL;
- the exact target repository;
- normal target-repository access; and
- the explicit local authority boundary.

The pilot must record:

- starting information and information withheld;
- repository surfaces consulted;
- capability map and posture decision;
- first write and all mutations;
- local issue, branch, pull request, validation and review evidence;
- subsequent real issue evidence;
- wrong turns and friction;
- unsupported assumptions and limitations;
- pinned reproducibility result; and
- final evaluator confidence.

IssueOps-repository delegated merge authority does not transfer to the target repository.

## Acceptance gates

### Safety

- remote authority stops at read-only assessment, proposal and separately authorised local issue creation;
- the first target write is the local issue or a valid existing equivalent;
- local readiness and planning precede branch creation;
- prohibited default changes do not occur without separate authority; and
- human approval or bounded local delegation governs merge.

### Proportionality

- one posture is selected from evidence;
- existing conventions are reused before new artefacts are proposed;
- every new surface has a distinct owner and tested need;
- minimal adoption does not install stage machinery; and
- no-change is permitted.

### Portability and compatibility

- an unfamiliar agent can start from the pinned source and target repository only;
- local names, layouts and compatible controls are preserved;
- conflicts and unsupported capabilities are surfaced rather than overwritten or simulated; and
- the target records the exact bootstrap source used.

### Real use

- the bootstrap pull request completes through the local lifecycle;
- one subsequent real issue completes through the adopted process;
- required validation is current and no available validation is failing;
- unsupported mutations are zero; and
- limitations and deviations are recorded honestly.

## Assessment decisions

Use one outcome before the first local write:

- **Ready to request local issue creation** — evidence, posture, issue text and owner permission are complete.
- **Already compatible; no change recommended** — retain the assessment and stop without mutation.
- **Clarification required** — authority, scope, posture or local convention is materially unclear.
- **Reject adoption** — the repository cannot safely provide the manual controls within the permitted scope.

## Initiative close-out decisions

After real external proof, use one decision:

- **Adopt** — the bootstrap reliably supports safe, proportionate external adoption and one subsequent real delivery.
- **Adapt** — the proposition is useful but material authority, portability, artefact-volume, versioning or usability limitations remain.
- **Reject** — the approach depends on excessive hidden context, unsafe authority or disproportionate process.

A structural or same-session walkthrough alone cannot justify `Adopt`.

## Related guidance

- [Bootstrap IssueOps in an existing repository](https://github.com/8ft0-ai/IssueOps/blob/main/BOOTSTRAP.md)
- [Portable bootstrap source pack](https://github.com/8ft0-ai/IssueOps/blob/main/bootstrap/README.md)
- [Adopt IssueOps in an existing repository](../how-to/adopt-issueops-in-an-existing-repository.md)
- [IssueOps operating protocol](../issueops-protocol.md)
- [Execution-contract fields](execution-contract-fields.md)
- [Operation permissions and evidence](operation-permissions-and-evidence.md)
- [Validation status and fallback policy](validation-status-and-fallback-policy.md)
- [Pull-request evidence requirements](pr-evidence-requirements.md)
- [Review decisions and merge blockers](review-decisions-and-merge-blockers.md)
