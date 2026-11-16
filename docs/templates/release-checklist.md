# 🚀 Static Site Release Checklist

## Before release
- [ ] Intended commit and release scope confirmed.
- [ ] Dependencies installed with npm ci.
- [ ] npm run build succeeds.
- [ ] Generated css/style.css exists.
- [ ] Local images and relative paths verified.
- [ ] Mobile and desktop layouts reviewed.
- [ ] Keyboard and image alternatives reviewed.
- [ ] External CDN dependency reviewed.
- [ ] No secrets, local caches, or unrelated files included.
- [ ] README, changelog, and docs updated where needed.

## Deployment
- [ ] Correct static root configured.
- [ ] Generated stylesheet included.
- [ ] HTTPS enabled.
- [ ] Custom domain and DNS checked, if applicable.
- [ ] Page and asset URLs verified.
- [ ] Browser console and network requests checked.

## After release
- [ ] Deployed commit and URL recorded.
- [ ] Live page verified.
- [ ] Rollback target retained.
- [ ] Known limitations documented.
- [ ] Follow-up issues created.

Record owner, date, and evidence. An unchecked item must not be described as complete.
