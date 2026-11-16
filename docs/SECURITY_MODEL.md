# 🔐 Security Model and Trust Boundaries

## 1. Current system boundary
The current application is a static HTML/CSS frontend. The browser retrieves static files from a hosting origin and also requests a Tailwind browser script from an external CDN.

No application-owned backend, API, database, authentication, user-submitted form, or payment flow is implemented.

## 2. Trust boundary diagram

~~~mermaid
flowchart LR
    subgraph Visitor["Visitor-controlled environment"]
      Browser[Browser]
    end
    subgraph Hosting["Static hosting origin"]
      HTML[index.html]
      CSS[Generated CSS]
      Assets[Images and SVG]
    end
    CDN[Tailwind CDN]
    Browser -->|HTTPS requests| HTML
    Browser -->|HTTPS requests| CSS
    Browser -->|HTTPS requests| Assets
    Browser -->|External script request| CDN
~~~

## 3. Threat register

| Threat | Current relevance | Control / follow-up |
|---|---|---|
| Secret accidentally committed | Possible | Secret scanning, review, no credentials in source |
| Dependency compromise | Build dependency exposure | Lockfile, dependency review, updates |
| Third-party script change | CDN reference exists | Prefer local reviewed build where feasible |
| Workflow token over-permission | Automation exists | Narrow workflow permissions |
| Misleading payment/security claim | Static copy mentions payments | Clarify there is no live payment implementation |
| Asset license misuse | Provenance incomplete | Record source and asset rights |

## 4. Secure development practices
- Keep secrets out of HTML, repository files, issues, and logs.
- Use locked dependency installation.
- Review dependency advisories and package ownership.
- Limit GitHub Actions permissions.
- Avoid running untrusted pull-request code with write credentials.
- Review external script origins.
- Use HTTPS in production hosting.
- Do not publish private contact information.

## 5. Future feature security gate
Before adding user input, accounts, APIs, uploads, or payments, define data classification and purpose, trust boundaries and data-flow diagrams, authentication and authorization, validation and abuse controls, secret management, logging and monitoring, retention and deletion, and security tests.

This guide is not a penetration test, audit, or certification.
