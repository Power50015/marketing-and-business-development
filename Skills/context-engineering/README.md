# Context Engineering Skills — Quick Reference

This directory contains 15 context engineering skills adapted from the upstream repository:
**muratcankoylan/Agent-Skills-for-Context-Engineering** (MIT License)

---

## Skill Index

| # | Skill | Purpose | Upstream Link |
|---|-------|---------|---------------|
| 1 | `context-fundamentals` | Context window anatomy, attention mechanics, progressive disclosure | [Upstream](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-fundamentals) |
| 2 | `context-degradation` | Diagnose lost-in-middle, poisoning, distraction, confusion, clash | [Upstream](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-degradation) |
| 3 | `context-compression` | Anchored Iterative, Opaque, Regenerative compression strategies | [Upstream](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-compression) |
| 4 | `context-optimization` | KV-cache, masking, compaction, partitioning for token efficiency | [Upstream](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-optimization) |
| 5 | `multi-agent-patterns` | Orchestrator, swarm, hierarchical architectures with context isolation | [Upstream](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/multi-agent-patterns) |
| 6 | `memory-systems` | Short/long-term memory, graph-based memory, framework comparison | [Upstream](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/memory-systems) |
| 7 | `tool-design` | Agent-tool contracts, consolidation, description engineering | [Upstream](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/tool-design) |
| 8 | `filesystem-context` | Dynamic discovery, offloading, scratchpads, plan persistence | [Upstream](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/filesystem-context) |
| 9 | `evaluation` | Deterministic checks, rubrics, quality gates for agent systems | [Upstream](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/evaluation) |
| 10 | `advanced-evaluation` | LLM-as-Judge, pairwise comparison, bias mitigation | [Upstream](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/advanced-evaluation) |
| 11 | `harness-engineering` | Locked metrics, durable logs, novelty gates, rollback, human approval | [Upstream](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/harness-engineering) |
| 12 | `project-development` | Task-model fit, batch pipelines, structured output, cost estimation | [Upstream](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/project-development) |
| 13 | `latent-briefing` | KV cache compaction for orchestrator→worker state sharing | [Upstream](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/latent-briefing) |

---

## How to Use These Skills

### Option 1: Read the Local SKILL.md Files

Each skill directory contains a `SKILL.md` file with:
- When to activate (and when NOT to activate)
- Core concepts and detailed topics
- Practical guidance and examples
- Guidelines and gotchas
- Integration with other skills

### Option 2: Access the Upstream Repository

For the most up-to-date versions, examples, and research references:

1. **Browse the repository**: https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering
2. **Install as Claude Code plugin**:
   ```bash
   /plugin marketplace add muratcankoylan/Agent-Skills-for-Context-Engineering
   /plugin install context-engineering@context-engineering-marketplace
   ```
3. **Install as Cursor plugin**: Available in the [Cursor Plugin Directory](https://cursor.directory/plugins/context-engineering)

---

## Integration with Marketing & Business Skills

These 15 context engineering skills are **foundational** — they make your 55+ marketing skills work reliably at scale.

### Integration Patterns

| Marketing Skill | Context Engineering Enhancement |
|-----------------|--------------------------------|
| `starter_prompt.md` (37-question discovery) | Use `context-compression` for long discovery sessions; use `filesystem-context` to save `PROJECT_BRIEF.md` |
| `marketing-plan` (12-month fCMO plan) | Use `multi-agent-patterns` to orchestrate framework analysis; use `evaluation` for plan quality gates |
| `seo-audit`, `cro`, `analytics` | Use `tool-design` to consolidate audit tools; use `filesystem-context` to offload large audit reports |
| `copywriting`, `cold-email` | Use `advanced-evaluation` with LLM-as-Judge for copy quality assessment |
| `customer-research`, `competitors` | Use `memory-systems` to persist research findings across sessions |
| All skills | Use `stop-slop` for quality control; use `context-degradation` to diagnose performance issues |

---

## Upstream Repository Metadata

| Property | Value |
|----------|-------|
| **Repository** | https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering |
| **Author** | Muratcan Koylan (@koylanai) |
| **License** | MIT |
| **Current Version** | 2.3.0 (May 2026) |
| **Stars** | 16.4k+ |
| **Academic Citations** | Peking University (2025), CMU/Yale/JHU et al. (2026) |
| **Skills Count** | 15 canonical skills |
| **Router Benchmark** | 600 runs across 4 models (Gemini, Composer, GPT-5.5, Claude Opus 4) |
| **Top-1 Accuracy** | 0.84–0.92 depending on model |

---

## Key Upstream Files

| File | Purpose | Link |
|------|---------|------|
| `README.md` | Overview, installation, activation scenarios | [View](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/README.md) |
| `SKILL.md` | Collection-level metadata and skill map (v2.3.0) | [View](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/SKILL.md) |
| `template/SKILL.md` | Canonical skill template structure | [View](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/template/SKILL.md) |
| `CHANGELOG.md` | Detailed version history with benchmark results | [View](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/CHANGELOG.md) |
| `examples/` | 5 complete demonstration projects | [Browse](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/examples) |
| `researcher/` | File-based research-to-skill operating system | [Browse](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/researcher) |

---

## When to Reference Upstream

Reference the upstream repository when:
- You need the most recent version of a skill (local files may lag)
- You want to see working code examples in `scripts/` directories
- You need to understand the router benchmark methodology
- You want to contribute improvements or new skills
- You need to cite academic research or production case studies

---

*Local copies provided for offline reference and integration with the 360° Business Discovery & Marketing Intelligence System.*

*All upstream content is MIT Licensed. Attribution required for commercial use.*