# Governance Model

Agent Governance Workbench uses a simple operating model:

1. Intake: define the task and success criteria.
2. Risk classification: decide whether the task is low, medium, or high risk.
3. Execution: assign a scoped owner.
4. Evidence: require files, tests, screenshots, or explicit notes.
5. Review: use an independent reviewer for medium and high-risk work.
6. Approval: require a human gate for public release, secret access, production changes, or irreversible actions.
7. Audit: keep a result card for later inspection.

## Risk levels

| Level | Examples | Default action |
| --- | --- | --- |
| Low | Synthetic docs, local drafts, read-only classification | Proceed with result card |
| Medium | Workflow changes, new templates, user-visible docs | Reviewer check |
| High | Public release, secret access, production write, irreversible action | Human approval gate |

## Separation of duties

The reviewer should not be the same agent that produced the work. This reduces confirmation bias and catches privacy mistakes earlier.
