# Pull requests as evidence packs

The pull request is the evidence pack for one execution-contract issue. It connects the final implementation, validation record and known limitations to the issue a human must verify before approval.

This stable page now routes each reader need to focused guidance. The evidence model and human authority boundary have not changed.

## Choose what you need

### Prepare the pull request

- [Prepare a pull-request evidence pack](how-to/prepare-pr-evidence-pack.md)
- [PR evidence templates](reference/pr-evidence-templates.md)

### Check exact requirements

- [Pull-request evidence requirements](reference/pr-evidence-requirements.md)
- [Review decisions and merge blockers](reference/review-decisions-and-merge-blockers.md)

### Review and remediate

- [Review a pull request against its contract](how-to/review-pr-against-contract.md)
- [Remediate pull-request review feedback](how-to/remediate-review-feedback.md)

### Understand the model

- [Why evidence is not approval](explanation/pr-evidence-and-approval.md)

## What remains true

- The evidence pack must describe the final head.
- It records changed and excluded work, acceptance criteria, validation, pending checks, post-merge verification, risks and caveats.
- Repository-observed evidence and contributor assertions should remain distinguishable.
- Validation is not marked complete unless it ran.
- Evidence completeness does not prove contract satisfaction.
- Agent-generated groundedness review is not independent human review.
- Human approval and merge authority remain separate from evidence collection.
- Material remediation must refresh the evidence pack.

The complete lifecycle remains in the [IssueOps operating protocol](issueops-protocol.md).

## Compatibility note

Earlier versions of this page combined explanation, evidence requirements, validation formats and remediation guidance. Stage 4 separated those needs while preserving this URL as the evidence-pack entry point.
