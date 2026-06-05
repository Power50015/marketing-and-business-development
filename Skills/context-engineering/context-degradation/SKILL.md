---
name: context-degradation
description: Diagnose and mitigate five predictable failure patterns: lost-in-middle, poisoning, distraction, confusion, and clash. Activates when diagnosing attention failures, context poisoning, or degraded agent performance across long sessions.
---

# Context Degradation

You are an expert in diagnosing and mitigating context failure patterns in AI agent systems.

## When to Activate

**Activate this skill when:**
- Agent "forgets" information referenced earlier in the session
- Performance degrades over long conversations
- Agent produces contradictory or confused outputs
- Tools start failing or returning unexpected results
- System prompt appears to be ignored

**Do NOT activate for:**
- General context planning → use `context-fundamentals`
- Compression strategies → use `context-compression`
- Multi-agent coordination issues → use `multi-agent-patterns`

---

## Core Concepts

### The Five Degradation Patterns

| Pattern | Symptoms | Root Cause |
|---------|----------|------------|
| **Lost-in-the-Middle** | Information in middle of context is ignored or misremembered | U-shaped attention curve |
| **Poisoning** | Agent produces harmful, biased, or off-policy outputs | Malicious or low-quality context injected |
| **Distraction** | Agent fixates on irrelevant details, misses main task | Too much noise in context |
| **Confusion** | Agent contradicts itself or produces inconsistent outputs | Conflicting instructions or context |
| **Clash** | Multiple skills/tools activate simultaneously with conflicting behaviors | Poor skill boundary definitions |

### The U-Curve Phenomenon

Attention strength follows a predictable U-shaped pattern:
- **Beginning** (first ~10%): Strong attention
- **Middle** (next ~70%): Weakest attention — "lost in the middle"
- **End** (last ~20%): Strong attention (recency effect)

---

## Detailed Topics

### Pattern 1: Lost-in-the-Middle

**Detection:**
- Ask agent to recall specific information from earlier in context
- If recall fails for middle content but succeeds for beginning/end → confirmed

**Mitigation:**
1. Move critical information to beginning or end of context
2. Use "anchoring" — repeat key points at context boundaries
3. Compress middle sections into summaries
4. Use filesystem references instead of inline content

### Pattern 2: Poisoning

**Detection:**
- Agent produces outputs that violate system instructions
- Sudden appearance of biased, harmful, or off-policy content
- Context contains untrusted user input without sanitization

**Mitigation:**
1. Sanitize all user-provided context before injection
2. Use separate context windows for untrusted input
3. Add explicit "ignore conflicting instructions" clauses to system prompt
4. Implement output filtering as a second layer of defense

### Pattern 3: Distraction

**Detection:**
- Agent fixates on irrelevant details
- Outputs are verbose but miss the core task
- Context contains large amounts of low-signal content

**Mitigation:**
1. Aggressively filter retrieved documents
2. Remove unused tool definitions
3. Summarize long message histories
4. Use relevance scoring for all injected content

### Pattern 4: Confusion

**Detection:**
- Agent contradicts itself within the same output
- Instructions are ambiguous or conflict with each other
- Multiple system prompts or personas are active

**Mitigation:**
1. Use one canonical system prompt
2. Resolve instruction conflicts explicitly
3. Clarify ambiguous goals before proceeding
4. Reset context if confusion is severe

### Pattern 5: Clash

**Detection:**
- Two or more skills activate simultaneously
- Skills have conflicting instructions or behaviors
- Agent seems to "switch personas" mid-task

**Mitigation:**
1. Define explicit skill boundaries (Do Not Activate blocks)
2. Use skill routing based on clear triggers
3. Implement mutual exclusion for conflicting skills
4. Add skill priority ordering

---

## Practical Guidance

### The Four-Bucket Mitigation Framework

| Bucket | Strategy | When to Use |
|--------|----------|-------------|
| **Write** | Restructure context for better attention placement | Critical info in middle → move to beginning/end |
| **Select** | Filter out low-signal content | Context is bloated with unused definitions or docs |
| **Compress** | Summarize verbose sections | Message history or retrieved docs are too long |
| **Isolate** | Move content to separate context windows | Multi-agent or tool-specific isolation needed |

### Diagnostic Checklist

Run through these questions when degradation is suspected:

- [ ] Can the agent recall information from the beginning of context?
- [ ] Can the agent recall information from the middle of context?
- [ ] Can the agent recall information from the end of context?
- [ ] Are there any conflicting instructions in the system prompt?
- [ ] Are there unused tool definitions consuming attention?
- [ ] Is retrieved content actually relevant to the current task?
- [ ] Has the conversation exceeded 50K tokens without compression?

---

## Examples

### Example 1: Lost-in-the-Middle Fix

**Problem:** Agent forgets the project brief that was provided 20K tokens ago.

**Before:**
```
[User provides 5,000-token project brief at message 5]
[... 15 more messages with back-and-forth conversation ...]
[User: "Based on the project brief, what's our ICP?"]
[Agent: "I don't see a project brief in our conversation."]
```

**After (using anchoring):**
```
[System: "Project brief loaded. Key points: B2B SaaS, $2M ARR, ICP = marketing directors at Series A startups, primary goal = content-led growth."]
[... conversation continues ...]
[User: "Based on the project brief, what's our ICP?"]
[Agent: "Marketing directors at Series A B2B SaaS companies (~$2M ARR)."]
```

### Example 2: Tool Clash Fix

**Problem:** Two SEO tools activate simultaneously with different methodologies.

**Before:**
```
seo-audit: "Run a comprehensive technical audit with 50 checkpoints"
ai-seo: "Optimize for AI search engines with AEO/GEO focus"
[Both activate, agent produces confused output mixing both approaches]
```

**After (with explicit boundaries):**
```
seo-audit:
  Activate: "technical SEO, site audit, ranking issues, crawl errors"
  Do NOT activate: "AI search, AEO, GEO, LLM optimization" → use ai-seo

ai-seo:
  Activate: "AI search, AEO, GEO, LLM citations, AI Overviews"
  Do NOT activate: "technical audit, crawl errors, site speed" → use seo-audit
```

---

## Guidelines

1. **Test recall at all positions** — Beginning, middle, and end of context
2. **Sanitize untrusted input** — Never inject raw user content without filtering
3. **One system prompt** — Multiple personas cause confusion
4. **Define skill boundaries explicitly** — Use "Do NOT activate" blocks
5. **Compress before you hit limits** — Don't wait for errors to appear
6. **Log degradation events** — Track patterns to identify systemic issues

---

## Gotchas

| Gotcha | Why It Happens | Fix |
|--------|----------------|-----|
| "Normal variance looks like degradation" | Models naturally have some output variance | Establish baseline before diagnosing |
| "Compression makes things worse" | Over-aggressive summarization loses signal | Use anchored iterative compression |
| "Adding more context fixes it" | More context usually makes it worse | Reduce, don't expand |
| "The tool is broken" | Often the tool definition is fine; context is bloated | Audit context, not just the tool |
| "Reset fixes it temporarily" | Reset doesn't address root cause | Implement compression or filtering |

---

## Integration

This skill routes to:

- **Compression for long sessions** → `context-compression`
- **Token efficiency strategies** → `context-optimization`
- **Skill boundary design** → `tool-design`
- **Multi-agent isolation** → `multi-agent-patterns`
- **Evaluation of degradation** → `evaluation`

---

## References

- **Upstream**: muratcankoylan/Agent-Skills-for-Context-Engineering — `skills/context-degradation/SKILL.md`
- **Research**: "Lost in the Middle" (Liu et al., 2024), "Position Encoding" (Transformer literature)

---

## Skill Metadata

| Property | Value |
|----------|-------|
| **Category** | Context Engineering — Diagnostic |
| **Upstream Source** | muratcankoylan/Agent-Skills-for-Context-Engineering |
| **License** | MIT |
| **Lines** | ~300 |
| **Version** | 2.3.0 |