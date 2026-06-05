# MoSCoW Method Template (Prioritization Framework)
### Rebuilt from Primary Research | Sources: Dai Clegg (DSDM) · Agile Business Consortium · GeeksForGeeks

---

## Before You Start — Critical Instructions

> **The single most important rule of the MoSCoW Method:**
> *"If everything is a 'Must Have', then nothing is a 'Must Have'. The purpose of MoSCoW is to force hard conversations about trade-offs before development begins. You must protect the project's time and budget by strictly limiting the 'Must Haves' to the absolute minimum required for success."*
> *(Source: Agile Business Consortium — MoSCoW Prioritization; Ludi.co — Agile Methods, 2025)*

**How to use this template:**

**Step 1** — Gather all stakeholders and define what "success" looks like for this specific project, sprint, or timebox.
**Step 2** — List all proposed features, tasks, or requirements.
**Step 3** — Categorize every item using the strict diagnostic questions below.
**Step 4** — Apply the **60-20-20 Rule**: Ensure your *Must Haves* do not exceed 60% of your total capacity/budget.
**Step 5** — Timebox the execution: Lock the scope and start working.

> ⚠️ **Research warning:** The "W" in MoSCoW stands for **Won't Have (this time)**, not *Will Not Have Ever*. It is a parking lot for good ideas that simply do not fit into the current timebox. Explicitly agreeing on what you *won't* do is just as important as agreeing on what you *will* do.
> *(Source: ProductPlan — MoSCoW Framework, 2025)*

> 🔁 **Review cycle:** MoSCoW is dynamic. If a timebox runs out of time, *Could Haves* and *Should Haves* are dropped to protect the *Must Haves*. Re-evaluate priorities at the start of every new sprint or project phase.

---

## STAGE 1: THE 60-20-20 CAPACITY CHECK

*Before you start categorizing, establish your boundaries. If you plan for 100% capacity and a developer gets sick or a bug appears, the project will fail. You must build in flexibility.*

- **Total Estimated Capacity for this Timebox:** *(e.g., 100 developer hours, or $50,000 budget)*
  >
- **Must Have Limit (Max 60%):** *(e.g., 60 hours)*
  >
- **Should Have Limit (~20%):** *(e.g., 20 hours)*
  >
- **Could Have (Flexibility/Buffer) (~20%):** *(e.g., 20 hours)*
  >

*(Source: St Andrews Univ. — Agile Capacity Planning, 2025)*

---

## STAGE 2: CATEGORIZATION

### 🔴 MUST HAVE (M)
*Non-negotiable. If even one of these is missing, the launch/project is considered a failure. Ask: "Is it illegal, unsafe, or entirely unusable without this?"*

| Requirement / Task | Owner / Team | Est. Effort/Cost |
|---|---|---|
| *(e.g., Secure User Login)* | | |
| *(e.g., Payment Gateway Integration)* | | |
| | | |
| | | |
| **Total Effort:** *(Must not exceed 60% capacity)* | | **[Total]** |

### 🟡 SHOULD HAVE (S)
*Important and highly desirable, but not vital for the immediate release. Ask: "Is it painful to leave this out, but manageable with a temporary manual workaround?"*

| Requirement / Task | Owner / Team | Est. Effort/Cost | Workaround if dropped? |
|---|---|---|---|
| *(e.g., 'Forgot Password' automated flow)* | | | *(Manual email reset by admin)* |
| *(e.g., Dashboard Analytics export)* | | | *(Provide raw data via database query)* |
| | | | |
| | | | |
| **Total Effort:** *(Aim for ~20% capacity)* | | **[Total]** |

### 🟢 COULD HAVE (C)
*The "Nice-to-haves". Desirable, but their absence won't cause major issues. Ask: "Would this add value if we have extra time, but its absence won't be noticed by core users?"*

| Requirement / Task | Owner / Team | Est. Effort/Cost |
|---|---|---|
| *(e.g., Dark Mode UI)* | | |
| *(e.g., Animated loading screens)* | | |
| | | |
| | | |
| **Total Effort:** *(Aim for ~20% capacity — acts as your buffer)* | | **[Total]** |

### ⚪ WON'T HAVE (W)
*Out of scope for this specific timebox. Ask: "Are we explicitly agreeing NOT to work on this right now to protect the Must Haves?"*

| Requirement / Task | Reason for delaying | Re-evaluate Date |
|---|---|---|
| *(e.g., Mobile App Version)* | *We must prove web viability first* | *Q4 2026* |
| *(e.g., AI Chatbot Integration)* | *Too expensive for MVP phase* | *Next funding round* |
| | | |

---

## STAGE 3: SYNTHESIS & STAKEHOLDER SIGN-OFF

*The MoSCoW matrix is useless if stakeholders don't agree to it. If the CEO expects a "Won't Have" feature for launch, you must have the hard conversation now.*

### The Trade-off Agreement
*If we run out of time or budget, we all agree to drop items from the bottom up (starting with 'Could Haves'). We will NOT extend the deadline or increase the budget to accommodate them.*

- **Approved by (Product Manager):** ___________________________
- **Approved by (Lead Engineer):** ___________________________
- **Approved by (Business Stakeholder):** ___________________________

---

## When to Use This Framework

| Situation | How This Template Helps |
|---|---|
| MVP (Minimum Viable Product) Scoping | Prevents "feature creep" by forcing founders to strip the product down to its absolute core *Must Haves* |
| Fixed Deadline Projects | When the deadline cannot move (e.g., regulatory compliance date, public holiday launch), MoSCoW ensures the scope shrinks instead of the deadline extending |
| Stakeholder Disputes | Neutralizes emotional arguments by using objective diagnostic questions to define what is truly critical |
| Timeboxing | Allows teams to work rapidly within a 2-week sprint, knowing exactly what to drop if they hit a roadblock |

*(Source: ProductPlan — Prioritization frameworks, 2025; SimpliAxis — Timeboxing, 2025)*

---

## Framework Limitations — Know What It Cannot Do

| Limitation | What to Use Instead |
|---|---|
| Does not account for task dependencies | Use a **Gantt Chart** or **PERT Chart** to map the order of operations |
| Does not help you manage your personal daily time effectively | Use the **Eisenhower Matrix** or **Pomodoro Technique** |
| Can be subjective if diagnostic questions are ignored | Use **RICE Scoring** (Reach, Impact, Confidence, Effort) if you need a strictly mathematical, data-driven prioritization method |

---

## Sources & References

| Source | Application in This Template |
|---|---|
| Clegg, Dai (Dynamic Systems Development Method) | Framework origin; Must, Should, Could, Won't definitions |
| Agile Business Consortium | Trade-off agreements; the "Won't Have this time" distinction |
| St Andrews Univ. — *Agile Capacity Planning*, 2025 | The 60-20-20 allocation rule to prevent burnout and protect core features |
| SimpliAxis — *Timeboxing*, 2025 | Using time constraints to enforce MoSCoW prioritization |
| ProductPlan — *Prioritization frameworks*, 2025 | Workaround identification for "Should Haves"; Stakeholder sign-off necessity |

---

*Template version: 1.0 — Fully Research-Rebuilt | June 2026*
*Framework origin: Dai Clegg (DSDM)*
*Owner: [Name / Team] | Review date: [Date]*
