# 🖼️ Asset Governance and Provenance

## 1. Why this matters
Images and icons can have different owners and license terms from the repository's source code. The MIT license for the project must not be treated as blanket permission to reuse every third-party image.

## 2. Existing asset locations
- Images/ contains editorial JPEG files.
- Images/SVG/ contains three SVG files.
- docs/assets/ is reserved for documentation illustrations and genuine screenshots.

## 3. Required asset record

For every newly added external asset, record:
- Repository-relative path.
- Asset type and dimensions.
- Intended page section.
- Original source URL.
- Author or rights holder.
- License and attribution requirements.
- Date obtained and any modifications.
- Whether it is decorative or informative.

Use docs/templates/asset-record.md.

## 4. Review process
1. Confirm the asset is relevant to the design.
2. Verify that the source and license permit the intended use.
3. Download from the original source, not an unknown mirror.
4. Optimize dimensions and file size without damaging quality.
5. Use a descriptive, stable filename.
6. Add correct alternative text in the HTML.
7. Update the asset record and pull request.

## 5. Screenshots
Screenshots must be captured from the actual running application. Record browser, viewport, commit, and date. Do not create mock screenshots that imply unimplemented functionality.

## 6. Removal and replacement
Before replacing an existing image, inspect where it is referenced. Update all references, verify the replacement license, and test the rendered result. Do not delete assets simply because their names look unfamiliar.
