"""Fast, dependency-free checks for the Fabulo static website repository."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PageInspector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lang = None
        self.title = []
        self.in_title = False
        self.h1_count = 0
        self.image_alts = []
        self.local_assets = []
        self.ids = set()
        self.fragments = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "title":
            self.in_title = True
        if tag == "h1":
            self.h1_count += 1
        if tag == "img":
            self.image_alts.append(attrs.get("alt"))
        if tag in {"img", "script", "link"}:
            key = "href" if tag == "link" else "src"
            value = attrs.get(key)
            if value and not value.startswith(("http://", "https://", "data:", "//", "#")):
                self.local_assets.append(value.split("?", 1)[0])
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        href = attrs.get("href", "")
        if href.startswith("#") and len(href) > 1:
            self.fragments.append(href[1:])

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data.strip())


class RepositoryQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.page = PageInspector()
        cls.page.feed(cls.html)

    def test_document_has_language_and_title(self):
        self.assertTrue(self.page.lang, "HTML language must be declared")
        self.assertTrue("".join(self.page.title).strip(), "Page title must not be empty")

    def test_document_has_one_primary_heading(self):
        self.assertEqual(self.page.h1_count, 1, "The landing page should have one h1")

    def test_images_have_alt_attributes(self):
        self.assertTrue(self.page.image_alts, "Expected at least one image")
        self.assertTrue(all(alt is not None for alt in self.page.image_alts),
                        "Every image must have an alt attribute; decorative images use alt=''")

    def test_local_assets_exist_after_build(self):
        missing = []
        for asset in self.page.local_assets:
            target = (ROOT / asset).resolve()
            if not target.is_relative_to(ROOT.resolve()) or not target.is_file():
                missing.append(asset)
        self.assertEqual(missing, [], f"Missing or unsafe local assets: {missing}")

    def test_internal_fragments_resolve(self):
        missing = sorted(set(self.page.fragments) - self.page.ids)
        self.assertEqual(missing, [], f"Broken in-page links: {missing}")

    def test_static_site_support_files_exist(self):
        for path in ("404.html", "robots.txt", "favicon.svg", "site.webmanifest",
                     "README.md", "LICENSE", "SECURITY.md", "CONTRIBUTING.md"):
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file(), f"Required file missing: {path}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
