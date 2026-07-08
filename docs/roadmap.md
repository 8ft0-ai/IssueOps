# Roadmap

This roadmap is intentionally conservative. The project starts by proving the manual execution-contract workflow before adding automation.

## Current baseline: Stage 1

Stage 1 establishes the manual execution-contract IssueOps baseline.

It includes:

- structured issue contracts;
- readiness checks before implementation;
- implementation plans before file changes;
- safe tool-operation checks before repository mutations;
- one branch per issue;
- Codex-assisted implementation within the contract;
- lightweight validation evidence;
- pull requests as evidence packs; and
- human contract verification before merge.

The first baseline release is [`v0.1.0`](releases/stage-1.md).

## Stage 2.1: Canonical documentation site

Stage 2.1 creates the MkDocs/GitHub Pages documentation track. The goal is to give readers a stable, curated entry point for the project thesis, workflow, controls, examples and release notes.

This stage keeps the wiki separate as project memory. It does not clean up or rewrite the wiki.

## Stage 2.2: GitHub Pages publishing

Stage 2.2 adds the publishing path for the MkDocs documentation site.

It introduces a GitHub Actions workflow that builds the site with `mkdocs build --strict`, uploads the generated `site/` directory as a Pages artifact and deploys it to GitHub Pages. The workflow runs on pushes to `main` and can also be started manually.

See [Publishing the documentation site](publishing.md) for the workflow, permissions and manual repository setting.

## Stage 2.3: Operating protocol hardening

Stage 2.3 documents the manual IssueOps operating protocol as a first-class process contract.

It makes the issue-to-PR lifecycle easier to follow by describing the readiness gate, implementation plan, branch discipline, safe tool-operation check, validation evidence, PR evidence pack, contract verification, review remediation and post-merge verification boundary in one canonical place.

See [IssueOps operating protocol](issueops-protocol.md) for the process overview.

## Stage 2.4: Dependency-aware readiness

Stage 2.4 strengthens the readiness gate by requiring dependency state and a safe starting point to be recorded before branch creation.

It documents how to handle issues with no dependency, satisfied dependencies, unsatisfied blocking dependencies and repository-setting or environment dependencies. This remains a manual readiness control and does not add automated dependency detection or branch enforcement.

See [IssueOps operating protocol](issueops-protocol.md#dependency-check-format) for the dependency-check format.

## Future work

Future stages may explore:

- richer documentation examples;
- workflow-change review checklists;
- pre-merge and post-merge validation guidance;
- review remediation and evidence-pack update protocols;
- lightweight release documentation;
- carefully bounded Codex execution triggers; and
- stronger review evidence gates.

These items are future possibilities, not implemented capabilities.

## Non-goals for the current baseline

The current baseline does not include automatic dependency detection, automatic Codex execution, auto-merge, branch protection changes, required status checks for agent work or application code.

Any future automation should be introduced through its own execution contract, implementation plan, validation evidence and human review.
