"""Build the approved Android vectors, adaptive resources, and review previews."""
from copy import deepcopy
from pathlib import Path
import hashlib
import json
import math
import shutil
import sys
import xml.etree.ElementTree as ET

import cairosvg

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/brand/plectara'
OUT = BASE / 'platform/android'
sys.path.insert(0, str(ROOT / 'tooling'))
from plectara_geometry import polygon

SVG = 'http://www.w3.org/2000/svg'
ANDROID = 'http://schemas.android.com/apk/res/android'
ET.register_namespace('', SVG)
ET.register_namespace('android', ANDROID)
A = '{' + ANDROID + '}'
N = '{' + SVG + '}'
SOURCE = ROOT / 'assets/brand/plectara/source/plectara-symbol.svg'
master = ET.parse(SOURCE).getroot()
source_outer = master.find(N + 'g')
original = source_outer.find(N + 'g')
palette = json.loads((ROOT / 'assets/tokens/color.tokens.json').read_text())['brand']
INK = palette['ink']['hex']

# A uniform 13% optical size increase with a one-dp inset from the safe circle.
# The center balances the raised arms and longer lower strands without reshaping them.
points = []
for shape in original:
    if shape.tag == N + 'path':
        points.extend(polygon(shape.get('d')).exterior.coords)
    else:
        cx, cy, r = (float(shape.get(k)) for k in ('cx', 'cy', 'r'))
        points.extend((cx + r * math.cos(i * math.pi / 360),
                       cy + r * math.sin(i * math.pi / 360)) for i in range(720))
center = (139.5, 164)
raw_radius = max(math.hypot(x-center[0], y-center[1]) for x,y in points)
SCALE = 32 / raw_radius
TX, TY = (54 - center[0] * SCALE, 54 - center[1] * SCALE)

def write(name, data):
    target = OUT / name
    target.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, bytes):
        target.write_bytes(data)
    else:
        target.write_text(data)
    return target

def svg_root(body, width=108, height=108, viewbox=None):
    return (f'<svg xmlns="{SVG}" width="{width}" height="{height}" '
            f'viewBox="{viewbox or f"0 0 {width} {height}"}">{body}</svg>')

def figure(mono=None):
    group = ET.Element(N+'g', {'transform': f'translate({TX:.10f} {TY:.10f}) scale({SCALE:.10f})'})
    for original_shape in original:
        shape = deepcopy(original_shape)
        if mono:
            shape.set('fill', mono)
        group.append(shape)
    return ET.tostring(group, encoding='unicode')

def vector(mono=False):
    root = ET.Element('vector', {A+'width':'108dp', A+'height':'108dp',
                               A+'viewportWidth':'108', A+'viewportHeight':'108'})
    group = ET.SubElement(root, 'group', {A+'name':'woven_figure',
        A+'translateX':f'{TX:.10f}', A+'translateY':f'{TY:.10f}',
        A+'scaleX':f'{SCALE:.10f}', A+'scaleY':f'{SCALE:.10f}'})
    names = ['jade_head','jade_upper','teal_ribbon','slate_ribbon',
             'copper_front','copper_lower','jade_lower']
    for name, shape in zip(names, original):
        if shape.tag == N+'circle':
            cx,cy,r = (float(shape.get(k)) for k in ('cx','cy','r'))
            path = f'M {cx-r},{cy} A {r},{r} 0 1,0 {cx+r},{cy} A {r},{r} 0 1,0 {cx-r},{cy} Z'
        else:
            path = shape.get('d')
        ET.SubElement(group, 'path', {A+'name':name, A+'fillColor':'#FFFFFF' if mono else shape.get('fill'),
                                    A+'pathData':path, A+'fillType':'nonZero'})
    ET.indent(root)
    return '<?xml version="1.0" encoding="utf-8"?>\n' + ET.tostring(root, encoding='unicode') + '\n'

write('res/drawable/plectara_foreground.xml', vector())
write('res/drawable/plectara_monochrome.xml', vector(True))
write('res/values/plectara_colors.xml',
      f'<?xml version="1.0" encoding="utf-8"?>\n<resources><color name="plectara_background">{INK}</color></resources>\n')
for version in (26,33):
    root = ET.Element('adaptive-icon')
    ET.SubElement(root,'background',{A+'drawable':'@color/plectara_background'})
    ET.SubElement(root,'foreground',{A+'drawable':'@drawable/plectara_foreground'})
    if version == 33:
        ET.SubElement(root,'monochrome',{A+'drawable':'@drawable/plectara_monochrome'})
    ET.indent(root)
    xml = '<?xml version="1.0" encoding="utf-8"?>\n' + ET.tostring(root,encoding='unicode')+'\n'
    for name in ('ic_launcher','ic_launcher_round'):
        write(f'res/mipmap-anydpi-v{version}/{name}.xml', xml)

write('source/plectara-android-foreground.svg', svg_root('<title>Plectara Android full-color foreground</title>'+figure()))
write('source/plectara-android-monochrome.svg', svg_root('<title>Plectara Android monochrome foreground</title>'+figure('#FFFFFF')))
write('source/plectara-android-background.svg', svg_root(f'<title>Plectara ink background</title><rect width="108" height="108" fill="{INK}"/>'))

THEMES = {
    'full-color': {'label':'Full color', 'bg':INK, 'fg':None},
    'jade-light': {'label':'Jade · light', 'bg':'#CBEDE1', 'fg':'#123B30'},
    'jade-dark': {'label':'Jade · dark', 'bg':'#234B3E', 'fg':'#B5E1CE'},
    'clay-light': {'label':'Clay · light', 'bg':'#FFDCC7', 'fg':'#633A23'},
    'clay-dark': {'label':'Clay · dark', 'bg':'#65432D', 'fg':'#FFDCC7'},
    'slate-light': {'label':'Slate · light', 'bg':'#D8E5FF', 'fg':'#293E61'},
    'slate-dark': {'label':'Slate · dark', 'bg':'#314869', 'fg':'#D8E5FF'},
}
SHAPES = ('circle','squircle','rounded-square')

def mask(shape):
    if shape == 'circle':
        return '<circle cx="54" cy="54" r="36"/>'
    if shape == 'rounded-square':
        return '<rect x="18" y="18" width="72" height="72" rx="16"/>'
    if shape == 'square':
        return '<rect x="18" y="18" width="72" height="72"/>'
    # Illustrative fourth-order superellipse, not a claim about a particular OEM.
    pts = []
    for i in range(721):
        t = i * 2 * math.pi / 720
        c, s = math.cos(t), math.sin(t)
        pts.append((54+36*math.copysign(abs(c)**.5,c),54+36*math.copysign(abs(s)**.5,s)))
    return '<path d="M '+' L '.join(f'{x:.5f},{y:.5f}' for x,y in pts)+' Z"/>'

def icon_body(shape, theme, uid='icon'):
    theme = THEMES[theme]
    return (f'<defs><clipPath id="{uid}">{mask(shape)}</clipPath></defs>'
            f'<g clip-path="url(#{uid})"><rect width="108" height="108" fill="{theme["bg"]}"/>'
            +figure(theme['fg'])+'</g>')

def export_png(svg, target, size):
    path = OUT/target
    path.parent.mkdir(parents=True,exist_ok=True)
    cairosvg.svg2png(bytestring=svg.encode(),write_to=str(path),output_width=size,output_height=size)
    return path

for shape in SHAPES:
    for theme in THEMES:
        data = svg_root(icon_body(shape,theme),1024,1024,'18 18 72 72')
        write(f'previews/svg/plectara-{theme}-{shape}.svg',data)
        for size in (1024,192,48):
            export_png(data, f'previews/png/plectara-{theme}-{shape}-{size}.png',size)

for density, scale in [('mdpi',1),('hdpi',1.5),('xhdpi',2),('xxhdpi',3),('xxxhdpi',4)]:
    for name,shape in [('ic_launcher','square'),('ic_launcher_round','circle')]:
        data=svg_root(icon_body(shape,'full-color'),108,108,'18 18 72 72')
        export_png(data,f'res/mipmap-{density}/{name}.png',int(48*scale))

# Publish canonical foreground sources and remove density bitmaps superseded by vectors.
for name in ('foreground', 'monochrome', 'background'):
    source = OUT / f'source/plectara-android-{name}.svg'
    shutil.copy2(source, BASE / 'source' / source.name)
    cairosvg.svg2png(url=str(source), write_to=str(BASE / f'png/plectara-android-{name}.png'), output_width=108, output_height=108)
for density in ('mdpi', 'hdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi'):
    obsolete = OUT / f'res/drawable-{density}/plectara_foreground.png'
    if obsolete.exists():
        obsolete.unlink()

files = []
for p in sorted(OUT.rglob('*')):
    if p.is_file() and p.name not in ('asset-manifest.json', '.DS_Store'):
        files.append({'path': str(p.relative_to(OUT)), 'bytes': p.stat().st_size,
                      'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
manifest = {
    'version': '2.3.0', 'approved': '2026-09-11',
    'source': str(SOURCE.relative_to(ROOT)),
    'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'generator': 'tooling/build-plectara-android.py',
    'geometry': 'Original six ribbon paths and circle preserved; the Android circle uses two equivalent arcs',
    'canvas_dp': [108, 108], 'scale': SCALE, 'translate': [TX, TY],
    'size_increase_percent': 100 * (SCALE / (.12 * 1.106) - 1),
    'safe_circle_radius_dp': 33, 'max_artwork_radius_dp': 32,
    'theme_examples': THEMES, 'shape_examples': list(SHAPES),
    'preview_sizes_px': [1024, 192, 48], 'preview_combinations': 21,
    'renderer': 'CairoSVG from approved geometry; illustrative launcher masks and theme colors',
    'consumer_integration': 'PL-OS asset publication; shipping app integration and device checks are separate',
    'files': files,
}
write('asset-manifest.json', json.dumps(manifest, indent=2) + '\n')
print('Built Android vector resources, 10 legacy icons, and 21 preview combinations in three sizes.')
