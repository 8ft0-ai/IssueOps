# Pull-request evidence requirements

The pull request is the evidence pack for one execution-contract issue. It must let a human reviewer compare the final repository change with the issue without relying on private chat history or memory.

This page is the canonical reference for evidence-pack content.

## Required sections

Every pull request should record:

| Section | Required content |
| --- | --- |
| **Execution contract** | Exactly one canonical `Issue #<issue-number>` declaration under `## Execution contract`. GitHub closing keywords are optional lifecycle syntax, not the canonical IssueOps linkage. |
| **Parent or roadmap** | The governing stage or initiative when one materially constrains the issue. |
| **Changed** | Files, behaviours or documentation areas changed and the purpose of the change. |
| **Deliberately excluded** | Relevant non-goals and adjacent work not included. |
| **Acceptance criteria** | How the final state satisfies the issue criteria. |
| **Validation status** | Checks actually performed, checks not performed or pending, and evidence tied to the final head. |
| **Post-merge verification** | Named checks that can run only after merge, deployment or environment configuration. |
| **Risks and caveats** | Remaining uncertainty, assumptions, limitations and residual risk. |
| **Groundedness review** | The pre-approval review of issue alignment, scope control, validation evidence and risk. |
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

- whether evidence is trustworthy and sufficient;
- whether the implementation satisfies the contract;
- whether scope and non-goals were respected;
- whether residual risk is acceptable; and
- whether approval and merge should occur.

An agent-generated groundedness review is transparent analysis in the evidence pack. It is not independent human review and does not itself grant approval or merge authority.

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
- scope control;
- validation evidence;
- risks and caveats; and
- one final recommendation.

Do not recommend approval when validation is materially incomplete, scope has drifted, the final evidence is stale, a material review finding remains unresolved or the implementation does not satisfy the issue.

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

Minor wording fixes may be handled in a review reply when they do not change meaning, scope, validation or risk.

## Related guidance

- [Prepare a pull-request evidence pack](../how-to/prepare-pr-evidence-pack.md)
- [PR evidence templates](pr-evidence-templates.md)
- [Review decisions and merge blockers](review-decisions-and-merge-blockers.md)
- [Why evidence is not approval](../explanation/pr-evidence-and-approval.md)
