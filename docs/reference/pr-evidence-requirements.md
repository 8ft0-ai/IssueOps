# Pull-request evidence requirements

The pull request is the evidence pack for one execution-contract issue. It must let a human reviewer compare the final repository change with the issue without relying on private chat history or memory.

This page is the canonical reference for evidence-pack content and the normal deliberate evidence-collection contract.

## Required sections

Every pull request should record:

| Section | Required content |
| --- | --- |
| **Execution contract** | Exactly one canonical `Issue #<issue-number>` declaration under `## Execution contract`. GitHub closing keywords are optional lifecycle syntax, not the canonical IssueOps linkage. |
| **Lifecycle authority** | Durable references for readiness, the detailed implementation plan, the separate human approval of that plan, and any additional procedural authority required by the work or explicit `N/A`. |
| **Parent or roadmap** | The governing stage or initiative when one materially constrains the issue. |
| **Changed** | Files, behaviours or documentation areas changed and the purpose of the change. |
| **Deliberately excluded** | Relevant non-goals and adjacent work not included. |
| **Acceptance criteria** | How the final state satisfies the issue criteria. |
| **Validation status** | Checks actually performed, checks not performed or pending, and evidence tied to the final head. |
| **Post-merge verification** | Named checks that can run only after merge, deployment or environment configuration. |
| **Risks and caveats** | Remaining uncertainty, assumptions, limitations and residual risk. |
| **Groundedness review** | The pre-approval review of issue alignment, lifecycle authority, scope control, validation evidence and risk. |
| **Final recommendation** | `Approve`, `Approve after minor fixes`, or `Do not approve yet`. |
| **Merge authorisation** | The source and limit of delegated merge authority where applicable. |

The pull request body must describe the final head. After material remediation, update it or add a clearly labelled evidence comment that makes the final state equally visible.

## Execution-contract linkage

The canonical IssueOps pull-request declaration is:

```md
## Execution contract

Issue #123
```

`Issue #<issue-number>` must be an exact standalone line inside one `## Execution contract` section. The normal case identifies exactly one governing issue in the same repository. The issue remains the execution contract; the pull request only identifies it.

`Closes #123`, `Fixes #123` and `Resolves #123` remain valid GitHub lifecycle syntax when merge should deliberately close an issue, but they are not the canonical IssueOps evidence linkage. A canonical declaration may coexist with matching closing syntax. If canonical and closing references identify different issues, the evidence linkage is conflicting and must not be guessed.

For historical compatibility, a single closing-keyword reference may still be recognised when no canonical declaration is present. That fallback is not the normal form for new IssueOps pull requests. Multiple legacy closing references remain conflicting.

Missing canonical/legacy linkage is incomplete evidence. Multiple execution-contract sections, multiple canonical declarations, or an `Issue`-shaped malformed declaration inside the canonical section are conflicting evidence. These states must not produce a false mechanical `complete` result.

## Lifecycle authority

The normal implementation PR evidence pack records these durable GitHub-native authority references:

```text
readiness assessment
detailed implementation plan
human approval of implementation plan
additional procedural authority: N/A or governing durable record
```

The detailed implementation plan and its human approval are separate records. The plan describes the proposed execution path; it does not authorise itself. Explicit human approval of that plan must exist before branch creation or implementation mutation begins, must clearly apply to the plan being executed, and must be durable in the repository record.

Required authority must predate the action it authorises. A comment created after implementation has already begun cannot be used to manufacture normal pre-action authority retrospectively. When the required pre-implementation human plan approval is missing or retrospective, the lifecycle record is defective and the PR must not receive an `Approve` recommendation merely because the implementation and technical validation are otherwise satisfactory.

Additional procedural authority is conditional. Record `N/A` when the governing work requires no additional procedural mutation. When `/collect-evidence` or another governed procedural mutation is used, record the durable authority that permits that action; repository collaborator status or connector capability is not a substitute for IssueOps procedural authority.

These lifecycle-authority fields are human review evidence. This requirement does not add automated semantic approval inference to the evidence collector or change the collector's mechanical completeness schema.

Implementation-plan approval is also distinct from later merge authority. The earlier approval permits the approved implementation path to begin; merge remains a separate human decision after substantive review of the final state.

## Deliberate evidence collection

The normal comment-triggered collection command is the exact zero-argument pull-request comment:

```text
/collect-evidence
```

### IssueOps authority and GitHub eligibility

Posting the command is an IssueOps repository mutation and requires explicit procedural authority from the current governing issue/session grant for the pull request in scope. Repository collaborator status, connector write capability or GitHub effective permission does not by itself grant that IssueOps authority.

After a newly created exact command comment is posted on a pull request, the repository-owned workflow independently enforces GitHub platform eligibility before collection:

- the event must be a newly created pull-request comment whose body is exactly `/collect-evidence`;
- the pull-request number is derived from the event, not from comment-supplied text;
- the target must still resolve as an open/current pull request in this repository;
- the comment actor's current effective repository permission must resolve to `write` or `admin`; and
- permission, API or context uncertainty fails closed before evidence collection.

The comment cannot select another pull request, ref, workflow name, arbitrary input map or shell fragment.

The workflow retains these explicit read-only repository permissions:

```text
contents: read
pull-requests: read
issues: read
checks: read
actions: read
```

The collector does not gain issue, pull-request, review, branch, commit, file, merge or settings mutation authority through this path.

### Request identity and correlation

For the comment-triggered path:

- one newly created exact command comment ID is one IssueOps request identity;
- editing or deleting that comment is not a new request;
- a second newly created exact command comment is a new deliberate request; and
- a GitHub workflow rerun is another attempt in the existing workflow-run lineage, not a new IssueOps request.

A comment-triggered result must be reconstructable as:

```text
request comment ID
  -> workflow run ID
  -> run attempt / terminal conclusion
  -> run summary / evidence artifact
```

The workflow summary records the trigger kind, pull-request number, request comment ID for comment-triggered runs, workflow run ID and run attempt. Manual `workflow_dispatch` remains a distinguishable fallback and has no request comment ID.

A run that has not reached a terminal conclusion is pending evidence. Pending collection must not be represented as a successful terminal result.

### Summary, artifact and durable record

When the collector reaches a report-producing result, generated evidence is exposed in the Actions run summary and uploaded as the short-lived artifact:

```text
evidence-pack-pr-<PR>-<run-id>
```

The workflow currently retains that artifact for seven days. The artifact is supporting evidence, not permanent governance evidence.

When a collection result is action-relevant to an IssueOps decision, the governing durable issue/PR record should preserve enough correlation to reconstruct the observation after artifact expiry, including:

- request comment ID for comment-triggered collection;
- workflow run ID;
- run attempt;
- terminal conclusion;
- artifact availability; and
- artifact retention/expiry status or date where available.

### Snapshot currentness

A collection is a snapshot of repository evidence for one pull request and decision-relevant state. The evidence pack records exact-target/current-head evidence; later material head, validation or review-state changes can make an earlier snapshot stale for the next decision.

When refreshed evidence is needed and the current session remains authorised, a new exact command comment creates a new deliberate request and snapshot. That new request does not itself approve the pull request, resolve review findings or advance the IssueOps lifecycle.

## Evidence sources

Distinguish where evidence comes from.

### Inline review-thread evidence

Submitted pull-request reviews and inline review-thread resolution are separate repository-observed evidence surfaces. A submitted review state such as `APPROVED`, a review count, or the absence of requested changes must never be used to infer that inline review threads are resolved.

When the repository-owned collector can completely retrieve GitHub's read-only `pullRequest.reviewThreads` surface under its existing token permission ceiling, the `pr.review-threads` evidence item records:

- `total_threads` — the declared total inline thread count;
- `unresolved_threads` — threads whose `isResolved` value is `false`;
- `resolved_threads` — threads whose `isResolved` value is `true`;
- `complete: true` — only after bounded cursor pagination terminates and the collected node count exactly matches the declared total; and
- `retrieval_surface: GitHub GraphQL pullRequest.reviewThreads` — the source contract used for the observation.

Review-thread pagination is bounded by the collector's existing page safety limit. GraphQL errors, transport failures, missing or malformed connection data, inconsistent totals, malformed thread nodes, missing or non-advancing continuation cursors, page-limit exhaustion, or a final collected-count/declared-total mismatch fail closed. In those cases `pr.review-threads` is classified `unavailable`, records `complete: false`, contributes a collection error, and makes the evidence pack mechanically incomplete.

The collector does not broaden workflow permissions to obtain this evidence. If the retained Actions `GITHUB_TOKEN` cannot access the required review-thread surface, the truthful result is unavailable/incomplete until a separately governed permission decision changes that boundary.

A mechanically complete review-thread surface only means the requested metadata was completely collected. It does not determine whether review findings are substantively resolved, whether the pull request satisfies its execution contract, or whether approval or merge is appropriate.

### Repository-observed evidence

Examples include:

- the final changed-file list and diff;
- file contents read from the branch;
- commit and head SHA;
- GitHub Actions checks and workflow logs;
- generated artefacts;
- review comments and unresolved threads;
- mergeability and branch state; and
- post-merge repository or deployment state.

### Contributor assertions

Examples include:

- why a change was made;
- what was deliberately excluded;
- assumptions and caveats;
- manual validation performed outside the repository; and
- interpretation of acceptance criteria.

Assertions should be specific and supported where possible. They are not equivalent to repository-observed evidence.

### Human decisions

A human reviewer or repository owner decides:

- whether an implementation plan is approved before implementation begins;
- whether evidence is trustworthy and sufficient;
- whether the implementation satisfies the contract;
- whether scope and non-goals were respected;
- whether residual risk is acceptable; and
- whether approval and merge should occur.

An agent-generated groundedness review is transparent analysis in the evidence pack. It is not independent human review and does not itself grant implementation, approval or merge authority.

## Validation status

Separate evidence that exists before merge from checks that can only exist afterwards.

```md
## Validation status

Pre-merge validation completed:

- [x] ...

Validation not performed or pending:

- None / exact pending check and reason.

Post-merge verification required:

- None / exact check, owner and evidence to record.
```

Do not mark a check complete unless it ran successfully against the relevant final state.

Pending validation blocks merge when it is needed to decide whether the implementation is correct, when available validation is failing, when the implementation is incomplete, or when the evidence pack would otherwise be misleading.

Post-merge verification may remain when:

- implementation is complete;
- available validation is not failing;
- the remaining check cannot run before merge or deployment;
- the check and residual risk are explicit; and
- the authorised human accepts that residual risk.

## Groundedness review

The groundedness review answers:

1. Did we do what was needed?
2. Did we only do what was asked?

It should address:

- issue alignment;
- lifecycle authority;
- scope control;
- validation evidence;
- risks and caveats; and
- one final recommendation.

Do not recommend approval when required pre-implementation authority is missing or retrospective, validation is materially incomplete, scope has drifted, the final evidence is stale, a material review finding remains unresolved or the implementation does not satisfy the issue.

## Material remediation

Evidence must be refreshed when remediation changes:

- validation status;
- security or permissions posture;
- dependency model;
- deployment behaviour;
- public claims;
- files outside the previously stated scope;
- assumptions or caveats; or
- remaining checks.

When material remediation or another decision-relevant head, validation or review-state change occurs after evidence collection, treat the earlier collection as a prior snapshot. If a fresh collection is required, request it deliberately under current authority and correlate it as a new request.

Minor wording fixes may be handled in a review reply when they do not change meaning, scope, validation or risk.

## Related guidance

- [Prepare a pull-request evidence pack](../how-to/prepare-pr-evidence-pack.md)
- [Review a pull request against its contract](../how-to/review-pr-against-contract.md)
- [PR evidence templates](pr-evidence-templates.md)
- [Review decisions and merge blockers](review-decisions-and-merge-blockers.md)
- [Why evidence is not approval](../explanation/pr-evidence-and-approval.md)
