# PR evidence templates

Use these compact templates when a pull request is low risk and the issue contract is narrow.

The full evidence-pack model still applies for risky changes, unclear scope, failed validation, workflow changes with deployment impact, permission changes or application code.

Every template should preserve the same core evidence:

- linked issue contract;
- what changed;
- what was excluded;
- validation performed;
- caveats or remaining checks;
- groundedness review; and
- final recommendation.

## Documentation-only change

```md
## Execution contract

Closes #N

## Evidence pack

Changed:

- 

Excluded:

- No automation, app code, branch protection, required checks or repository settings changed.

## Validation status

- [x] Changed docs read back from branch
- [x] Documentation currency checked where relevant
- [x] MkDocs build passed / fallback recorded
- [x] Diff scope checked

## Groundedness review

Issue alignment:
Scope control:
Validation evidence:
Risks and caveats:
Final recommendation: Approve / Approve after minor fixes / Do not approve yet
```

## Workflow change

```md
## Execution contract

Closes #N

## Evidence pack

Changed workflow files:

- 

Trigger and permission scope:

- 

Excluded:

- No branch protection, required checks or app code changed unless explicitly listed.

## Validation status

- [x] Workflow YAML read back
- [x] Workflow checklist applied
- [x] Dependencies pinned or bounded
- [x] Pre-merge validation completed
- [ ] Post-merge verification required, if applicable

## Groundedness review

Issue alignment:
Scope control:
Validation evidence:
Risks and caveats:
Final recommendation:
```

## Publishing or deployment change

```md
## Execution contract

Closes #N

## Evidence pack

Changed publishing path:

- 

Manual settings:

- None / listed below

## Validation status

- [x] Build command ran or fallback recorded
- [x] Artifact/deploy path reviewed
- [x] Pre-merge validation separated from post-merge verification
- [ ] Published URL or deployment checked after merge, if required

## Groundedness review

Issue alignment:
Scope control:
Validation evidence:
Risks and caveats:
Final recommendation:
```

## Process or label guidance change

```md
## Execution contract

Closes #N

## Evidence pack

Changed process guidance:

- 

Label state:

- Created / updated / removed / recommended-only / not applicable

Excluded:

- No automated transitions, branch protection, required checks or app code changed.

## Validation status

- [x] Changed docs read back
- [x] Manual versus automated behaviour checked
- [x] MkDocs build passed / fallback recorded
- [x] Scope checked

## Groundedness review

Issue alignment:
Scope control:
Validation evidence:
Risks and caveats:
Final recommendation:
```

## Future application-code change

```md
## Execution contract

Closes #N

## Evidence pack

Changed behaviour:

- 

Files changed:

- 

Excluded:

- 

## Validation status

- [x] Relevant tests run
- [x] Build/type checks run where available
- [x] Affected behaviour checked against acceptance criteria
- [x] Error handling reviewed where relevant
- [ ] Any environment-specific verification listed

## Groundedness review

Issue alignment:
Scope control:
Validation evidence:
Risks and caveats:
Final recommendation:
```

## Compact versus full evidence

Use a compact template when the change is small, low risk and fits one change type clearly.

Use the full evidence-pack structure when the change crosses multiple risk areas, changes workflow behaviour, changes permissions, affects deployment, includes application code, has incomplete validation or requires post-merge verification.
