# Delegated batch mode

Delegated batch mode is an owner-authorised way to complete multiple low-risk IssueOps issues without stopping for manual approval on every pull request.

It is not GitHub auto-merge. It is not a standing permission for agents to merge anything. It is a bounded manual delegation from the repository owner for a specific batch of work.

## Who can authorise it

Only the repository owner can authorise delegated batch mode.

The authorisation should be explicit in the conversation or issue record and should state the goal, such as completing a named backlog of open issues.

## Eligible work

Delegated batch mode is appropriate only for low-risk work, such as:

- documentation-only changes;
- process guidance changes;
- small navigation updates;
- wording or evidence-template changes; and
- label guidance where repository label definitions are not being created.

## Required gates

Each issue still requires:

- issue read-back;
- readiness decision;
- implementation plan;
- one feature branch per issue;
- scoped implementation;
- changed files read back from the branch;
- available validation not failing;
- PR evidence pack;
- pre-approval groundedness review; and
- merge only when the final recommendation is `Approve`.

## Stop conditions

Stop delegated batch mode and require manual review when:

- available validation fails;
- the diff includes workflow files, application code, branch protection, required checks or repository permissions not explicitly scoped;
- implementation correctness is uncertain;
- the issue is unclear or contradictory;
- label creation or other repository-state mutation is unavailable but required for acceptance;
- the PR recommendation is not `Approve`; or
- the change would be misleading if merged without human review.

## Recording merge authorisation

Each PR merged under delegated batch mode should include:

```md
## Merge authorisation

The repository owner explicitly authorised delegated batch completion for this backlog. This PR is complete, scoped, available validation is not failing and the groundedness review recommends approval.
```

## Relationship to auto-merge

Delegated batch mode does not configure GitHub auto-merge, branch protection, required status checks or automation.

Any future platform auto-merge must be introduced through its own issue contract, implementation plan, validation evidence and human review.
