"""Render the Plectara .icon with Apple's Icon Composer (macOS + Xcode)."""
import hashlib
import json
from pathlib import Path
import runpy
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/brand/plectara/platform/ios/liquid-glass'
ICON = BASE / 'Plectara.icon'
TOOL = Path('/Applications/Xcode.app/Contents/Applications/Icon Composer.app/Contents/Executables/ictool')
if not TOOL.is_file():
    raise SystemExit('Install Xcode with Icon Composer to render native iOS previews.')

runpy.run_path(str(ROOT / 'tooling/build-plectara-icon-layers.py'))
for source in (BASE / 'layers').glob('*.svg'):
    shutil.copy2(source, ICON / 'Assets' / source.name)

variants = [('Default', 'default'), ('Dark', 'dark'),
            ('ClearLight', 'clear-light'), ('ClearDark', 'clear-dark'),
            ('TintedLight', 'tinted-light'), ('TintedDark', 'tinted-dark')]
exports = []
for rendition, slug in variants:
    for points, scale in [(1024, 1), (60, 3), (20, 3)]:
        pixels = points * scale
        target = BASE / 'previews' / f'plectara-ios-{slug}-{pixels}.png'
        target.parent.mkdir(parents=True, exist_ok=True)
        args = [str(TOOL), str(ICON), '--export-image', '--output-file', str(target),
                '--platform', 'iOS', '--rendition', rendition,
                '--width', str(points), '--height', str(points), '--scale', str(scale)]
        if slug.startswith('tinted'):
            args += ['--tint-color', '0.55', '--tint-strength', '0.4']
        subprocess.run(args, check=True, capture_output=True, text=True)
        exports.append({'path': str(target.relative_to(BASE)), 'rendition': rendition,
                        'points': points, 'scale': scale, 'pixels': pixels,
                        'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})

manifest = {
    'version': '2.2.0', 'approved': '2026-09-11', 'platform': 'iOS',
    'renderer': 'Apple Icon Composer ictool',
    'renderer_version': subprocess.check_output([str(TOOL), '--version'], text=True).strip(),
    'tinted_preview': {'color': 0.55, 'strength': 0.4,
                       'note': 'Preview choice only. The device owner controls the tint.'},
    'source_files': {str(p.relative_to(ICON)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in sorted(ICON.rglob('*')) if p.is_file() and p.name != '.DS_Store'},
    'exports': exports,
}
(BASE / 'render-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(f'Rendered {len(exports)} native iOS previews across six appearances and three sizes.')
