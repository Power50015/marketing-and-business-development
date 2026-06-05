# Context Engineering (Agent Skills for Context Engineering)

> **AI-powered context engineering skillset for building, optimizing, and debugging production-grade AI agent systems.**
> Focuses on context curation, harness engineering, multi-agent architectures, and memory systems —
> designed to integrate with your existing marketing and business intelligence skills ecosystem.

---

## What This Skill Does

This skill provides a **foundation in context engineering** for any AI agent or multi-agent system.
Unlike prompt engineering (which refines instructions), context engineering manages
**everything that enters the model's attention budget**: system prompts, tool definitions,
retrieved documents, message history, and tool outputs.

**The skill answers five critical questions:**

1. **What is context?** — Anatomy of a context window: system prompts, tool definitions, retrieved docs, history, outputs.
2. **How does context degrade?** — Recognize five failure patterns: lost-in-middle, poisoning, distraction, confusion, clash.
3. **How do we compress context?** — Design compression strategies for long-running sessions (anchored iterative, opaque, regenerative).
4. **How do we optimize context?** — Apply compaction, masking, caching, and partitioning to extend effective capacity.
5. **How do we orchestrate multiple agents?** — Use multi-agent patterns (supervisor, swarm, hierarchical) with context isolation principles.

---

## Integration with Your Marketing & Business System

This skill is **designed to layer on top of** your existing 55+ marketing and business intelligence skills,
addressing the foundational "how to make agents work" layer that your current system assumes
but does not codify.

Integration points:
- **Discovery (`starter_prompt.md`)** → Use `context-fundamentals` to optimize how the 37-question discovery
  populates the context window; use `context-compression` if discovery sessions run long.
- **Framework Application (`Frameworks/`)** → Use `multi-agent-patterns` to orchestrate framework selection
  (e.g., one agent for SWOT, another for Porter, with context isolation).
- **Skill Execution (`Skills/`)** → Use `memory-systems` to persist cross-session skill outputs;
  use `filesystem-context` to offload large deliverables (marketing plans, audits) into files
  instead of bloating the conversation.
- **Quality Control (`stop-slop`)** → Use `evaluation` and `advanced-evaluation` to build rubrics
  for assessing marketing copy, business plans, and strategy deliverables.
- **Project Lifecycle** → Use `project-development` to decide whether a given marketing deliverable
  (e.g., a 12-month fCMO plan) is best produced via single-agent reasoning, multi-agent pipeline,
  or batch processing with structured output.

---

## When to Activate

Activate this skill when your AI system experiences any of the following:

- **Lost-in-the-middle**: Agent "forgets" files referenced earlier in a long session.
- **Tool bloat**: Too many tools defined, degrading performance of all tool calls.
- **Context overflow**: Sessions hitting token limits, truncating critical context.
- **Skill boundary confusion**: Wrong marketing skill activated for a task, or multiple
  conflicting skills loaded simultaneously.
- **Cross-session amnesia**: No memory of previous discovery, project briefs, or deliverables.
- **Multi-agent inefficiency**: Multiple agents duplicating work or working at cross-purposes.

---

## Core Concepts

### 1. Attention Budget

LLMs have finite "attention budget" — not just raw token capacity, but the quality of attention
given to each token. As context length grows, models exhibit predictable degradation:
- **Lost-in-the-middle**: Information in the middle of context is recalled poorly.
- **U-shaped attention**: Information at the beginning and end of context is strongest.

### 2. Context Components

Every interaction includes:
- **System prompt** (instructions, persona, constraints)
- **Tool definitions** (function schemas, descriptions)
- **Retrieved documents** (RAG, knowledge base, project files)
- **Message history** (conversation, prior reasoning, tool outputs)
- **Fresh output** (current reasoning, generated content)

### 3. Progressive Disclosure

Load only what is needed, when it is needed:
- At startup: skill names + descriptions only (for routing)
- On activation: full skill body (instructions, examples, guidelines)
- During execution: relevant references, data, and tool outputs only

### 4. Context Isolation (Multi-Agent)

Sub-agents exist primarily to **isolate context**, not to parallelize work:
- Each agent's context window is independent
- Only the orchestrator holds the full task context
- Communication between agents is intentional and filtered (e.g., via messages or files)

---

## Architectural Skills Integration

### Multi-Agent Patterns

Apply to your marketing system when:
- **Orchestrator pattern**: One agent coordinates discovery, framework selection, and skill execution.
- **Peer-to-peer (Swarm)**: Multiple agents each handle one framework (e.g., SWOT agent, Porter agent, Blue Ocean agent) with consensus for final synthesis.
- **Hierarchical**: Discovery agent → Framework agent → Execution agent → Quality agent, each passing only essential context forward.

### Memory Systems

Persist cross-session knowledge:
- **Short-term**: Chat history, current session reasoning
- **Long-term**: Project briefs, deliverables, customer research summaries
- **Graph-based**: Relationship maps (customer → pain point → solution → content)

For your system: use long-term memory to store `PROJECT_BRIEF.md` and completed deliverables;
use graph-based memory to map relationships between frameworks, skills, and customer insights.

### Tool Design

Ensure your 55+ marketing skills are designed as agent tools:
- **Consolidation Principle**: Combine related tools to minimize tool surface area
  (e.g., merge "keyword research" and "competitor analysis" into a single tool if they share 80% of context).
- **Description as Prompt**: The tool's description is part of the context.
  Write precise, unambiguous descriptions for each of your 55 skills.
- **Response Format**: Standardize output formats so tool outputs can be consumed by other tools.

### Filesystem Context

Offload large context into files:
- **Project Briefs**: Store `PROJECT_BRIEF.md` in filesystem, not in conversation.
- **Marketing Plans**: Store completed `final_plan.md` in filesystem, reference by path.
- **Scratchpads**: Use temporary files for intermediate reasoning (e.g., "current_framework_analysis.md").
- **Plan Persistence**: When a session ends, save the current plan state to a file
  so the next session can resume seamlessly.

---

## Quality Control & Evaluation

### Evaluation Framework

Apply to assess your marketing deliverables:

| Marketing Deliverable | Evaluation Criteria | Skill |
|---|---|---|
| SEO audit | Technical accuracy, actionability, prioritization | `seo-audit` + `evaluation` |
| Content strategy | Searchability, shareability, alignment with pillars | `content-strategy` + `evaluation` |
| Copywriting | Clarity, persuasion, voice match | `copywriting` + `advanced-evaluation` |
| Marketing plan | Specificity, budget realism, feasibility | `marketing-plan` + `evaluation` |
| Cold email | Reply likelihood, personalization, CTA effectiveness | `cold-email` + `advanced-evaluation` |

### Harness Engineering

Implement guardrails for autonomous marketing execution:
- **Locked metrics**: KPIs (e.g., traffic, conversions, CAC) cannot be changed by the agent.
- **Editable surfaces**: Marketing copy, campaign settings can be adjusted by the agent within bounds.
- **Append-only state**: All actions logged for human review.
- **Novelty gates**: New tactics/strategies flagged for human approval before execution.
- **Rollback**: Ability to revert any marketing change (e.g., ad copy, pricing).

---

## How to Integrate with Your Existing Skills

### Option 1: Layer as a New Skill Category

Add `Skills/context-engineering/` to your existing `Skills/` directory.
Structure: one directory per sub-skill with a `SKILL.md` file.

```
Skills/
├── context-engineering/          # NEW: context engineering skills
│   ├── context-fundamentals/SKILL.md
│   ├── context-degradation/SKILL.md
│   ├── context-compression/SKILL.md
│   ├── context-optimization/SKILL.md
│   ├── multi-agent-patterns/SKILL.md
│   ├── memory-systems/SKILL.md
│   ├── tool-design/SKILL.md
│   ├── filesystem-context/SKILL.md
│   ├── evaluation/SKILL.md
│   ├── advanced-evaluation/SKILL.md
│   ├── harness-engineering/SKILL.md
│   ├── project-development/SKILL.md
│   └── latent-briefing/SKILL.md
├── prospecting/
├── cold-email/
├── copywriting/
└── ... (existing 55+ skills)
```

### Option 2: Reference as External Plugin

Use the upstream repository as a plugin source:
```bash
# Claude Code
/plugin marketplace add muratcankoylan/Agent-Skills-for-Context-Engineering
/plugin install context-engineering@context-engineering-marketplace

# Cursor / Open Plugins
# Add to your plugin manifest
```

Your marketing skills continue to live in `Skills/` as before,
the context-engineering skills activate automatically when the agent detects
context, memory, or multi-agent needs.

### Option 3: Embed Core Principles

Extract key principles and embed them into your existing skills
(without creating new directories):

- Update `starter_prompt.md` to include context-engineering best practices (progressive disclosure, attention budget)
- Update each `Skills/*/SKILL.md` to include:
  - **When to Activate** — explicit triggers for routing
  - **Do Not Activate** — adjacent skills to avoid confusion
  - **Gotchas** — known failure modes (e.g., context overflow during long audits)
- Add `references/context-engineering/` for cross-skill documentation

---

## Usage Examples

### Example 1: Multi-Agent Marketing Audit

**Problem**: Run a comprehensive marketing audit that covers SEO, CRO, copywriting, and analytics.
Single agent would hit context limits or lose focus.

**Solution**: Multi-agent orchestration with context isolation.

```
Orchestrator Agent
├── SEO Agent (reads site, produces audit report)
├── CRO Agent (analyzes pages, produces CRO audit)
├── Copywriting Agent (reviews messaging, produces copy audit)
├── Analytics Agent (checks tracking, produces analytics audit)
└── Synthesis Agent (takes 4 delivered reports, produces unified action plan)
```

Each agent's context window contains only its specific area. No agent sees the full site crawl.
Context isolation prevents overload.

### Example 2: Long-Discovery Session Compression

**Problem**: Your 37-question discovery process takes 3+ hours. The initial context degrades
before the user completes all questions.

**Solution**: Anchor summary compression (anchored iterative approach).

- Every 10 questions: agent summarizes current understanding, appends to a "discovery_anchor.md" file.
- After 10 more questions: loads "discovery_anchor.md" + last 10 questions only.
- Repeats until all 37 questions are answered.
- Final brief compiled from the full chain of anchor summaries.

This keeps the active context under the model's effective attention window while preserving
everything learned across the full session.

### Example 3: Cross-Session Marketing Plan Persistence

**Problem**: After generating a 12-month marketing plan in session 1, starting a new chat in session 2
requires re-discovering the entire project context.

**Solution**: Filesystem-based memory.

- Session 1: Discovery completed, `PROJECT_BRIEF.md` saved to filesystem.
- Session 1: Marketing plan generated, `final_plan.md` saved to `marketing-plans/{client-slug}/`.
- Session 2: Agent loads only `PROJECT_BRIEF.md` and the latest progress file;
  does not need to re-run discovery or re-populate all frameworks.
- Memory system tracks: which plan version, which sections are approved, which are open,
  and what decisions remain.

---

## Key Design Principles (from upstream)

### Progressive Disclosure
Each skill loads only what is needed. Names and descriptions at startup,
full bodies on activation, references on demand.

### Platform Agnosticism
Patterns work across Claude Code, Cursor, GitHub Copilot, or custom agent platforms.
Skills are written in platform-agnostic language with pseudocode examples.

### Token Budget
Every skill is designed with a "token budget" in mind.
Skills stay under 500 lines, examples are concise, and references are offloaded to files.

### Skill Chaining
Each skill references related skills for flow-through.
`context-fundamentals` → `context-degradation` → `context-optimization` → multi-agent orchestration.

---

## System Metadata

| Property | Value |
|---|---|
| **Source** | https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering |
| **License** | MIT |
| **Skills Included** | 15 foundational + operational skills |
| **Upstream Author** | Muratcan Koylan |
| **Integration Type** | External plugin or embedded skill layer |
| **Compatible With** | Any agent platform (Claude Code, Cursor, Copilot, custom) |

---

## Next Steps

1. **Explore upstream**: Read the full [main SKILL.md](https://raw.githubusercontent.com/muratcankoylan/Agent-Skills-for-Context-Engineering/main/SKILL.md)
2. **Install plugin**: Add to your agent platform for automatic activation based on task context.
3. **Audit your skills**: Check which of your 55+ marketing skills have boundary confusion or context overflow issues.
4. **Experiment with multi-agent**: Try the multi-agent orchestration pattern for your next large deliverable (e.g., comprehensive marketing plan).
5. **Implement file-based memory**: Move `PROJECT_BRIEF.md` and deliverables to the filesystem so they persist across sessions.

---

*This skill bridges the gap between "how to make AI agents work" (context engineering) and
"what marketing intelligence to produce" (your existing 55+ skills).*

**Key differences from upstream**: Your existing `Skills/` model has 55+ domain-specific (marketing/business)
skills. This `context-engineering` skill set addresses the foundational agent infrastructure layer
(context, memory, multi-agent orchestration, evaluation) that makes all those 55+ skills work reliably at scale.
