# PL-OS v2.0.0 — Plectara brand migration

Date: 2026-09-04
Status: Approved release; deployment tracked through the existing Amplify workflow

[Local verification results](verification.md)

Plectara replaces LifestyleIQ in current specifications and site branding. The approved woven-person concept is implemented as scalable artwork. The muted teal, jade, copper, slate, ink, and ivory palette replaces the prior lime gradient. Component color roles change while the established component library, Inter typography, spacing, radii, and interactions remain intact.

The asset kit includes source SVGs, PNG exports, platform icons, social graphics, and an implementation guide. The owner approved the final vector artwork, uniform gaps, and restored outlined lettering. PL-OS replaces the current operating-system display name; the LIQ-OS repository slug remains unchanged. Legacy identifiers remain compatibility aliases. Historical ADRs and releases retain their original names and decisions.

The shared adapters pass 64 palette contrast checks. UI shapes, spacing, and typography tokens are unchanged. The Flutter adapter is a reference integration; this repository does not contain a product app runtime.

See [ADR-0012](../../adr/0012-rename-operating-system-pl-os.md), [ADR-0011](../../adr/0011-adopt-plectara.md), [brand kit](../../specs/01-brand/plectara-brand-kit.md), and [component migration](../../specs/02-design/plectara-color-migration.md).
