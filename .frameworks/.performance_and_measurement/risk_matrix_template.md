# Risk Matrix Template (5x5 Heat Map)

### Rebuilt from Primary Research | Sources: Project Management Institute · Vanta · TrackerNetworks

---

## Before You Start — Critical Instructions

> **The single most important rule of the Risk Matrix:**
> _"Do not rely on 'gut feelings' to score risks. You must define exactly what a '5' in Likelihood means (e.g., 'Happens once a month') and what a '5' in Impact means (e.g., 'Costs more than $1M'). If you don't define the scales, your team will score the same risk entirely differently."_
> _(Source: TrackerNetworks — Risk Assessment Biases, 2025; Smartsheet — Risk Matrices)_

**How to use this template:**

**Step 1** — Define your **Scales** (What does a 1 vs a 5 mean for your specific project?).
**Step 2** — Brainstorm potential risks and list them in the **Risk Register**.
**Step 3** — Score each risk for **Likelihood** and **Impact** (1 to 5). Multiply them to get the **Inherent Risk Score**.
**Step 4** — Define a **Mitigation Strategy** (Avoid, Reduce, Share, or Accept).
**Step 5** — Calculate the **Residual Risk Score** (the risk level _after_ your mitigation).

> ⚠️ **Research warning:** The biggest mistake in risk management is stopping at the "Inherent Risk." Identifying a risk is useless unless you define the _Mitigating Controls_ and calculate the _Residual Risk_ to see if the danger has actually been lowered to an acceptable level.
> _(Source: Optro.ai / Vanta — Modern Risk Management, 2025)_

---

## STAGE 1: DEFINE YOUR SCALES

_Customize these definitions so everyone scores risks using the same logic._

### Likelihood (Probability) Scale

- **1 - Rare:** Highly unlikely to occur _(e.g., <5% chance; happens once a decade)_
- **2 - Unlikely:** Not expected, but possible _(e.g., 5-20% chance; happens once a year)_
- **3 - Possible:** Might occur at some point _(e.g., 21-50% chance; happens once a quarter)_
- **4 - Likely:** Will probably occur _(e.g., 51-80% chance; happens once a month)_
- **5 - Almost Certain:** Expected to occur _(e.g., >80% chance; happens weekly)_

### Impact (Severity) Scale

- **1 - Negligible:** Minor issue, easily handled _(e.g., <$1k loss, no schedule delay)_
- **2 - Minor:** Noticeable, but won't derail the project _(e.g., <$10k loss, 1-week delay)_
- **3 - Moderate:** Significant issue requiring management _(e.g., <$50k loss, 1-month delay)_
- **4 - Major:** Severe damage to project goals _(e.g., <$250k loss, massive delay, bad PR)_
- **5 - Catastrophic:** Project failure, legal action, or bankruptcy _(e.g., >$250k loss)_

---

## STAGE 2: THE 5x5 HEAT MAP (Visual Guide)

_Formula: Likelihood (1-5) × Impact (1-5) = Risk Score (1-25)_

| Likelihood ⬇ \ Impact ➡ | 1 (Negligible) | 2 (Minor) | 3 (Moderate) | 4 (Major) | 5 (Catastrophic) |
| ----------------------- | :------------: | :-------: | :----------: | :-------: | :--------------: |
| **5 (Almost Certain)**  |      🟢 5      |   🟡 10   |    🔴 15     |   🔴 20   |      🔴 25       |
| **4 (Likely)**          |      🟢 4      |   🟡 8    |    🟡 12     |   🔴 16   |      🔴 20       |
| **3 (Possible)**        |      🟢 3      |   🟡 6    |     🟡 9     |   🟡 12   |      🔴 15       |
| **2 (Unlikely)**        |      🟢 2      |   🟢 4    |     🟡 6     |   🟡 8    |      🟡 10       |
| **1 (Rare)**            |      🟢 1      |   🟢 2    |     🟢 3     |   🟢 4    |       🟢 5       |

**Action Zones:**

- 🔴 **Red (15-25): Unacceptable / Extreme.** Immediate mitigation required. Project cannot proceed without controls.
- 🟡 **Yellow (6-12): Moderate / Tolerable.** Requires management attention and active monitoring.
- 🟢 **Green (1-5): Low / Acceptable.** Accept the risk and manage via routine procedures.

---

## STAGE 3: THE RISK REGISTER & MITIGATION PLAN

_List your risks here. Do not leave the "Owner" column blank._

| Risk ID | Risk Description                  | Inherent Score (L x I) | Mitigation Strategy | Mitigating Controls (What are we doing about it?)            | Residual Score (After Controls) | Owner      |
| ------- | --------------------------------- | ---------------------- | ------------------- | ------------------------------------------------------------ | ------------------------------- | ---------- |
| _R-01_  | _Key developer quits mid-project_ | _3 x 4 = 12 🟡_        | _Reduce_            | _Implement cross-training; require daily code documentation_ | _2 x 4 = 8 🟡_                  | _Lead Dev_ |
| _R-02_  | _Cloud server provider goes down_ | _2 x 5 = 10 🟡_        | _Share / Reduce_    | _Set up automated failover to AWS; buy cyber insurance_      | _1 x 3 = 3 🟢_                  | _IT Dir._  |
| _R-03_  |                                   |                        | `[Select]`          |                                                              |                                 |            |
| _R-04_  |                                   |                        | `[Select]`          |                                                              |                                 |            |
| _R-05_  |                                   |                        | `[Select]`          |                                                              |                                 |            |

_(Mitigation Strategy Options: **Avoid** [Change the plan to remove the risk], **Reduce** [Implement controls to lower L or I], **Share** [Transfer risk via insurance/outsourcing], **Accept** [Do nothing, risk is within tolerance])._

---

## SYNTHESIS & REVIEW

_After completing the register, review the Residual Scores._

**Diagnostic Questions:**

1. Are there any risks that _still_ score in the 🔴 **Red Zone** even after mitigating controls are applied?
   - _(If yes, the project is outside your risk appetite. You must either redesign the project or accept a high probability of failure)._
2. Do all 🔴 Red and 🟡 Yellow risks have a specific human **Owner** assigned to monitor them?
3. Are these risks reviewed continuously, or is this document going to sit in a folder until the project ends?

---

## When to Use This Framework

| Situation                 | How This Template Helps                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Project Kickoffs          | Forces the team to confront "what could go wrong" before money is spent                                                          |
| Cybersecurity / IT Audits | Required by compliance frameworks (like SOC 2, ISO 27001, NIST) to prove you understand and manage your systemic vulnerabilities |
| Vendor Selection          | Helps objectively compare the risks of using Vendor A (cheap but unreliable) vs Vendor B (expensive but stable)                  |

_(Source: Safe.Security — Cyber Risk, 2025; Vanta — Compliance Risk, 2025)_

---

## Framework Limitations — Know What It Cannot Do

| Limitation               | What to Use Instead                                                                                                                                                |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| The "Black Swan" Problem | Matrices are terrible at predicting unprecedented, catastrophic events (e.g., a global pandemic). Use **Scenario Planning / Wargaming** for existential threats.   |
| Subjective Bias          | Humans naturally underestimate Likelihood and overestimate their own ability to mitigate Impact. Use historical data whenever possible to score risks objectively. |

---

## Sources & References

| Source                                            | Application in This Template                                                  |
| ------------------------------------------------- | ----------------------------------------------------------------------------- |
| Project Management Institute (PMI)                | Standard 5x5 Matrix structure; Likelihood vs Impact                           |
| TrackerNetworks — _Risk Assessment Biases_, 2025  | The necessity of defining scales (Stage 1) to prevent subjective scoring bias |
| Optro.ai / Vanta — _Modern Risk Management_, 2025 | The critical difference between Inherent Risk and Residual Risk               |
| Safe.Security — _Cyber Risk_, 2025                | Identifying the 4 Mitigation Strategies (Avoid, Reduce, Share, Accept)        |

---

_Template version: 1.0 — Fully Research-Rebuilt | June 2026_
_Framework origin: Traditional Project Management / Risk Management_
_Owner: [Name / Team] | Review date: [Date]_
