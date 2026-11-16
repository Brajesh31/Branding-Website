# 🔎 SEO, Metadata, and Discoverability

## 1. Purpose and scope

This guide defines the search and social metadata baseline for the Fabulo static landing page. Metadata improves how a page is understood and previewed. It does not guarantee indexing, ranking, rich results, or traffic.

## 2. Current baseline

The homepage should maintain:
- A unique, descriptive document title.
- A concise meta description that accurately describes the editorial concept.
- A declared document language and viewport.
- Open Graph title, description, and type.
- A meaningful theme color.
- A crawlable static HTML document.
- Descriptive alternative text for informative images.
- Stable, lowercase, canonical URL paths once the production domain is confirmed.

## 3. Files and responsibilities

| File | Responsibility |
|---|---|
| `index.html` | Homepage title, description, social metadata, semantic content |
| `robots.txt` | Basic crawler access policy |
| `site.webmanifest` | Browser install metadata and theme |
| `favicon.svg` | Scalable browser icon |
| `404.html` | Useful not-found response on compatible static hosts |
| `docs/ASSET_GOVERNANCE.md` | Rights and attribution records for media |

## 4. Production domain checklist

Before adding a canonical URL or sitemap:
1. Confirm the final production hostname and HTTPS configuration.
2. Decide whether the site is hosted at a domain root or a subpath.
3. Add a canonical link using the exact public URL.
4. Create a sitemap containing only real, canonical, indexable URLs.
5. Add the sitemap URL to `robots.txt`.
6. Verify the domain in the relevant search webmaster platform.
7. Submit the sitemap and inspect indexing reports.

Do not publish a placeholder sitemap or invent a domain. A sitemap with guessed URLs is worse than no sitemap.

## 5. Social sharing

When a real share image is selected, add `og:image` and the relevant Twitter/X card metadata. The image must be an approved project asset, have a stable absolute URL, and meet the platform's current size and format guidance. Do not label a random editorial photograph as an official brand logo.

## 6. Content quality

- Write one clear page title and one primary heading.
- Keep headings hierarchical.
- Use descriptive copy rather than keyword repetition.
- Give images meaningful alt text when they convey content.
- Use empty alt text for decorative images.
- Avoid hidden keyword blocks, misleading claims, and duplicated metadata.

## 7. Verification

Before release:
- Inspect rendered HTML source.
- Test homepage and 404 behavior on the actual host.
- Validate metadata and social preview using current platform tools.
- Confirm all internal and asset URLs work on the production path.
- Confirm crawler access is intentional.

## 8. Limitations

This repository does not include analytics, a CMS, structured product data, a product catalog, or a verified production domain. Do not add product schema, review ratings, price markup, or organization claims that the project cannot substantiate.
