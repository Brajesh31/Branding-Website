#!/usr/bin/env python3
"""Validate key Fabulo repository files and relative Markdown links.

This is a lightweight consistency check. It does not render HTML, run browser
tests, validate WCAG conformance, or perform a security audit.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md",
    "SUPPORT.md", "CHANGELOG.md", "ROADMAP.md", "index.html",
    "package.json", "input.css", "tailwind.config.js",
    "docs/PROJECT_OVERVIEW.md", "docs/FEATURES.md", "docs/ARCHITECTURE.md",
    "docs/DEVELOPMENT.md", "docs/DEPLOYMENT.md", "docs/ACCESSIBILITY.md",
    "docs/TESTING.md", "docs/QA.md", "docs/PERFORMANCE.md",
    "docs/SECURITY_MODEL.md", "docs/FAQ.md",
    "docs/diagrams/system-flow.md", "docs/diagrams/build-flow.md",
    "docs/diagrams/contribution-flow.md", "docs/templates/README.md",
]
errors = []
warnings = []

for relative in REQUIRED:
    path = ROOT / relative
    if not path.is_file():
        errors.append(f"Missing required file: {relative}")
    elif path.stat().st_size == 0:
        errors.append(f"Empty required file: {relative}")

markdown_files = list(ROOT.rglob("*.md"))
link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
for md in markdown_files:
    try:
        content = md.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"Cannot decode UTF-8: {md.relative_to(ROOT)}")
        continue
    for target in link_pattern.findall(content):
        target = target.strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        resolved = (md.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"Link escapes repository: {md.relative_to(ROOT)} -> {target}")
            continue
        if not resolved.exists():
            errors.append(f"Broken local link: {md.relative_to(ROOT)} -> {target}")

if not (ROOT / "package-lock.json").is_file():
    warnings.append("package-lock.json is missing; npm ci may not be reproducible.")

for warning in warnings:
    print(f"WARNING: {warning}")

if errors:
    print("Repository validation failed:")
    for error in errors:
        print(f" - {error}")
    sys.exit(1)

print(f"Repository validation passed: {len(REQUIRED)} required files and {len(markdown_files)} Markdown files checked.")
