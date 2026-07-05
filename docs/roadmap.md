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

The recommended first baseline release is [`v0.1.0`](releases/stage-1.md).

## Stage 2.1: Canonical documentation site

Stage 2.1 creates the MkDocs/GitHub Pages documentation track. The goal is to give readers a stable, curated entry point for the project thesis, workflow, controls, examples and release notes.

This stage keeps the wiki separate as project memory. It does not clean up or rewrite the wiki.

## Future work

Future stages may explore:

- richer documentation examples;
- more explicit contract-readiness checklists;
- lightweight release documentation;
- optional GitHub Actions validation for the documentation site;
- carefully bounded Codex execution triggers; and
- stronger review evidence gates.

These items are future possibilities, not implemented capabilities.

## Non-goals for the current baseline

The current baseline does not include automatic Codex execution, auto-merge, branch protection changes, required status checks, GitHub Actions orchestration or application code.

Any future automation should be introduced through its own execution contract, implementation plan, validation evidence and human review.
