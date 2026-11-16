# ✅ Quality Assurance and Release Checklist

## 🔍 Source review
- [ ] Change solves the stated problem.
- [ ] Existing page and assets are preserved unless intentionally changed.
- [ ] No unrelated generated or IDE files are included.
- [ ] No secrets or private data are committed.
- [ ] Dependencies are justified and lockfile is updated.

## 🛠️ Build review
- [ ] npm ci completes from a clean checkout.
- [ ] npm run build completes.
- [ ] Generated stylesheet exists at the expected path.
- [ ] Tailwind content globs include changed markup.
- [ ] Repository validator completes.

## 🎨 Browser review
- [ ] Page opens through a local HTTP server.
- [ ] Images and stylesheet load successfully.
- [ ] No unexpected browser console errors.
- [ ] Desktop layout is coherent.
- [ ] Mobile layout is coherent.
- [ ] No accidental horizontal overflow.
- [ ] Typography and image crops remain intentional.

## ♿ Accessibility review
- [ ] Semantic landmarks and headings are logical.
- [ ] Images have appropriate alternatives.
- [ ] Interactive elements have accessible names.
- [ ] Keyboard operation and visible focus work.
- [ ] Contrast has been checked.
- [ ] Zoom/reflow has been reviewed.

## 🔐 Security and privacy review
- [ ] No secrets or credentials are present.
- [ ] Dependency changes have been reviewed.
- [ ] Workflow permissions are minimal.
- [ ] External script dependencies are understood.
- [ ] New data collection has a documented purpose and retention model.
- [ ] No payment/security guarantee is claimed without implementation and evidence.

## 🚀 Release review
- [ ] Build runs in the deployment environment.
- [ ] Generated CSS is published.
- [ ] Relative paths work on the deployed host.
- [ ] HTTPS is active.
- [ ] Deployed page is verified.
- [ ] Rollback target is known.
- [ ] Release commit and URL are recorded.

Only mark a box complete after performing the check. A checklist is a control, not proof by itself.
