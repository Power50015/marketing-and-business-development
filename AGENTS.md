# AGENTS.md

Workspace memory for AI agents working on this project.

## System Overview

This is a **Marketing & Business Expert System**. It guides AI agents through a two-phase process (Exploration → Expert) to understand a business/project deeply and provide evidence-backed advice using strategic frameworks and marketing skills.

## Entry Point

- **`prompt.md`** — Read this first. Contains the complete system: mandatory skills, understanding meter, 161 exploration questions, framework filling rules, memory system, and expert protocol.

## Session Start Protocol

Every session MUST:
1. Read `.ai/.brief/` — check for existing project briefs (filled frameworks).
2. Read `.memory/` — check for saved context, preferences, gaps.
3. Calculate understanding %.
4. If < 100%: start Exploration phase (ask questions or accept brain dump).
5. If = 100%: start Expert phase.

## Mandatory Skills

- **`.stop-slop`** — Apply to ALL output. No filler phrases, no AI patterns, no em dashes.
- **`agent-skills-for-context-engineering`** — Apply `filesystem-context` and `memory-systems`.

## Directory Structure

| Path | Purpose |
|------|---------|
| `prompt.md` | Main system prompt |
| `.ai/.frameworks/` | 51 framework templates (11 categories) |
| `.ai/.brief/` | Filled frameworks with project data |
| `.ai/.skills/.stop-slop/` | Stop slop skill |
| `.ai/.skills/.agent-skills-for-context-engineering/` | 15 context engineering skills |
| `.ai/.skills/.marketing/skills/` | 44 marketing skills |
| `.ai/archive/oldprompt.md` | Previous system (v2.1) — reference only |
| `.memory/` | Persistent memory across sessions |
| `output/` | Auto-generated export files |

## Core Rules

- Never give advice during Exploration (< 100% understanding).
- Show the Understanding Meter after every answer.
- Save framework answers to `.ai/.brief/<framework>.md`.
- Save critical context to `.memory/<topic>.md`.
- Always check if additional skills are needed.
- Apply `stop-slop` before delivering any output.
