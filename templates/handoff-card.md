# Handoff Card

```yaml
task_id: TASK-000
owner: Builder
risk: low | medium | high
status: ready
result_path: results/TASK-000-result.md
```

## Goal
Describe the single outcome this task should produce.

## Allowed Inputs
- List the exact files, links, or notes the agent may use.

## Allowed Writes
- List the exact output files the agent may create or modify.

## Boundaries
- Do not access secrets.
- Do not expand scope without returning to the coordinator.
- Stop if required information is missing.

## Acceptance Criteria
- The result is evidence-backed.
- Risk gates are respected.
- The result card is complete.
