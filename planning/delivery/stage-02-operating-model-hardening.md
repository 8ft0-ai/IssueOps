# Stage 2 — Published and hardened operating model

Status: completed.

## Original documented intent

The first Stage 2 issues focused on giving the Stage 1 model a canonical public documentation surface and a GitHub Pages publishing path.

[Issue #19](https://github.com/8ft0-ai/IssueOps/issues/19) established the MkDocs documentation track, while [issue #21](https://github.com/8ft0-ai/IssueOps/issues/21) added the publishing path. Later issues progressively hardened the operating protocol, readiness, validation, evidence, remediation and delegated-completion model.

## Retrospective interpretation

Stage 2 is best understood as one coherent operating-model hardening stage rather than twenty-three independently planned mini-stages.

The complete capability progression was not known at the start. Many increments arose from review findings, operational verification and dogfood evidence. This record groups them by outcome while preserving the detailed GitHub history as the canonical audit trail.

The strongest retrospective boundary begins with canonical documentation in issue #19 and ends with the Stage 2 baseline release preparation in issue #58 and PR #69.

## What shipped

### Canonical documentation and publishing

- MkDocs documentation site and navigation.
- GitHub Pages build and deployment workflow.
- Pinned documentation dependencies and strict MkDocs builds.
- Public publishing guidance and verified production deployment from `main`.

### Consolidated operating protocol

- One canonical protocol spanning issue readiness, dependency checks, implementation planning, branch discipline, safe tool operations, validation, PR evidence, contract verification, remediation, merge and post-merge verification.
- Clear separation between canonical guidance and supporting specialist pages.

### Readiness, validation and evidence controls

- Dependency-aware readiness and safe starting-point evidence.
- Documentation-currency and workflow-change review checklists.
- Change-type validation guidance.
- PR evidence templates and material-remediation evidence updates.
- Explicit pre-merge versus post-merge validation treatment.
- Repository-native evidence as the preferred proof path.

### Bounded delegation and completion

- Owner-authorised delegated batch mode for low-risk work.
- Stop conditions and explicit merge authority.
- Batch completion summaries.
- Compact safe-operation evidence for routine mutations without weakening the full check for higher-risk work.

### Operational proof and usability

- Verified GitHub Pages production deployment.
- Full-protocol dogfood through a real documentation change.
- Honest recording of an unintended repository mutation, circuit breaker and recovery.
- Automatic pull-request MkDocs validation against the exact PR commit.
- Production deployment restricted to pushes to `main`.
- Contributor usability walkthrough and a clearer small-change path.
- Stage 2 baseline release notes with a recommended `v0.2.0` tag.

## Linked issues and pull requests

Representative documentation and publishing work:

- [Issue #19](https://github.com/8ft0-ai/IssueOps/issues/19) / [PR #20](https://github.com/8ft0-ai/IssueOps/pull/20) — canonical MkDocs site.
- [Issue #21](https://github.com/8ft0-ai/IssueOps/issues/21) / [PR #22](https://github.com/8ft0-ai/IssueOps/pull/22) — GitHub Pages publishing.
- [Issue #23](https://github.com/8ft0-ai/IssueOps/issues/23) / [PR #32](https://github.com/8ft0-ai/IssueOps/pull/32) — canonical operating protocol.
- [Issue #27](https://github.com/8ft0-ai/IssueOps/issues/27) / [PR #37](https://github.com/8ft0-ai/IssueOps/pull/37) — review-remediation protocol.

Representative close-out and proof work:

- [Issue #53](https://github.com/8ft0-ai/IssueOps/issues/53) — production Pages verification.
- [Issue #54](https://github.com/8ft0-ai/IssueOps/issues/54) — repository labels, closed as a deferred non-blocking limitation.
- [Issue #55](https://github.com/8ft0-ai/IssueOps/issues/55) / [PR #60](https://github.com/8ft0-ai/IssueOps/pull/60) — full-protocol dogfood.
- [Issue #56](https://github.com/8ft0-ai/IssueOps/issues/56) / [PR #61](https://github.com/8ft0-ai/IssueOps/pull/61) — repository-native PR validation and deploy separation.
- [Issue #57](https://github.com/8ft0-ai/IssueOps/issues/57) / [PR #62](https://github.com/8ft0-ai/IssueOps/pull/62) — contributor usability review.
- [Issue #58](https://github.com/8ft0-ai/IssueOps/issues/58) / [PR #69](https://github.com/8ft0-ai/IssueOps/pull/69) — Stage 2 baseline release preparation.

## Proof runs, checks and artefacts

The strongest Stage 2 proof combines repository behaviour and process dogfood:

- production Pages deployment run `28924550021` and deployed commit evidence recorded through issue #53 and PR #60;
- dogfood validation run `29084183742`, which checked the exact feature-branch commit and exposed the need to separate PR validation from production deployment;
- repository-native PR validation in PR #61;
- usability PR #62 with successful workflow run `29088731483`;
- Stage 2 release PR #69 with successful workflow run `29089368571`;
- strict MkDocs builds, pinned dependency installation and Pages artefact uploads;
- production deploy jobs skipped for PRs and retained for pushes to `main`.

Representative produced artefacts include:

- `docs/issueops-protocol.md`;
- `docs/delegated-batch-mode.md`;
- `docs/pr-evidence-templates.md`;
- `docs/repository-native-validation.md`;
- `docs/contributor-usability-review.md`;
- `.github/workflows/pages.yml`; and
- `docs/releases/stage-2.md`.

## Intended versus actual delivery

Stage 2 began with documentation and publishing, then expanded through evidence-based increments.

Material changes from the early framing included:

- the operating protocol became a first-class canonical document rather than remaining distributed across Stage 1 pages;
- review feedback produced dedicated currency, workflow, remediation and final-evidence controls;
- bounded delegated batch mode was added to reduce repeated approval friction without enabling auto-merge;
- repository-native validation became an explicit evidence standard;
- the full dogfood run exposed that manual feature-branch validation attempted production deployment;
- PR #61 corrected that gap by adding automatic pull-request validation and restricting deployment to `main`;
- contributor usability review found a stale Stage 1 front door and improved the small-change path;
- repository lifecycle label creation remained blocked by connector capability and was explicitly deferred.

These changes are recorded as observed evolution, not retroactively inserted into a fictional original plan.

## Observed limitations and friction

- The protocol is comprehensive and still requires navigation across specialist pages for higher-risk work.
- Most controls remain manual or advisory rather than enforced by repository settings.
- The additional lifecycle labels do not exist.
- One full dogfood run and one documentation repository do not prove the model across every codebase or risk profile.
- Repository-native validation proves repository structure and declared evidence, not the substantive truth of every claim.
- The process creates maintenance work when roadmap, protocol, specialised guidance and release records all need currency checks.
- The connected identity cannot approve its own pull requests, so independent review evidence must be recorded even when GitHub cannot store a formal self-approval.

## Boundaries preserved

Stage 2 did not introduce:

- automatic agent execution;
- automatic dependency detection;
- automatic lifecycle transitions;
- required checks or branch protection changes;
- review bots;
- automatic review-thread resolution;
- GitHub auto-merge;
- autonomous merge or publication decisions; or
- Stage 3 implementation.

The documentation Pages workflow is the only standing publication automation, and production deployment remains restricted to `main`.

Written issue and pull-request evidence remains canonical. A human retains authority over scope, remediation, merge and acceptance of post-merge checks.

## Decisions and lessons

Stage 2 is adopted as a stronger manual operating-model baseline.

The most important lesson is that stronger agentic delivery does not come from adding automation first. It comes from separating authority, intent, actuation, evidence and approval clearly enough that limited automation can be introduced without confusing those boundaries.

Repository-native validation materially improves confidence, but it must be designed around the real lifecycle. A validation workflow that attempts production deployment from a PR is not merely noisy; it blurs the distinction between proof and release.

Compact paths reduce friction only when they remain entry points into the same control model rather than weaker alternatives.

## Implications for the next stage

Stage 3 should not begin with a catalogue of automation ideas. It should shape one bounded automation outcome from observed Stage 2 friction and define:

- which action may be automated;
- what authority remains human;
- what evidence the automation must produce;
- what failure stops the workflow;
- what repository or external mutations remain prohibited; and
- what real proof is required before adoption.

No Stage 3 execution contracts should be created until that roadmap is reviewed and approved.
