"""Validate generated Plectara assets, without a browser or app runtime."""
import ast
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile
from PIL import Image
from plectara_geometry import spaced_ribbons, polygon

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT/'assets/brand/plectara'
svgs = list((BASE/'source').glob('*.svg'))
for p in svgs:
    root = ET.parse(p).getroot()
    tags = [n.tag.rsplit('}',1)[-1] for n in root.iter()]
    assert 'image' not in tags and 'text' not in tags, p
    assert 'title' in tags and root.attrib.get('viewBox'), p

tree = ast.parse((ROOT/'tooling/build-plectara-brand.py').read_text())
raw = next(n.value for n in tree.body if isinstance(n,ast.Assign) and
           isinstance(n.value,ast.List) and any(isinstance(t,ast.Name) and t.id=='RIBBONS' for t in n.targets))
ribbons = [(str(i),ast.literal_eval(n.elts[1])) for i,n in enumerate(raw.elts)]
shapes = [polygon(d) for _,d in spaced_ribbons(ribbons)]
for i,j in [(0,1),(3,1),(2,1),(2,3),(4,3),(5,3),(5,4)]:
    assert 5.98 <= shapes[i].distance(shapes[j]) <= 6.02

for p in (BASE/'icons').glob('plectara-*.png'):
    size = int(p.stem.rsplit('-',1)[-1])
    assert Image.open(p).size == (size,size), p
catalog = BASE/'platform/ios/AppIcon.appiconset'
for entry in json.loads((catalog/'Contents.json').read_text())['images']:
    size = round(float(entry['size'].split('x')[0])*float(entry['scale'].rstrip('x')))
    im = Image.open(catalog/entry['filename'])
    assert im.size == (size,size)
    assert 'A' not in im.getbands(), entry['filename']

# Android adaptive foreground remains within the central 66/108 safe circle.
im = Image.open(BASE/'png/plectara-android-foreground.png').convert('RGBA')
for y in range(im.height):
    for x in range(im.width):
        if im.getpixel((x,y))[3]:
            assert (x+.5-54)**2+(y+.5-54)**2 <= 33**2

inventory = json.loads((BASE/'inventory.json').read_text())
for entry in inventory['files']:
    assert hashlib.sha256((BASE/entry['path']).read_bytes()).hexdigest() == entry['sha256']
with zipfile.ZipFile(BASE/'plectara-brand-kit.zip') as archive:
    assert archive.testzip() is None
    for entry in inventory['files']:
        assert archive.read(entry['path']) == (BASE/entry['path']).read_bytes()
for name in ('horizontal','horizontal-reversed','symbol','avatar'):
    assert (BASE/f'source/plectara-{name}.svg').read_bytes() == (ROOT/f'docs/assets/brand/plectara-{name}.svg').read_bytes()
assert (BASE/'plectara-brand-kit.zip').read_bytes() == (ROOT/'docs/assets/brand/plectara-brand-kit.zip').read_bytes()
print(f'Passed: {len(svgs)} vector SVGs, seven clearances, icon sizes, iOS opacity, Android safe area, inventory checksums, ZIP and site copies.')
