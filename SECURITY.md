# 🔐 Security Policy

## 📌 Project security scope

Fabulo is currently a static HTML and Tailwind CSS frontend with npm-based build tooling. The repository does not currently implement an application backend, database, authentication, customer account system, payment processing, or project-owned API.

This reduces the current application attack surface, but does not remove risks associated with dependencies, third-party scripts, repository permissions, build automation, hosting configuration, or asset provenance.

## ✅ Supported versions

Security fixes are generally considered for the latest state of the default branch. There is no separate long-term support or release branch policy at this time.

| Version | Security support |
|---|---|
| Latest default branch | Best-effort review and fixes |
| Older snapshots | No guaranteed support |

## 📣 Reporting a vulnerability

Please do not publish exploitable vulnerability details in a public issue.

Use GitHub's **Report a vulnerability** feature in the repository Security tab when private vulnerability reporting is available. If that option is unavailable, contact the repository maintainer through the private contact method listed in the owner's GitHub profile.

Include a concise description and affected component, reproduction steps and impact, relevant commit/file/package/workflow, proof-of-concept details that do not expose real user data, and a suggested mitigation if known.

Do not include passwords, live tokens, private keys, personal records, or unrelated third-party data.

## ⏱️ Response expectations

The maintainer will acknowledge reports as soon as reasonably practical, assess severity and reproducibility, and coordinate a fix or mitigation. No guaranteed response or resolution SLA is claimed for this project.

Please allow time for investigation and coordinated disclosure. Do not publicly disclose an unresolved issue without giving the maintainer a reasonable opportunity to respond.

## 🧱 Current security controls and review areas

### Source and dependencies
- Keep secrets out of the repository.
- Review changes to package.json and package-lock.json.
- Use npm ci for lockfile-based installs.
- Review dependency advisories and maintenance health.
- Avoid unnecessary dependencies.

### GitHub Actions
- Give workflows only the permissions they require.
- Avoid exposing secrets to untrusted pull-request code.
- Review scheduled workflows that write back to the repository.
- Pin and review third-party actions according to project policy.
- Use protected environments for deployment credentials if deployment is added.

### Browser and hosting
- Use HTTPS on the selected host.
- Review external script origins.
- Prefer locally built, reviewed CSS over unpinned runtime tooling where practical.
- Keep asset paths and MIME types correct.
- Avoid unsafe inline script additions.

### Future application features
If forms, uploads, APIs, accounts, or payments are introduced, perform a new threat assessment. Define validation, authorization, rate limiting, session handling, secret storage, logging, retention, deletion, and incident response before release.

## 🚫 Out of scope

This policy does not provide security guarantees for third-party hosting providers, browsers, extensions, external image sources, or dependencies. It is not a compliance certification or substitute for a professional security assessment.
