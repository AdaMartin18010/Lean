# Tools Directory

This directory contains automation tools for the Lean Formal Knowledge System.

## Available Tools

### 1. Skeleton Generator (`generate_skeleton.py`)

Automatically generates skeleton files and directory structures.

**Usage:**

```bash
cd analysis/tools
python generate_skeleton.py
```

**Features:**

- Creates directory structure based on configuration
- Generates skeleton files from templates
- Creates bilingual mirror files
- Supports variable substitution

### 2. Link Validator (`validate_links.py`)

Validates all cross-references and links in markdown files.

**Usage:**

```bash
cd analysis/tools
python validate_links.py
```

**Features:**

- Checks all markdown files recursively
- Validates relative and absolute links
- Handles anchor links
- Generates detailed validation report
- Exports results to `link_validation_report.md`

## Output Files

### Link Validation Report (`link_validation_report.md`)

Generated by the link validator, contains:

- Summary statistics
- List of broken links
- List of external links
- File-by-file breakdown

## Future Tools

### Planned Tools

1. **Content Analyzer**
   - Analyze content completeness
   - Check for missing sections
   - Validate LaTeX syntax

2. **Bilingual Sync Tool**
   - Keep Chinese and English versions in sync
   - Detect missing translations
   - Generate translation templates

3. **Reference Manager**
   - Extract and validate references
   - Generate bibliography
   - Check citation consistency

4. **Diagram Generator**
   - Generate Mermaid diagrams from code
   - Create architecture diagrams
   - Export to various formats

## Contributing

When adding new tools:

1. Follow the existing code style
2. Add proper documentation
3. Include error handling
4. Add usage examples
5. Update this README

## Requirements

- Python 3.7+
- pathlib (built-in)
- re (built-in)
- urllib (built-in)

## Installation

No additional installation required. All tools use Python standard library.

---

[Back to Project Root](../README.md)
