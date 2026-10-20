"""Generates the one-page idea slides for the main deck from a dict spec."""
import json, sys
INK, BODY, MUTED, BLUE, ORANGE, LINE, CARD = '#14202B', '#3D4A57', '#5F6B76', '#1F5C99', '#A9521A', '#E3DED3', '#FDFBF6'
SERIF = "'Source Serif 4', Georgia, serif"

def fmt(p):
    return ('+' if p >= 0 else '\u2212') + f'{abs(p):.0f}%'

def label(t, color=MUTED):
    return f'<p style="font-size:24px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{color}">{t}</p>'

def slide(d):
    pts = ''.join(
        f'<div style="display:flex;flex-direction:row;gap:20px;align-items:flex-start">'
        f'<p style="width:44px;height:44px;border-radius:50%;background:{BLUE};color:#F7F5F0;font-size:24px;font-weight:600;text-align:center;line-height:1.8">{i+1}</p>'
        f'<p style="flex:1;font-size:28px;line-height:1.4;color:{BODY}">{t}</p></div>'
        for i, t in enumerate(d['view']))
    rows = ''.join(
        f'<div style="display:flex;flex-direction:row;justify-content:space-between;align-items:baseline;padding:8px 0;border-bottom:1px solid {LINE}">'
        f'<p style="font-size:24px;color:{MUTED}">{k}</p><p style="font-size:28px;font-weight:600;color:{INK};font-variant-numeric:tabular-nums">{v}</p></div>'
        for k, v in d['keys'])
    # scenario bars: scale to bull value
    px = d['price']; vmax = max(v for _, v, _ in d['scen']) * 1.0
    W = 220
    scen = ''
    for name, v, pct in d['scen']:
        col = ORANGE if name == 'Bear' else (BLUE if name == 'Base' else '#6F95C2')
        w = round(v / vmax * W)
        scen += (f'<div style="display:flex;flex-direction:row;align-items:center;gap:16px;padding:6px 0">'
                 f'<p style="width:64px;font-size:24px;color:{MUTED}">{name}</p>'
                 f'<div style="width:{W}px;display:flex;flex-direction:row"><div style="width:{w}px;height:32px;background:{col}"></div></div>'
                 f'<p style="flex:1;font-size:28px;font-weight:600;color:{INK};text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums">${v:,.0f} <span style="color:{ORANGE if pct < 0 else BLUE}">{fmt(pct)}</span></p></div>')
    mx = 64 + 16 + round(px / vmax * W)
    marker = (f'<div style="position:absolute;left:{mx}px;top:-8px;width:3px;height:154px;background:{INK}"></div>'
              f'<p style="position:absolute;left:{mx - 90}px;top:150px;width:180px;font-size:24px;color:{INK};text-align:center">Price ${px:,.0f}</p>')
    return f'''<section id="{d['id']}" data-transition="fade" style="background:#F7F5F0;color:{INK};font-family:'IBM Plex Sans', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;gap:40px">
<div style="display:flex;flex-direction:column;gap:16px">
<p style="font-size:24px;font-weight:600;letter-spacing:3px;text-transform:uppercase;color:{BLUE}">{d['eyebrow']}</p>
<h2 style="font-family:{SERIF};font-size:56px;font-weight:600;line-height:1.12;letter-spacing:-0.5px;color:{INK}">{d['title']}</h2>
</div>
<div style="display:flex;flex-direction:row;gap:64px;flex:1">
<div style="flex:1;display:flex;flex-direction:column;gap:28px">
<div style="display:flex;flex-direction:column;gap:8px">{label('The debate')}<p style="font-size:28px;line-height:1.4;color:{BODY}">{d['debate']}</p></div>
<div style="display:flex;flex-direction:column;gap:16px">{label('Our view', BLUE)}{pts}</div>
<div style="display:flex;flex-direction:column;gap:8px">{label('We are wrong if', ORANGE)}<p style="font-size:28px;line-height:1.4;color:{BODY}">{d['wrong']}</p></div>
</div>
<div style="width:560px;display:flex;flex-direction:column;gap:24px;background:{CARD};border:1px solid {LINE};padding:32px">
<div style="display:flex;flex-direction:column;gap:4px">{label('Key numbers')}{rows}</div>
<div style="display:flex;flex-direction:column;gap:8px">{label('Scenarios, 12–18 months')}<div style="position:relative;display:flex;flex-direction:column">{scen}{marker}</div></div>
</div>
</div>
<p style="position:absolute;left:128px;bottom:64px;width:1500px;font-size:24px;color:{MUTED}">{d['foot']}</p>
<p style="position:absolute;right:128px;bottom:64px;width:80px;font-size:24px;color:{MUTED};text-align:right">{d['page']}</p>
</section>
'''

if __name__ == '__main__':
    specs = json.load(open(sys.argv[1]))
    for d in specs:
        open(f"{sys.argv[2]}/{d['id']}.html", 'w').write(slide(d))
        print('wrote', d['id'])
