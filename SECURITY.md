# Security Policy

## Project scope

Fabulo is a static HTML and Tailwind CSS page. This repository does not implement a server, authentication, database, payment processing, contact form, or application API. Security reports are still welcome for vulnerabilities in the repository, its build dependencies, or unsafe content included in the page.

## Reporting a vulnerability

Please do not publish unpatched vulnerability details in a public issue or pull request. Use GitHub's private vulnerability reporting for this repository if it is enabled: [Report a vulnerability](https://github.com/Brajesh31/Branding-Website/security/advisories/new). If private reporting is unavailable, contact the maintainer through [@brajesh31](https://github.com/brajesh31) and request a private reporting channel.

Include the affected file or dependency, the conditions needed to reproduce the issue, its likely impact, and any suggested mitigation. Do not include real credentials, personal data, or unrelated secrets in a report.

## Response

The maintainer will acknowledge a report when reasonably able, investigate the affected revision and dependency versions, and coordinate a fix and disclosure timeline with the reporter. This is a personal project without a guaranteed response-time or service-level commitment.

## Dependency and deployment practices

- Keep dependency changes deliberate and review lockfile changes.
- Do not commit credentials or private configuration. The current site does not require environment variables or secrets.
- Review third-party scripts and assets before adding them. The HTML currently loads Tailwind from its public CDN.
- Deploy only generated and reviewed static files, and use HTTPS through the hosting provider.
