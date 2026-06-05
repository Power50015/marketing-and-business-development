# Harness Engineering

## When to Use
Use this skill when you need to establish durable quality gates, locked metrics, and rollback mechanisms for marketing or agent workflows. Apply after a workflow has been designed but before deployment.

## Before Starting
- [ ] The workflow or pipeline to be hardened is clearly defined
- [ ] Success metrics are identified (what should be measured)
- [ ] Failure modes are understood (what can go wrong)
- [ ] Human approval requirements are known

## Framework / Methodology
1. **Define Locked Metrics** — Identify which metrics must never regress (e.g., conversion rate, latency, cost per output)
2. **Establish Durable Logs** — Set up append-only logging for all workflow executions (for audit and rollback)
3. **Design Novelty Gates** — Create checks that flag novel inputs or edge cases for human review
4. **Implement Rollback Triggers** — Define automatic rollback conditions when metrics breach thresholds
5. **Configure Human Approval** — Specify which decisions require human sign-off before proceeding

## Output Format
A harness configuration document containing:
- Locked metrics with thresholds
- Log retention policy
- Novelty detection rules
- Rollback triggers and procedures
- Human approval workflow

## Related Skills
- `evaluation/` — For defining evaluation rubrics
- `advanced-evaluation/` — For LLM-as-Judge setups
- `tool-design/` — For integrating harness tools into agent workflows
- `project-development/` — For cost estimation and pipeline decisions

## Common Mistakes
- Locking too many metrics (causes analysis paralysis)
- Setting novelty gates too sensitively (flags too many false positives)
- No rollback procedure defined (cannot recover from failures)
- Human approval bottlenecks (slows down routine operations)