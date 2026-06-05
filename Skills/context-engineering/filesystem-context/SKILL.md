---
name: filesystem-context
description: Filesystem-based dynamic context discovery, tool output offloading, plan persistence, and scratchpad patterns. Activates when moving large or durable context into files, creating scratchpads, or coordinating agents through shared artifacts.
---

# Filesystem Context

You are an expert in using filesystems for context management in AI agent systems.

## When to Activate

**Activate when:**
- Moving large or durable context into files
- Creating scratchpads for intermediate reasoning
- Supporting just-in-time context discovery
- Coordinating agents through shared artifacts
- Persisting plans across sessions

**Do NOT activate for:**
- Database or graph memory → `memory-systems`
- Context compression → `context-compression`

---

## Core Concepts

### Four Failure Modes Filesystem Solves

| Failure Mode | Filesystem Solution |
|--------------|---------------------|
| **Missing context** | Just-in-time file loading based on task |
| **Under-retrieved** | Explicit file references in conversation |
| **Over-retrieved** | Selective file loading, not bulk dumps |
| **Buried context** | File paths as anchors; content loaded on demand |

### Six Filesystem Patterns

| Pattern | Purpose | Example |
|---------|---------|---------|
| **Scratchpad** | Intermediate reasoning, working state | `scratch/current_analysis.md` |
| **Plan Persistence** | Save/resume multi-session plans | `plans/marketing_plan_v2.md` |
| **Sub-agent Communication** | Handoffs via files, not messages | `outputs/seo_audit.md` |
| **Dynamic Skill Loading** | Load skill files on demand | `skills/seo-audit/SKILL.md` |
| **Terminal/Log Persistence** | Command history, session logs | `logs/session_20260605.md` |
| **Self-Modification** | Agent updates its own instructions | `instructions/custom_rules.md` |

---

## Practical Guidance

### File Naming Conventions

- `scratch/` — Temporary, session-only
- `outputs/` — Generated deliverables
- `plans/` — Multi-session plans and progress
- `logs/` — Session history and audit trails
- `instructions/` — Custom rules and constraints

### Just-in-Time Discovery

Instead of loading all project files at startup:
1. Maintain an index file (`project_index.md`)
2. Load specific files based on task triggers
3. Use file paths as context anchors

---

## Examples

### Project Brief Persistence

```
Session 1:
- Discovery completed → save to `briefs/{client}_PROJECT_BRIEF.md`
- Agent: "Project brief saved. Resume anytime by loading this file."

Session 2:
- Agent loads `briefs/{client}_PROJECT_BRIEF.md`
- No re-discovery needed; continue from saved state
```

---

## Guidelines

1. Use filesystem for anything >10K tokens
2. File paths are context anchors — keep them stable
3. Structure directories by purpose (scratch, outputs, plans, logs)
4. Document file schemas for agent consumption
5. Use atomic writes (temp file + rename) for safety

---

## Gotchas

| Gotcha | Fix |
|--------|-----|
| Agent can't find files | Use absolute paths or document working directory |
| Files become stale | Add timestamps; implement invalidation |
| Too many files to manage | Use index file with metadata |
| Agent writes to wrong file | Explicit file routing in system prompt |

---

## Integration

Routes to: `memory-systems`, `multi-agent-patterns`, `tool-design`, `context-optimization`

---

## References

- **Upstream**: muratcankoylan/Agent-Skills-for-Context-Engineering — `skills/filesystem-context/SKILL.md`

---

## Skill Metadata

| Property | Value |
|----------|-------|
| **Category** | Context Engineering — Architectural |
| **License** | MIT |
| **Version** | 2.3.0 |