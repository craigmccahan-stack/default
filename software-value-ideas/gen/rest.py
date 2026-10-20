INK, BODY, MUTED, BLUE, ORANGE, LINE, CARD = '#14202B', '#3D4A57', '#5F6B76', '#1F5C99', '#A9521A', '#E3DED3', '#FDFBF6'
SERIF = "'Source Serif 4', Georgia, serif"
def head(sid, eyebrow, title, gap=40):
    return f'''<section id="{sid}" data-transition="fade" style="background:#F7F5F0;color:{INK};font-family:'IBM Plex Sans', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;gap:{gap}px">
<div style="display:flex;flex-direction:column;gap:16px">
<p style="font-size:24px;font-weight:600;letter-spacing:3px;text-transform:uppercase;color:{BLUE}">{eyebrow}</p>
<h2 style="font-family:{SERIF};font-size:56px;font-weight:600;line-height:1.12;letter-spacing:-0.5px;color:{INK}">{title}</h2>
</div>
'''
def foot(src, page):
    return (f'<p style="position:absolute;left:128px;bottom:64px;width:1500px;font-size:24px;color:{MUTED}">{src}</p>\n'
            f'<p style="position:absolute;right:128px;bottom:64px;width:80px;font-size:24px;color:{MUTED};text-align:right">{page}</p>\n</section>\n')
def lab(t, color=MUTED):
    return f'<p style="font-size:24px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{color}">{t}</p>'

# ---------- Slide 8: on deck ----------
def card(name, tkr, px, stats, like, wait, entry):
    st = ''.join(f'<div style="flex:1;display:flex;flex-direction:column;gap:4px"><p style="font-family:{SERIF};font-size:36px;font-weight:600;line-height:1.1;color:{INK}">{v}</p><p style="font-size:24px;color:{MUTED}">{k}</p></div>' for k, v in stats)
    return f'''<div style="flex:1;display:flex;flex-direction:column;gap:20px;background:{CARD};border:1px solid {LINE};padding:32px">
<div style="display:flex;flex-direction:row;justify-content:space-between;align-items:baseline"><p style="font-family:{SERIF};font-size:36px;font-weight:600;color:{INK}">{name} <span style="color:{MUTED}">{tkr}</span></p><p style="font-size:28px;font-weight:600;color:{INK}">{px}</p></div>
<div style="display:flex;flex-direction:row;gap:24px;border-top:1px solid {LINE};border-bottom:1px solid {LINE};padding:16px 0">{st}</div>
<p style="font-size:28px;line-height:1.4;color:{BODY}"><b style="color:{BLUE}">Why we like it.</b> {like}</p>
<p style="font-size:28px;line-height:1.4;color:{BODY}"><b style="color:{ORANGE}">Why we wait.</b> {wait}</p>
<div style="flex:1"></div>
<p style="font-size:28px;font-weight:600;color:{BLUE};background:#E4ECF5;padding:12px 20px">{entry}</p>
</div>'''
s8 = head('ondeck', 'On deck', 'FactSet and Salesforce: good businesses, not yet cheap enough', gap=36)
s8 += '<div style="display:flex;flex-direction:row;gap:48px">'
s8 += card('FactSet', 'FDS', '$303', [('Owner FCF yield', '6.1%'), ('Growth priced in', '3.8%'), ('Net debt', '~$1.2B')],
           'Record $86M net new ASV in Q4, &gt;95% retention, AI ASV doubled, ~7% fewer shares.',
           'Per-seat pricing; FY27 organic ASV guided to 5–6.5%.',
           'Buy below ~$250, an ~8% forward owner yield')
s8 += card('Salesforce', 'CRM', '$242', [('Owner FCF yield', '5.7%'), ('Growth priced in', '4.3%'), ('Net debt', '~$30B')],
           'Agentforce ARR above $1.5B (+240%), cRPO +14%, a 34% margin, and 14% fewer shares.',
           '~6–7% organic growth, ~$30B of debt-funded buybacks, and pricey M&amp;A.',
           'Buy below ~$195, a 7% forward owner yield')
s8 += '</div>\n'
s8 += f'<p style="font-size:24px;line-height:1.4;color:{BODY};border-left:4px solid {INK};padding:4px 0 4px 24px"><b style="color:{INK}">Also watching Workday:</b> Silver Lake talks reported 13 Aug at ~$224/share (~15x FY28 FCF); no deal announced as of 19 Oct.</p>\n'
s8 += foot('Prices at 19 Oct; both rose 7–12% from 6 Oct. Forward owner yield = FY27 FCF minus stock comp. Sources: company 8-Ks; Reuters.', 8)
open('decks/main/project/slides/ondeck.html', 'w').write(s8)

# ---------- Slide 9: traps ----------
rows = [
 ('HubSpot', 'HUBS', '12.6x EV/FCF', 'Stock comp is ~13% of revenue and absorbs most of FCF; seat-priced SMB CRM; growth slowing to 14%', 'Owner FCF margin above 10%'),
 ('monday.com', 'MNDY', '~8x EV/FCF', 'Per-seat work management sits in agents’ path; growth slowing from 22% to 16–17%', 'AI credits offset seat losses'),
 ('Dropbox', 'DBX', '9x EV/FCF', 'Revenue is flat; the 18% share-count cut was funded with $2.25B of net debt', 'A return to growth'),
 ('Gartner', 'IT', '~9% owner yield', 'Contract value +1.7%: research seats are among the easiest work for LLMs to replace', 'Contract value growth above 5%'),
 ('Fair Isaac', 'FICO', '19x peak EPS', 'The housing regulator ended its mortgage-score pricing power; −27% on 29 Sep', 'Clarity on the GSE pricing grid'),
 ('Gen Digital', 'GEN', '~8% owner yield', 'Net leverage of 3x; recent growth bought with MoneyLion; consumer churn', 'Net leverage below 2x'),
]
cols = [(300, 'Company'), (230, 'Looks cheap on'), (720, 'Why we pass'), (414, 'What would change our mind')]
hdr = ''.join(f'<p style="width:{w}px;font-size:24px;font-weight:600;color:{MUTED}">{t}</p>' for w, t in cols)
body = ''
for n, t, cheap, why, change in rows:
    body += (f'<div style="display:flex;flex-direction:row;align-items:center;padding:14px 0;border-bottom:1px solid {LINE}">'
             f'<p style="width:300px;font-size:28px;font-weight:600;color:{INK}">{n} <span style="font-weight:400;color:{MUTED};font-size:24px">{t}</span></p>'
             f'<p style="width:230px;font-size:24px;color:{INK};font-variant-numeric:tabular-nums">{cheap}</p>'
             f'<p style="width:720px;font-size:24px;line-height:1.35;color:{BODY};padding:0 32px 0 0">{why}</p>'
             f'<p style="width:414px;font-size:24px;line-height:1.35;color:{BODY}">{change}</p></div>')
s9 = head('traps', 'Value traps', 'Cheap for a reason: names that fail our tests')
s9 += f'<div style="display:flex;flex-direction:column"><div style="display:flex;flex-direction:row;padding:0 0 12px 0;border-bottom:2px solid {INK}">{hdr}</div>{body}</div>\n'
s9 += foot('Multiples at 6 Oct prices, on trailing or guided FCF. Sources: company filings (Q2 2026); Forbes (FICO, 30 Sep); Gen Digital.', 9)
open('decks/main/project/slides/traps.html', 'w').write(s9)

# ---------- Slide 10: risks & catalysts ----------
risks = [
 ('AI substitution speeds up', 'Net new ARR, paid seats, TurboTax units', 'ADBE, INTU'),
 ('Rates keep rising', '10-year above 5.5%; another Fed hike', 'All; GDDY most'),
 ('Leadership change misfires', 'New CEO’s FY27 plan; permanent CFO', 'ADBE'),
 ('TurboTax keeps losing share', '2027 tax-season unit data', 'INTU'),
 ('Bookings and FCF quality', 'Bookings vs revenue growth; class action', 'GDDY'),
]
rk = ''.join(
    f'<div style="display:flex;flex-direction:row;align-items:center;padding:14px 0;border-bottom:1px solid {LINE}">'
    f'<p style="width:320px;font-size:24px;font-weight:600;color:{INK};padding:0 16px 0 0">{a}</p>'
    f'<p style="width:440px;font-size:24px;color:{BODY};padding:0 24px 0 0">{b}</p>'
    f'<p style="flex:1;font-size:24px;color:{ORANGE};font-weight:600">{c}</p></div>' for a, b, c in risks)
cal = [('28 Oct', 'Fed decision'), ('29 Oct', 'GoDaddy Q3 results'), ('10–12 Nov', 'Adobe MAX, Miami Beach'), ('~19 Nov', 'Intuit Q1 FY27 results'),
       ('1 Dec', 'Adobe CEO handover; GoDaddy Investor Night'), ('Mid-Dec', 'Adobe Q4 and first FY27 guide'), ('Jan–Apr', 'First AI-native TurboTax season')]
cl = ''.join(f'<div style="display:flex;flex-direction:row;gap:20px;padding:10px 0;border-bottom:1px solid {LINE}"><p style="width:150px;font-size:24px;font-weight:600;color:{BLUE}">{d}</p><p style="flex:1;font-size:24px;color:{BODY}">{e}</p></div>' for d, e in cal)
s10 = head('risks', 'Risks and catalysts', 'What could go wrong, and when we will know')
s10 += f'''<div style="display:flex;flex-direction:row;gap:64px">
<div style="flex:1;display:flex;flex-direction:column">
<div style="display:flex;flex-direction:row;padding:0 0 12px 0;border-bottom:2px solid {INK}"><p style="width:320px;font-size:24px;font-weight:600;color:{MUTED}">Risk</p><p style="width:440px;font-size:24px;font-weight:600;color:{MUTED}">Signpost</p><p style="flex:1;font-size:24px;font-weight:600;color:{MUTED}">Most exposed</p></div>
{rk}
<p style="font-size:28px;line-height:1.4;color:{BODY};padding:20px 0 0 0"><b style="color:{INK}">How we would build it:</b> Adobe at full weight. Intuit at half after its October rally, adding below $300; GoDaddy at half, given its leverage. Hedge sector beta with IGV if needed.</p>
</div>
<div style="width:560px;display:flex;flex-direction:column;gap:8px;background:{CARD};border:1px solid {LINE};padding:32px">
{lab('Catalyst calendar')}
{cl}
</div>
</div>
'''
s10 += foot('GoDaddy Q3 date confirmed; Intuit Q1 and Adobe Q4 dates follow prior-year timing. Not investment advice.', 10)
open('decks/main/project/slides/risks.html', 'w').write(s10)
print('ok')
