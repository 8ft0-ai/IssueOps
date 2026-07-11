# Stage 3 — Read-only evidence-pack assistance

Status: delivering.

Record type: contemporaneous.

Approved through [planning issue #75](https://github.com/8ft0-ai/IssueOps/issues/75) on 11 July 2026. The deterministic evidence schema and local renderer were delivered through [issue #78](https://github.com/8ft0-ai/IssueOps/issues/78) and PR #79. Delivery continues through [issue #80](https://github.com/8ft0-ai/IssueOps/issues/80), which adds manually invoked, read-only GitHub collection for one pull request. Representative dogfood, measurement and adoption remain the final bounded slice.

## Problem statement

Stage 2 proved that the IssueOps operating model can produce strong repository-native evidence while preserving human contract and merge authority. It also showed that a contributor must repeatedly gather and reconcile evidence spread across the issue contract, readiness and planning comments, pull-request metadata, changed-file scope, head commits, workflow runs, validation results, review discussion and post-merge records.

The evidence exists, but assembling a current and provenance-linked review view remains repetitive and error-prone. Validation may move from pending to complete, a skipped deployment may be expected rather than a failure, and assertions written in a pull-request body may differ from repository-observed state. The first Stage 3 capability should reduce this coordination cost without deciding whether the contract is satisfied or transferring any repository mutation, merge or publication authority.

## Outcome to prove

Demonstrate that a manually invoked, read-only capability can generate a current, structured and provenance-linked evidence report for one pull request, reducing manual evidence-assembly effort while:

- preserving the issue and written repository record as the authority;
- distinguishing contributor assertions from repository-observed facts;
- representing incomplete, unavailable and pending validation honestly;
- making no repository, issue, pull-request, review, merge or publication mutations; and
- leaving evidence sufficiency and all approval decisions to a human.

The stage succeeds only if the capability is useful in a representative real workflow and safe when repository data is incomplete, changes during collection or cannot be retrieved.

## Goals

- Collect the minimum GitHub-native facts needed to support a pull-request evidence review.
- Render those facts into a stable, concise evidence snapshot with direct provenance links.
- Make stale, missing, pending and conflicting evidence visible.
- Reduce repeated transcription and reconciliation work.
- Establish a reusable evidence and provenance model for possible later capabilities.
- Prove the capability through repository-native dogfood and an explicit adopt, adapt or reject decision.

## Non-goals

- No automatic issue-readiness decision.
- No implementation-plan approval.
- No lifecycle transition or label mutation.
- No branch, commit, issue or pull-request creation by the capability.
- No pull-request body or comment posting or editing.
- No automatic remediation classification.
- No approval recommendation.
- No merge or auto-merge.
- No publication or deployment decision.
- No unrestricted issue-to-agent execution.
- No post-merge verification automation beyond reporting already observed GitHub-native facts.
- No broad orchestration platform.
- No cross-repository or organisation-wide evidence service in the first increment.
- No assumption that generated summaries are independently verified evidence.
- No lifecycle-assistance implementation in this stage.

## Operating and autonomy boundary

The selected first capability is **read-only pull-request evidence collection and evidence-pack assistance**.

It accepts exactly one repository pull-request target per run and produces an ephemeral evidence report.

### It may read

Where available and relevant:

- the linked issue body and issue comments;
- pull-request title, body, state, draft state, base and head references;
- current head commit SHA and mergeability metadata;
- changed-file names and diff statistics;
- pull-request conversation comments;
- submitted reviews and unresolved review-thread state;
- commit status and pull-request workflow-run metadata;
- workflow job and step outcomes;
- artefact metadata, without treating artefact existence as proof of content correctness;
- repository evidence templates and declared validation guidance; and
- source URLs and timestamps needed for provenance.

### It may produce

- a deterministic Markdown or structured-data evidence snapshot;
- an execution timestamp and resolved head SHA;
- direct links to every material source;
- sections for repository-observed facts, contributor-reported assertions, pending or unavailable evidence and collection errors;
- an explicit statement that human verification and decision are still required; and
- a workflow summary or downloadable run artefact if implementation uses GitHub Actions.

### It may not write

- issues or issue comments;
- pull-request bodies, comments, reviews or threads;
- labels, milestones or assignments;
- branches, commits, files or tags;
- workflow configuration outside an independently approved implementation change;
- merge state, auto-merge state or repository settings;
- publication, deployment or release state; or
- external systems.

The first adopted capability must operate with read-only repository permissions. Manual triggering of the report is permitted; standing automatic invocation is not part of the initial boundary.

### Human authority retained

Humans retain exclusive authority over:

- confirming issue readiness;
- approving implementation plans;
- accepting scope changes;
- deciding whether a linked issue or acceptance criterion has been satisfied;
- classifying material remediation;
- deciding whether missing or pending evidence is acceptable;
- interpreting risks and caveats;
- approving merge;
- approving publication or release; and
- adopting, adapting or rejecting the Stage 3 capability.

The report may state that evidence is present, absent, pending, unavailable or inconsistent. It must not convert those observations into an approval recommendation.

## Target workflow or target state

```text
human selects one pull request
  -> manually invokes read-only evidence collection
  -> collector resolves issue, PR and current head SHA
  -> collector reads configured GitHub-native evidence surfaces
  -> collector verifies that the head SHA remained stable during collection
  -> collector renders a provenance-linked evidence snapshot
  -> human checks the sources and corrects interpretation where required
  -> human decides what evidence to record and whether any next action is authorised
```

The generated report is an input to human review, not a replacement for the pull-request evidence pack or contract-verification decision.

### Evidence model

Every material item must be classified as one of:

- **Repository-observed:** directly retrieved from GitHub state, such as head SHA, changed files or workflow conclusion.
- **Contributor-reported:** stated in an issue, plan, pull-request body or comment but not independently proved by collection.
- **Derived:** mechanically computed from observed facts, such as counts or whether the head changed during the run.
- **Pending:** a declared check or result has not completed.
- **Unavailable:** the source could not be accessed or the repository does not expose the evidence.
- **Conflicting:** two sources disagree or the report cannot reconcile them safely.

Generated prose must be marked as generated. Source links, retrieval time and resolved commit or run identifiers must remain visible.

### Safety and failure model

#### Idempotency

For the same pull request, resolved head SHA and source state, repeated runs should produce materially equivalent structured output with stable ordering. A rerun must not create comments, labels or other duplicate repository actions.

#### Stale-head protection

Resolve the pull-request head SHA at the beginning and end of collection. If it changes, stop the completeness claim and report that the result is stale or incomplete. Do not silently mix evidence from different heads.

#### Partial failure

If a required source cannot be read:

- retain any safely collected facts;
- mark the affected section unavailable or incomplete;
- record the retrieval error without exposing credentials or sensitive data;
- do not mark the report complete; and
- return a failure or incomplete status suitable for repository-native validation.

#### Duplicate prevention

The first increment performs no issue or pull-request writes. Workflow summaries or artefacts, if used, are scoped to the individual run and identified by run ID and target head SHA.

#### Circuit breaker

Stop evidence collection or completeness claims when:

- the repository or pull-request target cannot be resolved;
- authentication does not provide the declared read access;
- the pull-request head changes during collection;
- pagination or API failure makes a required evidence set incomplete;
- source identity is ambiguous;
- the collector encounters data it cannot classify safely; or
- output would imply success from missing or contradictory evidence.

#### Manual recovery

A human may inspect the linked sources, correct repository records if needed and rerun the collector. Recovery requires no rollback because the capability makes no repository mutations.

#### Sensitive-data control

Collect metadata and bounded evidence needed for review. Do not ingest or reproduce full workflow logs by default. Any later proposal to inspect logs must have its own secret-redaction, size and authority review.

## Acceptance gates

- [ ] A documented evidence schema distinguishes repository-observed, contributor-reported, derived, pending, unavailable and conflicting information.
- [ ] One pull request can be processed through a manual, read-only invocation.
- [ ] The report records repository, pull request, linked issue, resolved head SHA, changed-file scope and collection timestamp.
- [ ] Relevant checks or workflow results are linked and represented without treating skipped, pending or unavailable results as success.
- [ ] Contributor assertions are visibly separated from independently observed GitHub state.
- [ ] Every material reported fact has a source link or is explicitly marked derived.
- [ ] The capability performs no issue, pull-request, label, branch, file, merge, publication or repository-setting mutations.
- [ ] Repeated collection for an unchanged target is idempotent and does not create duplicate actions.
- [ ] A moving-head or partial-API-failure case produces an incomplete result and activates the circuit breaker rather than a misleading complete report.
- [ ] Repository-native tests cover rendering, classification, pagination or completeness behaviour and error handling.
- [ ] One representative end-to-end dogfood run is completed against a real Stage 3 pull request.
- [ ] Manual versus assisted effort is compared using the same evidence requirements.
- [ ] The dogfood record confirms that the capability stayed within its authority boundary.
- [ ] Limitations, false positives, missing evidence and unintended consequences are documented.
- [ ] Stage close-out records an explicit **adopt**, **adapt** or **reject** decision.

## Proof plan

### Representative dogfood

Use one real, bounded Stage 3 implementation pull request with:

- a linked execution-contract issue;
- readiness and implementation-plan comments;
- repository-native validation;
- at least one validation-state transition, such as pending to completed, or one intentionally skipped job;
- a small, reviewable diff; and
- no requirement for production publication.

Run the evidence collector at least twice:

1. while a relevant check is pending or incomplete; and
2. after the same check reaches its final state.

The reports should show the state change without rewriting or mutating the pull request.

### Safe-failure proof

Exercise at least:

- an invalid or inaccessible pull-request target;
- a fixture or controlled test representing partial API failure;
- a head-SHA change during collection or equivalent deterministic test; and
- missing workflow or review data that is validly absent.

### Effort comparison

For the representative pull request, record:

- manual steps and elapsed effort required to assemble the defined evidence fields;
- assisted steps and elapsed effort using the generated report;
- fields omitted or incorrectly transcribed in either path;
- time still required for human interpretation; and
- whether the report reduced work without weakening review quality.

The comparison is evidence for a decision, not a predetermined productivity claim.

## Proposed implementation slices

These slices are approved as an ordered planning model. Each still requires its own execution-contract issue, readiness assessment, implementation plan, validation and human review. Capability implementation must not be inferred from approval of this roadmap.

```text
1. Formalise the approved Stage 3 roadmap
   - add the reviewed roadmap record and roadmap index entry
   - record status as approved after owner approval

2. Define the evidence schema and deterministic collector core
   - source classification and provenance model
   - stable rendering and fixture-based tests
   - no repository writes

3. Add manually invoked read-only GitHub integration
   - one pull-request target per run
   - least-privilege read permissions
   - report only to run summary or artefact
   - repository-native integration and failure tests

4. Dogfood, measure and close out
   - real Stage 3 pull-request run before and after validation completion
   - manual-versus-assisted comparison
   - authority-boundary audit
   - adopt, adapt or reject decision
   - completed delivery record, ledger and material graph update if warranted
```

Slices 2–4 must not absorb lifecycle assistance, execution triggering, post-merge automation or merge authority.

## Risks and controls

### Risk: generated output is mistaken for verified evidence

Control: classify every item, retain provenance, mark generated sections and require human verification.

### Risk: stale evidence is assembled across different commits

Control: resolve and recheck the head SHA; stop completeness claims when it changes.

### Risk: incomplete API results appear complete

Control: handle pagination explicitly, surface retrieval failures and use an incomplete outcome rather than silent omission.

### Risk: contributor assertions are treated as repository facts

Control: separate contributor-reported content from repository-observed state.

### Risk: skipped or unavailable validation is treated as success

Control: use explicit pending, skipped, unavailable and conflicting states; never infer success from absence.

### Risk: the capability becomes a review or lifecycle bot

Control: prohibit approval recommendations, state transitions, comments, labels and writes in the approved boundary.

### Risk: permissions expand during implementation

Control: require least-privilege read permissions and fail validation if write permissions are introduced without a new approved roadmap decision.

### Risk: the first increment becomes a general evidence platform

Control: support one repository and one pull-request target per run, with GitHub-native inputs only.

## Definition of done

Stage 3 is complete when:

- [ ] the approved execution issues are complete or explicitly resolved;
- [ ] the read-only capability has passed repository-native validation;
- [ ] a representative end-to-end dogfood run has been completed;
- [ ] safe-failure and recovery behaviour has evidence;
- [ ] manual and assisted effort have been compared;
- [ ] the authority-boundary audit confirms no unapproved mutations or decisions;
- [ ] limitations and deviations are recorded honestly;
- [ ] a completed Stage 3 delivery record exists;
- [ ] the delivery log is updated;
- [ ] the delivery graph is updated only if close-out creates a material causal decision point; and
- [ ] the next capability question is recorded without speculative execution work.

## Likely next decision boundary

If the capability is adopted, decide whether the proved evidence model should next support:

- advisory lifecycle visibility;
- bounded post-merge verification reporting; or
- no further automation until evidence from broader repositories exists.

Bounded execution triggering and auto-merge remain outside that next decision unless new evidence justifies reconsidering their authority cost.
