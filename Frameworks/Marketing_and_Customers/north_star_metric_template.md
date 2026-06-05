# North Star Metric (NSM) Framework Template
### Rebuilt from Primary Research | Sources: Sean Ellis · Amplitude · Reforge · GoPractice · Mixpanel

---

## Before You Start — Critical Instructions

> **The single most important rule of the North Star Metric:**
> *"Revenue is the price your customer pays. The North Star Metric is the value your customer gets in return. If you optimize for revenue without optimizing for customer value, you will eventually lose both. The NSM must represent the moment the customer experiences the core value of your product."*
> *(Source: Sean Ellis — Growth Hacking, 2024; Amplitude — North Star Playbook, 2025)*

**How to use this template:**

**Step 1** — Define the **Core Customer Value** your product delivers.
**Step 2** — Select the single **North Star Metric (NSM)** that best quantifies that value.
**Step 3** — Break the NSM down into the **Input Metrics** (The Constellation / Metric Tree).
**Step 4** — Assign specific **Input Metrics** to specific teams (Product, Marketing, Ops).
**Step 5** — Define the **Initiatives** (the actual work) that will drive the input metrics.

> ⚠️ **Research warning:** The most common mistake is choosing a vanity metric (e.g., "Total Registered Users") or a pure business metric (e.g., "Monthly Recurring Revenue / MRR") as the North Star. MRR is a lagging indicator. Your NSM must be a *leading indicator* of future revenue. If the NSM goes up, revenue should naturally follow.
> *(Source: Reforge — Retention & Engagement, 2025; GoPractice — NSM Guide, 2025)*

> 🔁 **Review cycle:** The North Star Metric should remain stable for **1 to 3 years**. If you are changing your NSM every quarter, it is not a North Star — it is an OMTM (One Metric That Matters).
> *(Source: Focused Chaos — NSM vs OMTM, 2025)*

---

## STAGE 1: DEFINING THE NORTH STAR (The Output)

*The NSM is the single, top-level metric that best captures the core value your product delivers to its customers. It serves as a compass for the entire organization.*

### 1. Identify Core Customer Value
*Before picking a metric, answer these questions in plain English:*

- **When does our customer say "Aha! This is valuable"?**
  >
- **What is the exact action they take that proves they got value?**
  >
- **If our business disappeared tomorrow, what specific progress or capability would our customers lose?**
  >

### 2. Draft Your North Star Metric Candidates
*Brainstorm 2–3 potential metrics based on the answers above. (Examples: Spotify = Time spent listening; Airbnb = Nights booked; WhatsApp = Messages sent).*

- **Candidate 1:**
- **Candidate 2:**
- **Candidate 3:**

### 3. The NSM Validation Checklist
*Run your best candidate through this checklist. It must pass ALL criteria.*

| Criteria | Question | Pass / Fail |
|---|---|---|
| **Value-Driven** | Does it measure the moment the customer finds value? | |
| **Leading Indicator** | Does it predict future revenue/retention (rather than just looking backward)? | |
| **Actionable** | Can the team actually influence this metric through their daily work? | |
| **Understandable** | Is it simple enough that every employee can understand it? | |
| **Frequency** | Does it happen frequently enough to measure changes quickly? (e.g., Daily/Weekly) | |

### The Decision: Our North Star Metric
> **NSM:** __________________________________________________________________
*Why we chose this:*
>

*(Source: Amplitude — NSM Validation Checklist, 2025; Mixpanel — Selecting Your NSM, 2025)*

---

## STAGE 2: THE METRIC TREE (The Inputs)

*A North Star Metric is too big for one team to move alone. You must break it down into a "Constellation" or "Metric Tree" of Input Metrics. These are the levers your teams can actually pull.*

**The Standard Equation:**
`North Star Metric = Breadth × Depth × Frequency`

### 1. Define the Input Levers

| Dimension | Definition | Your Specific Input Metric |
|---|---|---|
| **Breadth (Acquisition)** | How many active users are finding value? | *(e.g., # of newly activated users this week)* |
| **Depth (Engagement)** | How much value are they getting per session? | *(e.g., # of items engaged with per session)* |
| **Frequency (Retention)** | How often are they returning for that value? | *(e.g., # of return visits per week)* |
| **Efficiency (Performance)** | How fast/reliably is the value delivered? | *(e.g., Load time, success rate of core action)* |

### 2. The One Metric That Matters (OMTM)
*While the NSM is for the whole company for the next 1–3 years, the OMTM is what a specific squad focuses on for the next 3–6 months to drive one of the inputs.*

- **Current Company-Wide OMTM (Focus for this Quarter):**
  >
- **Why this input is the current bottleneck:**
  >

*(Source: Amplitude — The Metric Tree Framework, 2025; Reforge — Input vs Output Metrics, 2025)*

---

## STAGE 3: ACCOUNTABILITY & ALIGNMENT (The Leaves)

*Map your Input Metrics to specific teams and the actual work they are doing right now.*

| Strategic Dimension | Input Metric (KPI) | Owning Team / Squad | Current Initiative / Actionable Work |
|---|---|---|---|
| **Breadth** | | Marketing / Growth | |
| **Breadth** | | Sales / Partnerships | |
| **Depth** | | Product (Core) | |
| **Depth** | | UX / Design | |
| **Frequency** | | CRM / Lifecycle | |
| **Efficiency** | | Engineering / Ops | |

### Team Alignment Check
*Ask each team lead: "Can you draw a straight line from what your team is building this sprint to one of these Input Metrics?" If the answer is no, why are they building it?*

*(Source: Mural / Miro — NSM Alignment Workshops, 2025)*

---

## STAGE 4: GUARDRAIL METRICS (The Constraints)

*When you optimize heavily for one metric, you risk breaking something else. Guardrail metrics ensure you don't sacrifice long-term health for short-term NSM gains.*

| Risk / Unintended Consequence | Guardrail Metric (What we will monitor) | Red Line (Threshold to stop) |
|---|---|---|
| *(e.g., Pushing notifications to increase Frequency annoys users)* | *Unsubscribe rate / App deletion rate* | *> 2% per week* |
| | | |
| | | |

*(Source: ProdPad — KPIs vs North Stars, 2025)*

---

## When to Use This Framework

| Situation | How This Template Helps |
|---|---|
| Siloed departments | Forces Marketing, Product, and Engineering to realize they are all feeding the same ultimate metric |
| "Feature Factory" syndrome | Stops teams from shipping features just to ship them, demanding they prove how it moves an Input Metric |
| Confused strategy | Simplifies complex business models into a single, understandable equation for the whole company |
| Misaligned incentives | Prevents Sales from acquiring bad-fit customers just to hit revenue quotas (if NSM requires activation) |

*(Source: Product School — NSM Alignment, 2025; Growth Method — NSM Playbook, 2025)*

---

## Framework Limitations — Know What It Cannot Do

| Limitation | What to Use Instead |
|---|---|
| It ignores short-term cash flow | You must still track standard financial metrics (MRR, CAC, LTV, Burn Rate) alongside the NSM |
| It can be too abstract for daily engineering tasks | Engineers should focus on specific **Input Metrics** (latency, bug rates) rather than the overall NSM |
| It assumes a single core value | Multi-product conglomerates (e.g., Amazon, Google) require different NSMs for different business units |
| It can lead to tunnel vision | Always use **Guardrail Metrics** to prevent destructive optimization |

> *"The North Star Metric is a compass, not a map. It tells you which way is North, but it does not tell you how to cross the river. You still need great product sense, strategy, and execution to get there."*
> *(Source: GoPractice — NSM Limitations, 2025)*

---

## Sources & References

| Source | Application in This Template |
|---|---|
| Sean Ellis — *Growth Hacking Methodology* | Framework origin; NSM vs. Revenue distinction |
| Amplitude — *The North Star Playbook*, 2025 | The Metric Tree structure; Breadth, Depth, Frequency components; Validation Checklist |
| Reforge — *Retention & Engagement*, 2025 | Input vs. Output metrics definition |
| Focused Chaos — *NSM vs OMTM*, 2025 | Differentiating long-term NSM from short-term squad OMTMs |
| GoPractice — *NSM Guide*, 2025 | Framework limitations; the danger of vanity metrics |
| Mixpanel — *Selecting Your NSM*, 2025 | Brainstorming and selecting metrics based on customer value |
| ProdPad — *KPIs vs North Stars*, 2025 | The concept of Guardrail Metrics to prevent destructive optimization |
| Product School — *NSM Alignment*, 2025 | Using the NSM to break down organizational silos |

---

*Template version: 1.0 — Fully Research-Rebuilt | June 2026*
*Framework origin: Sean Ellis (Growth Hacking) / Amplitude Product Strategy*
*Owner: [Name / Team] | Review date: [Date]*
