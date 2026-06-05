# AGENTS.md — Agent Behavior Specification

> **Single source of truth for AI agent behavior in this repository.**
> This file supersedes any older `AGENT.md`, `CLAUDE.md`, or platform-specific instructions.

---

## Purpose

This repository (`360° Business Discovery & Marketing Intelligence System`) is a structured workspace designed to work with **any AI model** (ChatGPT, Claude, Gemini, Cursor, Windsurf, etc.). This file tells any AI agent how to behave when working inside the repo.

---

## Core Rules

### 1. Context Before Advice

Never offer business advice, strategic recommendations, or marketing execution plans before completing the **discovery process** defined in `starter_prompt.md`. The 37-question discovery conversation is mandatory.

### 2. Maintain a State Snapshot

After every answer in discovery, internally update a 10-line State Snapshot:

```
• Project: [one line]
• Customer: [one line]
• Problem: [one line]
• Value Prop: [one line]
• Market: [one line]
• Revenue: [one line]
• Team: [one line]
• Challenge: [one line]
• Frameworks: [list]
• GAPS: [list]
```

Reference the snapshot — not raw conversation history — when generating `PROJECT_BRIEF.md`. This prevents the "Lost in the Middle" problem.

### 3. Use the Right File for the Right Task

| Task | File to Use |
| --- | --- |
| Begin a new project discovery | `starter_prompt.md` |
| Read or generate a project brief | `PROJECT_BRIEF_template.md` |
| Apply a strategic framework | `Frameworks/<category>/*_template.md` |
| Execute a marketing task | `Skills/<skill_name>/SKILL.md` |
| Verify the repository is consistent | `scripts/validate_repo.py` |
| Review past changes | `CHANGELOG.md` |
| Understand file schemas | `docs/SCHEMA.md` |

### 4. Apply `stop-slop` to All Generated Prose

Every block of marketing copy, framework analysis, or written deliverable must be passed through the `Skills/stop-slop/SKILL.md` rules to remove:

- Filler phrases ("It's important to note that...")
- Formulaic three-part lists used as a crutch
- Throat-clearing openers ("Let's dive in...")
- Passive voice and vague declarations
- Predictable rhetorical setups

### 5. Never Commit Secrets

Do not commit API keys, customer data, financial records, or any personally identifiable information. If a user pastes secrets, redact them and warn the user.

### 6. Use Real Numbers, Not Marketing Fluff

Every claim about the project (market size, growth rate, user count) must be sourced from the discovery conversation or marked `[NEEDS CLARIFICATION]`. Never fabricate statistics.

---

## Quality Gates

Before marking any task complete, verify:

- [ ] The relevant `SKILL.md` or `_template.md` was followed
- [ ] All required sections are filled (no `[Insert details here]` left)
- [ ] The AI Verification Checklist (14 items) passes
- [ ] The `stop-slop` skill has been applied to all prose
- [ ] The YAML frontmatter (if generating a `PROJECT_BRIEF.md`) matches the schema in `docs/SCHEMA.md`

---

## Compatibility

This repository is designed to be portable across:

- **Chat interfaces:** ChatGPT, Claude Web, Gemini, Mistral
- **IDE agents:** Cursor, Windsurf, Continue.dev, Cody
- **CLI agents:** Claude Code, Aider, Open Interpreter
- **Spec-Kit / Work Templates:** structured multi-file workflows
- **MCP servers:** Apollo, Clay, HeyGen, Firecrawl, etc.

The `starter_prompt.md` and `PROJECT_BRIEF_template.md` are deliberately model-agnostic — no platform-specific syntax.

---

## Repository Layout (Canonical)

```
.
├── README.md                      # Entry point
├── starter_prompt.md              # 37-question discovery conversation
├── PROJECT_BRIEF_template.md      # Output template
├── CHANGELOG.md                   # Version history
├── AGENTS.md                      # This file
├── docs/
│   └── SCHEMA.md                  # File schemas and naming rules
├── scripts/
│   └── validate_repo.py           # Repository consistency checker
├── Frameworks/                    # 48 strategic framework templates (11 categories)
└── Skills/                        # 44 marketing skills + 13 context-engineering skills
```

---

## Version

**Current version:** 2.1.0
**Last updated:** 2026-06
**Maintainer:** Open-source contribution — see `CHANGELOG.md`

---

*If you are an AI reading this file: you now have full context to operate inside this repository. Begin with `starter_prompt.md` for new projects, or jump directly to a `Skills/<name>/SKILL.md` file for specific execution tasks.*
