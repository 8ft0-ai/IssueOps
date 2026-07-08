# Manual lifecycle labels

Labels support visibility in the manual IssueOps workflow.

They are not the source of truth. The issue contract, readiness comment, implementation-plan comment, pull request evidence pack, validation evidence and human review remain the authoritative record.

Labels do not trigger automation, Codex execution, branch protection, required checks, auto-merge or post-merge verification.

## Minimal lifecycle label set

Use a deliberately small label set:

| Label | Meaning | Apply when | Remove when |
| --- | --- | --- | --- |
| `contract/draft` | The issue contract exists but has not been checked for readiness. | An issue is created as a draft contract. | The issue is clarified and marked ready, or closed as not ready/not planned. |
| `contract/ready` | The issue is clear enough to implement safely. | Readiness and dependency checks pass. | Implementation begins, the contract changes materially, or the issue becomes blocked. |
| `plan/posted` | The implementation plan has been posted before branch creation. | The plan comment is added. | Usually left in place for auditability. |
| `review/changes-requested` | Review feedback requires remediation before approval. | Required review fixes are identified. | Required fixes are applied and remediation evidence is recorded. |
| `validation/pending` | Required validation remains incomplete or unavailable. | Validation cannot be completed before review or merge. | Validation is completed, marked not applicable, or moved to explicit post-merge verification. |
| `post-merge/verification-needed` | A post-merge check must remain visible after merge. | A workflow, publishing, release or environment check cannot be completed before merge. | The post-merge verification is completed and recorded. |

## Current repository state

The `contract/draft` label is already in use.

Repository-label creation was checked during Stage 2.16. The available connector can apply or remove labels on issues and pull requests, but it does not expose repository-label creation. Because creation is not available in the current tool environment, this documentation does not claim the remaining labels were created.

Recommended labels not yet created:

- `contract/ready`
- `plan/posted`
- `review/changes-requested`
- `validation/pending`
- `post-merge/verification-needed`

## Creation blocker

To complete label creation later, use GitHub UI or a repository-label creation API/tool that can create label definitions.

After creation, update this page to move the labels from recommended-only to available, and record the created labels in the PR evidence pack.

## Usage rules

Use labels to make state easier to scan, not to replace written evidence.

A label should never be the only place where a decision is recorded. For example:

- `contract/ready` should correspond to a readiness comment.
- `plan/posted` should correspond to an implementation-plan comment.
- `validation/pending` should correspond to PR evidence that names the missing validation.
- `post-merge/verification-needed` should correspond to a specific post-merge verification item.

## Non-goals

Do not add labels for every possible state.

Do not use labels to imply automation that does not exist.

Do not change historical labels unless there is a specific issue contract for doing so.

Do not attach GitHub Actions, branch protection, required checks or auto-merge behaviour to labels without a separate issue contract, implementation plan, validation evidence and review.
