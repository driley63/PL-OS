"""Build Plectara vector artwork and exports. Run with requirements-brand.txt.

The reviewed concept is retained in assets/brand/plectara/reference.
This geometric interpretation is the owner-approved editable vector master.
"""
from pathlib import Path
import json
import shutil
import zipfile
import sys
import hashlib
import subprocess
import cairosvg
from PIL import Image
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from plectara_geometry import spaced_ribbons, approved_wordmark, wordmark_body

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/brand/plectara'
palette = json.loads((ROOT/'assets/tokens/color.tokens.json').read_text())['brand']
INK, TEAL, JADE, COPPER, SLATE, IVORY = (palette[name]['hex'] for name in ('ink','teal','jade','copper','slate','ivory'))
# Outline coordinates are relative to (175, 226) in the approved reference.
# Keep the crossing gaps in these shared coordinates: independently positioning
# the arms breaks the apparent continuity of the strands through the torso.
RIBBONS = [
    (JADE, 'M128 108 C183 73 255 54 271 0 L276 0 C293 76 241 101 189 140 L177 149 Z'),
    (TEAL, 'M3 0 L8 0 C21 37 50 57 104 87 C151 113 203 144 188 192 C184 205 173 216 163 225 C140 202 125 183 106 161 C71 129 24 105 7 73 C-6 49 -2 21 3 0 Z'),
    # Underlying ribbons overlap their neighbors before a shared six-unit offset
    # cuts the channels. This avoids tapering gaps from hand-matched curves.
    (SLATE, 'M181 180 C211 217 243 264 243 296 C243 323 230 345 207 349 L180 349 C198 302 169 257 148 228 Z'),
    (COPPER, 'M96 143 C113 174 130 205 153 229 C188 263 206 303 194 349 L165 349 C174 305 142 276 109 246 C83 222 73 190 96 143 Z'),
    (COPPER, 'M90 200 C97 221 115 241 124 259 C95 280 58 309 70 349 C50 349 32 325 35 293 C37 265 57 240 90 200 Z'),
    (JADE, 'M98 242 L145 282 C113 303 105 323 112 349 L72 349 C62 315 76 285 98 242 Z'),
]
RIBBONS = spaced_ribbons(RIBBONS)
wordmark_size, wordmark_paths = approved_wordmark(BASE/'reference/approved-woven-person.png', retrace='--retrace-wordmark' in sys.argv)
font = instantiateVariableFont(TTFont(ROOT/'assets/brand/fonts/Inter-variable.ttf'), {'wght':650,'opsz':32})
glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
units = font['head'].unitsPerEm

def text_paths(text, x, y, size, color=INK):
    if text == 'Plectara':
        cap_height = size * font['OS/2'].sCapHeight / units
        scale = cap_height / wordmark_size[1]
        return f'<g transform="translate({x} {y-cap_height}) scale({scale})">'+wordmark_body(wordmark_paths, color)+'</g>'
    parts, cursor = [], 0
    for char in text:
        glyph = glyphs[cmap[ord(char)]]
        pen = SVGPathPen(glyphs); glyph.draw(pen)
        parts.append(f'<path transform="translate({cursor} 0)" d="{pen.getCommands()}"/>')
        cursor += glyph.width - units * .018
    return f'<g fill="{color}" transform="translate({x} {y}) scale({size/units} {-size/units})">'+''.join(parts)+'</g>'

def figure(x=0,y=0,scale=1,mono=None):
    # Uniform scaling preserves the reference silhouette and existing export height.
    # Full-color identity always uses a jade head, on every background.
    return f'<g transform="translate({x} {y}) scale({scale})"><g transform="translate(-11.5 0) scale(1.106)"><circle cx="138" cy="36" r="36.5" fill="{mono or JADE}"/>'+''.join(f'<path fill="{mono or c}" d="{d}"/>' for c,d in RIBBONS)+'</g></g>'

def svg(w,h,body,title='Plectara — woven person'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{title}</title>{body}</svg>'

def save(rel,content):
    p=BASE/rel; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(content); return p

def deliverable(p):
    # Finder may create this while inspecting a native .icon package.
    return p.is_file() and p.name != '.DS_Store'

def raster(source,target,w,h=None):
    p=BASE/target; p.parent.mkdir(parents=True,exist_ok=True)
    cairosvg.svg2png(url=str(source),write_to=str(p),output_width=w,output_height=h)
    return p

masters={}
for name, color in [('wordmark', INK), ('wordmark-white', '#FFFFFF')]:
    masters[name]=save(f'source/plectara-{name}.svg', svg(*wordmark_size, wordmark_body(wordmark_paths, color), title='Plectara — approved lettering outlined'))
    raster(masters[name],f'png/plectara-{name}.png',940,round(940*wordmark_size[1]/wordmark_size[0]))
for name,body,w,h in [
    ('symbol',figure(28,12),340,410),
    ('symbol-ink',figure(28,12,mono=INK),340,410),
    ('symbol-white',figure(28,12,mono='#FFFFFF'),340,410),
    ('horizontal',figure(24,26,.62)+text_paths('Plectara',235,205,164),940,295),
    ('horizontal-preview',f'<rect width="940" height="295" fill="{IVORY}"/>'+figure(24,26,.62)+text_paths('Plectara',235,205,164),940,295),
    ('horizontal-reversed',figure(24,26,.62)+text_paths('Plectara',235,205,164,'#FFFFFF'),940,295),
    ('horizontal-ink',figure(24,26,.62,mono=INK)+text_paths('Plectara',235,205,164),940,295),
    ('horizontal-white',figure(24,26,.62,mono='#FFFFFF')+text_paths('Plectara',235,205,164,'#FFFFFF'),940,295),
    ('stacked',figure(165,24,.95)+text_paths('Plectara',48,535,117),600,600),
    ('app-icon',f'<rect width="1024" height="1024" fill="{INK}"/>'+figure(290,200,1.58),1024,1024),
    ('avatar',f'<rect width="1024" height="1024" rx="224" fill="{INK}"/>'+figure(290,200,1.58),1024,1024),
]:
    masters[name]=save('source/plectara-'+name+'.svg',svg(w,h,body))
    raster(masters[name],'png/plectara-'+name+'.png',w,h)

for size in [16,24,32,48,64,72,96,120,144,152,180,192,256,512,1024,2048]:
    raster(masters['app-icon'],f'icons/plectara-{size}.png',size,size)
ico=Image.open(BASE/'icons/plectara-256.png')
ico.save(BASE/'icons/favicon.ico',sizes=[(16,16),(32,32),(48,48)])
save('icons/site.webmanifest',json.dumps({'name':'Plectara','short_name':'Plectara','icons':[{'src':f'plectara-{n}.png','sizes':f'{n}x{n}','type':'image/png','purpose':'any maskable'} for n in [192,512]],'theme_color':INK,'background_color':IVORY,'display':'standalone'},indent=2)+'\n')
ios=[]
for idiom,sizes in [('iphone',[20,29,40,60]),('ipad',[20,29,40,76,83.5])]:
    for size in sizes:
        for scale in ([2,3] if idiom=='iphone' else ([2] if size==83.5 else [1,2])):
            filename=f'{idiom}-{size}-{scale}x.png'; pixels=int(size*scale)
            raster(masters['app-icon'],'platform/ios/AppIcon.appiconset/'+filename,pixels,pixels)
            ios.append({'idiom':idiom,'size':f'{size}x{size}','scale':f'{scale}x','filename':filename})
raster(masters['app-icon'],'platform/ios/AppIcon.appiconset/marketing-1024.png',1024,1024)
ios.append({'idiom':'ios-marketing','size':'1024x1024','scale':'1x','filename':'marketing-1024.png'})
save('platform/ios/AppIcon.appiconset/Contents.json',json.dumps({'images':ios,'info':{'version':1,'author':'Plectara'}},indent=2)+'\n')
subprocess.run([sys.executable, str(ROOT/'tooling/build-plectara-android.py')], check=True)
for name,w,h,body in [
    ('social-card',1200,630,f'<rect width="1200" height="630" fill="{IVORY}"/>'+figure(95,135,.85)+text_paths('Plectara',395,350,155)+text_paths('A healthier whole.',399,421,38,TEAL)),
    ('social-banner',1584,396,f'<rect width="1584" height="396" fill="{INK}"/>'+figure(130,60,.7)+text_paths('Plectara',435,230,164,'#FFFFFF')+text_paths('A healthier whole.',443,296,40,JADE)),
    ('brand-board',1440,1000,f'<rect width="1440" height="1000" fill="{IVORY}"/>'+figure(112,72,.85)+text_paths('Plectara',440,300,187)+text_paths('Distinct strands. A healthier whole.',447,367,34,TEAL)+figure(212,498,.52,mono=INK)+f'<rect x="605" y="487" width="254" height="254" rx="55" fill="{INK}"/>'+figure(662,516,.49)+''.join(f'<rect x="{105+i*208}" y="842" width="185" height="72" rx="12" fill="{c}"/>'+text_paths(label,108+i*208,949,22,INK) for i,(c,label) in enumerate([(INK,'Ink'),(TEAL,'Teal'),(JADE,'Jade'),(COPPER,'Copper'),(SLATE,'Slate'),(IVORY,'Ivory')]))),
]:
    p=save(f'source/plectara-{name}.svg',svg(w,h,body)); raster(p,f'png/plectara-{name}.png',w,h)

docs=ROOT/'docs/assets/brand'; docs.mkdir(parents=True,exist_ok=True)
for name in ['horizontal','horizontal-reversed','horizontal-ink','horizontal-white',
             'symbol','symbol-ink','symbol-white','wordmark','wordmark-white',
             'stacked','app-icon','avatar']:
    shutil.copy2(masters[name],docs/f'plectara-{name}.svg')
    shutil.copy2(BASE/f'png/plectara-{name}.png',docs/f'plectara-{name}.png')
shutil.copy2(BASE/'png/plectara-brand-board.png',docs/'plectara-brand-board.png')
font_docs=ROOT/'docs/assets/fonts'; font_docs.mkdir(parents=True,exist_ok=True)
for filename in ['Inter-variable.ttf','OFL.txt']:
    shutil.copy2(ROOT/'assets/brand/fonts'/filename,font_docs/filename)
for directory, filenames in {
    'tokens':['color.tokens.json','spacing.tokens.json','radius.tokens.json','typography.tokens.json'],
    'web':['plectara-tokens.css','lifestyleiq-tokens.css'],
    'flutter':['plectara_colors.dart','lifestyleiq_colors.dart'],
    'fonts':['Inter-variable.ttf','OFL.txt'],
}.items():
    dest=BASE/directory; dest.mkdir(parents=True,exist_ok=True)
    for filename in filenames:
        source=ROOT/('assets/brand/fonts' if directory=='fonts' else 'assets/'+directory)/filename
        shutil.copy2(source,dest/filename)
for p in (BASE/'platform/ios/AppIcon.appiconset').glob('*.png'):
    with Image.open(p) as im:
        im.convert('RGB').save(p)
if '--render-ios' in sys.argv:
    subprocess.run([sys.executable, str(ROOT/'tooling/export-plectara-liquid-glass.py')], check=True)
glass = BASE/'platform/ios/liquid-glass'
glass_archive = BASE/'plectara-ios-liquid-glass.zip'
with zipfile.ZipFile(glass_archive, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in sorted(glass.rglob('*')):
        if deliverable(p):
            z.write(p, p.relative_to(glass))
shutil.copy2(glass_archive, docs/glass_archive.name)
glass_docs = docs/'ios-liquid-glass'
glass_docs.mkdir(parents=True, exist_ok=True)
for p in (glass/'previews').glob('*.png'):
    shutil.copy2(p, glass_docs/p.name)
shutil.copy2(glass/'render-manifest.json', glass_docs/'render-manifest.json')
android = BASE/'platform/android'
android_archive = BASE/'plectara-android-icons.zip'
with zipfile.ZipFile(android_archive, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in sorted(android.rglob('*')):
        if deliverable(p):
            z.write(p, p.relative_to(android))
shutil.copy2(android_archive, docs/android_archive.name)
android_docs = docs/'android-icons'
android_docs.mkdir(parents=True, exist_ok=True)
for p in (android/'previews/png').glob('*.png'):
    shutil.copy2(p, android_docs/p.name)
for p in (android/'previews/svg').glob('*.svg'):
    shutil.copy2(p, android_docs/p.name)
shutil.copy2(android/'asset-manifest.json', android_docs/'asset-manifest.json')
archive=BASE/'plectara-brand-kit.zip'
inventory={'version':'2.3.0','owner':'Plectara product owner / Brand Working Group','approved':'2026-09-11','source':'tooling/build-plectara-brand.py; tooling/build-plectara-android.py; tooling/export-plectara-liquid-glass.py; source/plectara-wordmark.svg; platform/ios/liquid-glass/Plectara.icon; assets/tokens/','files':[]}
for p in sorted(BASE.rglob('*')):
    if deliverable(p) and p not in (archive,BASE/'inventory.json'):
        inventory['files'].append({'path':str(p.relative_to(BASE)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
save('inventory.json',json.dumps(inventory,indent=2)+'\n')
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(BASE.rglob('*')):
        if deliverable(p) and p!=archive: z.write(p,p.relative_to(BASE))
shutil.copy2(archive,docs/'plectara-brand-kit.zip')
print('Built Plectara SVG masters, PNGs, platform icons, social graphics, and brand-kit ZIP.')
