# Pull-request evidence requirements

The pull request is the evidence pack for one execution-contract issue. It must let a human reviewer compare the final repository change with the issue without relying on private chat history or memory.

This page is the canonical reference for evidence-pack content.

## Required sections

Every pull request should record:

| Section | Required content |
| --- | --- |
| **Execution contract** | The linked issue, normally using a closing keyword when merge should close it. |
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

## Evidence sources

Distinguish where evidence comes from.

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
