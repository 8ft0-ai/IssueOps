# Contract verification

Contract verification is the human review step before approval. It asks whether the pull request fulfilled the issue contract and whether it stayed inside the contract boundaries.

The review should not judge the pull request only as a standalone diff. It should compare the evidence pack with the issue that authorised the work.

## Review questions

The reviewer should check:

- whether the expected outcome in the issue was delivered;
- whether each acceptance criterion was addressed;
- whether the stated non-goals were respected;
- whether the validation evidence is accurate;
- whether any pending validation is clearly recorded; and
- whether any scope drift, uncertainty or implementation risk remains.

## Evidence to inspect

For documentation-only work, the reviewer can usually inspect:

- the changed Markdown files;
- `mkdocs.yml` navigation;
- internal documentation links;
- release notes and example links; and
- the absence of unrelated automation or application code changes.

For later code changes, the reviewer should also inspect the repository’s normal test, build and runtime evidence.

## Final recommendation

Use one final recommendation:

- Approve
- Approve after minor fixes
- Do not approve yet

Approval should be grounded in evidence. If validation is incomplete, the scope has drifted or the implementation does not satisfy the issue, the recommendation should not be approval.

## Example

See the [example contract verification](examples/contract-verification-example.md) page for a small evidence-pack review.
