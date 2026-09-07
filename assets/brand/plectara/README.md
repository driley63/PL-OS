# Plectara approved brand kit — PL-OS v2.1.0

Owner: Plectara product owner / Brand Working Group
Artwork approval: 2026-09-04
Color standard approval: 2026-09-07
Status: Owner-approved jade-head standard for the v2.1.0 release

## Use these files

| Location | Contents and use |
| --- | --- |
| `source/` | SVG masters: symbol, outlined wordmark, horizontal, stacked, reversed, and monochrome variants |
| `png/` | Generated logo PNGs, app/avatar tiles, social card, social banner, and brand board |
| `icons/` | 16–2048 px app exports, favicon, and PWA manifest |
| `platform/ios/AppIcon.appiconset/` | Generated iPhone/iPad/store icon catalog |
| `platform/android/res/` | Adaptive foreground/background and legacy launcher densities |
| `reference/approved-woven-person.png` | Original approved concept; retained for provenance only |
| `tokens/`, `web/`, `flutter/` | Color source and generated integration adapters |
| `fonts/` | Inter and its SIL Open Font License for UI/supporting copy |
| `contrast-report.md` | 64 checked light/dark text and control pairs |
| `inventory.json` | File inventory and SHA-256 checksums |

`plectara-horizontal.svg` is the transparent primary lockup. Use `plectara-horizontal-reversed.svg` on dark backgrounds. The `horizontal-preview` export includes an ivory background for easy review; it is not the transparent master.

## Choose a logo

**Always use a jade head (`#76B7A5`) with the full-color figure**, on light and dark backgrounds. The previous ink-headed color variant is superseded. The original concept in `reference/` is historical provenance and is not a production download.

| Variant | Figure | Lettering | Background |
| --- | --- | --- | --- |
| `horizontal` | Jade head; original colored strands | Ink `#192D38` | White or ivory |
| `horizontal-reversed` | Same jade head and colored strands | White `#FFFFFF` | Ink or approved dark background |
| `horizontal-ink` | Entire figure ink `#192D38` | Same ink | Light |
| `horizontal-white` | Entire figure white `#FFFFFF` | Same white | Dark |

Each variant is available in `source/` as SVG and `png/` as a transparent 940 × 295 PNG. Standalone figures use `symbol`, `symbol-ink`, and `symbol-white`; standalone lettering uses `wordmark` and `wordmark-white`. Preserve the original lettering outlines, capitalization, spacing, proportions, and alignment. Do not retype or recolor the wordmark jade. Inter is for UI and supporting copy only.

The PL-OS brand kit page shows all nine treatments with direct SVG and PNG downloads. The preview backgrounds belong to the page, not the transparent downloads. Square app icons are intentionally opaque for platform use.

The social card is 1200 × 630; the banner is 1584 × 396. The optional line “A healthier whole” is campaign copy, not part of the logo. The brand board can be used in presentations. SVG masters and monochrome exports also serve as press/vendor assets.

## Production rules

Preserve aspect ratio, colors, the restored outlined lettering, and the six-unit transparent separation channels. The larger head/leg openings are intentional negative space. Prefer 32 px or larger for the full weave; 16 px favicons communicate silhouette only.

If a full-color logo is difficult to see, increase its size, use a clearer background, or choose an entire monochrome version. Do not change the head or individual strands to compensate.

Allow one head diameter of clear space around the standalone figure, half around a lockup. Use unrounded opaque app sources where platforms apply their own masks. Do not bake the social avatar's rounded corners into iOS icons.

The original lettering is custom outlined artwork recovered from the approved concept, not an identified font. Inter remains the UI family and is licensed separately in `fonts/OFL.txt`. Artwork approval is not legal registration or a guarantee of exclusive rights. No company suffix or registration symbol is authorized by this kit.

## Regenerate

From the repository root, install `tooling/requirements-brand.txt`, then run:

```sh
python tooling/build-plectara-tokens.py
python tooling/build-plectara-brand.py
python tooling/validate-brand.py
```

Normal builds reuse the approved `source/plectara-wordmark.svg`. Do not retrace it or regenerate the concept image for ordinary exports. Source modifications require renewed visual review. See the canonical PL-OS brand specifications for full usage and governance.
