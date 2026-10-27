# Flutter Insights references

Run `python3 tooling/render-insights-flutter.py --app-root /path/to/Plectara` from PL-OS. Flutter and the app's cached dependencies must be installed. This prepares an ignored preview project under `outputs/`, resolves cached dependencies offline, and renders twelve PNGs at 3× through the Flutter engine.

The scene imports the actual Plectara app theme, woven backdrop, reading cards, care notice, Today highlight, finding cards, and detail route. Proposed outcome filtering and compact seeded plan/log content are preview-only compositions using Flutter controls and the shared theme. The source Plectara checkout is read-only to this renderer.

The widget capture harness loads Inter and Material icons, uses iOS theme selection and safe-area insets, and opens the real detail route and modal filter sheet. Captures omit system status/home indicators; they are not simulator captures or native accessibility certification. It fails on Flutter render errors. The metadata records PNG hashes and the hashes of imported app components, including any uncommitted app work used as the source.

These Dart sources replace the retired SVG renderer. No SVG exists for a Flutter raster capture. Edit the scene or actual shared components through their respective review process, then re-render.

## Refined composition review

Run `python3 tooling/render-insights-flutter.py --review-only` to render only the proposed Insights inventory in light and dark. It writes the goal-focused inventory (`screens/insights-refined-*.png`), the profile goal picker (`screens/insights-goals-*.png`), and `screens/review.json`, leaving the twelve earlier captures and the normative specification unchanged. The local viewer defaults to this proposal. The capture check also exercises combined saved-goal/evidence filtering, profile-driven Capital Case labels, goals with no findings, 44-unit selector targets and enlarged text reflow.

The review fixture supplies saved goals using the actual app goal IDs/labels. `RefinedInsights` receives that data through its `goals` and `findingGoals` properties; it has no built-in Sleep/Hydration outcome filter catalog. Custom profile labels are displayed in Capital Case without changing stored wording or IDs. The Caffeine/Sleep bridge has no directional arrow; its shared zero-to-ten comparison uses theme chart tones and explicit numeric labels.
