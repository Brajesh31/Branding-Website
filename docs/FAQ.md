# ❓ Frequently Asked Questions

## 🚀 How do I run the project?
Install dependencies with npm ci, run npm run build, and serve the repository root with python -m http.server 8000. Open http://localhost:8000.

## 🎨 Why do my Tailwind changes not appear?
Run npm run build or keep npm run watch running. Check that tailwind.config.js scans the file containing your classes. Confirm the browser is loading the generated stylesheet rather than a stale cached file.

## 🖼️ Why is an image missing after deployment?
Check exact filename case, relative path, published directory, and network response. Some local systems use case-insensitive filesystems, while production hosts may be case-sensitive.

## 🛍️ Is Fabulo a real online store?
No. The current repository is a static landing page concept. There is no catalogue, cart, checkout, order processing, payment integration, rewards engine, account system, or inventory service.

## 💳 Are the payment and cashback messages functional?
No. They are static promotional copy. Do not enter payment information or treat the page as a payment service.

## 🧪 Is there a test suite?
The Tailwind build and repository structure validator are available. Dedicated browser automation, visual regression, and accessibility test frameworks are not currently assumed. See TESTING.md.

## 🚀 Where is the site deployed?
The repository documentation does not establish a confirmed production hosting provider. Deployment instructions are provider-neutral until the actual hosting target is documented.

## 🔐 Where should I report a vulnerability?
Follow the root SECURITY.md. Do not post exploit details or secrets in a public issue.

## 🛠️ Troubleshooting

### npm install fails
Check Node.js and npm versions, remove only the local node_modules directory if appropriate, then retry npm ci. Do not delete the lockfile to hide a dependency issue.

### Build fails
Read the first meaningful error, verify the manifest and lockfile are consistent, and confirm the Tailwind input and config files exist.

### Styles appear stale
Rebuild CSS, inspect the network response, verify the stylesheet path, and check browser caching.

### Page works locally but not on host
Check published root, generated stylesheet, case-sensitive paths, HTTPS, and host-specific routing rules.

### Mobile layout overflows
Use responsive DevTools, identify the overflowing element, and correct its width/flex/grid behavior. Do not mask the issue with global horizontal clipping.
