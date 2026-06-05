# SCHEMA.md — File Schemas & Naming Rules

> **Single source of truth for file structure in the 360° Business Discovery & Marketing Intelligence System.**
> This file defines what every key file should look like so that:
> - Any AI can parse the workspace reliably.
> - The `validate_repo.py` script can verify consistency.
> - Contributors can add new files without breaking the system.

---

## 1. Root Files (Top-Level)

| File | Purpose | Required? |
| --- | --- | --- |
| `README.md` | Project entry point and overview | Yes |
| `starter_prompt.md` | 37-question discovery conversation | Yes |
| `PROJECT_BRIEF_template.md` | Output template for project briefs | Yes |
| `AGENTS.md` | Agent behavior spec (this is canonical) | Yes |
| `CHANGELOG.md` | Version history | Yes |
| `.gitignore` | VCS ignore rules | Yes |
| `LICENSE` | License file | Yes |
| `CONTRIBUTING.md` | Contribution guide | Optional but recommended |

---

## 2. YAML Frontmatter — `PROJECT_BRIEF.md`

Every generated `PROJECT_BRIEF.md` MUST include this YAML block at the top, between two `---` lines.

### Required Keys

| Key | Type | Example |
| --- | --- | --- |
| `project_name` | string | `"Acme Analytics"` |
| `industry` | string | `"B2B SaaS / Marketing Analytics"` |
| `stage` | enum | `Pre-idea \| Idea \| MVP \| Early Revenue \| Growing \| Scaling` |
| `team_size` | integer | `3` |
| `financial_status` | enum | `Self-funded \| Investor-backed \| Revenue-generating \| Pre-revenue` |
| `discovery_date` | date | `"2026-06-05"` |
| `confidence_level` | integer 0–100 | `87` |
| `generated_by` | string | `"360° Business Discovery System v2.1"` |
| `priority_frameworks` | list of strings | `["SWOT/TOWS", "Porter's Five Forces"]` |
| `priority_skills` | list of strings | `["seo-audit", "copywriting"]` |
| `available_frameworks_path` | string | `"Frameworks/"` |
| `available_skills_path` | string | `"Skills/"` |
| `how_to_use` | list of strings | `["Step 1 ...", "Step 2 ..."]` |

### Optional Keys

| Key | Type | Notes |
| --- | --- | --- |
| `customer_segment` | string | Brief ICP description |
| `main_challenge` | string | Top obstacle from discovery |
| `review_date` | date | When to revisit this brief |

### Validation

Run `python scripts/validate_repo.py` to confirm template YAML matches the schema.

---

## 3. `SKILL.md` Schema

Every skill folder under `Skills/<skill_name>/` MUST contain a `SKILL.md` with this structure:

```markdown
# <Skill Name>

## When to Use
[1–3 sentences: trigger conditions]

## Before Starting
- [ ] Required context item 1
- [ ] Required context item 2
...

## Framework / Methodology
[Step-by-step process to follow]

## Output Format
[What deliverable the AI should produce]

## Related Skills
- `related-skill-1/` — Why related
- `related-skill-2/` — Why related

## Common Mistakes
- Mistake 1
- Mistake 2
```

### Naming

- Folder name: `kebab-case` (e.g., `cold-email`, `ai-seo`)
- File name: `SKILL.md` (uppercase, exact)
- No spaces; lowercase preferred.

---

## 4. `<framework>_template.md` Schema

Every framework file under `Frameworks/<category>/` MUST end with `_template.md` and contain:

```markdown
# <Framework Name>

## Source
[Original author, year, publication — e.g., "Porter, 1979, HBR"]

## When to Use
[1–3 sentences]

## Step-by-Step Application
1. Step 1
2. Step 2
...

## Worked Example
[Optional: 1 real-world example]

## Limitations & Alternatives
- Limitation 1
- Alternative framework 1
```

### Naming

- Folder: `Frameworks/<Category_Name>/` (Title_Case_With_Underscores)
- File: `<framework_name>_template.md` (lowercase, underscores)
- Categories: `Business_Models`, `External_Analysis`, `Finance_and_Risk`,
  `Growth_and_Innovation`, `Internal_Analysis`, `Marketing_and_Customers`,
  `Operations_and_Projects`, `Performance_and_Measurement`,
  `Strategy_and_Direction`, `Thinking_and_Problem_Solving`,
  `Time_and_Priority_Management`.

---

## 5. Discovery Areas (8 Total)

Discovery has exactly 8 areas totaling 37 questions:

| # | Area | Q-Count | Weight |
| --- | --- | --- | --- |
| 1 | Big Picture | 4 | 12% |
| 2 | Customer & Problem | 5 | 15% |
| 3 | Value Proposition | 4 | 12% |
| 4 | Market & Competition | 5 | 12.5% |
| 5 | Business Model | 5 | 12.5% |
| 6 | Marketing & Sales | 5 | 10% |
| 7 | Team & Operations | 5 | 10% |
| 8 | Challenges & Goals | 4 | 16% |
| | **Total** | **37** | **100%** |

Any new question added must:
- Be assigned to one of the 8 areas.
- Not push the total above 37 without explicit version bump.
- Maintain the weight percentages.

---

## 6. AI Verification Checklist (14 Items)

The canonical checklist (used in `PROJECT_BRIEF.md` and `starter_prompt.md`):

1. Can describe the project in one sentence
2. Knows the target customer
3. Understands the problem solved
4. Knows the main competitors
5. Understands the revenue model
6. Knows the current financial status
7. Knows team size and composition
8. Knows the #1 challenge
9. Knows what success looks like in 12 months
10. Knows which frameworks are selected
11. Knows which marketing skills are selected
12. Knows which work templates are relevant
13. State Snapshot is up to date
14. `stop-slop` skill is being applied to all prose

---

## 7. Versioning

This project follows **Semantic Versioning** (SemVer):

- `MAJOR.MINOR.PATCH`
- Current: `2.1.0`
- Bump `MAJOR` for breaking schema changes
- Bump `MINOR` for new skills, frameworks, or features
- Bump `PATCH` for documentation / typo fixes

Update `CHANGELOG.md` on every version bump.

---

## 8. Reference Counts (v2.1)

| Item | Count |
| --- | --- |
| Discovery questions | 37 |
| Discovery areas | 8 |
| Marketing skills | 44 |
| Context-engineering skills | 13 |
| Total skills | 57 |
| Framework templates | 48 |
| Framework categories | 11 |
| AI Verification Checklist items | 14 |

Any change to these counts must be reflected in this file, `README.md`, and `CHANGELOG.md` simultaneously.

---

*Maintained by the project. Last updated: 2026-06 — v2.1*
