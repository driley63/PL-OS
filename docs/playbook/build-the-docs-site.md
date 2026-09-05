# Build The Docs Site

## Steps

1. Create a Python virtual environment.
2. Install requirements-docs.txt.
3. Run mkdocs serve locally.
4. Run mkdocs build --strict.
5. Confirm customHttp.yml still permits required MkDocs, Google Fonts, and Mermaid HTTPS assets.
6. Publish from CI on main.

## Exit Criteria

- The change can be reviewed from repository content.
- Related specs, ADRs, RFCs, assets, and release notes are updated.
- The change is consistent with PL-OS Core.
- Amplify response headers continue to upgrade insecure resource requests and restrict unnecessary browser capabilities.
