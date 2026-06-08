# Marketing & Business Expert System

An AI-powered strategic analysis system that guides agents through a structured two-phase process to understand any business or project deeply and produce evidence-backed analysis using 51 strategic frameworks and 44 marketing skills.

## How It Works

```
Session Start → Read brief & memory → Determine phase
                                        ↓
                    ┌──────────────────────────────┐
                    │   EXPLORATION (< 100%)        │
                    │   Ask questions / Brain dump  │
                    │   Save to .brief/ → .memory/  │
                    └──────────┬───────────────────┘
                               ↓
                    ┌──────────────────────────────┐
                    │   EXPERT (100%)                │
                    │   Apply frameworks & skills    │
                    │   Evidence-backed advice       │
                    └──────────────────────────────┘
```

**Phase 1 — Exploration:** The system asks structured questions or accepts a brain dump, builds understanding across 8 areas (37 core questions, 161 in the full bank), tracks progress with a live understanding meter, and saves everything to persistent brief files.

**Phase 2 — Expert:** Once understanding reaches 100%, the system reads the saved briefs and memory, activates relevant frameworks and skills, and delivers actionable, evidence-backed analysis.

## Quick Start

1. Open any AI tool that supports custom prompts (Claude Code, Cursor, ChatGPT, etc.).
2. Point it to this project or paste the contents of `prompt.md` as the system prompt.
3. The AI will read `.ai/.brief/` and `.memory/` — if they are empty, it starts asking questions.
4. Two ways to start: **A) Guided** — questions one at a time, or **B) Brain Dump** — write everything at once.
5. When understanding hits 100%, the AI enters Expert phase and gives analysis.

## What's Inside

```
├── prompt.md                    # Main system prompt
├── AGENTS.md                    # Quick reference for AI agents
│
├── .ai/
│   ├── .brief/                  # Filled frameworks (your project data)
│   ├── .frameworks/             # 51 strategic framework templates
│   │   ├── .business_models/    # BMC, Lean Canvas, Value Prop, etc.
│   │   ├── .external_analysis/  # PESTLE, Porter's Five Forces, etc.
│   │   ├── .finance_and_risk/   # CBA, Break-Even
│   │   ├── .growth_and_innovation/ # Ansoff, BCG, Kano, etc.
│   │   ├── .internal_analysis/  # SWOT/TOWS, Value Chain, VRIO
│   │   ├── .marketing_and_customers/ # Journey Map, JTBD, STP
│   │   ├── .operations_and_projects/ # Kotter 8-Step
│   │   ├── .performance_and_measurement/ # OKRs, BSC, SMART
│   │   ├── .strategy/           # Business & E-commerce Strategy
│   │   ├── .strategy_and_direction/ # Blue Ocean, 7S, Generic Strategies
│   │   └── .thinking_and_problem_solving/ # PDCA, MECE, Root Cause
│   │
│   ├── .skills/
│   │   ├── .stop-slop/          # Remove AI writing patterns
│   │   ├── .agent-skills-for-context-engineering/  # 15 context skills
│   │   └── .marketing/skills/   # 44 marketing skills
│   │
│   └── archive/
│       └── oldprompt.md         # Previous version (reference only)
│
├── .memory/                     # Persistent AI memory across sessions
│   ├── preferences.md
│   └── gaps.md
│
└── output/                      # Auto-generated export files
```

## Frameworks Available (51)

| Category | Frameworks |
|----------|-----------|
| Business Models | Business Model Canvas, Lean Canvas, Value Proposition Canvas, Value Disciplines |
| External Analysis | PESTLE, Porter's Five Forces, 3Cs Ohmae, Product Lifecycle, Consumer Adoption Curve |
| Finance & Risk | Cost-Benefit Analysis, Break-Even Analysis |
| Growth & Innovation | Ansoff Matrix, BCG Matrix, GE-McKinsey Nine-Box, Three Horizons, Greiner Growth, Kano, Consolidation-Endgame |
| Internal Analysis | SWOT/TOWS, Value Chain, VRIO, Profitability Tree, Five Stages of Growth, Digital Transformation |
| Marketing & Customers | Customer Journey Map, JTBD, Marketing Mix (4Ps/7Ps), STP, North Star Metric |
| Operations | Kotter 8-Step Change Model |
| Performance | Balanced Scorecard, OKRs, SMART Goals, Eisenhower Matrix, MoSCoW, Risk Matrix |
| Strategy | Business Strategy, E-commerce Strategy |
| Strategy & Direction | Blue Ocean Strategy, Porter's Generic Strategies, Hoshin Kanri, McKinsey 7S |
| Thinking & Problem Solving | Design Thinking, MECE Issue Tree, PDCA, Pyramid Principle, Root Cause Analysis |

## Marketing Skills Available (44)

ab-testing, ad-creative, ads, ai-seo, analytics, aso, churn-prevention, co-marketing, cold-email, community-marketing, competitor-profiling, competitors, content-strategy, copy-editing, copywriting, cro, customer-research, directory-submissions, emails, free-tools, image, launch, lead-magnets, marketing-ideas, marketing-plan, marketing-psychology, onboarding, paywalls, popups, pricing, product-marketing, programmatic-seo, prospecting, referrals, revops, sales-enablement, schema, seo-audit, signup, site-architecture, sms, social, video.

## The Understanding Meter

After every answer, the system shows progress:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJECT UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall: 45% ███████░░░░░░░░░░

Area Progress:
  ✅ Big Picture          [3/4] — Feeds: BMC, Three Horizons
  🔄 Customer & Problem   [2/5] — Feeds: JTBD, 3Cs
  ⬜ Value Proposition    [1/4] — Feeds: Value Prop Canvas, Blue Ocean
  ⬜ Market & Competition [0/5] — Feeds: Porter, PESTLE
  ⬜ Business Model       [0/5] — Feeds: Profitability Tree
  ⬜ Marketing & Sales    [0/5] — Feeds: Ansoff, STP
  ⬜ Team & Operations    [0/5] — Feeds: McKinsey 7S, VRIO
  ⬜ Challenges & Goals   [0/4] — Feeds: SWOT/TOWS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Memory System

The `.memory/` directory stores critical context across sessions:
- User preferences (tone, format, language)
- Key facts and metrics
- Corrections and decisions
- Information gaps

Every new session reads `.memory/` and `.ai/.brief/` first, so the AI never starts from zero.

## Core Design Principles

- **No advice during exploration** — The AI cannot give recommendations until it has full context.
- **Persistent memory** — All context is saved to files, not held in conversation history.
- **Skills-first** — Every response must pass through `stop-slop` and context-engineering filters.
- **Framework-driven** — Analysis is grounded in proven strategic frameworks, not generic wisdom.
- **Progress transparency** — The Understanding Meter shows exactly where gaps remain.

## Links

- **Stop Slop:** Hardik Pandya's AI writing pattern removal (`.ai/.skills/.stop-slop/`)
- **Agent Skills for Context Engineering:** 15 skills for production agent systems (`.ai/.skills/.agent-skills-for-context-engineering/`)
- **Marketing Skills:** Corey Haines' marketing skill library (`.ai/.skills/.marketing/`)

## License

MIT
