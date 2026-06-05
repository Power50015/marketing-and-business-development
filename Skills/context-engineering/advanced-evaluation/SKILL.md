---
name: advanced-evaluation
description: LLM-as-a-Judge techniques: direct scoring, pairwise comparison, rubric generation, and bias mitigation. Activates when using LLM judges, pairwise comparison, calibration, or human-aligned quality assessment.
---

# Advanced Evaluation

You are an expert in LLM-as-a-Judge evaluation techniques for AI systems.

## When to Activate

**Activate when:**
- Using LLM judges to evaluate outputs
- Running pairwise comparisons (A vs B)
- Generating domain-specific rubrics
- Mitigating evaluator bias
- Calibrating LLM judges with human preferences

**Do NOT activate for:**
- Deterministic checks → `evaluation`
- Business KPIs → `analytics`

---

## Core Concepts

### Evaluation Taxonomy

| Method | Description | Best For |
|--------|-------------|----------|
| **Direct Scoring** | LLM scores output against criteria | Rubric-based evaluation |
| **Pairwise Comparison** | LLM compares two outputs (A vs B) | A/B testing, model comparison |
| **Rubric Generation** | LLM creates evaluation criteria | New domains, evolving standards |
| **Calibration** | Align LLM scores with human ratings | Quality assurance |

### Bias Landscape

| Bias | Description | Mitigation |
|------|-------------|------------|
| **Position Bias** | Prefer first/last option | Randomize order; swap and re-evaluate |
| **Verbosity Bias** | Prefer longer outputs | Normalize for length; explicit criteria |
| **Style Bias** | Prefer certain writing styles | Diverse training examples |
| **Self-Affinity Bias** | Prefer outputs from similar models | Cross-model evaluation |

---

## Practical Guidance

### Pairwise Comparison Pipeline

```
1. Generate outputs A and B (randomize labels)
2. LLM judge evaluates: "Which is better? Why?"
3. Swap positions; re-evaluate
4. If judgments disagree → flag for human review
5. Log both judgments for bias analysis
```

### Rubric Generation

1. Provide 5-10 example outputs (good and bad)
2. LLM identifies differentiating criteria
3. Human reviews and refines rubric
4. Test rubric against held-out examples
5. Deploy for production evaluation

---

## Guidelines

1. Always randomize position in pairwise comparisons
2. Use multiple judges when possible
3. Calibrate LLM scores with human ratings
4. Log all evaluations with full context
5. Monitor for drift in judge behavior

---

## Gotchas

| Gotcha | Fix |
|--------|-----|
| Judge prefers verbose but empty outputs | Add "signal-to-noise" criteria to rubric |
| Position bias skews results | Swap positions; require consistent judgment |
| Judge can't explain its reasoning | Ask for specific evidence from outputs |
| Scores drift over time | Periodic re-calibration with human reviews |

---

## Integration

Routes to: `evaluation`, `harness-engineering`, `copy-editing` (for quality assessment)

---

## References

- **Upstream**: muratcankoylan/Agent-Skills-for-Context-Engineering — `skills/advanced-evaluation/SKILL.md`

---

## Skill Metadata

| Property | Value |
|----------|-------|
| **Category** | Context Engineering — Operational |
| **License** | MIT |
| **Version** | 2.3.0 |