# v2.6.0 verification

Status: Local validation passed; publication pending
Date: 2026-09-28

## Evidence

- [Approved source and scope](../../assets/app/plectara/source/approval.json)
- [Browser layout and local interactions](../../assets/app/plectara/verification/browser-review.json)
- [App color fixtures and measurements](../../assets/app/plectara/verification/contrast-report.json)
- [Offline reference verification](../../assets/app/plectara/verification/offline-review.json)
- [Asset checksums and dimensions](../../assets/app/plectara/manifest.json)
- [Built-site gallery and download review](site-review.json)

## Completed checks

| Check | Result |
| --- | --- |
| Approved fragment and canonical artwork | Source hash matches approval; embedded texture/logo/font and exact saved widget texture match their packaged originals |
| App-local colors | 58 pairs pass; minimum ordinary-text ratio 4.5149:1; copper is measured separately as decoration |
| Browser and offline reference | All four screens at wide/narrow review widths; icons/fonts loaded, no horizontal overflow, no layout issues or script errors |
| Local interactions | Navigation, filters, timeframe, theme switch, focus restoration and review alternatives pass; capture/assistant flows remain visual-only |
| Screenshot export | Eight populated PNGs and two empty Today PNGs at 714 px width, plus four comparison sheets; final empty state captured from the approved source |
| Approved versus offline renders | Matching dimensions/content; small raster edge differences recorded; approved populated PNGs preserved |
| Package integrity | 38 inventoried files plus manifest; deterministic ZIP matches on repeat packaging; ZIP and documentation mirror match source bytes |
| Shared colors | 64 palette and 140 component checks pass; six contrast regression tests pass |
| Shared brand assets | Existing vector, logo, iOS/Android, checksum, ZIP and site validation passes |
| Existing widget kit | Exact texture/logos, six transparent previews, ZIP and site parity pass; generated output has no diff |
| Documentation | Strict MkDocs build passes |
| Built site | Desktop/mobile in both themes; eight gallery images load, responsive two/one-column layout, no horizontal overflow or script errors, local links resolve and ZIP matches source |

## Limits and publication

This is PL-OS documentation and asset verification. Native app/device and assistive-technology review remain required before an app release; these results do not establish ADA compliance. The Flutter color adapter is a mapping example and has not been compiled into the native app. Main-branch publication and live hosting verification follow a separately authorized merge.
