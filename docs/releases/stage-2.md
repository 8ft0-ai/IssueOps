# Stage 2 baseline release

Recommended tag: `v0.2.0`

Release title: Stage 2 — Published and Hardened IssueOps Operating Model

## Summary

Stage 2 extends the manual execution-contract baseline into a documented, published, dogfooded and repository-validated operating model.

The central contract remains unchanged: the issue defines bounded intent, the implementation plan records the proposed path, the pull request carries evidence, and a human decides whether the work may merge. Stage 2 improves the controls around that loop without turning advisory process into autonomous enforcement.

## Included

- A canonical MkDocs documentation site and GitHub Pages publishing path.
- A consolidated IssueOps operating protocol covering readiness through post-merge verification.
- Dependency-aware readiness and safe starting-point evidence.
- Documentation currency and workflow-change review checklists.
- PR review remediation and final-evidence update guidance.
- Clear separation between pre-merge validation and post-merge verification.
- Change-type validation guidance and compact PR evidence templates.
- Repository-native validation as the preferred evidence path.
- Owner-authorised delegated batch mode for bounded low-risk work.
- Batch completion summaries and compact safe-operation evidence.
- A full Stage 2 protocol dogfood run, including honest circuit-breaker evidence after an unintended repository mutation.
- Automatic pull-request documentation validation with production deployment restricted to pushes to `main`.
- A contributor usability review and a clearer small-change entry path.
- Verified GitHub Pages production deployment evidence.

## Operational evidence

Stage 2 close-out included:

- production Pages verification from `main`;
- a complete protocol dogfood run;
- repository-native validation against the exact pull-request commit;
- successful strict MkDocs builds and Pages artefact uploads;
- production deployment correctly skipped for pull requests;
- a first-time-contributor walkthrough covering navigation, terminology, duplication and applicability.

The detailed issue, pull-request, workflow-run and review history remains the canonical audit trail.

## Deferred limitation: lifecycle labels

Stage 2 defines a small advisory lifecycle label model, but the additional repository label definitions were not created. The connected tooling can apply existing labels but cannot create repository-level label definitions with descriptions and colours.

This limitation does not weaken the operating contract because:

- written issue and pull-request evidence remains canonical;
- no workflow or enforcement depends on the labels;
- label transitions are not automated; and
- the documented labels remain optional visibility aids.

Issue #54 was therefore closed as a non-blocking deferred limitation rather than being reported as complete.

## Manual controls versus automated enforcement

Stage 2 documents and proves a stronger process, but most controls remain deliberate human practices.

Automated in the current baseline:

- pull-request-triggered MkDocs validation;
- strict documentation build;
- Pages artefact creation; and
- production deployment from `main`.

Manual or advisory in the current baseline:

- issue readiness and dependency assessment;
- implementation-plan approval;
- safe-operation evidence;
- lifecycle labels;
- contract verification;
- review-remediation classification;
- merge approval; and
- post-merge verification decisions.

## Excluded

- Automatic agent execution.
- Automatic issue or pull-request lifecycle transitions.
- Automatic dependency detection.
- Required status checks or branch protection changes.
- Review bots or automatic review-thread resolution.
- GitHub auto-merge configuration.
- Automatic publication beyond the existing documentation deployment path.
- Stage 3 orchestration or enforcement capabilities.

## Known limitations

- The operating protocol is comprehensive and still requires contributors to navigate specialised guidance for higher-risk work.
- Repository-native validation currently focuses on the documentation repository and does not establish a general application-code validation framework.
- The lifecycle label definitions remain unavailable.
- One complete dogfood run proves the process is workable, not that every future repository or change type will have the same friction profile.
- Human authority remains essential for scope, evidence quality, merge and publication decisions.

## Release recommendation

Use `v0.2.0` for the Stage 2 baseline. The minor-version increment is appropriate because Stage 2 adds a substantial compatible operating-model layer while preserving the Stage 1 execution-contract thesis and manual human-approval boundary.

Stage 3 should begin with a shaping and planning decision, not an implementation backlog. Any automation should be introduced through a reviewed stage roadmap that states the outcome, autonomy boundary, evidence gates and explicit exclusions before execution issues are created.
