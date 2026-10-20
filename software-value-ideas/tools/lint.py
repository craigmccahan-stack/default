"""Static checks for Slides-type slide files: allowed tags, allowed CSS properties, font sizes, element counts."""
import re, sys, pathlib, json

ALLOWED_TAGS = {'section','h1','h2','h3','p','ul','ol','li','br','b','i','u','a','span','div','img','table','tr','th','td',
                'svg','hr','x-shape','x-icon','x-connector','x-embed','aside',
                # svg internals
                'path','rect','circle','line','polyline','polygon','g','defs','marker','lineargradient','stop','ellipse','clippath','radialgradient'}
ALLOWED_PROPS = {'position','left','top','right','bottom','width','height','min-width','min-height','max-width','max-height','display',
    'flex-direction','flex-wrap','gap','align-items','justify-content','justify-items','align-self','justify-self','flex','flex-grow',
    'flex-shrink','flex-basis','grid-template-columns','grid-template-rows','grid-column','grid-row','aspect-ratio','padding','overflow',
    'font-family','font-size','font-weight','font-style','font','line-height','letter-spacing','text-align','text-transform','white-space',
    'text-decoration','font-variant-numeric','-webkit-text-stroke','color','background','background-clip','-webkit-text-fill-color',
    'border','border-top','border-right','border-bottom','border-left','border-radius','box-shadow','text-shadow','opacity','transform',
    'filter','backdrop-filter','mix-blend-mode','object-fit'}

def check(path):
    s = pathlib.Path(path).read_text()
    issues = []
    body = re.sub(r'<svg.*?</svg>', '<svg></svg>', s, flags=re.S)
    tags = re.findall(r'<\s*([a-zA-Z][\w-]*)', body)
    for t in set(tags):
        if t.lower() not in ALLOWED_TAGS:
            issues.append(f'tag <{t}>')
    sections = re.findall(r'<section\b', s)
    if len(sections) != 1:
        issues.append(f'{len(sections)} sections')
    for st in re.findall(r'style="([^"]*)"', body):
        for decl in st.split(';'):
            if not decl.strip():
                continue
            prop = decl.split(':', 1)[0].strip().lower()
            if prop not in ALLOWED_PROPS:
                issues.append(f'prop {prop}')
            m = re.match(r'\s*font-size\s*:\s*(\d+(?:\.\d+)?)px', decl)
            if m and float(m.group(1)) < 24:
                issues.append(f'font-size {m.group(1)}px')
            if re.search(r'\b(em|rem|vw|vh)\b', decl) and 'letter-spacing' not in decl:
                if re.search(r'\d(em|rem|vw|vh)\b', decl):
                    issues.append(f'unit in "{decl.strip()}"')
            if 'var(' in decl:
                issues.append('var()')
    n = len(tags)
    if n > 200:
        issues.append(f'{n} elements > 200')
    svg_sizes = [len(x.encode()) for x in re.findall(r'<svg.*?</svg>', s, flags=re.S)]
    for z in svg_sizes:
        if z > 52000:
            issues.append(f'svg {z} bytes')
    if '<text' in s:
        issues.append('svg <text>')
    return n, sorted(set(issues))

if __name__ == '__main__':
    root = pathlib.Path(sys.argv[1])
    deck = json.loads((root / 'project/deck.json').read_text())
    for sid in deck['order']:
        f = root / 'project/slides' / f'{sid}.html'
        if not f.exists():
            print(f'{sid}: MISSING'); continue
        n, iss = check(f)
        print(f'{sid}: {n} tags; ' + ('; '.join(iss) if iss else 'ok'))
