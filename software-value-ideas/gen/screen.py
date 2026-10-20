# Generates the screen scatter slide for the main deck.
W, H = 1000, 600
L, R, T, B = 80, 960, 50, 520
XMAX, YMAX = 12.0, 4.0
X = lambda v: L + v / XMAX * (R - L)
Y = lambda s: B - s / YMAX * (B - T)
BLUE, ORANGE, GRAY, INK, LINE = '#1F5C99', '#A9521A', '#9AA8B5', '#14202B', '#E3DED3'
# ticker, owner FCF yield %, durability score, kind, label side
pts = [
    ('INTU', 7.6, 3.5, 'pick', 'r'), ('ADBE', 8.9, 3.0, 'pick', 'r'), ('GDDY', 10.4, 2.5, 'pick', 'l'),
    ('FDS', 6.1, 2.0, 'deck', 'l'), ('CRM', 5.7, 2.5, 'deck', 'r'),
    ('DOCU', 4.5, 2.5, 'other', 'l'), ('CSU', 4.5, 3.0, 'other', 'r'), ('NOW', 1.8, 3.0, 'other', 'r'),
    ('HUBS', 2.6, 1.0, 'other', 'r'), ('IT', 8.9, 1.0, 'trap', 'r'), ('DBX', 7.5, 1.0, 'trap', 'l'), ('GEN', 7.7, 2.0, 'trap', 'r'),
]
svg = [f'<svg aria-label="Scatter of owner FCF yield against durability score" style="position:absolute;left:0;top:0" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
zx, zy = X(7), Y(2.4)
svg.append(f'<rect x="{zx:.1f}" y="{T}" width="{R - zx:.1f}" height="{zy - T:.1f}" fill="#E4ECF5"/>')
for v in (4, 8, 12):
    svg.append(f'<line x1="{X(v):.1f}" y1="{T}" x2="{X(v):.1f}" y2="{B}" stroke="{LINE}" stroke-width="2"/>')
for s in (1, 2, 3, 4):
    svg.append(f'<line x1="{L}" y1="{Y(s):.1f}" x2="{R}" y2="{Y(s):.1f}" stroke="{LINE}" stroke-width="2"/>')
svg.append(f'<line x1="{L}" y1="{B}" x2="{R}" y2="{B}" stroke="{INK}" stroke-width="2"/>')
svg.append(f'<line x1="{L}" y1="{T}" x2="{L}" y2="{B}" stroke="{INK}" stroke-width="2"/>')
for t, x, y, k, side in pts:
    cx, cy = X(x), Y(y)
    if k == 'pick':
        svg.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="12" fill="{BLUE}"/>')
    elif k == 'deck':
        svg.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="10" fill="#F7F5F0" stroke="{BLUE}" stroke-width="4"/>')
    elif k == 'trap':
        svg.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="10" fill="{ORANGE}"/>')
    else:
        svg.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="10" fill="{GRAY}"/>')
svg.append('</svg>')
labels = []
for t, x, y, k, side in pts:
    cx, cy = X(x), Y(y)
    color = BLUE if k in ('pick', 'deck') else (ORANGE if k == 'trap' else '#3D4A57')
    weight = '700' if k == 'pick' else '600'
    w = 110
    if side == 'r':
        lx, align = cx + 16, 'left'
    else:
        lx, align = cx - 16 - w, 'right'
    labels.append(f'<p style="position:absolute;left:{lx:.0f}px;top:{cy - 40:.0f}px;width:{w}px;font-size:24px;font-weight:{weight};color:{color};text-align:{align}">{t}</p>')
ticks = []
for v in (0, 4, 8, 12):
    ticks.append(f'<p style="position:absolute;left:{X(v) - 40:.0f}px;top:{B + 8}px;width:80px;font-size:24px;color:#5F6B76;text-align:center">{v}%</p>')
for s in (0, 2, 4):
    ticks.append(f'<p style="position:absolute;left:0px;top:{Y(s) - 17:.0f}px;width:60px;font-size:24px;color:#5F6B76;text-align:right">{s}</p>')
titles = [
    f'<p style="position:absolute;left:{L}px;top:{B + 48}px;width:{R - L}px;font-size:24px;color:#3D4A57;text-align:center">Owner FCF yield: FCF minus stock comp, as % of market cap</p>',
    f'<p style="position:absolute;left:0px;top:0px;width:420px;font-size:24px;color:#3D4A57">Durability score (0–4)</p>',
    f'<p style="position:absolute;left:{zx + 16:.0f}px;top:{T + 8}px;width:300px;font-size:24px;font-weight:600;color:{BLUE}">Buy zone</p>',
]
host = f'<div style="width:{W}px;height:{H + 40}px;position:relative">' + ''.join(svg) + ''.join(titles) + ''.join(ticks) + ''.join(labels) + '</div>'
n_pinned = 1 + len(titles) + len(ticks) + len(labels)
print('pinned children:', n_pinned)
open('gen/screen_host.html', 'w').write(host)
