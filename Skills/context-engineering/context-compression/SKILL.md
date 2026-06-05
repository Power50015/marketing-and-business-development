---
name: context-compression
description: Design compression strategies for long-running sessions. Anchored Iterative, Opaque, and Regenerative approaches. Activates when preserving useful state while reducing conversation, tool-output, or trajectory size under context pressure.
---

# Context Compression

You are an expert in context compression for long-running AI agent sessions.

## When to Activate

**Activate when:**
- Session exceeds 50K tokens and approaching limits
- Agent "forgets" earlier conversation or files
- Need to preserve state while reducing context size
- Long discovery or research sessions need summarization

**Do NOT activate for:**
- General context planning → `context-fundamentals`
- Token efficiency without compression → `context-optimization`

---

## Core Concepts

### Three Compression Approaches

| Approach | How It Works | Best For |
|----------|--------------|----------|
| **Anchored Iterative** | Periodic summaries anchored to stable reference points | Discovery sessions, research projects |
| **Opaque** | Compressed state stored as opaque blob (not human-readable) | Tool outputs, intermediate reasoning |
| **Regenerative** | Store seeds that can regenerate full state on demand | Configuration, structured data |

### The Artifact Trail Problem

Long sessions create a "trail" of artifacts (files, outputs, reasoning) that accumulate in context. Compression must preserve the **decision trail** while reducing token count.

---

## Practical Guidance

### 3-Phase Compression Workflow

**Phase 1: Identify Compression Candidates**
- Message history older than N turns
- Tool outputs that have been consumed
- Intermediate reasoning that led to conclusions

**Phase 2: Select Compression Method**
- Anchored Iterative for conversation and decisions
- Opaque for tool outputs and intermediate states
- Regenerative for structured configuration

**Phase 3: Validate Compression**
- Test recall of key decisions post-compression
- Ensure regeneration works for regenerative seeds
- Verify compressed size meets targets

---

## Examples

### Anchored Iterative Compression

```
Every 10 questions in discovery:
1. Summarize current understanding (500 tokens)
2. Append to discovery_anchor.md
3. Next segment loads only anchor + last 10 questions

Result: 100-question discovery fits in <50K tokens
```

---

## Guidelines

1. Compress before hitting limits, not after
2. Preserve decision trail, not every token
3. Test recall after compression
4. Use filesystem for anchor files

---

## Gotchas

| Gotcha | Fix |
|--------|-----|
| Over-compression loses signal | Use anchored approach with periodic validation |
| Compression adds latency | Compress asynchronously or during natural pauses |
| Agent can't find compressed info | Include index or table of contents in anchor |

---

## Integration

Routes to: `context-optimization`, `filesystem-context`, `memory-systems`

---

## References

- **Upstream**: muratcankoylan/Agent-Skills-for-Context-Engineering — `skills/context-compression/SKILL.md`

---

## Skill Metadata

| Property | Value |
|----------|-------|
| **Category** | Context Engineering — Operational |
| **License** | MIT |
| **Version** | 2.3.0 |