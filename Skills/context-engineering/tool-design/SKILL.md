---
name: tool-design
description: Agent-tool contract design, tool surface consolidation, description engineering, and error message optimization. Activates when defining agent-tool contracts, consolidating tool surfaces, or making tool errors actionable.
---

# Tool Design

You are an expert in designing tools that AI agents can use effectively.

## When to Activate

**Activate when:**
- Defining agent-tool contracts
- Consolidating tool surfaces (too many tools)
- Improving tool descriptions for better routing
- Making tool errors actionable

**Do NOT activate for:**
- Context window management → `context-fundamentals`, `context-optimization`
- Multi-agent tool sharing → `multi-agent-patterns`

---

## Core Concepts

### The Consolidation Principle

**Fewer, richer tools outperform many narrow tools.**

Each tool definition consumes attention. Consolidate related operations into unified interfaces.

### Tool-Agent Contract

| Element | Description |
|---------|-------------|
| **Name** | Clear, action-oriented (e.g., `analyze_seo` not `seo_tool`) |
| **Description** | The "prompt" for when to use this tool |
| **Parameters** | Typed, documented, with defaults where possible |
| **Response Format** | Structured, parseable, consistent |
| **Error Messages** | Actionable — tell agent what to try next |

### Description as Prompt

The tool description is part of the context. It tells the agent:
- When to use this tool
- What it returns
- What it's best for

---

## Practical Guidance

### Tool Description Engineering

Ask four questions:
1. What problem does this tool solve?
2. When should the agent reach for it?
3. What does success look like?
4. What are common failure modes?

### Error Message Design

**Bad:** `{"error": "Invalid input"}`

**Good:** `{"error": "Missing required field 'url'. This tool needs a URL to analyze. Example: analyze_seo(url='https://example.com')"}`

---

## Guidelines

1. Consolidate tools with overlapping context
2. Write descriptions that route correctly
3. Structure responses for agent consumption
4. Make errors actionable, not cryptic
5. Test tool usage with real agent flows

---

## Gotchas

| Gotcha | Fix |
|--------|-----|
| Tools perform poorly after adding more | Consolidate; remove unused definitions |
| Agent uses wrong tool for task | Improve description clarity; add routing hints |
| Tool outputs bloat context | Return summaries, not raw data |
| Errors cause agent to give up | Make errors actionable with examples |

---

## Integration

Routes to: `context-optimization`, `evaluation`, `filesystem-context`

---

## References

- **Upstream**: muratcankoylan/Agent-Skills-for-Context-Engineering — `skills/tool-design/SKILL.md`

---

## Skill Metadata

| Property | Value |
|----------|-------|
| **Category** | Context Engineering — Architectural |
| **License** | MIT |
| **Version** | 2.3.0 |