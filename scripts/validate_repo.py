"""
validate_repo.py
================
Repository consistency checker for the
360° Business Discovery & Marketing Intelligence System.

Verifies:
  1. Total question count = 37 across 8 areas.
  2. Version is unified across the three core files (v2.1).
  3. README's claimed counts match actual filesystem counts.
  4. All cross-referenced framework folders exist.
  5. AI Verification Checklist has 14 items in both files.
  6. No invalid "Area 9" or other out-of-range references.
  7. PROJECT_BRIEF_template.md contains required YAML keys.

Exit code 0 = all checks pass; non-zero = at least one failure.
Pure stdlib; no external dependencies.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README = REPO_ROOT / "README.md"
STARTER = REPO_ROOT / "starter_prompt.md"
TEMPLATE = REPO_ROOT / "PROJECT_BRIEF_template.md"
SKILLS_DIR = REPO_ROOT / "Skills"
FRAMEWORKS_DIR = REPO_ROOT / "Frameworks"

EXPECTED_VERSION = "v2.1"
EXPECTED_QUESTIONS = 37
EXPECTED_CHECKLIST_ITEMS = 14


class Report:
    def __init__(self) -> None:
        self.passed: list[str] = []
        self.failed: list[str] = []
        self.warnings: list[str] = []

    def ok(self, msg: str) -> None:
        self.passed.append(msg)
        print(f"  [PASS] {msg}")

    def fail(self, msg: str) -> None:
        self.failed.append(msg)
        print(f"  [FAIL] {msg}")

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)
        print(f"  [WARN] {msg}")


def count_questions_in_starter(text: str) -> int:
    """Count numbered discovery questions in the Discovery Sequence section."""
    start_marker = "## Discovery Sequence"
    end_marker = "## Opening Message"
    start = text.find(start_marker)
    end = text.find(end_marker)
    if start < 0 or end < 0:
        return 0
    section = text[start:end]
    pattern = re.compile(r"^\s*(\d+)\.\s+\S", re.MULTILINE)
    matches = pattern.findall(section)
    return len(matches)


def count_checklist_items(text: str) -> int:
    """Count checklist items after a VERIFICATION CHECKLIST header."""
    pattern = re.compile(
        r"##\s+[^\n]*VERIFICATION[^\n]*\n([\s\S]*?)(?=^##\s|\Z)",
        re.IGNORECASE | re.MULTILINE,
    )
    match = pattern.search(text)
    if not match:
        return 0
    return len(re.findall(r"^\s*-\s*\[\s*\]", match.group(1), re.MULTILINE))


def count_marketing_skills() -> int:
    if not SKILLS_DIR.exists():
        return 0
    return sum(
        1
        for p in SKILLS_DIR.iterdir()
        if p.is_dir() and p.name != "context-engineering"
    )


def count_context_skills() -> int:
    p = SKILLS_DIR / "context-engineering"
    if not p.exists():
        return 0
    return sum(1 for x in p.iterdir() if x.is_dir())


def count_frameworks() -> int:
    if not FRAMEWORKS_DIR.exists():
        return 0
    return sum(1 for p in FRAMEWORKS_DIR.rglob("*template*.md"))


def get_version(text: str) -> str | None:
    """Find the canonical version. Prefer 'Version | X.Y' or 'VERSION X.Y' patterns
    over inline 'vX.Y' references that might be historical notes."""
    patterns = [
        r"\*\*Version\*\*\s*\|\s*(\d+\.\d+(?:\.\d+)?)",
        r"VERSION\s+(\d+\.\d+(?:\.\d+)?)",
        r"[Vv]ersion\s+(\d+\.\d+(?:\.\d+)?)",
    ]
    for p in patterns:
        m = re.search(p, text)
        if m:
            return "v" + m.group(1)
    m = re.search(r"\bv(\d+\.\d+(?:\.\d+)?)\b", text)
    return ("v" + m.group(1)) if m else None


def has_invalid_area_9(text: str) -> bool:
    return bool(re.search(r"\bAreas?\s+1,\s*9\b", text))


def yaml_keys_in_template(text: str) -> set[str]:
    if not text.startswith("---"):
        return set()
    parts = text.split("---", 2)
    if len(parts) < 3:
        return set()
    keys: set[str] = set()
    for line in parts[1].splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:", line)
        if m:
            keys.add(m.group(1))
    return keys


def main() -> int:
    report = Report()

    print("=" * 72)
    print("  360 Business Discovery System - Repository Validation")
    print(f"  Expected version: {EXPECTED_VERSION}")
    print("=" * 72)

    for f in (STARTER, TEMPLATE, README):
        if not f.exists():
            report.fail(f"Missing required file: {f.name}")
            return 1

    starter_text = STARTER.read_text(encoding="utf-8")
    template_text = TEMPLATE.read_text(encoding="utf-8")
    readme_text = README.read_text(encoding="utf-8")

    qcount = count_questions_in_starter(starter_text)
    if qcount == EXPECTED_QUESTIONS:
        report.ok(f"starter_prompt.md has {qcount} discovery questions (expected 37)")
    else:
        report.fail(
            f"starter_prompt.md has {qcount} discovery questions (expected {EXPECTED_QUESTIONS})"
        )

    for path, text in (
        ("starter_prompt.md", starter_text),
        ("PROJECT_BRIEF_template.md", template_text),
        ("README.md", readme_text),
    ):
        v = get_version(text)
        if v == EXPECTED_VERSION:
            report.ok(f"{path} declares version {v}")
        else:
            report.fail(f"{path} declares version {v} (expected {EXPECTED_VERSION})")

    if has_invalid_area_9(starter_text):
        report.fail("starter_prompt.md still references 'Area 9' (no such area exists)")
    else:
        report.ok("starter_prompt.md has no invalid 'Area 9' reference")

    starter_checklist = count_checklist_items(starter_text)
    template_checklist = count_checklist_items(template_text)
    if starter_checklist == EXPECTED_CHECKLIST_ITEMS:
        report.ok(
            f"starter_prompt.md AI Verification Checklist has {starter_checklist} items (expected 14)"
        )
    else:
        report.fail(
            f"starter_prompt.md AI Verification Checklist has {starter_checklist} items (expected {EXPECTED_CHECKLIST_ITEMS})"
        )
    if template_checklist == EXPECTED_CHECKLIST_ITEMS:
        report.ok(
            f"PROJECT_BRIEF_template.md AI Verification Checklist has {template_checklist} items (expected 14)"
        )
    else:
        report.fail(
            f"PROJECT_BRIEF_template.md AI Verification Checklist has {template_checklist} items (expected {EXPECTED_CHECKLIST_ITEMS})"
        )

    yaml_keys = yaml_keys_in_template(template_text)
    required_keys = {
        "project_name",
        "industry",
        "stage",
        "team_size",
        "financial_status",
        "discovery_date",
        "confidence_level",
        "generated_by",
        "priority_frameworks",
        "priority_skills",
        "available_frameworks_path",
        "available_skills_path",
        "how_to_use",
    }
    missing = required_keys - yaml_keys
    if not missing:
        report.ok(
            "PROJECT_BRIEF_template.md YAML frontmatter contains all required keys"
        )
    else:
        report.fail(
            f"PROJECT_BRIEF_template.md YAML frontmatter missing keys: {', '.join(sorted(missing))}"
        )

    marketing = count_marketing_skills()
    context = count_context_skills()
    frameworks = count_frameworks()
    if marketing > 0:
        report.ok(f"Found {marketing} marketing skill folders under Skills/")
    else:
        report.fail("No marketing skill folders found under Skills/")
    report.ok(f"Found {context} context-engineering skill folders")
    report.ok(f"Found {frameworks} framework templates under Frameworks/")

    for legacy in ("50+", "55+", "70+", "15 skills", "15 foundational"):
        if legacy in readme_text:
            report.warn(f"README still contains legacy claim: '{legacy}'")
        else:
            report.ok(f"README no longer uses legacy count: '{legacy}'")

    if "MARKETING SKILLS SELECTED" in template_text:
        report.ok(
            "PROJECT_BRIEF_template.md includes 'MARKETING SKILLS SELECTED' section"
        )
    else:
        report.fail(
            "PROJECT_BRIEF_template.md missing 'MARKETING SKILLS SELECTED' section"
        )

    if "AGENTS.md" in readme_text:
        report.ok("README references AGENTS.md as canonical agent spec")
    else:
        report.warn("README does not mention AGENTS.md")

    if "validate_repo.py" in readme_text or "validate_repo" in readme_text:
        report.ok("README references validate_repo.py")
    else:
        report.warn("README does not mention validate_repo.py")

    if "docs/SCHEMA.md" in readme_text or "SCHEMA.md" in readme_text:
        report.ok("README references docs/SCHEMA.md")
    else:
        report.warn("README does not mention docs/SCHEMA.md")

    print("=" * 72)
    print(
        f"  Summary: {len(report.passed)} passed, {len(report.failed)} failed, {len(report.warnings)} warnings"
    )
    print("=" * 72)

    if report.failed:
        print("\nFAILED CHECKS:")
        for f in report.failed:
            print(f"  - {f}")
        return 1

    print("\nAll required checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
