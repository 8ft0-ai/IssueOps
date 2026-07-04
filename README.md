# IssueOps

The Agent Does Not Need a Ticket. It Needs an Execution Contract.

This repository demonstrates an issue-driven delivery flow for agentic coding work. The intent is to start with a simple, manual operating model and then add process, validation and automation in small, reviewable stages.

Stage 1 establishes the manual IssueOps foundation:

- work starts from a structured GitHub issue;
- the issue is checked for readiness before implementation starts;
- a plan is posted to the issue before a branch is created;
- Codex is the preferred agentic coding tool for implementation;
- changes are delivered through pull requests, not direct commits to `main`;
- validation evidence and caveats are recorded in the pull request; and
- a human approves and merges the change.

Start with [`docs/issueops.md`](docs/issueops.md) for the workflow and [`AGENTS.md`](AGENTS.md) for agent operating rules.
