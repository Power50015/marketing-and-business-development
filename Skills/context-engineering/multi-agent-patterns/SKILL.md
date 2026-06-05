---
name: multi-agent-patterns
description: Orchestrator, peer-to-peer (swarm), and hierarchical multi-agent architectures. Core insight: sub-agents exist primarily to isolate context. Activates when choosing coordination patterns, isolating context across agents, or designing handoffs.
---

# Multi-Agent Patterns

You are an expert in multi-agent architecture design for AI systems.

## When to Activate

**Activate when:**
- Choosing coordination patterns for complex tasks
- Need to isolate context across different work streams
- Designing handoffs between specialized agents
- Evaluating whether parallel agents are justified

**Do NOT activate for:**
- Single-agent context issues → `context-fundamentals`, `context-degradation`
- Memory persistence → `memory-systems`

---

## Core Concepts

### The Core Insight

**Sub-agents exist primarily to isolate context, not to parallelize work.**

Each agent's context window is independent. Only the orchestrator holds the full task context.

### Three Architectural Patterns

| Pattern | Structure | Best For |
|---------|-----------|----------|
| **Orchestrator (Supervisor)** | One agent coordinates, workers execute specialized tasks | Clear task decomposition, centralized control |
| **Peer-to-Peer (Swarm)** | Agents collaborate directly, no central coordinator | Exploratory tasks, consensus building |
| **Hierarchical** | Multi-level management chain | Large-scale projects, complex dependencies |

### Context Isolation Mechanisms

1. **Separate context windows** — Each agent sees only its relevant context
2. **Filtered communication** — Orchestrator filters what passes between workers
3. **File-based handoffs** — Agents communicate via filesystem, not direct messages

---

## Practical Guidance

### When to Use Multi-Agent

| Signal | Recommendation |
|--------|----------------|
| Task has clear sub-components | Orchestrator pattern |
| Need diverse perspectives | Swarm pattern |
| Complex dependencies | Hierarchical pattern |
| Context exceeds single window | Partition across agents |
| Token cost is ~15x higher with multi-agent | Consider single-agent with compression |

### The Telephone Game Problem

In hierarchical patterns, information degrades at each level. Mitigation:
- Limit hierarchy depth to 2-3 levels
- Use written handoffs (files) not verbal (messages)
- Orchestrator validates at each level

---

## Examples

### Marketing Audit Orchestration

```
Orchestrator Agent
├── SEO Agent (reads site, produces audit report)
├── CRO Agent (analyzes pages, produces CRO audit)
├── Copywriting Agent (reviews messaging, produces copy audit)
├── Analytics Agent (checks tracking, produces analytics audit)
└── Synthesis Agent (takes 4 reports, produces unified action plan)
```

Each agent's context contains only its specific area. No agent sees the full site crawl.

---

## Guidelines

1. Start with single-agent; add agents only when context isolation is needed
2. Orchestrator must maintain global state
3. Use files for inter-agent communication
4. Limit hierarchy depth to prevent telephone game
5. Consolidate workers with overlapping context

---

## Gotchas

| Gotcha | Fix |
|--------|-----|
| Agents duplicate work | Clear task boundaries in orchestrator handoff |
| Context leaks between agents | Use separate sessions/threads per agent |
| Orchestrator becomes bottleneck | Parallelize independent workers |
| Cost explodes | Token budget per worker; consolidate overlapping agents |

---

## Integration

Routes to: `context-isolation`, `filesystem-context`, `tool-design`, `evaluation`

---

## References

- **Upstream**: muratcankoylan/Agent-Skills-for-Context-Engineering — `skills/multi-agent-patterns/SKILL.md`

---

## Skill Metadata

| Property | Value |
|----------|-------|
| **Category** | Context Engineering — Architectural |
| **License** | MIT |
| **Version** | 2.3.0 |