# Local IssueOps bootstrap execution-contract template

Use this template only after the read-only assessment is complete.

Creating the issue requires explicit target-repository owner permission. The issue authorises only the scope written into it; the remote bootstrap specification does not grant additional mutation, approval or merge authority.

```md
# Adopt the manual IssueOps workflow for this repository

## Bootstrap source

- Specification: `IssueOps Bootstrap 0.1`
- Current entry point: `https://github.com/8ft0-ai/IssueOps/blob/main/BOOTSTRAP.md`
- Pinned entry point: `https://github.com/8ft0-ai/IssueOps/blob/<commit-sha>/BOOTSTRAP.md`
- Assessment record: <link or attached assessment>

## Problem

Describe the material gap between the repository's current delivery controls and the selected IssueOps adoption posture.

Do not describe missing IssueOps filenames as a problem when compatible local controls already exist.

## Expected outcome

State the observable local repository state after adoption.

Include:

- the selected posture;
- the controls that will exist or be adapted;
- the existing conventions that will remain authoritative; and
- how a later real issue can use the adopted process.

## Selected adoption posture

- Already compatible / Minimal manual adoption / Stage-capable adoption

Evidence:

- <local repository evidence>

Why this is the lightest sufficient posture:

- <reason>

## Existing conventions to preserve

- Agent instructions: <path and treatment>
- Contributor guidance: <path and treatment>
- Issue conventions: <path and treatment>
- Pull-request and review conventions: <path and treatment>
- Validation: <commands, workflows or required evidence>
- Branch and dependency conventions: <rules>
- Merge authority and method: <rules>
- Planning conventions, when applicable: <rules or not applicable>

## Scope

List exact files, templates or local surfaces that may change.

- <path or surface>: <bounded change>

A no-change scope is valid for an already-compatible repository.

## Non-goals

- No workflow or automatic lifecycle change unless separately authorised.
- No CLI, installer, generator, schema, bot, app or launcher.
- No repository-setting, permission, required-check or branch-protection change.
- No auto-merge configuration.
- No new labels as a prerequisite.
- No application-code change.
- No organisation-wide rollout.
- No replacement of compatible local conventions merely to use IssueOps terminology.
- <repository-specific exclusions>

## Acceptance criteria

- [ ] The selected posture is implemented without adding unnecessary control surfaces.
- [ ] Existing local conventions are preserved or each adaptation is explicit.
- [ ] The issue-contract requirements are locally discoverable.
- [ ] Readiness and implementation planning occur before branch creation.
- [ ] One issue-scoped branch is used for the bootstrap change.
- [ ] Validation and review evidence match the repository's actual conventions.
- [ ] The pull request records changed scope, exclusions, acceptance evidence, validation, caveats and groundedness.
- [ ] Human approval or explicitly bounded local delegation governs merge.
- [ ] No prohibited default mutation or authority expansion occurs.
- [ ] The pinned bootstrap source is recorded.
- [ ] <repository-specific observable criterion>

## Validation evidence expected

Repository-native validation:

```text
<exact commands or workflows>
```

Additional evidence:

- changed-file read-back;
- final diff and final-head identification;
- link, syntax or generated-output checks relevant to the changed surfaces;
- compatibility review against existing local conventions;
- confirmation that prohibited default mutations did not occur; and
- any legitimate post-merge verification.

## Change risk

Describe the consequence of incorrect adoption, including duplicated controls, weakened authority, broken validation or excessive process.

Risk level:

- Low / Moderate / High

## Agent instructions

- Re-read this issue and all comments before implementation.
- Use repository state rather than chat history as authoritative.
- Post readiness and dependency evidence before branch creation.
- Post an implementation plan before mutation.
- Make the smallest coherent change that satisfies this contract.
- Preserve existing repository conventions unless this issue explicitly adapts them.
- Stop rather than invent missing product, governance, validation or authority intent.
- Do not introduce a prohibited default change as an incidental improvement.
- Follow local review and merge policy.

## Relationship to a roadmap or parent

- None / <local parent or roadmap and this issue's contribution>

Do not create stage machinery unless the selected posture is Stage-capable and the local repository has approved it.

## Dependencies

Required prior work or state:

- Repository-owner permission for this issue and scope: <evidence>
- Stable starting branch: <branch>
- Existing local instructions reviewed: <paths>
- <other dependency>

Safe starting state:

- Base branch or commit: <branch or SHA>
- Why it is safe: <reason>

## Authority boundary

Before readiness and planning are complete, this issue does not authorise a branch, file change or pull request.

This issue authorises only the scope above. It does not authorise:

- workflow, settings, permission or application-code changes outside scope;
- approval or merge contrary to local policy;
- automatic lifecycle transitions; or
- mutation of another repository.

Local merge authority:

- Per-PR human approval / Explicit bounded local delegation / Other: <exact rule>

## Post-merge verification

- <exact check, owner and evidence location> / None.

## Subsequent real issue

Identify how the adopted process will be proved through one later real issue.

- Candidate issue or selection rule:
- Required evidence:
- Authority boundary:
```

## Quality check before creation

Do not request creation until:

- the pinned bootstrap source is known;
- the assessment supports one posture;
- scope and non-goals are exact;
- local validation and merge authority are recorded;
- existing conventions to preserve are named;
- prohibited changes are visible; and
- implementation can proceed without inventing intent.

If these conditions are not met, retain the proposed issue as text and request clarification without mutating the target repository.
