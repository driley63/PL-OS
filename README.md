# PL-OS

Plectara Operating System (PL-OS) is the canonical source of truth for Plectara's brand, design language, product experience, engineering standards, AI behavior, and release governance.

This repository treats product documentation like software. Specifications are versioned, reviewed, released, and traceable to decisions. Word and PDF versions can be generated later, but Markdown is the authoritative source.

## Current Version

- Version: v2.0.0
- Status: Approved v2.0.0 release
- Prepared: 2026-09-04
- Product name: Plectara
- Operating system name: PL-OS
- Design philosophy: "Translating daily habits into a plan towards optimal health."

The local folder and GitHub repository remain `LIQ-OS` for compatibility; **PL-OS** is the current system name. Historical releases retain their original names.

See the [approved brand kit](docs/specs/01-brand/plectara-brand-kit.md), [component migration](docs/specs/02-design/plectara-color-migration.md), and [v2.0.0 notes](docs/releases/v2.0.0/README.md).

## Repository Map

```text
LIQ-OS/
|-- docs/                  Canonical Markdown source for the MkDocs site
|   |-- core/              Foundational constitution, governance, versioning, and quality standards
|   |-- specs/             Versioned specification volumes
|   |-- adr/               Accepted architectural and product decision records
|   |-- rfc/               Reviewable proposals before decisions are locked
|   |-- playbook/          Contributor workflows and operating guidance
|   `-- releases/          Release notes and manifests
|-- templates/             Reusable templates for specs, ADRs, RFCs, releases, and reviews
|-- assets/                Source assets, token files, and generated asset placeholders
|-- tooling/               Local validation and publishing helpers
|-- .github/               GitHub issue templates, PR template, and CI workflows
|-- amplify.yml            AWS Amplify Hosting build configuration
|-- customHttp.yml         AWS Amplify Hosting response headers
|-- mkdocs.yml             Documentation site configuration
`-- requirements-docs.txt  Documentation build dependencies
```

## Core Principles

- Understanding over tracking: data is useful only when it leads to understanding.
- Action over observation: insights should point to practical next steps.
- Clarity over complexity: health information should become easier to interpret.
- Evidence over assumption: recommendations should expose reasoning and confidence.
- Consistency over novelty: reuse approved patterns unless a change is justified.
- Accessibility by default: inclusive behavior is part of the baseline.
- Implementation-first: every standard should map cleanly to production artifacts.

## Local Documentation Build

```bash
python3 -m pip install --user -r requirements-docs.txt
python3 -m mkdocs serve
```

To validate the production build locally:

```bash
python3 -m mkdocs build --strict
```

## AWS Amplify Deployment

`amplify.yml` builds this site with MkDocs and deploys the generated `site/` folder. `customHttp.yml` applies Amplify response headers for HTTPS hardening, mixed-content upgrades, framing restrictions, and MIME sniffing protection. Connect the GitHub `main` branch in Amplify and enable automatic builds. Amplify should use the checked-in build specification and redeploy when either hosting file changes.

```bash
git add amplify.yml customHttp.yml mkdocs.yml requirements-docs.txt docs .github
git commit -m "docs(site): harden PL-OS documentation deployment"
git push origin main
```

## First Commit Steps

```bash
unzip LIQ-OS-github-ready-v1.0.1.zip
cd LIQ-OS
git init
git add .
git commit -m "docs(core): bootstrap PL-OS v1.0.1"
git branch -M main
git remote add origin https://github.com/driley63/LIQ-OS.git
git push -u origin main
```

If the remote repository already has files, unzip into a fresh branch instead, review the diff, then merge through a pull request.
