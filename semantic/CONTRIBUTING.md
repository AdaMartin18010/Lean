# Contributing Guide (semantic)

[Back](README.md) | [Strict Index](INDEX.md)

---

## How to Contribute

- Propose edits via PRs; keep edits atomic and well-described
- Follow `_TEMPLATE-WIKI-STYLE.md` for new pages
- Ensure Lean code blocks compile and include required imports
- Update cross-references and local navigation links

---

## Standards

- Wikipedia-style sections, bilingual titles (CN/EN when applicable)
- Lean 4 (2025) conventions: `syntax`, `macro_rules`, `termination_by`
- Consistent math notation: inline \( ... \) and block \[ ... \]

---

## Workflow

1. Create a branch and describe the scope
2. Add or edit files; run local checks:
   - `python scripts/check_numbering.py`
   - `python scripts/check_references.py`
   - `bash scripts/xref_check.sh`
3. Update `CONTINUOUS_PROGRESS.md` when adding new sections
4. Submit PR with summary, motivation, and impact

---

## Issue Types

- Bug, Content Improvement, Feature Request, Navigation/Link Issue
- Use `ISSUE_TEMPLATES.md` for structure

---

Last Update: 2025-09-15
