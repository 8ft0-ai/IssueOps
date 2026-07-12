# PR evidence templates

These templates implement the canonical [pull-request evidence requirements](pr-evidence-requirements.md). Choose the smallest template that truthfully represents the change and its risk.

Do not pre-check validation that has not run. Replace placeholder recommendations with the current evidence-based decision.

## Full evidence-pack template

````md
## Execution contract

Closes #<issue-number>

Parent stage or initiative:

- None / #<number> — <title>

## Evidence pack

Changed:

- ...

Deliberately excluded:

- ...

Acceptance criteria:

- ...

## Validation status

Exact final head:

- `<commit SHA>`

Pre-merge validation completed:

- [x] ...

Validation not performed or pending:

- None / exact pending check and reason.

Post-merge verification required:

- None / exact follow-up.

## Risks and caveats

- ...

## Groundedness review

Did we do what was needed?

- ...

Did we only do what was asked?

- ...

Issue alignment:

- ...

Scope control:

- ...

Validation evidence:

- ...

Risks and caveats:

- ...

Final recommendation:

- Approve / Approve after minor fixes / Do not approve yet

## Merge authorisation

- Human repository authority and any delegated-batch authorisation, including its limits.
````

Use the full template when a change crosses risk areas, changes workflows or permissions, affects deployment, includes application code, has incomplete validation, requires material remediation, or retains post-merge verification.

## Documentation-only template

````md
## Execution contract

Closes #<issue-number>

## Evidence pack

Changed:

- ...

Deliberately excluded:

- No application code, automation, workflow, branch-protection, required-check or repository-setting change unless explicitly listed.

## Validation status

Pre-merge validation completed:

- [x] Changed documentation read back
- [x] Navigation and internal links reviewed where applicable
- [x] Documentation currency checked where relevant
- [x] `mkdocs build --strict`
- [x] Scope checked against the issue

Validation not performed or pending:

- None / exact pending validation.

Post-merge verification required:

- None / published-site or environment check.

## Groundedness review

Issue alignment:

- ...

Scope control:

- ...

Validation evidence:

- ...

Risks and caveats:

- ...

Final recommendation:

- Approve / Approve after minor fixes / Do not approve yet
````

## Workflow-change template

````md
## Execution contract

Closes #<issue-number>

## Evidence pack

Changed workflow files:

- ...

Triggers, permissions and side effects:

- ...

Deliberately excluded:

- No branch-protection, required-check, repository-setting or application-code change unless explicitly listed.

## Validation status

Pre-merge validation completed:

- [x] Workflow YAML read back
- [x] Workflow-change checklist applied
- [x] Dependencies pinned or bounded
- [x] Trigger and permission scope reviewed
- [x] Available repository-native validation passed

Validation not performed or pending:

- None / exact pending check.

Post-merge verification required:

- None / exact workflow observation.

## Groundedness review

Issue alignment:

- ...

Scope control:

- ...

Validation evidence:

- ...

Risks and caveats:

- ...

Final recommendation:

- Approve / Approve after minor fixes / Do not approve yet
````

## Publishing or deployment template

````md
## Execution contract

Closes #<issue-number>

## Evidence pack

Changed publishing or deployment path:

- ...

Manual settings or environment dependencies:

- None / listed below.

## Validation status

Pre-merge validation completed:

- [x] Build command completed
- [x] Artefact and deployment path reviewed
- [x] Pre-merge validation separated from post-merge verification

Validation not performed or pending:

- None / exact pending check.

Post-merge verification required:

- [ ] Published URL or environment state to verify

## Groundedness review

Issue alignment:

- ...

Scope control:

- ...

Validation evidence:

- ...

Risks and caveats:

- ...

Final recommendation:

- Approve / Approve after minor fixes / Do not approve yet
````

## Remediation evidence template

```md
## Remediation evidence

Review feedback addressed:

- Comment or thread:
- Classification: Required fix / Optional improvement / Clarification needed / Out of scope
- Change made:
- Validation rerun:
- Scope impact:

Final contract check:

- Did the PR still do what was needed?
- Did the PR still only do what was asked?

Remaining items:

- None / follow-up issue / clarification pending.
```

Use this as a top-level comment when material remediation is clearer as an amendment. Update the full PR body when the final evidence, scope, risk or remaining checks would otherwise be stale.

## Compact versus full evidence

Use a compact template only when:

- the issue is narrow and low risk;
- the change fits one clear change type;
- required validation is complete;
- no material remediation or complex post-merge check remains; and
- the compact body still covers every canonical requirement that matters.

A short PR body is not a reason to omit scope exclusions, unavailable validation, caveats or the final recommendation.
