# 🗂️ Repository Structure and File Responsibilities

This document explains the role of key files and directories. The live Git tree remains the authoritative inventory. Generated artifacts and IDE-specific files may appear locally and should not be copied into the repository without a clear reason.

## 🌳 High-level structure

~~~text
Branding-Website/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── feature_request.yml
│   │   └── config.yml
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── codeql.yml
│   │   └── update-readme.yml
│   ├── dependabot.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── Images/                       # Existing editorial images and SVG assets
├── css/                          # Generated Tailwind output, ignored by Git
├── docs/
│   ├── assets/                   # Documentation diagrams and approved screenshots
│   ├── diagrams/                 # Editable Mermaid diagrams
│   ├── templates/                # Reusable engineering templates
│   ├── SEO_AND_METADATA.md
│   ├── RELEASE_PROCESS.md
│   ├── OPERATIONS.md
│   └── ...                       # Product and engineering guides
├── scripts/
│   └── validate-repository.py
├── tests/
│   └── test_repository.py        # Dependency-free static checks
├── 404.html                      # Static-host not-found page
├── favicon.svg                   # Browser identity
├── index.html                    # Main landing page
├── robots.txt                    # Basic crawler policy
├── site.webmanifest              # Browser application metadata
├── input.css                     # Tailwind source
├── package.json                  # Build and test scripts
├── package-lock.json             # Locked npm dependencies
├── tailwind.config.js             # Tailwind configuration
├── CHANGELOG.md
├── CITATION.cff
├── CODEOWNERS
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── ROADMAP.md
├── SECURITY.md
└── SUPPORT.md
~~~

## 📁 Directory ownership

| Directory | Responsibility | Change expectations |
|---|---|---|
| .github/ | Repository collaboration and automation | Review permissions and triggers |
| Images/ | Site imagery and SVG assets | Preserve rights and path case |
| css/ | Generated stylesheet output | Build artifact, not hand-edited source |
| docs/ | Product and engineering documentation | Keep links and implementation claims accurate |
| docs/assets/ | Original diagrams and real screenshots | Record provenance and capture details |
| docs/diagrams/ | Editable Mermaid sources | Update with architecture changes |
| docs/templates/ | Reusable review and planning forms | Keep templates generic and actionable |
| scripts/ | Repository maintenance utilities | Document behavior and limitations |
| tests/ | Automated static repository checks | Keep tests deterministic and dependency-light |

## 📄 Root file responsibilities

| File | Responsibility |
|---|---|
| index.html | Static landing page |
| 404.html | Not-found experience for compatible static hosts |
| favicon.svg | Browser tab icon |
| site.webmanifest | Browser install and theme metadata |
| robots.txt | Crawler access policy |
| input.css | Tailwind directives and custom CSS input |
| tailwind.config.js | Tailwind content scanning and configuration |
| package.json | npm scripts and dependencies |
| package-lock.json | Locked dependency resolution |
| README.md | Public project entry point |
| CONTRIBUTING.md | Contributor workflow and standards |
| CODE_OF_CONDUCT.md | Community expectations and enforcement |
| SECURITY.md | Private vulnerability reporting |
| SUPPORT.md | Help and issue routing |
| CHANGELOG.md | Factual change history |
| ROADMAP.md | Proposed and prioritized work |
| LICENSE | Project code license |
| CITATION.cff | Citation metadata |
| CODEOWNERS | Default review ownership |

## 🔁 Build artifact lifecycle

The npm build command writes css/style.css. The source of truth is input.css plus the Tailwind configuration and scanned markup. Do not hand-edit the generated stylesheet as the durable source of a change. The generated CSS is intentionally ignored by Git and recreated in CI and deployment builds.

## 🧹 Repository hygiene

Do not commit node_modules, local environment files, credentials, browser caches, temporary exports, or unrelated IDE workspace state. Preserve existing assets unless their removal is intentional, reviewed, and all references are updated.
