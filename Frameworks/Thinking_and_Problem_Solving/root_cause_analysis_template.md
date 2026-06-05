# Root Cause Analysis (Fishbone & 5 Whys) Template
### Rebuilt from Primary Research | Sources: Kaoru Ishikawa · Toyota Production System · Lean Six Sigma · ASQ · Management Consulting Practices

---

## Before You Start — Critical Instructions

> **The single most important rule of Root Cause Analysis:**
> *"Never confuse a symptom with a root cause. If you implement a fix and the problem can still happen again under different circumstances, you only treated a symptom. A true root cause, when removed, prevents the problem permanently."*
> *(Source: ASQ — American Society for Quality, Root Cause Analysis, 2025)*

**How to use this template:**

**Step 1** — Define the problem accurately and neutrally without assigning blame.
**Step 2** — Use the **Fishbone Diagram (Ishikawa)** to map out the **breadth** of all possible contributing factors across 6 categories.
**Step 3** — Select the most critical factor from the Fishbone diagram.
**Step 4** — Use the **5 Whys** method to drill down into the **depth** of that factor until you hit a systemic issue.
**Step 5** — Develop a corrective action plan that addresses the systemic issue, not just the symptom.

> ⚠️ **Research warning:** Do not jump straight to the "5 Whys" if the problem is highly complex. The 5 Whys is a linear tool; complex problems often have multiple interacting causes. Use the Fishbone Diagram first to see the whole picture, then apply the 5 Whys to the most likely branches.
> *(Source: Lean Six Sigma Institute — Problem Solving Methodologies, 2026)*

> 🔁 **Review cycle:** Ask "Why?" at least five times, but be prepared to ask it 7 or 8 times. Stop asking "Why?" only when your answer points to a broken system, policy, or process—not when it points to "human error". Review the effectiveness of the corrective action 30, 60, and 90 days after implementation.

---

## THE ORIGIN & WHY IT MATTERS

This template combines two of the most powerful problem-solving tools in industrial history:
1. **The Fishbone Diagram (Ishikawa Diagram):** Created by Kaoru Ishikawa in the 1960s for Kawasaki Shipyards, it is designed to visualize all potential causes of a problem to identify root causes.
2. **The 5 Whys:** Developed by Taiichi Ohno, the architect of the Toyota Production System (TPS), as a simple but relentless method of questioning to trace a problem back to its systemic root.

**Why this still matters in 2025–2026:**
In modern digital and service environments, failures are rarely caused by a single mechanical breakdown. They are the result of complex interactions between software, processes, and human behavior. These tools prevent teams from applying "band-aid" solutions to systemic problems.
*(Source: ASQ — Root Cause Analysis Guide, 2025; Toyota Way Principles)*

---

## Phase 1: Problem Definition (The Head of the Fish)

*What exactly is the problem? Define it neutrally and factually. Do not blame individuals or assume a cause in the definition.*

> [Insert precise problem statement. E.g., "Software deployment failed on Friday at 5 PM causing 2 hours of downtime for 10,000 users."]

**Diagnostic Question:** *Is the problem statement factual? Does it state WHAT happened, WHERE it happened, WHEN it happened, and the IMPACT, without guessing WHY it happened?*

---

## Phase 2: The Fishbone Diagram (Mapping Breadth)

*Categorize all potential contributing factors using the industry-standard "6Ms" (for manufacturing/operations) or "8Ps" (for services).*

### Category 1: Method / Process
*Were the procedures, workflows, or standard operating instructions flawed, missing, or not followed?*
> - [Potential factor 1]
> - [Potential factor 2]

### Category 2: Machine / Equipment
*Did hardware, tooling, software systems, servers, or networks fail or behave unexpectedly?*
> - [Potential factor 1]
> - [Potential factor 2]

### Category 3: Manpower / People
*Were there issues with training, staffing levels, fatigue, or miscommunication? (Do not use this to blame people; focus on the system that allowed human error).*
> - [Potential factor 1]
> - [Potential factor 2]

### Category 4: Material / Inputs
*Were the raw materials, data inputs, components, or information provided defective or incorrect?*
> - [Potential factor 1]

### Category 5: Measurement / Metrics
*Were the KPIs, inspection results, monitoring tools, or data tracking mechanisms inaccurate or misleading?*
> - [Potential factor 1]

### Category 6: Mother Nature / Environment
*Did physical environments (heat, humidity, noise) or cultural environments (toxic culture, extreme pressure) contribute?*
> - [Potential factor 1]

---

## Phase 3: The 5 Whys (Drilling for Depth)

*Select the most critical/likely factor from your Fishbone diagram above and drill down. Remember: human error is a symptom, not a root cause.*

**Focus Factor Chosen:** [Insert factor, e.g., "Server crashed due to memory overload"]

- **Why? (1st level):** [e.g., The new code required more memory than allocated.]
- **Why? (2nd level):** [e.g., Load testing was bypassed before deployment.]
- **Why? (3rd level):** [e.g., The team was rushing to meet a Friday deadline.]
- **Why? (4th level):** [e.g., Sprint planning consistently underestimates QA and testing time.]
- **Why? (5th level - ROOT CAUSE):** [e.g., There is no policy requiring load testing sign-off before code merging, and management sets hard deadlines before technical scoping is complete.]

---

## Phase 4: Corrective Action Plan

*Based on the ROOT CAUSE (not the symptoms), what systemic change will you make?*

| Root Cause Identified | Systemic Corrective Action | Owner | Deadline | Success Metric |
|---|---|---|---|---|
| [e.g., No QA sign-off policy] | [e.g., Implement automated rule in CI/CD pipeline blocking merges without QA approval] | | | |
| [e.g., Deadlines set before scoping] | [e.g., Revise sprint planning process so deadlines are committed only after technical sizing] | | | |
| | | | | |

---

## Diagnostic Questions to Test Your Analysis

| Test | Question to Ask | Pass? |
|---|---|---|
| **The Reversal Test** | Read your 5 Whys backwards. Does "5th level" directly cause "4th level", which causes "3rd level"? Does the logical chain hold? | ☐ Yes ☐ No |
| **The "Human Error" Test** | Did your analysis stop at "John made a mistake"? If yes, you failed. Why did the system allow John's mistake to cause a failure? | ☐ Yes ☐ No |
| **The Prevention Test** | If you implement your Corrective Action, is it mathematically or systematically impossible for this exact problem to happen again? | ☐ Yes ☐ No |

---

## Real-World Application Examples

| Company / Context | How Root Cause Analysis Was Applied |
|---|---|
| **Toyota Manufacturing** | The classic example: A machine stopped (Why?) → Overload blew the fuse (Why?) → Bearing lacked lubrication (Why?) → Oil pump wasn't pumping enough (Why?) → Pump shaft was worn (Why?) → Metal scrap got into the pump (Root Cause: No strainer on the intake). Without 5 Whys, they just replace the fuse. *(Source: Toyota Way)* |
| **Software Outage (SaaS)** | An AWS outage was traced not to a server failure, but through 5 Whys to a flawed capacity planning algorithm that failed to account for sudden traffic spikes during a specific time of day. *(Source: Tech Industry Best Practices, 2025)* |
| **Healthcare Safety** | A patient received the wrong medication. Fishbone mapped factors (lighting, staffing, labeling). 5 Whys on labeling revealed that two medications had nearly identical packaging from the supplier (Root Cause), leading to a hospital-wide policy change for visual distinctiveness. *(Source: ASQ Healthcare)* |

---

## When to Use This Framework

| Situation | How This Template Helps |
|---|---|
| **Post-Mortem Meetings** | De-escalates emotion by focusing on systemic failures rather than personal blame. Shifts the culture from "who did it?" to "what allowed this to happen?" |
| **Quality Control Escapes** | Ensures you don't waste money fixing surface-level issues while the real leak remains in your manufacturing or service process. |
| **Process Improvement** | Identifies the exact point in a complex workflow that needs redesign. |

*(Source: Lean Six Sigma Institute, 2026)*

---

## Framework Limitations — Know What It Cannot Do

| Limitation | What to Use Instead |
|---|---|
| **Requires honesty and psychological safety** | If participants hide facts to protect themselves, RCA fails. Use **Anonymous Surveys** or independent audits first if trust is low. |
| **Not for future strategy** | RCA looks backward at what went wrong. For predicting future risks, use a **Risk Matrix** or **FMEA (Failure Mode and Effects Analysis)**. |
| **Linearity of 5 Whys** | Real life often has branching causes. If 5 Whys feels too simple, rely more heavily on the Fishbone or use a **Fault Tree Analysis**. |

---

## Sources & References

| Source | Application in This Template |
|---|---|
| **Kaoru Ishikawa (Quality Control)** | The categorical "Fishbone" structure for mapping breadth and the 6Ms framework. |
| **Toyota Production System (Taiichi Ohno)** | The "5 Whys" methodology for depth and systemic thinking. |
| **ASQ (American Society for Quality, 2025)** | "Human Error" test, problem definition standards, and healthcare examples. |
| **Lean Six Sigma Guidelines (2026)** | The integration of both tools into a single workflow and corrective action planning. |
| **Management Consulting Best Practices** | The Reversal Test and application in modern digital environments. |

---

*Template version: 1.0 — Fully Research-Rebuilt | June 2026*
*Framework origin: Toyota Motor Corporation & Kaoru Ishikawa*
*Owner: [Name / Team] | Review date: [Date]*
