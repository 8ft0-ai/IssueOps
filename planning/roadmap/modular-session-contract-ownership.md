# Modular session contract ownership and Slice 2 decomposition

Status: approved.

Record type: contemporaneous Slice 1 decision and decomposition record.

Authority: issue [#133](https://github.com/8ft0-ai/IssueOps/issues/133) authorises this planning decision only. It does not authorise the future guidance, examples, pilots or automation described below.

## Purpose, authority and relationship

This record completes **Slice 1 — Contract definition and source ownership** under issue [#133](https://github.com/8ft0-ai/IssueOps/issues/133).

It decomposes the active [Modular IssueOps session architecture](modular-issueops-session-architecture.md), which originated under issue [#113](https://github.com/8ft0-ai/IssueOps/issues/113), was adapted under issue [#131](https://github.com/8ft0-ai/IssueOps/issues/131), and was merged through PR [#132](https://github.com/8ft0-ai/IssueOps/pull/132) at commit `efa307d6d7ec9c8324059e71ea2bb5e63dc969ce`.

The adapted roadmap remains the approved source of initiative intent. This record decides ownership and recommends the smallest future Slice 2 documentation set. It does not rewrite the roadmap, make the modular session architecture operational, adopt it, or grant authority for pilots.

## Problem statement

The approved roadmap identifies a narrow transition problem between bounded sessions:

```text
thin session grant
  -> repository-native state reconciliation
  -> role-specific work
  -> durable handover or evidence record
```

The candidate session layer overlaps several already-established owners. Without a deliberate ownership decision, future material could duplicate the portable bootstrap, the canonical lifecycle, repository-local operational state, existing documentation modes or planning evidence.

Slice 1 must therefore answer two questions without implementing the answer:

1. Which source owns each concern needed to start, perform, hand over and verify bounded session work?
2. What is the smallest coherent future artefact set that can express the genuinely missing session-layer rules without becoming a second protocol or state database?

## Outcome to prove

This decision succeeds when every required concern has one authoritative owner or an explicitly unresolved status, and when the recommended Slice 2 set:

- adds only session invocation, role-boundary and transition responsibilities;
- links rather than copies bootstrap, protocol and repository-local rules;
- preserves mandatory receiving-session verification;
- follows the adopted Diátaxis documentation architecture;
- leaves real handovers in GitHub-native records by default;
- keeps pilot evidence in repository-local GitHub and `planning/` records; and
- requires separate authority before any future artefact or pilot is created.

## Bounded baseline examined

The baseline was intentionally limited to the sources needed to distinguish adoption, lifecycle, current state, documentation ownership and transition evidence.

### Repository and roadmap sources

- the active [modular-session roadmap](modular-issueops-session-architecture.md) at merge commit `efa307d6d7ec9c8324059e71ea2bb5e63dc969ce`;
- the [roadmap index](index.md);
- the portable [bootstrap entry point](../../BOOTSTRAP.md);
- the [bootstrap source-pack ownership](../../bootstrap/README.md);
- the bootstrap [repository assessment](../../bootstrap/repository-assessment.md), [convention mapping](../../bootstrap/convention-mapping.md) and [local issue source](../../bootstrap/bootstrap-issue-template.md);
- the canonical [IssueOps operating protocol](../../docs/issueops-protocol.md);
- the adopted [documentation architecture](../../docs/explanation/documentation-architecture.md);
- the current [Reference](../../docs/reference/index.md), [How-to](../../docs/how-to/index.md) and [Examples](../../docs/examples/README.md) surfaces; and
- the [planning ownership boundary](../README.md).

### Transition and evidence records

- issue #131 [readiness](https://github.com/8ft0-ai/IssueOps/issues/131#issuecomment-5162667863), [implementation plan](https://github.com/8ft0-ai/IssueOps/issues/131#issuecomment-5162670516), [backlog groundedness](https://github.com/8ft0-ai/IssueOps/issues/131#issuecomment-5162671625) and retained [execution deviation](https://github.com/8ft0-ai/IssueOps/issues/131#issuecomment-5162713423);
- PR #132's [final evidence pack](https://github.com/8ft0-ai/IssueOps/pull/132), retained [deviation disclosure](https://github.com/8ft0-ai/IssueOps/pull/132#issuecomment-5162715040), independent review [`4848894063`](https://github.com/8ft0-ai/IssueOps/pull/132#pullrequestreview-4848894063), [merge record](https://github.com/8ft0-ai/IssueOps/pull/132#issuecomment-5172608353) and [post-merge verification](https://github.com/8ft0-ai/IssueOps/pull/132#issuecomment-5172648719);
- issue #113's [post-adaptation reconciliation](https://github.com/8ft0-ai/IssueOps/issues/113#issuecomment-5172649700); and
- portable-bootstrap pilot issue [#121](https://github.com/8ft0-ai/IssueOps/issues/121), including its blocked start, explicit target authority, fresh-context proof, deviation handling and close-out evidence.

This is not a comprehensive prompt-library or handover audit. The baseline covers the required ownership categories and one representative fresh-session proof without treating every historical prompt as a source candidate.

## Responsibility classification

| Classification | Authoritative owner | Session-layer treatment |
| --- | --- | --- |
| Portable-bootstrap responsibility | `BOOTSTRAP.md` and `bootstrap/` | Link a pinned source only when external adoption or first-local-issue handoff is relevant. Do not repeat assessment, posture or handoff instructions. |
| Canonical IssueOps protocol responsibility | `docs/issueops-protocol.md` and its focused Reference pages | Link the lifecycle and exact rules. Do not restate mandatory gates, validation policy, review vocabulary or merge authority. |
| Target-repository responsibility | Current repository instructions and GitHub issues, comments, branches, commits, pull requests, checks and reviews | Discover current facts before action. Current repository state overrides stale summaries. |
| Session-grant fact | Future focused Reference, instantiated by a bounded human or authorised coordinator grant | Carry only invocation facts and an expected starting state. The grant does not prove repository state or create authority beyond its cited record. |
| Session-role boundary | Future focused Reference | Constrain one session's purpose, permitted responsibility and prohibitions. A role label does not grant mutation, review independence, approval or merge authority. |
| Durable-handover transition fact | Real repository-local issue or PR comment by default, governed by future focused Reference | State transition claims and navigation links only. Do not reproduce the issue, PR, checks or complete evidence pack. |
| Evidence or pilot measurement | Separately authorised pilot issues, GitHub evidence and `planning/` close-out records | Record actual proof level, deviations, friction, limitations and adoption outcome. Do not turn examples into evidence. |
| Removable duplication | No enduring owner | Remove copied protocol text, copied repository facts, parallel manifests, repeated evidence packs and handovers with no continuation need. Replace them with canonical links or current-state inspection. |
| Unresolved ownership question | Separately authorised Slice 2 or pilot decision | Resolve only where the baseline does not justify a single owner, particularly exceptional file-based handovers and any later need for machine-readable representation. |

## Ownership matrix

The owner column identifies the canonical record for the concern. Other surfaces may link or summarise it, but they do not share ownership.

| Required concern | Authoritative owner | Permitted session-layer use | Status or caveat |
| --- | --- | --- | --- |
| Repository identity | Current target-repository metadata and the cited primary GitHub record | A session grant names the repository to inspect. | The named repository remains an invocation claim until fetched. |
| External bootstrap source | `BOOTSTRAP.md` and `bootstrap/` | A grant may cite an immutable bootstrap source when adoption is in scope. | Not required for ordinary work in an already governed repository. |
| Local instructions and conventions | Current target-repository instructions, contributor guidance and repository policy | Reconciliation discovers and cites them. | Never replace them with a mandatory copied repository profile. |
| Execution objective and scope | Governing GitHub issue or approved planning record | A grant identifies the primary record and may summarise its objective. | The summary cannot broaden or narrow the governing contract silently. |
| Authority boundary | Governing repository-local issue, within higher repository policy and explicit human authority | A grant states the bounded authority it was given and cites the owner. | Repository access, a role name or a handover never supplies missing authority. |
| Expected starting state | Session grant | State what the receiving session is expected to find. | This is intentionally untrusted until reconciliation. |
| Issue readiness | Readiness or dependency decision on the governing issue | A grant or handover links the latest decision. | Head or dependency movement may make it stale. |
| Branch and pull-request state | Current GitHub branch, commit and pull-request metadata | A handover may name exact refs and SHAs as observed transition facts. | The receiving session must fetch them again. |
| Validation status | Current checks and the exact-head PR evidence pack | A handover links completed, failing, pending or unavailable evidence. | No session may promote pending, unavailable or stale evidence to passed. |
| Review findings | Submitted reviews, conversation comments and inline review threads | A handover links open findings and the reviewed head. | Same-session remediation cannot be represented as independent review. |
| Merge authority | Explicit authorised human decision and repository merge policy | A grant or handover states which decision is still required. | Authority is never inferred from write access, review status or a session role. |
| Execution deviations | Durable issue, PR or close-out deviation record under the canonical policy | A handover links action-relevant deviations and their containment state. | A receiving session verifies containment and stale-evidence effects. |
| First incomplete gate | Current repository-local record set, interpreted through the canonical lifecycle | The receiving session records its reconciled conclusion in the relevant issue or PR. | A handover may propose a gate but does not own the conclusion. |
| Next permitted action | Current repository-local issue or PR comment that combines verified state with the governing authority | A handover may quote or link one bounded next action. | If no current authorised action is recorded, the status is unresolved and the session stops. |
| Required human decision | Explicit issue or PR comment by the authorised human decision-maker | A grant or handover identifies the decision and its location. | Absence of a decision is not implicit approval. |
| Handover verification | Receiving-session reconciliation comment linked to current canonical GitHub records | Record which claims were confirmed, stale, contradicted or unsupported. | Verification must precede action; private chat history is not evidence. |

## Separation of responsibilities

### Bootstrap

`BOOTSTRAP.md` and `bootstrap/` own portable entry, read-only assessment, capability and convention mapping, posture selection, prohibited default changes and the first-local-issue handoff. They do not own normal session invocation after a target repository already has local authority.

### Protocol

`docs/issueops-protocol.md` owns the canonical lifecycle, mandatory gates and human authority boundary. Focused Reference pages own exact lifecycle fields, formats, statuses and blockers. The session layer consumes these rules; it does not reproduce them.

### Target repository

Repository-local issues and approved planning records own intent and authority. Branches and commits own implementation history. Pull requests, checks and review records own final scope, validation and review state. Current GitHub records remain authoritative across every session boundary.

### Session grant

A session grant owns only the facts supplied to invoke one bounded session: which repository and primary record to inspect, which role to perform, what authority has been granted, what starting state is expected and where the session must stop. It is not a protocol, repository profile, approval record or proof of current state.

### Role boundaries

Shape, Deliver, Review or evaluate, and Close and reconcile are responsibility boundaries, not authority sources. The future normative owner must define their invariants and prohibitions without copying the lifecycle procedure. A session that needs another role stops or receives a new explicit grant; it does not silently expand itself.

### Handover transition facts

A real handover remains a GitHub-native issue or PR comment by default. It owns only the outgoing session's transition claims, links, first known incomplete gate, next proposed action and required decision. Underlying state remains with the issue, branch, PR, checks and reviews. Every receiving session verifies action-relevant claims before continuing.

An approved repository file is unresolved as an exceptional handover location. It may be considered later only when a separately authorised cross-session need cannot be served proportionately by a GitHub comment. Such a file would still link canonical GitHub owners and could not become a second state database.

### Pilot evidence

Pilot contracts, observations and close-out decisions belong to separately authorised GitHub issues, PRs and `planning/` records. Examples remain illustrative and cannot prove independent or end-to-end behaviour.

## Source-location decision

### Selected future ownership

The bounded evidence supports the existing-surface hypothesis:

1. **One focused Reference page** should own the exact future session-grant fields, role invariants, durable-handover fields, status meanings and receiving-session verification requirements.
2. **One task-focused How-to guide** should own the procedure for starting or resuming a bounded session. It should link to the canonical lifecycle for delivery, review and close-out steps rather than reproduce those procedures.
3. **One non-normative Example** should illustrate an interrupted session, a GitHub-native handover and fresh-session reconciliation. It must identify itself as illustrative and must not become a template or evidence claim.
4. **Real handovers** should remain repository-local issue or PR comments by default.
5. **Initiative decisions and pilot evidence** should remain in GitHub and `planning/`.

These are source-ownership decisions and a Slice 2 recommendation. They do not create or approve the content, filename or implementation of any future user-facing page.

### Rejected or deferred options

| Option | Decision | Reason |
| --- | --- | --- |
| Separate Reference pages for session grants, each role, handovers and receiving verification | Rejected for Version 0.1 | The concerns form one compact normative contract; splitting them would increase navigation and drift risk before pilots demonstrate a distinct reader need. |
| Separate How-to guides for each role | Rejected for Version 0.1 | Existing lifecycle procedures already own role-specific execution tasks. The missing task is starting or resuming a bounded session. |
| A new top-level `issueops/`, `.github/issueops/`, `prompts/` or similar source area | Rejected | Existing Reference, How-to and Examples surfaces provide the required ownership modes. Symmetry, packaging convenience or possible automation is not evidence of need. |
| `planning/` as the operational source for grants or handovers | Rejected | Planning owns initiative intent, decomposition and evidence navigation, not current user-facing rules or operational state. |
| `BOOTSTRAP.md`, `bootstrap/` or the canonical protocol as the session-contract owner | Rejected | Those sources already have distinct adoption and lifecycle responsibilities. Adding session contracts there would blur handoff boundaries and create duplication. |
| New issue or PR templates in Slice 2 | Deferred | Real handovers should first be proved as ordinary GitHub-native comments. Template support is a later decision only if evidence shows repeated, material omission. |
| Schema, validator, generator, CLI, workflow, service, database, queue or GitHub App | Deferred beyond Version 0.1 | Manual proof must identify a repeated failure that cannot be solved proportionately by the selected documentation and repository-native records. |

## Minimum recommended Slice 2 artefact set

The minimum coherent set is **three substantive artefacts within existing documentation surfaces**:

1. **Normative Reference — session grants, role boundaries and handover verification.** One page should consolidate the exact contract categories and invariants for compact grants, the four roles, durable handovers and receiving-session verification. Consolidation is preferred because these concerns jointly define one transition contract.
2. **How-to — start or resume a bounded IssueOps session.** One procedure should cover both new and resumed sessions, including current-state reconciliation and accurate stopping, while linking to existing lifecycle procedures for implementation, review, remediation and close-out.
3. **Example — interrupted delivery and verified resume.** One non-normative illustration should show a real GitHub-native transition, stale-risk checks and the receiving session's verification outcome without presenting copy-ready operational prompts as canonical.

Navigation-only index changes may accompany those pages but are not separate substantive artefacts. Slice 2 may reuse or extend an existing suitable page when independent review confirms that doing so preserves one clear owner. A smaller two-artefact set is not recommended now because embedding the illustration in Reference would blur norm and example, while embedding it in How-to would risk turning one scenario into the procedure.

No separate role pack, handover template, scorecard template or initiative manifest is recommended. Pilot issues can define their bounded measurement questions, and a later consolidated planning record can compare outcomes.

## Pilot prerequisites

No pilot is authorised by this record. Before a separately authorised pilot begins:

- the approved Slice 2 normative and procedural owners must exist, link to canonical sources and pass independent review;
- the pilot issue must name the exact repository, primary record, role, authority, safe starting point, validation, evidence level and stop boundary;
- the pilot must use real bounded work where practical and must not manufacture repository changes merely to exercise the architecture;
- current repository state must be refreshed before each mutation;
- the expected baseline and comparison measures must be recorded in the pilot issue or its linked planning record;
- human approval and merge authority must remain explicit; and
- no pilot may create automation, hidden coordination state or a parallel lifecycle database.

The required proof set remains:

1. **Planning-only authority boundary:** a Shape session stops without implementation mutation.
2. **Interrupted delivery and fresh-session resume:** a fresh Deliver session verifies a GitHub-native handover, finds the earliest incomplete gate and creates no duplicate issue, branch or pull request. Level 3 fresh independent-agent evidence is required.
3. **Independent review role separation:** a Review or evaluate session verifies the exact head without implementation reasoning, remediation or merge authority. Level 3 evidence is required where independence is claimed.
4. **Bounded end-to-end handover using real work:** at least two roles exchange durable GitHub-native transition records, and the proof includes Close and reconcile behaviour that records intended versus actual delivery and stops at the next decision boundary.

Equivalent evidence for Close and reconcile may be proposed only in the separately reviewed pilot contract; it must not be assumed from delivery or review evidence alone.

## Target workflow or target state

The ownership model is:

```text
portable adoption need
  -> BOOTSTRAP.md and bootstrap/ own assessment and first-local-issue handoff
  -> repository-local issue owns objective, scope and authority
  -> canonical protocol owns lifecycle and mandatory gates
  -> thin session grant supplies bounded invocation facts
  -> receiving session reconciles current GitHub state
  -> one role operates under repository-local authority
  -> issue, branch, PR, checks and reviews retain operational state
  -> GitHub-native handover records transition claims only when continuation is needed
  -> receiving session verifies those claims before action
  -> pilot and adoption evidence remains in GitHub and planning/
```

The selected future Reference, How-to and Example pages are absent until separately authorised Slice 2 delivery is completed and independently accepted.

## Acceptance gates

- [x] The baseline is representative, bounded and linked.
- [x] Every required concern has one authoritative owner or an explicit unresolved status.
- [x] Session-grant facts are separated from repository state and lifecycle rules.
- [x] Role boundaries constrain responsibility without granting authority.
- [x] Handover facts link canonical owners rather than creating parallel state.
- [x] Receiving-session verification remains mandatory.
- [x] Source locations follow the adopted Diátaxis architecture.
- [x] No new top-level operational source directory is selected.
- [x] The recommended Slice 2 set is consolidated to three substantive artefacts.
- [x] Pilot prerequisites are defined without creating or executing pilots.
- [x] Bootstrap, protocol and repository-local owners remain unchanged.
- [x] The next implementation and pilot boundaries require separate authority.

## Proposed implementation slices

### Completed Slice 1 — ownership decision and decomposition

This record classifies responsibilities, assigns owners, selects future source modes, recommends the minimum Slice 2 set and defines pilot prerequisites. It creates no operational session material.

### Separately authorised Slice 2 — minimal manual guidance

A future execution contract may implement the three recommended documentation artefacts, or a smaller independently justified reuse of existing pages, within the existing Diátaxis surfaces. It must define exact paths, content boundaries, validation and independent review before mutation.

### Separately authorised Slice 3 — role and resume pilots

Only after Slice 2 is merged and accepted may separately governed pilots test planning-only authority, interrupted resume, independent review and bounded end-to-end handover.

### Separately authorised Slice 4 — comparative close-out

After pilot evidence exists, a separately governed close-out may compare intended and actual outcomes and recommend `Adopt`, `Adapt` or `Reject`. It must not create speculative automation work.

## Risks and controls

| Risk | Control |
| --- | --- |
| The planning record becomes an operational template | Describe ownership, options and boundaries only; omit copy-ready grants, handovers and role prompts. |
| The future Reference becomes a second protocol | Limit it to session invocation, role and transition invariants; link lifecycle rules to the canonical protocol. |
| A grant or handover becomes stale authority | Treat expected state and transition claims as untrusted until repository-native reconciliation. |
| Roles imply permission | State that role describes responsibility and prohibitions; authority comes from current repository-local records and explicit human decisions. |
| Real handovers duplicate evidence packs | Keep them to action-relevant transition facts and links, and create them only for a genuine continuation need. |
| The future artefact set becomes a prompt pack | Consolidate to one Reference, one How-to and one Example; create no role-specific pack. |
| Pilot examples are mistaken for proof | Keep examples non-normative and record actual evidence in separately authorised GitHub and planning records. |
| Retained history is cleaned up | Preserve the issue #131 and PR #132 deviation records and their exact-head consequences. |
| Issue #90 or automation work is absorbed | Keep issue #90 independently governed and defer every schema or automation question beyond evidence-backed adoption. |

## Unresolved questions and caveats

- Exact Slice 2 filenames and whether an existing page can be extended safely remain implementation decisions for a separately reviewed execution contract.
- The future Reference must decide exact field names, required versus conditional status and role invariants without importing the whole lifecycle.
- The future How-to must decide the shortest safe procedure without becoming a second delivery, review or close-out guide.
- An exceptional file-based handover location remains unresolved until a real cross-session need cannot be served proportionately by a GitHub comment.
- The three-artefact recommendation is evidence-based but not adopted operational guidance. Slice 2 review may consolidate further when it preserves distinct normative, procedural and illustrative ownership.
- The issue #131 and PR #132 no-op commit and repeated connector-action deviation remain material process caveats. This record uses their retained history as evidence and does not normalise it into a clean execution narrative.
- The representative portable-bootstrap pilot demonstrates fresh-context and evidence separation, but it does not by itself prove the modular session contract.

## Definition of done

Slice 1 is complete when:

- [x] the ownership and classification decision is recorded;
- [x] all required concerns are assigned or explicitly unresolved;
- [x] selected and rejected source-location options are explained;
- [x] the minimum recommended Slice 2 set is explicit and proportionate;
- [x] pilot prerequisites include planning-only, interrupted-resume, independent-review and Close-and-reconcile proof;
- [x] non-goals, risks, caveats and retained deviations are visible;
- [x] the active roadmap remains unchanged;
- [x] no operational artefact or pilot is created; and
- [ ] this exact two-file Slice 1 change is independently reviewed and merged under repository-owner authority.

## Likely next decision boundary

The next boundary is a new, independently reviewed Slice 2 execution issue.

That issue may authorise only the smallest accepted documentation change within existing Reference, How-to and Examples surfaces. It must specify exact paths, the relationship to current canonical documentation, final-head validation and independent review. It must not authorise pilots, templates in GitHub configuration, schemas, generators, automation or adoption.

Pilot issue creation remains a later decision after Slice 2 is merged and independently accepted.

## Operating and autonomy boundary

This record authorises no further repository mutation.

Future grants, role definitions, handover rules, examples and pilots require their own repository-local issues, readiness decisions, implementation plans, feature branches, final-head validation, evidence packs and independent reviews. Current target-repository instructions and human authority govern every mutation.

A session grant, role name, handover or repository access does not grant approval or merge authority. Human decisions remain explicit unless a repository owner separately provides bounded delegation under the canonical gates.

## Non-goals

This decision does not:

- create a session-grant or handover template;
- create role-specific operational prompts;
- create or execute a pilot;
- define a machine-readable schema;
- create a validator, generator, CLI, workflow, service, database, queue or GitHub App;
- create a new top-level operational directory;
- modify `BOOTSTRAP.md`, `bootstrap/` or `docs/issueops-protocol.md`;
- implement issue #90;
- remove or migrate existing prompts;
- alter settings, permissions, checks, protection or merge authority;
- automate claiming, execution, review, merging or publication;
- adopt the modular session architecture; or
- represent this same-session planning review as independent evidence.
