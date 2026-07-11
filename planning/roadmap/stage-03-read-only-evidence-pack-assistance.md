# Stage 3 — Read-only evidence-pack assistance

Status: completed.

Record type: contemporaneous.

Approved through [planning issue #75](https://github.com/8ft0-ai/IssueOps/issues/75) on 11 July 2026. Delivery proceeded through Issues #76, #78, #80 and #82, with recovery through Issue #84 after the premature merge of PR #83. The final close-out evidence is carried by PR #85.

Close-out decision: **Adapt**. Retain the bounded read-only capability for controlled use, but address explicit non-closing execution-contract linkage and manual invocation friction before broader adoption.

## Problem statement

Stage 2 proved that the IssueOps operating model can produce strong repository-native evidence while preserving human contract and merge authority. It also showed that a contributor repeatedly gathers and reconciles evidence spread across the issue contract, readiness and planning comments, pull-request metadata, changed-file scope, head commits, workflow runs, validation results, review discussion and post-merge records.

The evidence exists, but assembling a current and provenance-linked review view is repetitive and error-prone. Validation may move from pending to complete, a skipped deployment may be expected rather than a failure, and assertions written in a pull-request body may differ from repository-observed state. Stage 3 therefore selected one bounded capability to reduce this coordination cost without deciding whether the contract is satisfied or transferring repository mutation, merge or publication authority.

## Outcome to prove

Demonstrate that a manually invoked, read-only capability can generate a current, structured and provenance-linked evidence report for one pull request, reducing manual evidence-assembly effort while:

- preserving the issue and written repository record as the authority;
- distinguishing contributor assertions from repository-observed facts;
- representing incomplete, unavailable and pending validation honestly;
- making no repository, issue, pull-request, review, merge or publication mutations; and
- leaving evidence sufficiency and all approval decisions to a human.

The stage was also required to close with an explicit **adopt**, **adapt** or **reject** decision. It closed with **Adapt** because live dogfood proved the core safety and usefulness while exposing contract-linkage and invocation limitations.

## Goals

- Collect the minimum GitHub-native facts needed to support a pull-request evidence review.
- Render those facts into a stable, concise evidence snapshot with direct provenance links.
- Make stale, missing, pending and conflicting evidence visible.
- Reduce repeated transcription and reconciliation work.
- Establish a reusable evidence and provenance model for possible later capabilities.
- Prove the capability through repository-native dogfood and an explicit decision.

## Non-goals

- No automatic issue-readiness decision or implementation-plan approval.
- No lifecycle transition, label mutation or remediation classification.
- No branch, commit, issue, pull-request, review or thread mutation by the capability.
- No approval, merge, publication or deployment recommendation.
- No merge or auto-merge.
- No unrestricted issue-to-agent execution.
- No broad orchestration platform.
- No cross-repository or organisation-wide evidence service in this stage.
- No assumption that generated summaries are independently verified evidence.
- No lifecycle-assistance implementation.

## Operating and autonomy boundary

The selected capability is **read-only pull-request evidence collection and evidence-pack assistance**.

It accepts exactly one repository pull-request target per run and produces an ephemeral evidence report.

### It may read

Where available and relevant:

- linked issue and pull-request metadata;
- pull-request title, body, state, draft state, base and head references;
- current head commit SHA;
- changed-file names and diff statistics;
- pull-request conversation comments and submitted reviews;
- check and pull-request workflow-run metadata;
- workflow job outcomes;
- source URLs and timestamps needed for provenance; and
- repository evidence templates and declared validation guidance.

The delivered implementation does not collect unresolved inline review-thread state. That omission is recorded in the close-out decision.

### It may produce

- deterministic Markdown and structured-data evidence snapshots;
- collection timestamps and resolved head SHA;
- direct links to material sources;
- separate sections for repository-observed facts, contributor assertions, pending or unavailable evidence and collection errors;
- an explicit human-verification and decision warning; and
- a run summary and downloadable run artefact.

### It may not write

- issues or issue comments;
- pull-request bodies, comments, reviews or threads;
- labels, milestones or assignments;
- branches, commits, files or tags;
- merge state, auto-merge state or repository settings;
- publication, deployment or release state; or
- external systems.

The capability operates with read-only repository permissions. Manual triggering is permitted; standing automatic invocation is not part of the boundary.

### Human authority retained

Humans retain exclusive authority over:

- confirming issue readiness and approving implementation plans;
- accepting scope changes;
- deciding whether a linked issue or acceptance criterion is satisfied;
- classifying material remediation;
- deciding whether missing or pending evidence is acceptable;
- interpreting risks and caveats;
- approving merge, publication or release; and
- adopting, adapting or rejecting the capability.

The report may state that evidence is present, absent, pending, unavailable or inconsistent. It must not convert those observations into an approval recommendation.

## Target workflow or target state

```text
human selects one pull request
  -> manually invokes read-only evidence collection
  -> collector resolves the PR and current head SHA
  -> collector reads bounded GitHub-native evidence surfaces
  -> collector verifies that the head SHA remained stable
  -> collector renders a provenance-linked evidence snapshot
  -> human checks sources and interprets gaps
  -> human decides what evidence to retain and what action, if any, is authorised
```

The generated report is an input to human review, not a replacement for the execution contract or contract-verification decision.

### Evidence model

Every material item is classified as one of:

- **Repository-observed** — directly retrieved from GitHub state.
- **Contributor-reported** — stated in an issue, plan, PR body or comment but not independently proved by collection.
- **Derived** — mechanically computed from observed facts.
- **Pending** — a declared check or result has not completed.
- **Unavailable** — the source could not be accessed or does not expose the evidence.
- **Conflicting** — sources disagree or cannot be reconciled safely.

Generated prose is marked as generated. Source links, retrieval time and resolved identifiers remain visible.

### Safety and failure model

- Repeated runs for the same head and source state produce materially equivalent, stably ordered output and no duplicate repository actions.
- The PR head is resolved at the start and end; a change stops the completeness claim.
- Partial API failure retains safe facts, records the failure and produces a non-complete report.
- Pagination and workflow-run limits fail incomplete rather than silently omitting data.
- An unresolved target, insufficient authentication, ambiguous source identity or unclassifiable evidence activates a circuit breaker.
- Manual recovery requires only source inspection and rerun because the collector makes no repository mutations.
- Full workflow logs are not ingested by default.

## Acceptance gates

- [x] A documented schema distinguishes repository-observed, contributor-reported, derived, pending, unavailable and conflicting information.
- [x] One pull request can be processed through a manual, read-only invocation.
- [ ] The live report records the linked execution-contract issue without relying on auto-closing syntax. The implementation supports closing-keyword linkage, but PR #85 intentionally used no closing keyword and the issue was omitted; this is the primary Adapt gap.
- [x] The report records repository, pull request, resolved head SHA, changed-file scope and collection timestamp.
- [x] Relevant checks and workflows are linked without treating skipped, pending or unavailable results as success.
- [x] Contributor assertions are visibly separated from independently observed GitHub state.
- [x] Every material reported fact has a source link or is explicitly marked derived.
- [x] The capability performs no issue, PR, label, branch, file, merge, publication or settings mutations.
- [x] Repeated collection creates separate run-scoped artefacts and no duplicate repository actions.
- [x] Moving-head and partial-API-failure tests produce non-complete results and activate fail-closed behaviour.
- [x] Repository-native tests cover rendering, classification, pagination, completeness and error handling.
- [x] A representative pending-to-final dogfood sequence was completed against PR #85.
- [x] Manual and assisted effort were compared using the same evidence requirements.
- [x] The dogfood record confirms that the capability stayed within its authority boundary.
- [x] Limitations, missing evidence and unintended consequences are documented.
- [x] Close-out records an explicit **Adapt** decision.

## Proposed implementation slices

The four approved slices were delivered in order:

1. **Formalise the approved Stage 3 roadmap** — Issue #76 / PR #77.
2. **Define the evidence schema and deterministic collector core** — Issue #78 / PR #79.
3. **Add manually invoked read-only GitHub integration** — Issue #80 / PR #81.
4. **Dogfood, measure and close out** — Issue #82, recovery Issue #84 and PR #85.

The slices did not absorb lifecycle assistance, execution triggering, post-merge automation or merge authority.

## Risks and controls

### Generated output mistaken for verified evidence

Control: classify every item, retain provenance, mark generated sections and require human verification.

### Stale evidence assembled across commits

Control: resolve and recheck the head SHA and stop completeness claims when it changes.

### Incomplete API results appear complete

Control: explicit pagination, bounded collection, surfaced errors and non-complete outcomes.

### Contributor assertions treated as repository facts

Control: separate contributor-reported content from repository-observed state.

### Skipped or unavailable validation treated as success

Control: explicit pending, skipped, unavailable and conflicting states; never infer success from absence.

### Capability becomes a review or lifecycle bot

Control: prohibit approval recommendations, state transitions, comments, labels and writes.

### Permissions expand during implementation

Control: least-privilege read permissions and validation evidence. Live logs confirmed read-only Actions, Checks, Contents, Issues, Metadata and Pull Requests permissions.

### Manual automation is operationally fragile

Control: record branch-selection and timing friction honestly. Any improvement requires a separate planning and execution contract.

### Advisory gates are bypassed

Control: the PR #83 incident is retained as evidence. No repository-setting change is authorised by this stage.

## Definition of done

Stage 3 close-out completed the following:

- [x] approved execution slices were delivered or explicitly resolved;
- [x] the read-only capability passed repository-native validation;
- [x] a representative pending-to-final live dogfood sequence was completed;
- [x] safe-failure and recovery behaviour has evidence;
- [x] manual and assisted effort were compared;
- [x] the authority audit confirmed no unapproved mutations or decisions;
- [x] limitations and deviations are recorded honestly;
- [x] a completed Stage 3 delivery record exists in this close-out PR;
- [x] the delivery index and concise log are updated in this close-out PR;
- [x] the material Stage 3 decision is represented in the delivery graph; and
- [x] the next capability question is recorded without speculative execution work.

## Likely next decision boundary

The next activity, if any, is a planning question about adapting:

- explicit execution-contract linkage that does not require a closing keyword; and
- manual invocation and target-selection ergonomics.

No next-stage implementation issue is created by this close-out. Advisory lifecycle visibility, post-merge reporting, bounded execution triggering and auto-merge remain unauthorised unless new evidence justifies their authority cost.
