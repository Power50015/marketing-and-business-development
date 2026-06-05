---
name: context-fundamentals
description: Establish mental models for what context is, how attention mechanics work, why context quality > quantity, and the anatomy of a context window. Activates when planning agent architecture or explaining how context components affect model behavior.
---

# Context Fundamentals

You are an expert in context engineering for AI agent systems. Your goal is to help users understand and optimize how information enters the model's attention budget.

## When to Activate

**Activate this skill when:**
- Planning agent architecture or system design
- Explaining how context components affect model behavior
- Establishing context-window mental models for a new project
- Team needs to understand why "more context" isn't always better

**Do NOT activate for:**
- Lost-in-middle, poisoning, attention failures → use `context-degradation`
- Compression strategies for long sessions → use `context-compression`
- Token efficiency, masking, caching → use `context-optimization`
- Multi-agent coordination → use `multi-agent-patterns`

---

## Core Concepts

### 1. Context Is Not Just Tokens

A context window contains five distinct components, each competing for the model's attention:

| Component | Description | Typical Size |
|-----------|-------------|--------------|
| **System Prompt** | Instructions, persona, constraints | 500-5,000 tokens |
| **Tool Definitions** | Function schemas, descriptions | 1,000-10,000 tokens |
| **Retrieved Documents** | RAG, knowledge base, project files | Variable (often largest) |
| **Message History** | Conversation, prior reasoning, tool outputs | Grows over time |
| **Fresh Output** | Current reasoning, generated content | 100-5,000 tokens |

**Key insight:** These components are not equal. The model's attention to each varies based on position, recency, and relevance.

### 2. Attention Budget > Token Budget

Models don't just have a "token limit" — they have an **attention budget** that degrades predictably:

- **Lost-in-the-middle**: Information in the middle of context is recalled poorly
- **U-shaped attention**: Beginning and end of context receive strongest attention
- **Attention scarcity**: As context grows, attention per token shrinks

### 3. Progressive Disclosure

Load only what is needed, when it is needed:

```
Startup:   Skill names + descriptions only (for routing)
           ↓
On-demand: Full skill body (instructions, examples, guidelines)
           ↓
Execution: Relevant references, data, tool outputs only
```

### 4. Context Quality > Context Quantity

The goal is **not** to maximize tokens in context. The goal is to maximize the **signal-to-noise ratio** within the constrained attention window.

---

## Detailed Topics

### Anatomy of Context Degradation

As context grows, models exhibit predictable failure patterns:

| Context Size | Typical Behavior |
|--------------|------------------|
| < 10K tokens | Strong recall across entire context |
| 10K-50K | Beginning and end strong; middle weakens |
| 50K-100K | Middle becomes unreliable; recency bias increases |
| 100K+ | "Lost-in-the-middle" severe; may ignore early instructions |

### The Five Components in Detail

**System Prompt**
- Highest priority (always in attention "hot zone")
- Should be concise and unambiguous
- Conflicting system prompts cause confusion

**Tool Definitions**
- Each tool adds to context weight
- Too many tools → all tools perform worse
- Consolidation Principle: merge related tools

**Retrieved Documents**
- Often the largest component
- Must be filtered aggressively
- Relevance scoring is critical

**Message History**
- Grows unbounded over time
- Requires summarization/compression strategies
- Early conversation often forgotten

**Fresh Output**
- Model's own reasoning
- Strongest attention (recency effect)
- Can be used as "working memory"

---

## Practical Guidance

### For New Agent Systems

1. **Start minimal**: Begin with only essential system prompt and tools
2. **Add incrementally**: Introduce new components only when needed
3. **Measure attention**: Test recall at different context positions
4. **Document tradeoffs**: Every added component has an attention cost

### For Existing Systems

1. **Audit context components**: What's in the window right now?
2. **Identify bloat**: Which components are rarely used?
3. **Consolidate tools**: Can 10 tools become 5?
4. **Filter retrieval**: Is every retrieved document actually used?

---

## Examples

### Example 1: System Prompt Bloat

**Before (1,200 tokens):**
```
You are a helpful AI assistant with expertise in marketing, business strategy,
customer research, product development, content creation, SEO, analytics, and
many other domains. You should always be polite, professional, thorough, and
provide detailed answers. You have access to many tools and should use them
wisely. Remember to... [continues for 50+ lines]
```

**After (200 tokens):**
```
You are a marketing intelligence agent. Use tools to gather data, apply
frameworks to analyze it, and produce actionable recommendations.
Be direct, specific, and evidence-based.
```

### Example 2: Tool Consolidation

**Before (15 separate tools):**
- `search_keywords()`
- `analyze_keyword_volume()`
- `get_keyword_difficulty()`
- `find_keyword_opportunities()`
- `cluster_keywords()`
- [10 more...]

**After (3 consolidated tools):**
- `keyword_research(query, options)` — handles all keyword tasks
- `content_analyze(url)` — full content audit
- `competitor_analyze(domain)` — competitive intelligence

---

## Guidelines

1. **Every token must earn its place** — If it's not actively used, remove it
2. **System prompt is sacred** — Keep it under 500 tokens when possible
3. **Tools are expensive** — Each tool definition costs attention; consolidate aggressively
4. **Retrieval must be filtered** — Never dump raw search results into context
5. **History needs compression** — Long conversations must be summarized
6. **Position matters** — Critical info should be at beginning or end
7. **Test at scale** — What works at 10K tokens may fail at 100K

---

## Gotchas

| Gotcha | Why It Happens | Fix |
|--------|----------------|-----|
| "The agent forgot what I said earlier" | Lost-in-the-middle effect | Move critical info to beginning/end; use compression |
| "Tools work poorly after adding more" | Attention dilution | Consolidate tools; remove unused definitions |
| "System prompt is being ignored" | Prompt too long or conflicting | Shorten to <500 tokens; remove contradictions |
| "Retrieval returns irrelevant docs" | Poor filtering before injection | Add relevance scoring; filter aggressively |
| "Agent seems confused about its role" | Multiple conflicting system prompts | Use one canonical system prompt |

---

## Integration

This skill routes to:

- **Context degradation patterns** → `context-degradation`
- **Compression for long sessions** → `context-compression`
- **Token efficiency strategies** → `context-optimization`
- **Multi-agent architectures** → `multi-agent-patterns`
- **Memory persistence** → `memory-systems`
- **Filesystem offloading** → `filesystem-context`
- **Tool design best practices** → `tool-design`

---

## References

- **Upstream**: muratcankoylan/Agent-Skills-for-Context-Engineering — `skills/context-fundamentals/SKILL.md`
- **Research**: "Lost in the Middle" phenomenon (Liu et al., 2024)
- **Attention mechanics**: Transformer attention patterns and position encoding

---

## Skill Metadata

| Property | Value |
|----------|-------|
| **Category** | Context Engineering — Foundational |
| **Upstream Source** | muratcankoylan/Agent-Skills-for-Context-Engineering |
| **License** | MIT |
| **Lines** | ~250 |
| **Version** | 2.3.0 |