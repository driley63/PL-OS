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
palette = json.loads((ROOT/'assets/tokens/color.tokens.json').read_text())['brand']
ink, jade = (palette[name]['hex'] for name in ('ink', 'jade'))
strand_colors = {palette[name]['hex'] for name in ('teal', 'jade', 'copper', 'slate')}
ns = '{http://www.w3.org/2000/svg}'
svgs = list((BASE/'source').glob('*.svg'))
for p in svgs:
    root = ET.parse(p).getroot()
    tags = [n.tag.rsplit('}',1)[-1] for n in root.iter()]
    assert 'image' not in tags and 'text' not in tags, p
    assert 'title' in tags and root.attrib.get('viewBox'), p
    # Inspect each figure, including the mixed color/monochrome brand board.
    # A full-color head must never drift with the background or export type.
    for group in root.iter(f'{ns}g'):
        head = group.find(f'{ns}circle')
        if head is None:
            continue
        fills = {path.get('fill') for path in group.findall(f'{ns}path')}
        if fills == strand_colors:
            assert head.get('fill') == jade, f'{p}: full-color head must be jade'
        else:
            assert fills in ({ink}, {'#FFFFFF'}), f'{p}: unexpected figure colors'
            assert fills == {head.get('fill')}, f'{p}: monochrome head must match strands'

for name, color in [('horizontal-ink', ink), ('horizontal-white', '#FFFFFF'),
                    ('symbol-ink', ink), ('symbol-white', '#FFFFFF'),
                    ('wordmark', ink), ('wordmark-white', '#FFFFFF')]:
    root = ET.parse(BASE/f'source/plectara-{name}.svg').getroot()
    fills = {n.get('fill') for n in root.iter() if n.get('fill')}
    assert fills == {color}, f'{name}: all foreground artwork must use {color}'

for name, color in [('horizontal', ink), ('horizontal-reversed', '#FFFFFF')]:
    root = ET.parse(BASE/f'source/plectara-{name}.svg').getroot()
    wordmark = root.findall(f'{ns}g')[1]
    assert {n.get('fill') for n in wordmark.iter() if n.get('fill')} == {color}

ink_wordmark = ET.parse(BASE/'source/plectara-wordmark.svg').getroot()
white_wordmark = ET.parse(BASE/'source/plectara-wordmark-white.svg').getroot()
assert [n.get('d') for n in ink_wordmark.iter(f'{ns}path')] == [n.get('d') for n in white_wordmark.iter(f'{ns}path')]

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
for name in ('horizontal','horizontal-reversed','horizontal-ink','horizontal-white',
             'symbol','symbol-ink','symbol-white','wordmark','wordmark-white',
             'stacked','app-icon','avatar'):
    for directory, ext in [('source','svg'), ('png','png')]:
        assert (BASE/f'{directory}/plectara-{name}.{ext}').read_bytes() == (ROOT/f'docs/assets/brand/plectara-{name}.{ext}').read_bytes()
    im = Image.open(BASE/f'png/plectara-{name}.png')
    if name != 'app-icon':
        assert im.mode == 'RGBA' and im.getchannel('A').getextrema() == (0,255), name
assert (BASE/'plectara-brand-kit.zip').read_bytes() == (ROOT/'docs/assets/brand/plectara-brand-kit.zip').read_bytes()
print(f'Passed: {len(svgs)} vector SVGs, jade color heads, ink/white monochrome and lettering, transparent downloads, seven clearances, icon sizes, iOS opacity, Android safe area, inventory checksums, ZIP and site copies.')
