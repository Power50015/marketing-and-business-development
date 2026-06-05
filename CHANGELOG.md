# Changelog

All notable changes to the **360° Business Discovery & Marketing Intelligence System** are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the project adheres to [Semantic Versioning](https://semver.org/).

---

## [2.1.0] — 2026-06-05

### Fixed
- Duplicate `### AREA 8` header in `starter_prompt.md` (line 731). Renamed to `## 🗺️ STRATEGIC MAP — FRAMEWORKS & SKILLS SELECTED` to remove ambiguity with `### AREA 8 — Challenges, Risks & The Real Question` (line 293).
- Invalid `Areas 1, 9` reference in the Framework Output Mapping table. Replaced with `Areas 1, 5` (no Area 9 exists; the system has 8 areas only).
- Inconsistent AI Verification Checklist count (11 vs 13) across `starter_prompt.md` and `PROJECT_BRIEF_template.md`. Unified to **14 items** in both files.
- Stale self-check reference: `"all 11 items"` → `"all 14 items"` in `starter_prompt.md` line 1027.
- Version mismatches across files: all three core files now declare **v2.1**.

### Changed
- Corrected skill counts in `README.md`: 55+ → **44 marketing skills**; 15 → **13 context-engineering skills**; 70+ → **57 total skills**.
- Corrected framework count: 50+ → **48 strategic frameworks**; 7 categories → **11 categories**.
- `PROJECT_BRIEF_template.md` YAML frontmatter now includes `priority_skills: []`, `available_skills_path:`, and an expanded `how_to_use:` block (6 items, matching `starter_prompt.md`).
- Added `## 🛠️ MARKETING SKILLS SELECTED` section to `PROJECT_BRIEF_template.md` (previously only present in `starter_prompt.md`).
- AI Verification Checklist is now a canonical 14-item list in both `starter_prompt.md` and `PROJECT_BRIEF_template.md`, including the new items:
  - "I have refreshed my State Snapshot with the latest answers"
  - "I am applying the 'stop-slop' skill to ensure my generated prose is natural and free of AI patterns"

### Removed
- `repo-temp/` directory (250+ stale files: Python experiments, JSONL traces, PNG screenshots, macOS plist LaunchAgents). Content is no longer needed and was unrelated to the core system.
- `AGENT.md` and `CLAUDE.md` (existed only inside `repo-temp/`; content already captured in the new `AGENTS.md`).
- `AARRR Framework` reference from the "Built on" list in `README.md` (no corresponding template exists in `Frameworks/`).

### Added
- `AGENTS.md` — single, canonical agent behavior spec (model-agnostic).
- `.gitignore` — comprehensive ignore rules (OS files, Python/Node artifacts, logs, JSONL traces, screenshots, etc.).
- `scripts/validate_repo.py` — automated consistency checker. Verifies question count, version unification, checklist count, YAML keys, filesystem counts, and the absence of legacy claims. Run with `python scripts/validate_repo.py`.
- `docs/SCHEMA.md` — official schema for `PROJECT_BRIEF.md` YAML, `SKILL.md`, `<framework>_template.md`, and discovery area definitions.
- `CHANGELOG.md` — this file.
- New reference counts section in `docs/SCHEMA.md` (Section 8) so the canonical numbers live in one place.

### Migration Notes
If you have existing `PROJECT_BRIEF.md` files generated before v2.1, add the new YAML keys:
```yaml
priority_skills: []
available_skills_path: "Skills/"
```
And add a `## 🛠️ MARKETING SKILLS SELECTED` section after `## STRATEGIC FRAMEWORKS SELECTED`. Your existing content does not need to change.

---

## [2.0.0] — 2026-06 (pre-cleanup)

### Added
- Initial release of the v2 architecture.
- 37-question discovery across 8 areas.
- 48 strategic framework templates across 11 categories.
- 44 marketing skill modules + 13 context-engineering skills.
- `starter_prompt.md` and `PROJECT_BRIEF_template.md`.
- README and supporting documentation.

### Known Issues (resolved in 2.1.0)
- See `2.1.0` `Fixed` and `Changed` sections.

---

*Format: Keep a Changelog 1.1.0*
*Versioning: Semantic Versioning 2.0*
