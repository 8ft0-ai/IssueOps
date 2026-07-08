# Contract verification

Contract verification is the human review step before approval. It asks whether the pull request fulfilled the issue contract and whether it stayed inside the contract boundaries.

The review should not judge the pull request only as a standalone diff. It should compare the evidence pack with the issue that authorised the work.

## Review questions

The reviewer should check:

- whether the expected outcome in the issue was delivered;
- whether each acceptance criterion was addressed;
- whether the stated non-goals were respected;
- whether the pre-merge validation evidence is accurate;
- whether any validation not performed is clearly recorded;
- whether any post-merge verification is explicitly named; and
- whether any scope drift, uncertainty or implementation risk remains.

## Evidence to inspect

For documentation-only work, the reviewer can usually inspect:

- the changed Markdown files;
- `mkdocs.yml` navigation;
- internal documentation links;
- release notes and example links; and
- the absence of unrelated automation or application code changes.

For later code changes, the reviewer should also inspect the repository’s normal test, build and runtime evidence.

## Pre-merge versus post-merge checks

Pre-merge validation is evidence available before the merge decision. It should be complete enough to support review of the issue contract.

Post-merge verification is evidence that can only be collected after merge, deployment, release or environment-specific configuration. It must be recorded rather than ignored.

Pending validation should block merge when:

- it is needed to decide whether the implementation satisfies the issue;
- available validation is failing;
- the implementation is incomplete;
- the remaining check is required before a safe merge decision; or
- the PR would be misleading without the result.

Post-merge verification can be acceptable when:

- the implementation is complete;
- available validation is not failing;
- the remaining check cannot run until after merge or deployment;
- the PR clearly records the remaining check; and
- the reviewer explicitly accepts the residual risk.

## Final recommendation

Use one final recommendation:

- Approve
- Approve after minor fixes
- Do not approve yet

Approval should be grounded in evidence. If validation is incomplete in a way that prevents the reviewer from deciding whether the issue was satisfied, the recommendation should not be approval.

If the only remaining check is legitimate post-merge verification, the recommendation may be approval, but the review should say what still needs to be verified after merge.

## Example

See the [example contract verification](examples/contract-verification-example.md) page for a small evidence-pack review.
