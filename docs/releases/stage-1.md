# Stage 1 baseline release

Recommended tag: `v0.1.0`

Release title: Stage 1: Manual Execution-Contract IssueOps

## Summary

This release establishes the Stage 1 manual IssueOps baseline for agentic coding with Codex.

The release defines the issue as the execution contract, the pull request as the evidence pack and human review as contract verification. It also adds practical controls for safe repository operations and lightweight validation evidence before any automation is introduced.

## Included

- Execution-contract issue model.
- Manual readiness review before implementation.
- Manual implementation plan before file changes.
- Safe tool-operation check before repository mutation.
- One branch per issue.
- Codex as contract-bound implementer.
- Lightweight validation evidence for documentation and template changes.
- Pull request evidence-pack template.
- Contract verification before approval.
- Example execution contracts and verification reviews.
- Manual label model.

## Excluded

- Automatic Codex execution.
- GitHub Actions orchestration.
- Required status checks.
- Branch protection changes.
- Auto-merge.
- Application code.
- Release automation.

## Release recommendation

After the Stage 1.4 release-prep pull request is merged, the repository is ready to tag `v0.1.0` as the first manual execution-contract IssueOps baseline.

The tag should be created as a separate explicit release action after review and merge.
