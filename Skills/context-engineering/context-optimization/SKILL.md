---
name: context-optimization
description: Apply KV-cache reuse, observation masking, compaction, and partitioning strategies to extend effective context capacity. Activates when improving token efficiency, retrieval precision, prefix reuse, masking, partitioning, or budget allocation.
---

# Context Optimization

You are an expert in optimizing context usage for AI agent systems.

## When to Activate

**Activate when:**
- Need to improve token efficiency
- Retrieval precision is low
- Want to reuse prefixes or cached state
- Context budget allocation needs optimization

**Do NOT activate for:**
- Compression of long sessions → `context-compression`
- Diagnosing degradation patterns → `context-degradation`

---

## Core Concepts

### Four Optimization Strategies

| Strategy | Description | Typical Savings |
|----------|-------------|-----------------|
| **KV-Cache Reuse** | Reuse cached key-value states for repeated prefixes | 30-70% on repeated calls |
| **Observation Masking** | Hide tool outputs not needed for current step | 20-50% per step |
| **Compaction** | Merge redundant or verbose context sections | 10-40% overall |
| **Partitioning** | Split context across multiple agents or calls | Varies by task |

---

## Practical Guidance

### Decision Framework

| Problem | Strategy | Threshold |
|---------|----------|-----------|
| Repeated system prompts | KV-cache reuse | Same prompt >2 times |
| Tool output bloat | Observation masking | Output >1K tokens |
| Verbose history | Compaction | History >20K tokens |
| Multi-phase tasks | Partitioning | Task has clear phases |

---

## Guidelines

1. Profile before optimizing — measure actual token usage
2. Start with KV-cache — highest ROI for repeated calls
3. Mask aggressively — most tool outputs are transient
4. Partition at natural boundaries — not arbitrarily

---

## Gotchas

| Gotcha | Fix |
|--------|-----|
| KV-cache invalidation breaks reuse | Ensure prefix is truly identical |
| Masking hides needed info | Test with masked vs unmasked |
| Partitioning loses global context | Use orchestrator to maintain state |

---

## Integration

Routes to: `context-compression`, `tool-design`, `multi-agent-patterns`

---

## References

- **Upstream**: muratcankoylan/Agent-Skills-for-Context-Engineering — `skills/context-optimization/SKILL.md`

---

## Skill Metadata

| Property | Value |
|----------|-------|
| **Category** | Context Engineering — Operational |
| **License** | MIT |
| **Version** | 2.3.0 |