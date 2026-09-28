# Tooling

## Capture widget kit

`python tooling/build-capture-widget-kit.py` packages the owner-approved widget files, refreshes bundled specifications and the SHA-256 manifest, and mirrors the downloadable assets into the documentation site. It verifies the exact embedded texture, canonical logos, title case labels, absence of Edit, and six 2× screenshots with transparent corners. It preserves saved artwork rather than regenerating it.

## Current accessibility checks

```bash
python tooling/build-plectara-tokens.py
python tooling/check-component-contrast.py
python -m unittest discover -s tooling -p 'test_component_contrast.py'
```

The palette generator maintains the original 64 checks and adapters. The component checker adds 140 checks and rejects a stale report. Use `--write` to regenerate the component report after intentional changes. It leaves the released brand kit untouched.

For measured app overrides, pass `--fixtures path/to/measurements.json`. Each pair requires `name`, `foreground`, `background`, and `minimum`; optional `foregroundAlpha` and ordered `backgroundLayers` (`color`, `alpha`) describe sRGB compositing. Failures return exit status 1. The dated evidence in `docs/assets/audits/` is intentionally failing source-audit data, not the CI pass set.

See [Accessibility Testing](../docs/specs/04-engineering/accessibility-testing.md) for component and manual app checks.

## Original v1.0.0 tooling roadmap

- Token generation from JSON to Flutter, CSS, iOS, and Android formats.
- Asset export validation.
- Link validation.
- Release manifest validation.
- PDF and Word generation from Markdown.
