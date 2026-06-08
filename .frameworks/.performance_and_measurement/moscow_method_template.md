# MoSCoW Method Template (Prioritization Framework)

### Rebuilt from Primary Research | Sources: Dai Clegg (DSDM) · Agile Business Consortium · GeeksForGeeks

---

## Before You Start — Critical Instructions

> **The single most important rule of the MoSCoW Method:**
> _"If everything is a 'Must Have', then nothing is a 'Must Have'. The purpose of MoSCoW is to force hard conversations about trade-offs before development begins. You must protect the project's time and budget by strictly limiting the 'Must Haves' to the absolute minimum required for success."_
> _(Source: Agile Business Consortium — MoSCoW Prioritization; Ludi.co — Agile Methods, 2025)_

**How to use this template:**

**Step 1** — Gather all stakeholders and define what "success" looks like for this specific project, sprint, or timebox.
**Step 2** — List all proposed features, tasks, or requirements.
**Step 3** — Categorize every item using the strict diagnostic questions below.
**Step 4** — Apply the **60-20-20 Rule**: Ensure your _Must Haves_ do not exceed 60% of your total capacity/budget.
**Step 5** — Timebox the execution: Lock the scope and start working.

> ⚠️ **Research warning:** The "W" in MoSCoW stands for **Won't Have (this time)**, not _Will Not Have Ever_. It is a parking lot for good ideas that simply do not fit into the current timebox. Explicitly agreeing on what you _won't_ do is just as important as agreeing on what you _will_ do.
> _(Source: ProductPlan — MoSCoW Framework, 2025)_

> 🔁 **Review cycle:** MoSCoW is dynamic. If a timebox runs out of time, _Could Haves_ and _Should Haves_ are dropped to protect the _Must Haves_. Re-evaluate priorities at the start of every new sprint or project phase.

---

## STAGE 1: THE 60-20-20 CAPACITY CHECK

_Before you start categorizing, establish your boundaries. If you plan for 100% capacity and a developer gets sick or a bug appears, the project will fail. You must build in flexibility._

- **Total Estimated Capacity for this Timebox:** _(e.g., 100 developer hours, or $50,000 budget)_
  >
- **Must Have Limit (Max 60%):** _(e.g., 60 hours)_
  >
- **Should Have Limit (~20%):** _(e.g., 20 hours)_
  >
- **Could Have (Flexibility/Buffer) (~20%):** _(e.g., 20 hours)_
  >

_(Source: St Andrews Univ. — Agile Capacity Planning, 2025)_

---

## STAGE 2: CATEGORIZATION

### 🔴 MUST HAVE (M)

_Non-negotiable. If even one of these is missing, the launch/project is considered a failure. Ask: "Is it illegal, unsafe, or entirely unusable without this?"_

| Requirement / Task                                 | Owner / Team | Est. Effort/Cost |
| -------------------------------------------------- | ------------ | ---------------- |
| _(e.g., Secure User Login)_                        |              |                  |
| _(e.g., Payment Gateway Integration)_              |              |                  |
|                                                    |              |                  |
|                                                    |              |                  |
| **Total Effort:** _(Must not exceed 60% capacity)_ |              | **[Total]**      |

### 🟡 SHOULD HAVE (S)

_Important and highly desirable, but not vital for the immediate release. Ask: "Is it painful to leave this out, but manageable with a temporary manual workaround?"_

| Requirement / Task                          | Owner / Team | Est. Effort/Cost | Workaround if dropped?                  |
| ------------------------------------------- | ------------ | ---------------- | --------------------------------------- |
| _(e.g., 'Forgot Password' automated flow)_  |              |                  | _(Manual email reset by admin)_         |
| _(e.g., Dashboard Analytics export)_        |              |                  | _(Provide raw data via database query)_ |
|                                             |              |                  |                                         |
|                                             |              |                  |                                         |
| **Total Effort:** _(Aim for ~20% capacity)_ |              | **[Total]**      |

### 🟢 COULD HAVE (C)

_The "Nice-to-haves". Desirable, but their absence won't cause major issues. Ask: "Would this add value if we have extra time, but its absence won't be noticed by core users?"_

| Requirement / Task                                                | Owner / Team | Est. Effort/Cost |
| ----------------------------------------------------------------- | ------------ | ---------------- |
| _(e.g., Dark Mode UI)_                                            |              |                  |
| _(e.g., Animated loading screens)_                                |              |                  |
|                                                                   |              |                  |
|                                                                   |              |                  |
| **Total Effort:** _(Aim for ~20% capacity — acts as your buffer)_ |              | **[Total]**      |

### ⚪ WON'T HAVE (W)

_Out of scope for this specific timebox. Ask: "Are we explicitly agreeing NOT to work on this right now to protect the Must Haves?"_

| Requirement / Task               | Reason for delaying                 | Re-evaluate Date     |
| -------------------------------- | ----------------------------------- | -------------------- |
| _(e.g., Mobile App Version)_     | _We must prove web viability first_ | _Q4 2026_            |
| _(e.g., AI Chatbot Integration)_ | _Too expensive for MVP phase_       | _Next funding round_ |
|                                  |                                     |                      |

---

## STAGE 3: SYNTHESIS & STAKEHOLDER SIGN-OFF

_The MoSCoW matrix is useless if stakeholders don't agree to it. If the CEO expects a "Won't Have" feature for launch, you must have the hard conversation now._

### The Trade-off Agreement

_If we run out of time or budget, we all agree to drop items from the bottom up (starting with 'Could Haves'). We will NOT extend the deadline or increase the budget to accommodate them._

- **Approved by (Product Manager):** ************\_\_\_************
- **Approved by (Lead Engineer):** ************\_\_\_************
- **Approved by (Business Stakeholder):** ************\_\_\_************

---

## When to Use This Framework

| Situation                            | How This Template Helps                                                                                                                                     |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MVP (Minimum Viable Product) Scoping | Prevents "feature creep" by forcing founders to strip the product down to its absolute core _Must Haves_                                                    |
| Fixed Deadline Projects              | When the deadline cannot move (e.g., regulatory compliance date, public holiday launch), MoSCoW ensures the scope shrinks instead of the deadline extending |
| Stakeholder Disputes                 | Neutralizes emotional arguments by using objective diagnostic questions to define what is truly critical                                                    |
| Timeboxing                           | Allows teams to work rapidly within a 2-week sprint, knowing exactly what to drop if they hit a roadblock                                                   |

_(Source: ProductPlan — Prioritization frameworks, 2025; SimpliAxis — Timeboxing, 2025)_

---

## Framework Limitations — Know What It Cannot Do

| Limitation                                                    | What to Use Instead                                                                                                             |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Does not account for task dependencies                        | Use a **Gantt Chart** or **PERT Chart** to map the order of operations                                                          |
| Does not help you manage your personal daily time effectively | Use the **Eisenhower Matrix** or **Pomodoro Technique**                                                                         |
| Can be subjective if diagnostic questions are ignored         | Use **RICE Scoring** (Reach, Impact, Confidence, Effort) if you need a strictly mathematical, data-driven prioritization method |

---

## Sources & References

| Source                                             | Application in This Template                                                 |
| -------------------------------------------------- | ---------------------------------------------------------------------------- |
| Clegg, Dai (Dynamic Systems Development Method)    | Framework origin; Must, Should, Could, Won't definitions                     |
| Agile Business Consortium                          | Trade-off agreements; the "Won't Have this time" distinction                 |
| St Andrews Univ. — _Agile Capacity Planning_, 2025 | The 60-20-20 allocation rule to prevent burnout and protect core features    |
| SimpliAxis — _Timeboxing_, 2025                    | Using time constraints to enforce MoSCoW prioritization                      |
| ProductPlan — _Prioritization frameworks_, 2025    | Workaround identification for "Should Haves"; Stakeholder sign-off necessity |

---

_Template version: 1.0 — Fully Research-Rebuilt | June 2026_
_Framework origin: Dai Clegg (DSDM)_
_Owner: [Name / Team] | Review date: [Date]_
