# Plectara brand kit

Status: Owner-approved master artwork (2026-09-04)
Version: 2.0.0

![Plectara brand board](../../assets/brand/plectara-brand-board.png)

Plectara turns daily signals into useful patterns. The woven person brings four distinct strands together into one human form. The short supporting line, “A healthier whole,” is optional campaign copy, not part of the logo.

## Assets

The repository's `assets/brand/plectara/` directory contains editable SVGs, transparent PNGs, monochrome and reversed lockups, a stacked lockup, square app icons, a rounded social avatar, favicon, web manifest, iOS asset catalog, Android adaptive and legacy resources, social card, banner, and downloadable ZIP. Source artwork has outlined lettering and no embedded bitmap or external font dependency.

- [Horizontal SVG](../../assets/brand/plectara-horizontal.svg)
- [Standalone symbol SVG](../../assets/brand/plectara-symbol.svg)
- [Avatar SVG](../../assets/brand/plectara-avatar.svg)
- [Download complete brand kit](../../assets/brand/plectara-brand-kit.zip)

The approved reference PNG and owner-approved vector master are both preserved. The owner approved the final geometry, consistent gaps, and restored lettering on 2026-09-04. Subsequent exports use these approved sources. The logo lettering is recovered from the approved image as vector outlines, not substituted with a different font. Inter remains the UI and supporting-copy family. The recovered lettering is artwork, not an installable font.

Adjacent woven strands use one six-unit clearance in the symbol's construction coordinates. The boundaries are geometric offsets of their neighboring strands, with subpixel approximation, rather than independently drawn curves. This rule applies to the narrow separation channels, not the larger intentional openings around the head and between the legs. Gaps are transparent and work on any background.

## Usage

Use the horizontal lockup for headers and presentations, the standalone symbol for spacious contexts, and the app tile for launchers and avatars. Keep one head diameter of clear space around the standalone symbol and half a head diameter around lockups. Prefer 32 px or larger for the full woven symbol. At 16 px, the exported favicon conveys silhouette only; individual strands are not expected to remain legible.

Use the ink version on ivory or white and white version on dark backgrounds. Color logos on ink use a jade head for contrast. The full-color mark is decorative identity artwork; UI text and state indicators use the accessible semantic palette.

Do not stretch, rotate, add gradients or effects, independently move strands, or change strand colors. The approved design has four color identities; split visible pieces of one ribbon are not additional strands.

## Build

Install `tooling/requirements-brand.txt` in the local Python environment. From the repository, run `python tooling/build-plectara-tokens.py`, then `python tooling/build-plectara-brand.py`, and finally `python tooling/validate-brand.py`. Inter is bundled with its SIL Open Font License. CairoSVG also requires a system Cairo library.

Normal builds reuse `source/plectara-wordmark.svg` as the lettering master. To explicitly recover it again from the approved PNG, use `--retrace-wordmark` under Python 3.12; the installed VTracer build crashes under Python 3.14. Do not retrace or substitute the wordmark during ordinary asset exports.
