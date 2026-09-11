"""Validate generated Plectara assets, without a browser or app runtime."""
import ast
import hashlib
import json
import math
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile
from PIL import Image
from plectara_geometry import spaced_ribbons, polygon

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT/'assets/brand/plectara'
def deliverable(p):
    return p.is_file() and p.name != '.DS_Store'

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

# Native icon layers must preserve the approved geometry rather than tracing a mockup.
glass = BASE/'platform/ios/liquid-glass'
icon = glass/'Plectara.icon'
document = json.loads((icon/'icon.json').read_text())
master = ET.parse(BASE/'source/plectara-app-icon.svg').getroot()
outer = master.find(f'{ns}g')
figure = outer.find(f'{ns}g')
def shape_signature(node):
    return node.tag, tuple(sorted(node.attrib.items()))
expected_shapes = sorted(shape_signature(node) for node in figure)
actual_shapes = []
layer_files = sorted((glass/'layers').glob('*.svg'))
assert len(layer_files) == 7
for p in layer_files:
    root = ET.parse(p).getroot()
    assert root.get('viewBox') == '0 0 1024 1024'
    assert root.get('width') == root.get('height') == '1024'
    assert not {'rect', 'image', 'filter', 'mask', 'clipPath', 'linearGradient', 'radialGradient'} & {n.tag.rsplit('}',1)[-1] for n in root.iter()}
    layer_outer = root.find(f'{ns}g')
    layer_figure = layer_outer.find(f'{ns}g')
    assert layer_outer.attrib == outer.attrib and layer_figure.attrib == figure.attrib
    assert len(layer_figure) == 1
    actual_shapes.append(shape_signature(layer_figure[0]))
    assert p.read_bytes() == (icon/'Assets'/p.name).read_bytes()
assert sorted(actual_shapes) == expected_shapes, 'Liquid Glass geometry or colors drifted'
references = [layer['image-name'] for group in document['groups'] for layer in group['layers']]
assert sorted(references) == [p.name for p in layer_files]
for group in document['groups']:
    for layer in group['layers']:
        assert layer['fill-specializations'] == [{'appearance': 'tinted', 'value': {'solid': 'extended-srgb:1.00000,1.00000,1.00000,1.00000'}}]
fill_channels = [float(v) for v in document['fill']['solid'].split(':',1)[1].split(',')]
assert all(abs(a-b) < .00001 for a,b in zip(fill_channels, [int(ink[i:i+2],16)/255 for i in (1,3,5)] + [1]))

render = json.loads((glass/'render-manifest.json').read_text())
assert render['renderer'] == 'Apple Icon Composer ictool' and render['renderer_version']
assert set(render['source_files']) == {str(p.relative_to(icon)) for p in icon.rglob('*') if deliverable(p)}
for name, checksum in render['source_files'].items():
    assert hashlib.sha256((icon/name).read_bytes()).hexdigest() == checksum, 'Native previews need re-rendering'
renditions = {'Default', 'Dark', 'ClearLight', 'ClearDark', 'TintedLight', 'TintedDark'}
assert len(render['exports']) == 18
assert {(e['rendition'],e['points'],e['scale']) for e in render['exports']} == {(r,p,s) for r in renditions for p,s in [(1024,1),(60,3),(20,3)]}
for entry in render['exports']:
    p = glass/entry['path']
    assert hashlib.sha256(p.read_bytes()).hexdigest() == entry['sha256']
    im = Image.open(p)
    size = entry['points'] * entry['scale']
    assert im.mode == 'RGBA' and im.size == (size,size) and size == entry['pixels']
    assert all(im.getpixel(point)[3] == 0 for point in [(0,0),(size-1,0),(0,size-1),(size-1,size-1)])
    assert im.getchannel('A').getextrema() == (0,255)
    assert p.read_bytes() == (ROOT/'docs/assets/brand/ios-liquid-glass'/p.name).read_bytes()
assert (glass/'render-manifest.json').read_bytes() == (ROOT/'docs/assets/brand/ios-liquid-glass/render-manifest.json').read_bytes()
with zipfile.ZipFile(BASE/'plectara-ios-liquid-glass.zip') as archive:
    assert archive.testzip() is None
    assert set(archive.namelist()) == {str(p.relative_to(glass)) for p in glass.rglob('*') if deliverable(p)}
    for p in glass.rglob('*'):
        if deliverable(p):
            assert archive.read(str(p.relative_to(glass))) == p.read_bytes()
assert (BASE/'plectara-ios-liquid-glass.zip').read_bytes() == (ROOT/'docs/assets/brand/plectara-ios-liquid-glass.zip').read_bytes()

# Android vectors preserve the approved mark and owner-reviewed optical placement.
android = BASE/'platform/android'
a = '{http://schemas.android.com/apk/res/android}'
foreground = ET.parse(android/'res/drawable/plectara_foreground.xml').getroot()
monochrome = ET.parse(android/'res/drawable/plectara_monochrome.xml').getroot()
for vector in (foreground, monochrome):
    assert vector.tag == 'vector'
    assert vector.get(a+'width') == vector.get(a+'height') == '108dp'
    assert vector.get(a+'viewportWidth') == vector.get(a+'viewportHeight') == '108'
    assert {node.tag for node in vector.iter()} == {'vector', 'group', 'path'}
    assert len(vector.findall('group')) == 1
    assert len(vector.findall('.//path')) == 7
    assert not any(a+'strokeColor' in p.attrib or a+'fillAlpha' in p.attrib for p in vector.findall('.//path'))
placement = foreground.find('group')
assert placement.attrib == monochrome.find('group').attrib
scale = float(placement.get(a+'scaleX'))
tx, ty = (float(placement.get(a+k)) for k in ('translateX','translateY'))
assert abs(scale - 0.14997176395618853) < 1e-9
assert placement.get(a+'scaleX') == placement.get(a+'scaleY')
assert abs(tx - 33.0789389281117) < 1e-9 and abs(ty - 29.40463071118508) < 1e-9
color_paths, mono_paths = (v.findall('.//path') for v in (foreground, monochrome))
assert [p.get(a+'pathData') for p in color_paths[1:]] == [p.get('d') for p in figure.findall(f'{ns}path')]
assert [p.get(a+'pathData') for p in color_paths] == [p.get(a+'pathData') for p in mono_paths]
assert [p.get(a+'fillColor') for p in color_paths] == [p.get('fill') for p in figure]
assert {p.get(a+'fillColor') for p in mono_paths} == {'#FFFFFF'}
head = figure.find(f'{ns}circle')
cx, cy, radius = (float(head.get(k)) for k in ('cx','cy','r'))
assert color_paths[0].get(a+'pathData') == f'M {cx-radius},{cy} A {radius},{radius} 0 1,0 {cx+radius},{cy} A {radius},{radius} 0 1,0 {cx-radius},{cy} Z'
for p in figure.findall(f'{ns}path'):
    assert all(math.hypot(tx+x*scale-54, ty+y*scale-54) <= 32.000001 for x,y in polygon(p.get('d')).exterior.coords)
assert math.hypot(tx+cx*scale-54, ty+cy*scale-54) + radius*scale <= 32.000001
for version in (26,33):
    for name in ('ic_launcher', 'ic_launcher_round'):
        adaptive = ET.parse(android/f'res/mipmap-anydpi-v{version}/{name}.xml').getroot()
        expected = {'background':'@color/plectara_background','foreground':'@drawable/plectara_foreground'}
        if version == 33:
            expected['monochrome'] = '@drawable/plectara_monochrome'
        assert adaptive.tag == 'adaptive-icon' and len(adaptive) == len(expected)
        assert {n.tag:n.get(a+'drawable') for n in adaptive} == expected
background = ET.parse(android/'res/values/plectara_colors.xml').getroot()
assert background.find('color').get('name') == 'plectara_background'
assert background.find('color').text == ink
assert not list((android/'res').glob('drawable-*/plectara_foreground.png')), 'Legacy foreground PNGs override the vector'
for density, size in [('mdpi',48),('hdpi',72),('xhdpi',96),('xxhdpi',144),('xxxhdpi',192)]:
    for name in ('ic_launcher','ic_launcher_round'):
        im = Image.open(android/f'res/mipmap-{density}/{name}.png').convert('RGBA')
        assert im.size == (size,size)
        if name == 'ic_launcher':
            assert im.getchannel('A').getextrema() == (255,255)
        else:
            assert all(im.getpixel(xy)[3] == 0 for xy in [(0,0),(size-1,0),(0,size-1),(size-1,size-1)])
for name in ('foreground', 'monochrome', 'background'):
    filename = f'plectara-android-{name}.svg'
    assert (android/'source'/filename).read_bytes() == (BASE/'source'/filename).read_bytes()
    root = ET.parse(android/'source'/filename).getroot()
    assert root.get('viewBox') == '0 0 108 108'
    if name != 'background':
        group = root.find(f'{ns}g')
        expected_shapes = [dict(p.attrib) for p in figure]
        if name == 'monochrome':
            for attrs in expected_shapes:
                attrs['fill'] = '#FFFFFF'
        assert [p.attrib for p in group] == expected_shapes
        assert group.get('transform') == f'translate({tx:.10f} {ty:.10f}) scale({scale:.10f})'
android_manifest = json.loads((android/'asset-manifest.json').read_text())
assert android_manifest['version'] == '2.3.0' and android_manifest['approved'] == '2026-09-11'
assert android_manifest['source_sha256'] == hashlib.sha256((ROOT/android_manifest['source']).read_bytes()).hexdigest()
expected_files = {str(p.relative_to(android)) for p in android.rglob('*') if deliverable(p) and p.name != 'asset-manifest.json'}
assert {e['path'] for e in android_manifest['files']} == expected_files
for entry in android_manifest['files']:
    path = android/entry['path']
    assert path.stat().st_size == entry['bytes']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == entry['sha256']
themes = {'full-color','jade-light','jade-dark','clay-light','clay-dark','slate-light','slate-dark'}
shapes = {'circle','squircle','rounded-square'}
expected_pngs = {f'plectara-{t}-{s}-{n}.png' for t in themes for s in shapes for n in (1024,192,48)}
expected_svgs = {f'plectara-{t}-{s}.svg' for t in themes for s in shapes}
assert {p.name for p in (android/'previews/png').glob('*.png')} == expected_pngs
assert {p.name for p in (android/'previews/svg').glob('*.svg')} == expected_svgs
for filename in expected_pngs:
    path = android/'previews/png'/filename
    im = Image.open(path)
    size = int(path.stem.rsplit('-',1)[-1])
    assert im.mode == 'RGBA' and im.size == (size,size)
    assert im.getchannel('A').getextrema() == (0,255)
    assert all(im.getpixel(xy)[3] == 0 for xy in [(0,0),(size-1,0),(0,size-1),(size-1,size-1)])
for directory, names in [('png',expected_pngs),('svg',expected_svgs)]:
    for filename in names:
        assert (android/'previews'/directory/filename).read_bytes() == (ROOT/'docs/assets/brand/android-icons'/filename).read_bytes()
assert (android/'asset-manifest.json').read_bytes() == (ROOT/'docs/assets/brand/android-icons/asset-manifest.json').read_bytes()
with zipfile.ZipFile(BASE/'plectara-android-icons.zip') as archive:
    assert archive.testzip() is None
    assert set(archive.namelist()) == expected_files | {'asset-manifest.json'}
    for filename in archive.namelist():
        assert archive.read(filename) == (android/filename).read_bytes()
assert (BASE/'plectara-android-icons.zip').read_bytes() == (ROOT/'docs/assets/brand/plectara-android-icons.zip').read_bytes()

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
print(f'Passed: {len(svgs)} vector SVGs, jade heads, monochrome and lettering, transparent downloads, seven clearances, iOS opacity and 18 native renders, Android vectors and safe area, 63 Android PNGs and 21 SVGs, 10 legacy Android icons, inventory checksums, ZIP and site copies.')
