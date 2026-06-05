---
name: memory-systems
description: Short-term, long-term, and graph-based memory architectures. Framework comparison (Mem0, Zep/Graphiti, Letta, Cognee, LangMem). Activates when persisting cross-session knowledge, tracking entities over time, or designing retrieval and update semantics.
---

# Memory Systems

You are an expert in memory architecture design for AI agent systems.

## When to Activate

**Activate when:**
- Persisting cross-session knowledge
- Tracking entities over time
- Choosing memory frameworks
- Designing retrieval and update semantics

**Do NOT activate for:**
- Single-session context management → `context-fundamentals`, `context-optimization`
- File-based persistence → `filesystem-context`

---

## Core Concepts

### Memory Layers

| Layer | Persistence | Use Case |
|-------|-------------|----------|
| **Short-term** | Session-only | Conversation history, working state |
| **Long-term** | Cross-session | Project briefs, user preferences, learned facts |
| **Graph-based** | Cross-session + relationships | Entity tracking, knowledge graphs |

### Framework Comparison

| Framework | Type | Best For |
|-----------|------|----------|
| **Mem0** | Long-term memory | User preferences, persistent facts |
| **Zep/Graphiti** | Graph memory | Entity relationships, knowledge graphs |
| **Letta** | Hybrid | Multi-session conversations |
| **Cognee** | Graph + RAG | Complex knowledge retrieval |
| **LangMem** | Multi-layer | General-purpose memory |

---

## Practical Guidance

### Escalation Path

1. Start with filesystem (simple, no dependencies)
2. Add Mem0 for user-specific persistence
3. Add graph memory when relationships matter
4. Use hybrid approach for complex systems

---

## Guidelines

1. Filesystem first — simplest solution
2. Add framework only when filesystem hits limits
3. Define clear retention policies
4. Test retrieval accuracy after updates

---

## Gotchas

| Gotcha | Fix |
|--------|-----|
| Memory grows unbounded | Implement TTL or manual pruning |
| Stale facts persist | Version memory entries; track provenance |
| Retrieval returns irrelevant facts | Improve embedding or add filters |

---

## Integration

Routes to: `filesystem-context`, `context-fundamentals`, `tool-design`

---

## References

- **Upstream**: muratcankoylan/Agent-Skills-for-Context-Engineering — `skills/memory-systems/SKILL.md`

---

## Skill Metadata

| Property | Value |
|----------|-------|
| **Category** | Context Engineering — Architectural |
| **License** | MIT |
| **Version** | 2.3.0 |