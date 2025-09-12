#!/usr/bin/env bash
set -euo pipefail

# Link & numbering check runner for the semantic docs
# Usage: bash scripts/xref_check.sh semantic

ROOT_DIR=${1:-semantic}

echo "[1/3] Checking markdown links (best-effort)..."
if command -v npx >/dev/null 2>&1 && command -v git >/dev/null 2>&1; then
  has_errors=0
  while IFS= read -r f; do
    # Only process files under ROOT_DIR
    case "$f" in
      ${ROOT_DIR}/*)
        echo "- checking: $f"
        npx --yes markdown-link-check "$f" --quiet || has_errors=1
        ;;
    esac
  done < <(git ls-files -- '*.md')
  if [ $has_errors -ne 0 ]; then
    echo "markdown-link-check reported issues (see output above)."
  else
    echo "markdown-link-check: no issues detected (best-effort)."
  fi
else
  echo "npx or git not found; skipping markdown-link-check"
fi

echo "[2/3] Checking numbering continuity..."
python3 "$(dirname "$0")/check_numbering.py" --input "${ROOT_DIR}" --output numbering_report.json || true

echo "[3/3] Checking cross-references..."
python3 "$(dirname "$0")/check_references.py" --input "${ROOT_DIR}" --output references_report.json || true

echo "Done. Reports: numbering_report.json, references_report.json"


