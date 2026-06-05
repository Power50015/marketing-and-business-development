# Project Development

## When to Use
Use this skill when evaluating whether a marketing task or deliverable is suitable for agent automation, or when designing agent pipelines for complex multi-step projects.

## Before Starting
- [ ] The project or task to be automated is defined
- [ ] Success criteria are clear (what does "done" look like)
- [ ] Constraints are known (budget, timeline, quality requirements)
- [ ] Available agent capabilities are understood

## Framework / Methodology
1. **Task-Model Fit Analysis** — Assess whether the task is suitable for LLM automation (structured vs. creative, deterministic vs. exploratory)
2. **Pipeline Design** — Break the project into sequential or parallel agent steps
3. **Cost Estimation** — Estimate token costs, API calls, and human review time for each step
4. **Structured Output Design** — Define output schemas for each agent step (JSON, markdown, etc.)
5. **Batch Pipeline Planning** — For repetitive tasks, design batch processing with quality sampling

## Output Format
A project development plan containing:
- Task-model fit assessment (go/no-go recommendation)
- Pipeline architecture diagram
- Cost breakdown per step
- Output schemas for each agent
- Batch processing strategy (if applicable)

## Related Skills
- `context-fundamentals/` — For understanding agent capabilities
- `tool-design/` — For integrating external tools into pipelines
- `evaluation/` — For quality checks at each pipeline stage
- `multi-agent-patterns/` — For complex orchestrations

## Common Mistakes
- Automating tasks that require human judgment without approval gates
- Underestimating token costs for long-running pipelines
- No structured output schemas (causes downstream parsing failures)
- Ignoring batch optimization (processes items one-by-one when batching is possible)