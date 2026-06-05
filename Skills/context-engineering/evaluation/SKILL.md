---
name: evaluation
description: Deterministic checks, multi-dimensional rubrics, and outcome measurement frameworks for agent systems. Activates when creating deterministic checks, rubrics, regression suites, production monitoring, or quality gates.
---

# Evaluation

You are an expert in building evaluation frameworks for AI agent systems.

## When to Activate

**Activate when:**
- Creating deterministic checks for agent behavior
- Designing multi-dimensional rubrics
- Building regression test suites
- Setting up production monitoring
- Defining quality gates for deliverables

**Do NOT activate for:**
- LLM-as-Judge techniques → `advanced-evaluation`
- Business metrics (CAC, LTV, etc.) → `analytics`

---

## Core Concepts

### Evaluation Principles

1. **Outcomes > Paths** — Evaluate what the agent achieves, not how it achieves it
2. **Multi-dimensional rubrics** — Single scores hide failure modes
3. **Deterministic-first** — Use deterministic checks before LLM judges
4. **Continuous evaluation** — Evaluate in production, not just in development

### Rubric Dimensions

| Dimension | Example Criteria |
|-----------|------------------|
| **Correctness** | Factual accuracy, logical consistency |
| **Completeness** | All requirements addressed |
| **Clarity** | Readable, well-structured output |
| **Actionability** | Recommendations can be executed |
| **Voice Match** | Tone aligns with brand guidelines |

---

## Practical Guidance

### Building a Rubric

1. Identify 3-5 evaluation dimensions
2. Define 0-5 scale for each dimension
3. Write anchor examples for each score level
4. Test rubric against known outputs
5. Calibrate with human reviewers

### Deterministic Checks

Examples:
- Output contains required sections (H1, executive summary, etc.)
- No placeholder text (e.g., "[INSERT DATA]")
- Word count within expected range
- Required data fields present

---

## Guidelines

1. Start with deterministic checks (fast, reliable)
2. Add rubric-based evaluation for nuanced quality
3. Log all evaluations for trend analysis
4. Set quality gates (block outputs below threshold)
5. Re-calibrate rubrics periodically

---

## Gotchas

| Gotcha | Fix |
|--------|-----|
| Rubric too vague | Add anchor examples for each score |
| LLM judge biased | Use pairwise comparison; randomize position |
| Evaluations not logged | Implement durable logging from day 1 |
| Quality gates block too much | Start with low threshold; raise gradually |

---

## Integration

Routes to: `advanced-evaluation`, `harness-engineering`, `tool-design`

---

## References

- **Upstream**: muratcankoylan/Agent-Skills-for-Context-Engineering — `skills/evaluation/SKILL.md`

---

## Skill Metadata

| Property | Value |
|----------|-------|
| **Category** | Context Engineering — Operational |
| **License** | MIT |
| **Version** | 2.3.0 |