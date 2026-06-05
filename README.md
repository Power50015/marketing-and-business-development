# 360° Business Discovery & Marketing Intelligence System

> **AI-powered business intelligence framework for entrepreneurs, consultants, and marketing teams.**
> Combines structured business discovery, 48 strategic frameworks, and 44 executable marketing skills into a single integrated workspace that works with any LLM.

---

## What This System Does

This is a complete **business intelligence operating system** that lets any AI model act as a senior business consultant and marketing strategist. Instead of generic advice, the AI conducts structured discovery, populates proven frameworks, and executes specific marketing tasks — all with rich context from a deep discovery process.

**The system answers four critical questions:**

1. **Where are we?** — Structured 8-area discovery covering project, customer, value prop, market, business model, marketing, team, and challenges.
2. **What framework applies?** — 48 research-backed strategic frameworks (SWOT, Blue Ocean, Porter's Five Forces, McKinsey 7S, etc.).
3. **What marketing moves make sense?** — 44 specialized skills covering every marketing discipline from SEO to video production, cold email to pricing strategy.
4. **How do we execute?** — Ready-to-use templates, evaluation rubrics, and integration guides for real-world tools.

---

## System Architecture

The system is organized as a **multi-layer intelligence stack**:

```
┌─────────────────────────────────────────────────────────────┐
│  LAYER 1: DISCOVERY ENGINE                                  │
│  └── starter_prompt.md — structured 37-question discovery  │
│      conversation that builds 100% project understanding     │
│      before generating any advice. Outputs PROJECT_BRIEF.md │
├─────────────────────────────────────────────────────────────┤
│  LAYER 2: STRATEGIC FRAMEWORKS (Frameworks/)               │
│  └── 48 templates across 11 categories:                    │
│      Strategy & Direction (Blue Ocean, Porter, 7S, etc.)   │
│      External Analysis (Five Forces, PESTLE, BCG, etc.)    │
│      Internal Analysis (SWOT/TOWS, Profitability Tree)     │
│      Growth & Innovation (Ansoff, Three Horizons, etc.)    │
│      Marketing & Customers (4Ps/7Ps, Journey Map, JTBD)    │
│      Finance & Risk (Break-Even, Cost-Benefit)             │
│      Performance & Operations (OKRs, SMART Goals, PDCA)    │
├─────────────────────────────────────────────────────────────┤
│  LAYER 3: CONTEXT ENGINEERING (Skills/context-engineering/) │
│  └── 13 foundational agent infrastructure skills:           │
│      Context Fundamentals, Degradation, Compression,        │
│      Optimization, Multi-Agent Patterns, Memory Systems,    │
│      Tool Design, Filesystem Context, Evaluation,           │
│      Advanced Evaluation, Harness Engineering,              │
│      Project Development, Latent Briefing                   │
│      (Source: muratcankoylan/Agent-Skills-for-Context-Engineering)│
├─────────────────────────────────────────────────────────────┤
│  LAYER 4: MARKETING SKILLS (Skills/)                         │
│  └── 44 specialized skill modules for specific tasks:        │
│      SEO, Content Strategy, Copywriting, Ads, Analytics     │
│      Cold Email, Prospecting, CRO, A/B Testing             │
│      Video, Social, PR, Launch, Pricing...               │
│      Each skill: before-starting → framework → output format│
├─────────────────────────────────────────────────────────────┤
│  LAYER 5: QUALITY CONTROL                                    │
│  └── stop-slop skill — removes AI writing patterns, filler │
│      phrases, and formulaic structures from all generated   │
│      prose before it reaches the user.                     │
├─────────────────────────────────────────────────────────────┤
│  OUTPUT: PROJECT_BRIEF.md + filled frameworks +           │
│          marketing execution plans + action plans           │
└─────────────────────────────────────────────────────────────┘
```

---

## How It Works

### For First-Time Users

1. **Start with `starter_prompt.md`** — Copy and paste it to any AI (ChatGPT, Claude, Cursor, etc.)
2. **Answer 37 discovery questions** across 8 areas — the AI shows you exactly how well it understands your project (0–100%)
3. **Receive PROJECT_BRIEF.md** — A complete project intelligence brief with strategic frameworks selected and marketing skills mapped
4. **Execute with specific skills** — The AI now knows your project deeply and can apply any skill with full context

### For Existing Projects

If you already have a `PROJECT_BRIEF.md`, **any AI reading it** has instant full context and can:

- Apply strategic frameworks directly to your situation
- Execute specific marketing skills with your context pre-loaded
- Generate action plans, content, campaigns, or analysis that is actually relevant

---

## Directory Structure

```
├── starter_prompt.md                          # The discovery conversation prompt
├── PROJECT_BRIEF_template.md                    # Template for the generated project brief
├── README.md                                    # This file
├── Frameworks/                                  # 48 strategic framework templates
│   ├── Strategy_and_Direction/                  # Blue Ocean, Porter, 7S, VRIO, etc.
│   ├── External_Analysis/                       # Five Forces, PESTLE, BCG, Ansoff, etc.
│   ├── Internal_Analysis/                       # SWOT/TOWS, Profitability Tree
│   ├── Growth_and_Innovation/                   # Three Horizons, Greiner, GE/McKinsey
│   ├── Marketing_and_Customers/                 # 4Ps/7Ps, STP, Journey Map, JTBD
│   ├── Business_Models/                         # BMC, Lean Canvas, Value Proposition
│   ├── Finance_and_Risk/                        # Break-Even, Cost-Benefit, Risk Matrix
│   ├── Performance_and_Measurement/             # OKRs, Balanced Scorecard
│   ├── Operations_and_Projects/                 # SMART Goals, PDCA, RACI, Kotter
│   ├── Time_and_Priority_Management/            # Eisenhower Matrix, MoSCoW
│   ├── Thinking_and_Problem_Solving/            # MECE, Pyramid Principle, RCA
│   ├── business_strategy_template_general.md    # Complete strategy document
│   ├── action_plan_template_EN.md              # Execution planning template
│   └── ecommerce_strategy_template.md          # E-commerce specific strategy
├── Skills/                                      # 44 marketing skill modules
│   ├── context-engineering/                     # Context engineering (13 skills)
│   │   ├── context-fundamentals/                # Context window anatomy & attention mechanics
│   │   ├── context-degradation/                 # Lost-in-middle, poisoning, distraction patterns
│   │   ├── context-compression/                 # Anchored Iterative, Opaque, Regenerative compression
│   │   ├── context-optimization/                # Compaction, masking, caching, partitioning
│   │   ├── multi-agent-patterns/                # Orchestrator, swarm, hierarchical architectures
│   │   ├── memory-systems/                      # Short/long-term & graph-based memory
│   │   ├── tool-design/                         # Agent-tool contracts, consolidation, descriptions
│   │   ├── filesystem-context/                  # Dynamic discovery, offloading, persistence
│   │   ├── evaluation/                          # Deterministic checks, rubrics, quality gates
│   │   ├── advanced-evaluation/                 # LLM-as-Judge, pairwise, bias mitigation
│   │   ├── harness-engineering/                 # Locked metrics, durable logs, novelty gates
│   │   ├── project-development/                 # Task-model fit, pipelines, cost estimation
│   │   └── latent-briefing/                     # KV cache compaction for orchestrator→worker
│   ├── prospecting/                             # B2B/B2C lead list building
│   ├── cold-email/                              # Outreach email sequences
│   ├── copywriting/                             # Marketing copy
│   ├── copy-editing/                            # Quality control for copy
│   ├── seo-audit/                               # Technical SEO analysis
│   ├── content-strategy/                        # Content planning
│   ├── cro/                                     # Conversion optimization
│   ├── ab-testing/                              # Experiment design
│   ├── analytics/                               # Tracking & measurement
│   ├── video/                                   # AI video production
│   ├── social/                                  # Social media strategy
│   ├── ads/                                     # Paid advertising
│   ├── ad-creative/                             # Ad creative design
│   ├── marketing-plan/                          # Full 12-month fCMO plan
│   ├── marketing-ideas/                         # 139 tactical ideas library
│   ├── marketing-psychology/                    # Behavioral marketing
│   ├── product-marketing/                       # Positioning & ICP
│   ├── pricing/                                 # Pricing strategy
│   ├── churn-prevention/                        # Retention tactics
│   ├── referrals/                               # Referral programs
│   ├── onboarding/                              # User activation
│   ├── signup/                                  # Conversion flows
│   ├── lead-magnets/                            # Lead capture assets
│   ├── free-tools/                              # Free tool marketing
│   ├── emails/                                  # Lifecycle email sequences
│   ├── competitor-profiling/                    # Deep competitor research
│   ├── competitors/                             # Competitive analysis
│   ├── community-marketing/                     # Community building
│   ├── co-marketing/                            # Partnership marketing
│   ├── directory-submissions/                   # Directory marketing
│   ├── programmatic-seo/                        # Scaled SEO content
│   ├── ai-seo/                                  # AI search optimization
│   ├── site-architecture/                       # Site structure
│   ├── schema/                                  # Structured data
│   ├── image/                                   # AI image generation
│   ├── sms/                                     # SMS marketing
│   ├── popups/                                  # Modal/popup marketing
│   ├── paywalls/                                # Paywall strategy
│   ├── launch/                                  # Product launches
│   ├── sales-enablement/                        # Sales materials
│   ├── revops/                                  # Revenue operations
│   ├── aso/                                     # App store optimization
│   ├── stop-slop/                               # Remove AI writing patterns
│   └── ... (and more)
└── .git/                                        # Version control
```

---

## Key Design Principles

### 1. Context Before Advice
The system **refuses to give advice until it fully understands your project**. The 37-question discovery process ensures the AI doesn't jump to generic recommendations.

### 2. Frameworks are Research-Backed
Every framework template includes:
- Original academic source (Harvard, INSEAD, McKinsey, etc.)
- When and why to use it
- Step-by-step application guide
- Real-world examples
- Limitations and what to use instead

### 3. Skills are Specific, Not Generic
Each skill is a **specialized module** with:
- Clear trigger conditions (when to use it)
- Before-starting checklist (what context to gather)
- Framework or methodology to apply
- Output format (what deliverable to produce)
- Related skills (what connects to what)
- Common mistakes to avoid

### 4. Quality Control is Built-In
The `stop-slop` skill actively removes:
- Filler phrases and throat-clearing openers
- Formulaic AI writing patterns
- Passive voice and vague declarations
- Predictable three-part lists and rhetorical setups

### 5. Skills Chain Together
Skills reference related skills, creating a **natural workflow**:
- `product-marketing` → sets context for everything else
- `customer-research` → feeds `copywriting` and `cro`
- `prospecting` → feeds `cold-email` → feeds `sales-enablement`
- `content-strategy` → feeds `copywriting` → feeds `seo-audit`
- `analytics` → feeds `ab-testing` and `cro`

---

## Quick Start

### Option A: Guided Discovery (Recommended)

1. Open your AI and paste the contents of `starter_prompt.md`
2. The AI will ask you one question at a time
3. Answer each question — watch your "Understanding Meter" progress 0% → 100%
4. At 100%, the AI generates your complete `PROJECT_BRIEF.md`
5. The brief includes recommended frameworks and skills mapped to your project

### Option B: Brain Dump (Faster)

1. Paste `starter_prompt.md`
2. Dump everything you know about your project in one message (even messy notes)
3. The AI maps your input against all 37 discovery questions
4. It shows you what was covered and asks only about gaps
5. Generates the brief once gaps are filled

### Option C: Direct Skill Execution

If you already have a `PROJECT_BRIEF.md` or just want to use a single skill:

1. Read the relevant `Skills/{skill}/SKILL.md`
2. Provide the context it asks for (or your PROJECT_BRIEF)
3. Follow its framework to get a specific deliverable

---

## Framework Selection Logic

The system uses a decision tree to recommend the right frameworks based on discovery:

| Discovery Finding | Recommended Framework | Priority |
|---|---|---|
| Customer not clearly defined | 3Cs Ohmae, Consumer Adoption Curve | Immediate |
| Value prop not defensible | Blue Ocean Strategy, VRIO | Immediate |
| Market dynamics unclear | Porter's Five Forces | Immediate |
| Unit economics unknown | Profitability Tree | Immediate |
| Strategy unclear | Porter Generic Strategies | Short-term |
| Early stage/growth options | Ansoff Matrix | Short-term |
| Team misaligned | McKinsey 7S | Short-term |
| Product at inflection point | Product Lifecycle | Short-term |
| Multiple products to prioritize | BCG Matrix, GE/McKinsey 9-Box | Strategic |
| Organization growing fast | Greiner Growth Model | Strategic |

---

## Skill Categories

| Category | Skills | Purpose |
|---|---|---|
| **Context Engineering** | Context Fundamentals, Degradation, Compression, Optimization, Multi-Agent Patterns, Memory Systems, Tool Design, Filesystem Context, Evaluation, Advanced Evaluation, Harness Engineering, Project Development, Latent Briefing (13 skills) | Foundational agent infrastructure — make all other skills work reliably at scale |
| **Acquisition** | SEO, content strategy, ads, social, PR, prospecting, cold email, launch, programmatic SEO, directory submissions | Find and attract customers |
| **Conversion** | Copywriting, CRO, landing pages, signup, popups, lead magnets | Turn visitors into leads/customers |
| **Activation** | Onboarding, first-session optimization, paywalls | Deliver first valued experience |
| **Retention** | Emails, churn prevention, lifecycle marketing, community marketing | Keep customers engaged |
| **Revenue** | Pricing, upsells, bundles, sales enablement | Maximize customer value |
| **Analytics** | A/B testing, analytics, CRO, customer research | Measure and improve |
| **Creative** | Video, image, ad creative, copywriting, copy-editing | Produce marketing assets |
| **Strategy** | Marketing plan, competitors, competitor profiling, marketing psychology | Strategic direction |
| **Operations** | RevOps, sales enablement | Scale marketing operations |
| **Quality** | Stop-slop | Ensure human-quality output |

---

## Technical Integration

The system is designed to work with **any AI model** and supports:

- **MCP (Model Context Protocol)** integrations for tools like Apollo, Clay, HeyGen, Firecrawl
- **API-based tools** for analytics, CRM, and marketing platforms
- **File-system based workflows** for autonomous agents (Cursor, Spec-Kit, Windsurf)
- **Chat-based delivery** for web-based AI assistants

---

## Why This System Exists

Most AI business advice is generic because the AI lacks context. This system solves that by:

1. **Structuring the discovery** — forcing deep understanding before advice
2. **Applying proven frameworks** — not reinventing strategic thinking
3. **Executing at the skill level** — delivering specific deliverables, not vague suggestions
4. **Quality-controlling the output** — removing AI slop before it reaches the user
5. **Chaining skills together** — creating end-to-end marketing workflows

---

## System Metadata

| Property | Value |
|---|---|
| **System Name** | 360° Business Discovery & Marketing Intelligence System |
| **Version** | 2.1 |
| **Discovery Questions** | 37 across 8 areas |
| **Strategic Frameworks** | 48 across 11 categories |
| **Context Engineering Skills** | 13 (from muratcankoylan/Agent-Skills-for-Context-Engineering) |
| **Marketing Skills** | 44 covering all marketing disciplines |
| **Total Skills** | 57 (13 foundational + 44 domain-specific) |
| **Compatible With** | Any LLM (ChatGPT, Claude, Gemini, Cursor, etc.) |
| **Discovery Output** | `PROJECT_BRIEF.md` — complete project intelligence |
| **Quality Control** | `stop-slop` skill for every output |
| **Author** | Enhanced from v1.0 | June 2026 |

---

## Next Steps

1. **Start a project:** Open `starter_prompt.md` and begin discovery
2. **Apply frameworks:** Browse `Frameworks/` for the right strategic tool
3. **Execute marketing:** Pick a skill from `Skills/` and follow its framework
4. **Quality check:** Run `stop-slop` on any generated prose before publishing
5. **Validate the workspace:** Run `python scripts/validate_repo.py` to confirm all files are consistent

---

## Repository Tooling

| File | Purpose |
|---|---|
| `AGENTS.md` | Canonical agent behavior spec — read this first if you are an AI |
| `CHANGELOG.md` | Version history and migration notes |
| `docs/SCHEMA.md` | File schemas (YAML frontmatter, SKILL.md, framework templates) |
| `scripts/validate_repo.py` | Automated consistency checker — run before committing |

---

*Built on: Jobs-To-Be-Done Theory | Business Model Canvas | Porter's Five Forces | McKinsey 7S | Blue Ocean Strategy | VRIO | Three Horizons | Ansoff Matrix | SWOT/TOWS | SMART Goals | OKRs | Context Engineering | Attention Mechanics | Multi-Agent Orchestration | Memory Systems | Harness Engineering*

*Compatible with: Any AI model | Skills workflows | Spec-Kit | Work Templates | Claude Code Plugin | Open Plugins | Cursor*

*Context Engineering source: muratcankoylan/Agent-Skills-for-Context-Engineering (MIT License)*
