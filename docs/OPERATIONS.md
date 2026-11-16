# 🧭 Static Site Operations Guide

## 1. Operating model

Fabulo is a static frontend. Operational responsibility is therefore focused on source integrity, build reproducibility, hosting availability, asset delivery, browser behavior, and safe releases.

There is no application server, database, queue, authentication service, or payment processor in the current repository.

## 2. Routine maintenance

| Frequency | Activity | Evidence |
|---|---|---|
| Every change | Build and repository tests | CI run and local output |
| Every dependency update | Review changelog, audit impact, rebuild | Lockfile diff and CI |
| Every release | Smoke test public page and assets | Release checklist |
| Monthly | Review dependency alerts and open issues | Security/dependency review |
| Quarterly | Review asset rights, docs, browser support, and roadmap | Updated records |

## 3. Incident classification

- **P1:** Public site unavailable or widespread security exposure.
- **P2:** Major layout, asset, or navigation failure affecting core experience.
- **P3:** Limited visual defect or broken non-critical asset.
- **P4:** Documentation issue, minor polish, or low-impact enhancement.

Severity should reflect actual user impact, not the size of the code change.

## 4. Initial response

1. Confirm the issue from a clean browser session.
2. Determine whether the failure is in the source, build, hosting, DNS, or third-party dependency.
3. Record affected URLs, timestamps, browser, and reproducible steps.
4. Avoid publishing credentials, private logs, or personal data in public issues.
5. Roll back if the release causes significant user impact and a known-good deployment exists.
6. Create an incident record for P1 and P2 events.

## 5. Monitoring boundaries

No uptime monitor, analytics provider, error tracking platform, or alerting service is configured by this repository. Do not claim active monitoring until a provider is deliberately selected and connected.

## 6. Recovery checklist

- [ ] Confirm current public availability.
- [ ] Identify last known-good source revision.
- [ ] Restore or redeploy a known-good build.
- [ ] Confirm static assets load.
- [ ] Verify the 404 behavior.
- [ ] Document cause and user impact.
- [ ] Create follow-up work with an owner and acceptance criteria.
