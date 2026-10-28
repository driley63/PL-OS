# Preferences design references

The owner selected **Section Hub** on October 27, 2026. The middle group heading is **Settings**. The specification and public gallery expose only this direction. `history/organization-study.html` retains the reviewed two-option study; Direct List is not a second approved layout.

## Sources

- `decision.json`: selected direction and review status.
- `current-inventory.json`: existing application destinations and conditional behavior from source review.
- `provenance.json`: original study and artwork provenance.
- `styles.css`, `preferences.js`, `reference.html`: app-only reference renderer, extracted from the reviewed study.
- `scenes.json`: 14 scenes, each captured in light and dark appearance.
- `gallery.html`: paired public gallery template.

## Rebuild

1. Run `python3 tooling/build-preferences-reference.py` from the repository root.
2. Serve `docs` locally. Open `assets/app/preferences-organization/reference.html?scene=preferences&theme=light` in the browser. Each scene accepts `scene` and `theme`; add `scale=1` for interactive inspection.
3. Wait for `html[data-capture-ready="true"]`. Capture the `.phone` bounds at the default 3× CSS zoom, with a full-page clip. Save each PNG as `screens/<scene>-<theme>.png` beneath the public reference directory. Do not resize captures or capture the surrounding review UI.
4. Record image/font readiness, missing icons, overflow, dimensions, scroll positions, theme text parity, and target measurements in `capture-observations.json`. The root source contains prototype-only controls; existing-editor rows are static placements.
5. Run `.venv/bin/python tooling/package-preferences-reference.py` to validate pixels and observations, generate the manifest/gallery, and refresh the specification's marked screenshot block.
6. Build the strict documentation site and inspect the rendered spec/gallery before delivery.

The package is a design reference. Example switches do not authorize or persist real consent. Account buttons are inert previews. Existing native forms, permissions, account actions, and consent rules remain authoritative. No app files are modified by these scripts.
