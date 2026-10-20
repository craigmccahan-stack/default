"""Slide components + builder for the single-stock deep-dive decks (Slides artifact type format)."""
import json, os, sys

INK, BODY, MUTED, BLUE, BLUE2, BLUE3, ORANGE, LINE, CARD, PAPER, GREY = (
    '#14202B', '#3D4A57', '#5F6B76', '#1F5C99', '#6F95C2', '#A9BCD6', '#A9521A', '#E3DED3', '#FDFBF6', '#F7F5F0', '#9AA8B5')
SERIF = "'Source Serif 4', Georgia, serif"
SANS = "'IBM Plex Sans', Arial, sans-serif"


def esc(t):
    return t


def lab(t, color=MUTED):
    return f'<p style="font-size:24px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{color}">{t}</p>'


def open_slide(sid, eyebrow, title, gap=40):
    return (f'<section id="{sid}" data-transition="fade" style="background:{PAPER};color:{INK};font-family:{SANS};'
            f'padding:128px 128px 160px;display:flex;flex-direction:column;gap:{gap}px">\n'
            f'<div style="display:flex;flex-direction:column;gap:16px">\n'
            f'<p style="font-size:24px;font-weight:600;letter-spacing:3px;text-transform:uppercase;color:{BLUE}">{eyebrow}</p>\n'
            f'<h2 style="font-family:{SERIF};font-size:56px;font-weight:600;line-height:1.12;letter-spacing:-0.5px;color:{INK}">{title}</h2>\n</div>\n')


def close_slide(src, page):
    return (f'<p style="position:absolute;left:128px;bottom:64px;width:1500px;font-size:24px;color:{MUTED}">{src}</p>\n'
            f'<p style="position:absolute;right:128px;bottom:64px;width:80px;font-size:24px;color:{MUTED};text-align:right">{page}</p>\n</section>\n')


def fmt_pct(p):
    return ('+' if p >= 0 else '−') + f'{abs(p):.0f}%'


def points(items, size=28, gap=20):
    out = ''
    for i, t in enumerate(items):
        out += (f'<div style="display:flex;flex-direction:row;gap:20px;align-items:flex-start">'
                f'<p style="width:44px;height:44px;border-radius:50%;background:{BLUE};color:{PAPER};font-size:24px;font-weight:600;text-align:center;line-height:1.8">{i+1}</p>'
                f'<p style="flex:1;font-size:{size}px;line-height:1.4;color:{BODY}">{t}</p></div>')
    return f'<div style="display:flex;flex-direction:column;gap:{gap}px">{out}</div>'


def key_card(rows, scen, price, width=560, title='Key numbers'):
    r = ''.join(
        f'<div style="display:flex;flex-direction:row;justify-content:space-between;align-items:baseline;padding:8px 0;border-bottom:1px solid {LINE}">'
        f'<p style="font-size:24px;color:{MUTED}">{k}</p><p style="font-size:28px;font-weight:600;color:{INK};font-variant-numeric:tabular-nums">{v}</p></div>'
        for k, v in rows)
    W = 220
    vmax = max(v for _, v, _ in scen)
    s = ''
    for name, v, pct in scen:
        col = ORANGE if name == 'Bear' else (BLUE if name == 'Base' else BLUE2)
        w = round(v / vmax * W)
        s += (f'<div style="display:flex;flex-direction:row;align-items:center;gap:16px;padding:6px 0">'
              f'<p style="width:64px;font-size:24px;color:{MUTED}">{name}</p>'
              f'<div style="width:{W}px;display:flex;flex-direction:row"><div style="width:{w}px;height:32px;background:{col}"></div></div>'
              f'<p style="flex:1;font-size:28px;font-weight:600;color:{INK};text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums">${v:,.0f} '
              f'<span style="color:{ORANGE if pct < 0 else BLUE}">{fmt_pct(pct)}</span></p></div>')
    mx = 64 + 16 + round(price / vmax * W)
    marker = (f'<div style="position:absolute;left:{mx}px;top:-8px;width:3px;height:154px;background:{INK}"></div>'
              f'<p style="position:absolute;left:{mx - 90}px;top:150px;width:180px;font-size:24px;color:{INK};text-align:center">Price ${price:,.0f}</p>')
    return (f'<div style="width:{width}px;display:flex;flex-direction:column;gap:24px;background:{CARD};border:1px solid {LINE};padding:32px">'
            f'<div style="display:flex;flex-direction:column;gap:4px">{lab(title)}{r}</div>'
            f'<div style="display:flex;flex-direction:column;gap:8px">{lab("Scenarios, 12–18 months")}'
            f'<div style="position:relative;display:flex;flex-direction:column">{s}{marker}</div></div></div>')


def col_chart(title, labels, values, fmt, colors=None, height=300, bar=64, note=None, width=None):
    """Single-series column chart built from divs; bars share one baseline."""
    vmax = max(values)
    cols = ''
    for i, (l, v) in enumerate(zip(labels, values)):
        c = (colors[i] if colors else BLUE)
        h = max(2, round(v / vmax * (height - 44)))
        cols += (f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:6px">'
                 f'<p style="font-size:24px;font-weight:600;color:{INK};white-space:nowrap;font-variant-numeric:tabular-nums">{fmt(v)}</p>'
                 f'<div style="width:{bar}px;height:{h}px;background:{c}"></div></div>')
    xl = ''.join(f'<p style="flex:1;font-size:24px;color:{MUTED};text-align:center">{l}</p>' for l in labels)
    w = f'width:{width}px;' if width else 'flex:1;'
    nt = f'<p style="font-size:24px;line-height:1.4;color:{MUTED}">{note}</p>' if note else ''
    return (f'<div style="{w}display:flex;flex-direction:column;gap:12px">{lab(title)}'
            f'<div style="display:flex;flex-direction:row;align-items:flex-end;gap:8px;height:{height}px;border-bottom:2px solid {INK}">{cols}</div>'
            f'<div style="display:flex;flex-direction:row;gap:8px">{xl}</div>{nt}</div>')


def hbars(title, items, fmt, width=None, label_w=360, bar_w=420):
    """items: (label, value, side_text, color)"""
    vmax = max(v for _, v, _, _ in items)
    rows = ''
    for l, v, side, c in items:
        w = max(4, round(v / vmax * bar_w))
        rows += (f'<div style="display:flex;flex-direction:row;align-items:center;gap:16px;padding:10px 0;border-bottom:1px solid {LINE}">'
                 f'<p style="width:{label_w}px;font-size:24px;font-weight:600;color:{INK}">{l}</p>'
                 f'<div style="width:{bar_w}px;display:flex;flex-direction:row;align-items:center;gap:12px"><div style="width:{w}px;height:32px;background:{c}"></div>'
                 f'<p style="font-size:24px;font-weight:600;color:{INK};white-space:nowrap;font-variant-numeric:tabular-nums">{fmt(v)}</p></div>'
                 f'<p style="flex:1;font-size:24px;color:{BODY}">{side}</p></div>')
    w = f'width:{width}px;' if width else 'flex:1;'
    return f'<div style="{w}display:flex;flex-direction:column;gap:8px">{lab(title)}{rows}</div>'


def stat_row(stats, size=56):
    cells = ''.join(
        f'<div style="flex:1;display:flex;flex-direction:column;gap:6px;border-top:2px solid {INK};padding:16px 0 0 0">'
        f'<p style="font-family:{SERIF};font-size:{size}px;font-weight:600;line-height:1.05;color:{c if c else INK}">{v}</p>'
        f'<p style="font-size:24px;line-height:1.35;color:{BODY}">{k}</p></div>'
        for v, k, c in stats)
    return f'<div style="display:flex;flex-direction:row;gap:40px">{cells}</div>'


def table(cols, rows, size=24, first_bold=True, head_color=MUTED, zebra=False):
    """cols: [(width or None for flex, header, align)], rows: list of cell strings."""
    def cell(w, a, t, bold=False, color=BODY, pad_r=24):
        ws = f'width:{w}px;' if w else 'flex:1;'
        fw = 'font-weight:600;' if bold else ''
        return f'<p style="{ws}font-size:{size}px;line-height:1.35;{fw}color:{color};text-align:{a};padding:0 {pad_r}px 0 0">{t}</p>'
    hdr = ''.join(cell(w, a, h, True, head_color) for w, h, a in cols)
    body = ''
    for r in rows:
        cells = ''
        for i, ((w, h, a), t) in enumerate(zip(cols, r)):
            cells += cell(w, a, t, bold=(first_bold and i == 0), color=(INK if i == 0 else BODY))
        body += f'<div style="display:flex;flex-direction:row;align-items:center;padding:14px 0;border-bottom:1px solid {LINE}">{cells}</div>'
    return (f'<div style="display:flex;flex-direction:column"><div style="display:flex;flex-direction:row;align-items:flex-end;padding:0 0 12px 0;border-bottom:2px solid {INK}">{hdr}</div>{body}</div>')


def cover(d):
    stats = ''.join(
        f'<div style="flex:1;display:flex;flex-direction:column;gap:6px;border-top:1px solid #3A4A5A;padding:20px 0 0 0">'
        f'<p style="font-family:{SERIF};font-size:56px;font-weight:600;line-height:1.05;color:{c}">{v}</p>'
        f'<p style="font-size:24px;color:#B9C4CF">{k}</p></div>' for v, k, c in d['cover_stats'])
    return (f'<section id="cover" data-transition="fade" style="background:{INK};color:{PAPER};font-family:{SANS};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:space-between">\n'
            f'<p style="font-size:24px;font-weight:600;letter-spacing:4px;text-transform:uppercase;color:#8DB6E3">Equity research · Software · Deep dive · Long</p>\n'
            f'<div style="display:flex;flex-direction:column;gap:28px">'
            f'<h1 style="font-family:{SERIF};font-size:120px;font-weight:600;line-height:1.05;letter-spacing:-2px;color:{PAPER}">{d["name"]} <span style="color:#8DB6E3">{d["ticker"]}</span></h1>'
            f'<p style="font-size:36px;line-height:1.35;color:#B9C4CF;width:1400px">{d["tagline"]}</p></div>\n'
            f'<div style="display:flex;flex-direction:row;gap:48px">{stats}</div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1664px;font-size:24px;color:#9AA8B5">20 October 2026 · Prices as of the 19 October 2026 close · For discussion only, not investment advice</p>\n</section>\n')


def deck_json(title, order, sections):
    return json.dumps({"v": 4, "createdOnFiles": {"v": 1, "at": "2026-10-07T13:30:00Z"}, "lists": "css", "title": title, "order": order,
                       "sections": sections,
                       "faces": {"source-serif-4": {"family": "Source Serif 4", "href": "https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400..700&display=swap"},
                                 "ibm-plex-sans": {"family": "IBM Plex Sans", "href": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400..700&display=swap"}},
                       "designSystems": []}, ensure_ascii=False)


def write_deck(root, title, slides, sections):
    os.makedirs(os.path.join(root, 'project/slides'), exist_ok=True)
    order = [sid for sid, _ in slides]
    open(os.path.join(root, 'project/deck.json'), 'w').write(deck_json(title, order, sections) + '\n')
    for sid, html in slides:
        open(os.path.join(root, 'project/slides', f'{sid}.html'), 'w').write(html)
    return order
