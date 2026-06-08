# North Star Metric (NSM) Framework Template

### Rebuilt from Primary Research | Sources: Sean Ellis · Amplitude · Reforge · GoPractice · Mixpanel

---

## Before You Start — Critical Instructions

> **The single most important rule of the North Star Metric:**
> _"Revenue is the price your customer pays. The North Star Metric is the value your customer gets in return. If you optimize for revenue without optimizing for customer value, you will eventually lose both. The NSM must represent the moment the customer experiences the core value of your product."_
> _(Source: Sean Ellis — Growth Hacking, 2024; Amplitude — North Star Playbook, 2025)_

**How to use this template:**

**Step 1** — Define the **Core Customer Value** your product delivers.
**Step 2** — Select the single **North Star Metric (NSM)** that best quantifies that value.
**Step 3** — Break the NSM down into the **Input Metrics** (The Constellation / Metric Tree).
**Step 4** — Assign specific **Input Metrics** to specific teams (Product, Marketing, Ops).
**Step 5** — Define the **Initiatives** (the actual work) that will drive the input metrics.

> ⚠️ **Research warning:** The most common mistake is choosing a vanity metric (e.g., "Total Registered Users") or a pure business metric (e.g., "Monthly Recurring Revenue / MRR") as the North Star. MRR is a lagging indicator. Your NSM must be a _leading indicator_ of future revenue. If the NSM goes up, revenue should naturally follow.
> _(Source: Reforge — Retention & Engagement, 2025; GoPractice — NSM Guide, 2025)_

> 🔁 **Review cycle:** The North Star Metric should remain stable for **1 to 3 years**. If you are changing your NSM every quarter, it is not a North Star — it is an OMTM (One Metric That Matters).
> _(Source: Focused Chaos — NSM vs OMTM, 2025)_

---

## STAGE 1: DEFINING THE NORTH STAR (The Output)

_The NSM is the single, top-level metric that best captures the core value your product delivers to its customers. It serves as a compass for the entire organization._

### 1. Identify Core Customer Value

_Before picking a metric, answer these questions in plain English:_

- **When does our customer say "Aha! This is valuable"?**
  >
- **What is the exact action they take that proves they got value?**
  >
- **If our business disappeared tomorrow, what specific progress or capability would our customers lose?**
  >

### 2. Draft Your North Star Metric Candidates

_Brainstorm 2–3 potential metrics based on the answers above. (Examples: Spotify = Time spent listening; Airbnb = Nights booked; WhatsApp = Messages sent)._

- **Candidate 1:**
- **Candidate 2:**
- **Candidate 3:**

### 3. The NSM Validation Checklist

_Run your best candidate through this checklist. It must pass ALL criteria._

| Criteria              | Question                                                                          | Pass / Fail |
| --------------------- | --------------------------------------------------------------------------------- | ----------- |
| **Value-Driven**      | Does it measure the moment the customer finds value?                              |             |
| **Leading Indicator** | Does it predict future revenue/retention (rather than just looking backward)?     |             |
| **Actionable**        | Can the team actually influence this metric through their daily work?             |             |
| **Understandable**    | Is it simple enough that every employee can understand it?                        |             |
| **Frequency**         | Does it happen frequently enough to measure changes quickly? (e.g., Daily/Weekly) |             |

### The Decision: Our North Star Metric

> **NSM:** ********************************\_\_********************************
> _Why we chose this:_

_(Source: Amplitude — NSM Validation Checklist, 2025; Mixpanel — Selecting Your NSM, 2025)_

---

## STAGE 2: THE METRIC TREE (The Inputs)

_A North Star Metric is too big for one team to move alone. You must break it down into a "Constellation" or "Metric Tree" of Input Metrics. These are the levers your teams can actually pull._

**The Standard Equation:**
`North Star Metric = Breadth × Depth × Frequency`

### 1. Define the Input Levers

| Dimension                    | Definition                                   | Your Specific Input Metric                       |
| ---------------------------- | -------------------------------------------- | ------------------------------------------------ |
| **Breadth (Acquisition)**    | How many active users are finding value?     | _(e.g., # of newly activated users this week)_   |
| **Depth (Engagement)**       | How much value are they getting per session? | _(e.g., # of items engaged with per session)_    |
| **Frequency (Retention)**    | How often are they returning for that value? | _(e.g., # of return visits per week)_            |
| **Efficiency (Performance)** | How fast/reliably is the value delivered?    | _(e.g., Load time, success rate of core action)_ |

### 2. The One Metric That Matters (OMTM)

_While the NSM is for the whole company for the next 1–3 years, the OMTM is what a specific squad focuses on for the next 3–6 months to drive one of the inputs._

- **Current Company-Wide OMTM (Focus for this Quarter):**
  >
- **Why this input is the current bottleneck:**
  >

_(Source: Amplitude — The Metric Tree Framework, 2025; Reforge — Input vs Output Metrics, 2025)_

---

## STAGE 3: ACCOUNTABILITY & ALIGNMENT (The Leaves)

_Map your Input Metrics to specific teams and the actual work they are doing right now._

| Strategic Dimension | Input Metric (KPI) | Owning Team / Squad  | Current Initiative / Actionable Work |
| ------------------- | ------------------ | -------------------- | ------------------------------------ |
| **Breadth**         |                    | Marketing / Growth   |                                      |
| **Breadth**         |                    | Sales / Partnerships |                                      |
| **Depth**           |                    | Product (Core)       |                                      |
| **Depth**           |                    | UX / Design          |                                      |
| **Frequency**       |                    | CRM / Lifecycle      |                                      |
| **Efficiency**      |                    | Engineering / Ops    |                                      |

### Team Alignment Check

_Ask each team lead: "Can you draw a straight line from what your team is building this sprint to one of these Input Metrics?" If the answer is no, why are they building it?_

_(Source: Mural / Miro — NSM Alignment Workshops, 2025)_

---

## STAGE 4: GUARDRAIL METRICS (The Constraints)

_When you optimize heavily for one metric, you risk breaking something else. Guardrail metrics ensure you don't sacrifice long-term health for short-term NSM gains._

| Risk / Unintended Consequence                                      | Guardrail Metric (What we will monitor) | Red Line (Threshold to stop) |
| ------------------------------------------------------------------ | --------------------------------------- | ---------------------------- |
| _(e.g., Pushing notifications to increase Frequency annoys users)_ | _Unsubscribe rate / App deletion rate_  | _> 2% per week_              |
|                                                                    |                                         |                              |
|                                                                    |                                         |                              |

_(Source: ProdPad — KPIs vs North Stars, 2025)_

---

## When to Use This Framework

| Situation                  | How This Template Helps                                                                                 |
| -------------------------- | ------------------------------------------------------------------------------------------------------- |
| Siloed departments         | Forces Marketing, Product, and Engineering to realize they are all feeding the same ultimate metric     |
| "Feature Factory" syndrome | Stops teams from shipping features just to ship them, demanding they prove how it moves an Input Metric |
| Confused strategy          | Simplifies complex business models into a single, understandable equation for the whole company         |
| Misaligned incentives      | Prevents Sales from acquiring bad-fit customers just to hit revenue quotas (if NSM requires activation) |

_(Source: Product School — NSM Alignment, 2025; Growth Method — NSM Playbook, 2025)_

---

## Framework Limitations — Know What It Cannot Do

| Limitation                                         | What to Use Instead                                                                                    |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| It ignores short-term cash flow                    | You must still track standard financial metrics (MRR, CAC, LTV, Burn Rate) alongside the NSM           |
| It can be too abstract for daily engineering tasks | Engineers should focus on specific **Input Metrics** (latency, bug rates) rather than the overall NSM  |
| It assumes a single core value                     | Multi-product conglomerates (e.g., Amazon, Google) require different NSMs for different business units |
| It can lead to tunnel vision                       | Always use **Guardrail Metrics** to prevent destructive optimization                                   |

> _"The North Star Metric is a compass, not a map. It tells you which way is North, but it does not tell you how to cross the river. You still need great product sense, strategy, and execution to get there."_
> _(Source: GoPractice — NSM Limitations, 2025)_

---

## Sources & References

| Source                                      | Application in This Template                                                          |
| ------------------------------------------- | ------------------------------------------------------------------------------------- |
| Sean Ellis — _Growth Hacking Methodology_   | Framework origin; NSM vs. Revenue distinction                                         |
| Amplitude — _The North Star Playbook_, 2025 | The Metric Tree structure; Breadth, Depth, Frequency components; Validation Checklist |
| Reforge — _Retention & Engagement_, 2025    | Input vs. Output metrics definition                                                   |
| Focused Chaos — _NSM vs OMTM_, 2025         | Differentiating long-term NSM from short-term squad OMTMs                             |
| GoPractice — _NSM Guide_, 2025              | Framework limitations; the danger of vanity metrics                                   |
| Mixpanel — _Selecting Your NSM_, 2025       | Brainstorming and selecting metrics based on customer value                           |
| ProdPad — _KPIs vs North Stars_, 2025       | The concept of Guardrail Metrics to prevent destructive optimization                  |
| Product School — _NSM Alignment_, 2025      | Using the NSM to break down organizational silos                                      |

---

_Template version: 1.0 — Fully Research-Rebuilt | June 2026_
_Framework origin: Sean Ellis (Growth Hacking) / Amplitude Product Strategy_
_Owner: [Name / Team] | Review date: [Date]_
