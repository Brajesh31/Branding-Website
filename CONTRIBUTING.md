# 🤝 Contributing to Fabulo

Thank you for considering a contribution. This guide explains how to propose changes, prepare a development environment, validate work, document decisions, and submit reviewable pull requests.

Our goal is to keep the project approachable without sacrificing quality. A contribution should improve the real repository, not merely add volume or claims.

## 📌 1. Project context

Fabulo is currently a static fashion-brand landing page built with HTML and Tailwind CSS. It contains editorial sections, local imagery, a Tailwind CLI build, and supporting configuration.

It is not currently an e-commerce application. Do not introduce assumptions about product inventory, checkout, payment processing, user accounts, customer data, or APIs unless the proposal explicitly includes the design and implementation of those systems.

## 🎯 2. What contributions are useful?

- 🐛 Fixing broken layouts, asset paths, or browser rendering defects.
- 📱 Improving responsive behavior on small and large screens.
- ♿ Improving semantic HTML, keyboard navigation, image alternatives, and contrast.
- 🎨 Refining spacing, typography, color consistency, and editorial presentation.
- ⚡ Optimizing images and reducing unnecessary runtime dependencies.
- 🧪 Adding repeatable validation or browser tests.
- 📚 Improving accurate documentation and diagrams.
- 🔐 Improving dependency hygiene and workflow permissions.
- 🧹 Removing dead code or redundant configuration with a clear reason.

A large number of files is not automatically a better contribution. Each new file should have a purpose, a maintenance path, and a useful relationship to the actual implementation.

## 🚫 3. Changes that need prior discussion

Open an issue before making disruptive changes such as replacing the static architecture with a framework, adding a backend/database/CMS, introducing authentication or payments, changing the build output or deployment model, adding major dependencies, or removing existing assets and automation.

Explain the problem, alternatives, migration impact, security/privacy consequences, and maintenance cost.

## 🧰 4. Development environment

Prerequisites: Git, Node.js and npm compatible with the project dependencies, Python 3 for optional local serving and validation, and a modern browser.

Clone and install:

~~~bash
git clone https://github.com/Brajesh31/Branding-Website.git
cd Branding-Website
npm ci
~~~

Build and serve:

~~~bash
npm run build
python -m http.server 8000
~~~

Visit http://localhost:8000. For automatic stylesheet rebuilding, run npm run watch.

Check package.json before relying on a script. Do not invent commands that are not defined.

## 🌿 5. Branching strategy

Create a focused branch from the default branch:

~~~bash
git checkout main
git pull --ff-only
git checkout -b type/short-description
~~~

| Prefix | Use |
|---|---|
| feat/ | New user-visible capability |
| fix/ | Defect correction |
| docs/ | Documentation-only changes |
| style/ | Visual or formatting changes |
| refactor/ | Internal restructuring |
| test/ | Test and validation changes |
| chore/ | Tooling and maintenance |
| security/ | Security improvements |

Keep a branch focused on one coherent outcome.

## 🧑‍💻 6. Coding standards

### HTML and semantics
- Use semantic landmarks where appropriate.
- Maintain a logical heading order.
- Use anchors for navigation and buttons for actions.
- Give controls accessible names.
- Use meaningful alt text for informative images and empty alt text for decorative images.
- Avoid duplicate IDs and invalid nesting.
- Preserve readable indentation.

### Tailwind CSS
- Use existing configuration and conventions.
- Keep utility classes readable and logically grouped.
- Avoid arbitrary values when shared tokens or existing utilities are appropriate.
- Confirm content globs include any new markup location.
- Rebuild the stylesheet after utility changes.

### Visual design
- Preserve the editorial fashion direction unless a change intentionally revises it.
- Use consistent spacing, typography, and image treatment.
- Avoid excessive animation.
- Respect reduced-motion preferences when adding motion.
- Test touch-sized interactions on mobile.

### Assets
- Preserve exact filename case.
- Prefer descriptive filenames.
- Optimize image dimensions and compression for rendered use.
- Record source, author, license, and attribution where required.
- Do not add unlicensed or misleading imagery.
- Do not create fake screenshots or claim a feature exists based on a mockup.

### Dependencies
- Avoid adding a dependency for a task that can be solved with existing tools.
- Explain why a new package is needed.
- Update package-lock.json with package manifest changes.
- Review package maintenance, license, security history, and runtime impact.
- Never commit node_modules.

## 🧪 7. Required validation

Run relevant checks before opening a pull request:

~~~bash
npm ci
npm run build
python3 scripts/validate-repository.py
~~~

Then serve and inspect the page:

~~~bash
python -m http.server 8000
~~~

Review:
- [ ] Build exits successfully.
- [ ] Generated stylesheet exists.
- [ ] No broken local image or CSS requests.
- [ ] No unexpected browser console errors.
- [ ] No horizontal overflow at narrow widths.
- [ ] Layout is coherent at tablet and desktop widths.
- [ ] Keyboard navigation and focus are visible.
- [ ] Informative images have useful alternatives.
- [ ] Interactive controls work and have clear names.
- [ ] No secrets or private data are included.
- [ ] Documentation and diagrams match implementation.

Do not state that a test passed unless you ran it. If a check cannot be performed, state that clearly in the pull request.

## 📝 8. Commit message guidance

Use concise, descriptive messages. Conventional Commit-style prefixes are encouraged:

~~~text
feat: add responsive collection navigation
fix: correct hero image overflow on mobile
docs: expand deployment and accessibility guides
test: add repository structure validation
chore: update Tailwind build tooling
~~~

Avoid vague messages such as update, changes, or final work.

## 🔍 9. Pull request process

1. Confirm the branch is based on the latest default branch.
2. Keep the diff focused and remove temporary files.
3. Run build and relevant validation.
4. Update documentation, project structure, and diagrams where needed.
5. Add before/after screenshots for visual changes, captured from the real page.
6. Complete the pull request template.
7. Explain trade-offs and known limitations.
8. Respond to review comments with follow-up commits.
9. Merge only after required checks and approvals are complete.

A useful pull request description includes problem and motivation, implementation summary, architecture decisions, real screenshots, checks actually executed, limitations, and related issues.

## 🔐 10. Security and privacy

Never commit API keys, passwords, access tokens, private certificates, personal records, or production secrets. Do not paste secrets into issues or pull requests.

If a change introduces a form, tracking, browser storage, API, authentication, or other data processing, document the data collected, purpose, retention, access, third-party processors, and deletion path. Reassess the threat model before release.

Report suspected vulnerabilities privately as described in SECURITY.md.

## 📚 11. Documentation expectations

Documentation is part of the change when behavior or architecture changes. Update project overview, feature inventory, architecture and data-flow diagrams, setup and command references, accessibility and responsive guidance, testing and QA, security and privacy boundaries, deployment and maintenance instructions, and changelog/roadmap where appropriate.

Keep examples executable and links valid. Clearly label proposals, assumptions, and unverified statements.

## ⚖️ 12. Code of Conduct

All contributors must follow CODE_OF_CONDUCT.md. Be respectful, assume good faith, critique work rather than people, and make participation safe for everyone.

## 🙌 13. Recognition

Contributors should be credited through normal Git history and contribution records. Do not add names, affiliations, or endorsements without permission.

Thank you for helping make Fabulo clearer, more accessible, and easier to maintain.
