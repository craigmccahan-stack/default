import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from deep import *

ROOT = os.path.join(HERE, '..', 'decks', 'godaddy')
B = lambda t: f'<b style="color:{INK}">{t}</b>'
S = []

S.append(('cover', cover(dict(name='GoDaddy', ticker='GDDY',
    tagline='A domain toll road with a 10% owner cash yield, priced as if the web were shrinking',
    cover_stats=[('$107', 'Share price, 19 Oct', PAPER), ('$140', 'Base-case value, +31%', '#8DB6E3'),
                 ('10.4%', 'Owner FCF yield', PAPER), ('$13.6B', 'Market cap', PAPER)]))))

body = (f'<div style="display:flex;flex-direction:row;gap:64px;flex:1">'
        f'<div style="flex:1;display:flex;flex-direction:column;gap:24px">{lab("Our thesis", BLUE)}' +
        points([f'{B("Per-share cash compounds.")} FCF per share rose from ~$5.00 in 2021 to ~$11.48 in 2025, about 23% a year.',
                f'{B("The share count keeps falling.")} Diluted shares are down ~30% since 2019, to 127M; over 95% of FCF goes to buybacks.',
                f'{B("The core is durable.")} 81M domains; domains revenue +5%; Applications &amp; Commerce +11% at a ~47% segment margin.',
                f'{B("There is optionality.")} Gen Digital made an unsolicited approach (FT, 24 Sep); an Investor Night on 1 Dec resets targets.']) +
        f'<p style="font-size:28px;font-weight:600;color:{BLUE};background:#E4ECF5;padding:14px 20px">Long, half position. Base case $140 (+31%); bear case $60 (−44%).</p></div>' +
        key_card([('Market cap · EV', '$13.6B · $16.3B'), ('Owner FCF, trailing', '$1.4B'), ('Owner FCF yield', '10.4%'), ('Growth priced in', '0.8% a year')],
                 [('Bear', 60, -44), ('Base', 140, 31), ('Bull', 205, 92)], 107) + '</div>\n')
S.append(('summary', open_slide('summary', 'Investment summary', 'A cash machine priced as if the web were shrinking') + body +
          close_slide('Owner FCF = FCF minus stock comp. Scenarios: 6x, 10x and 14x owner FCF per share. Sources: GoDaddy filings; FT via TIKR.', 2)))

mix = hbars('Q2 2026 revenue, $M', [
    ('Applications &amp; Commerce', 515, '+11% · 47% segment margin', BLUE),
    ('Core: domains', 470, '+5%', BLUE2),
    ('Core: aftermarket', 129, '+9%', BLUE2),
    ('Core: hosting and other', 184, 'rest of Core (+4% in total)', GREY)], lambda v: f'${v:,.0f}M', width=1040, label_w=330, bar_w=300)
kp = ''.join(
    f'<div style="display:flex;flex-direction:column;gap:4px;padding:14px 0;border-bottom:1px solid {LINE}">'
    f'<p style="font-family:{SERIF};font-size:36px;font-weight:600;color:{INK}">{v}</p><p style="font-size:24px;color:{BODY}">{k}</p></div>'
    for v, k in [('81M', 'Domains under management'), ('20.5M', 'Customers, flat year on year'),
                 ('$250', 'Revenue per customer, up 9%'), ('33%', 'Normalised EBITDA margin, up from ~23% in 2021')])
body = (f'<div style="display:flex;flex-direction:row;gap:56px">'
        f'<div style="width:1040px;display:flex;flex-direction:column;gap:36px">{mix}'
        f'<p style="font-size:28px;line-height:1.4;color:{BODY}">{B("Why it is durable:")} a domain is a business’s identity, email address and trust anchor. Renewals are automatic and switching is rare; GoDaddy is the largest registrar.</p></div>'
        f'<div style="flex:1;display:flex;flex-direction:column;background:{CARD};border:1px solid {LINE};padding:28px 32px">{lab("Key operating metrics", BLUE)}{kp}</div></div>\n')
S.append(('business', open_slide('business', 'The business', 'Domains are the toll road; software add-ons drive the margin') + body +
          close_slide('Q2 2026 revenue $1.3B. Core $783M, of which hosting and other derived. Sources: GoDaddy Q2-26 8-K, call highlights.', 3)))

yrs = ['2021', '2022', '2023', '2024', '2025', '2026E']
body = (f'<div style="display:flex;flex-direction:row;gap:64px">' +
        col_chart('Revenue, $B', yrs, [3.82, 4.09, 4.25, 4.57, 4.95, 5.24], lambda v: f'{v:.2f}', colors=[BLUE3]*5 + [BLUE2], height=330, bar=72) +
        col_chart('Free cash flow, $B', yrs, [0.86, 0.97, 1.09, 1.36, 1.61, 1.80], lambda v: f'{v:.2f}', colors=[BLUE]*5 + [BLUE2], height=330, bar=72) +
        '</div>\n' +
        stat_row([('6.5%', 'Revenue CAGR, 2021–26E', None), ('16%', 'FCF CAGR, 2021–26E', None),
                  ('~23%', 'FCF per share CAGR, 2021–25', BLUE), ('−30%', 'Diluted shares since 2019', None)]))
S.append(('history', open_slide('history', 'Track record', 'Revenue grows mid-single digits; cash per share far faster') + body +
          close_slide('2026E = guidance midpoints. FCF as GoDaddy defines it. Sources: GoDaddy 8-Ks and 10-Ks; StockAnalysis.', 4)))

rows = [
    ['AI search kills the small-business website', 'Zero-click Google searches hit 68% in early 2026, up from 60% in 2024; AI Overviews show on 48% of searches. Yet the .com/.net base grew 5.1% (Verisign) and GoDaddy domains revenue +5%.', f'<span style="color:{ORANGE}">The website add-on is at risk; the domain itself is not.</span>'],
    ['AI builders take new customers', 'Lovable reached $500M ARR and Wix’s Base44 $150M, against Airo’s $50M run-rate. GoDaddy’s customer count is flat at 20.5M.', f'<span style="color:{ORANGE}">Real share loss at the top of the funnel; growth now comes from revenue per customer.</span>'],
    ['Promotions show pricing power is gone', 'The $4.99 .com offer cut bookings growth to 3–6%; revenue per customer still +9% and EBITDA margin 33%.', f'<span style="color:{BLUE}">A self-inflicted bookings hit, not a margin problem.</span>'],
    ['Too much debt for a shrinking business', 'Net debt $2.7B, ~1.7x EBITDA; 2026 FCF ~$1.8B; $600M of notes due Dec 2027.', f'<span style="color:{BLUE}">Comfortable: FCF covers net debt in 1.5 years.</span>'],
]
body = table([(340, 'What bears say', 'left'), (None, 'What the data shows', 'left'), (440, 'Our read', 'left')], rows)
body += f'<p style="font-size:28px;line-height:1.4;color:{BODY}">{B("Net:")} AI threatens GoDaddy’s add-ons more than its domains, and at a 10% owner yield slow growth is already priced.</p>'
S.append(('debate', open_slide('debate', 'The bear case', 'Four bear arguments, tested against the numbers') + body + '\n' +
          close_slide('Sources: SparkToro/Similarweb via Search Engine Land; Wells Fargo; Verisign Q2-26; Wix Q2-26; Lovable; GoDaddy filings.', 5)))

def card_list(title, color, items):
    it = ''.join(f'<div style="display:flex;flex-direction:column;gap:4px;padding:14px 0;border-bottom:1px solid {LINE}">'
                 f'<p style="font-family:{SERIF};font-size:36px;font-weight:600;color:{color}">{v}</p><p style="font-size:24px;line-height:1.35;color:{BODY}">{k}</p></div>' for v, k in items)
    return f'<div style="flex:1;display:flex;flex-direction:column;background:{CARD};border:1px solid {LINE};padding:24px 32px">{lab(title, color)}{it}</div>'
body = (f'<div style="display:flex;flex-direction:row;gap:48px">' +
        card_list('Headwinds', ORANGE, [('68%', 'of US Google searches end without a click (Jan–Apr 2026)'),
                                        ('8% vs 15%', 'click-through with and without an AI Overview (Pew)'),
                                        ('$500M', 'ARR at Lovable, an AI-native site builder')]) +
        card_list('Tailwinds', BLUE, [('1M+', '.ai domains registered, ~20x in 5.5 years'),
                                      ('ANS', 'Agent Name Service: identity for AI agents, going to the Linux Foundation'),
                                      ('5x', 'Airo bookings run-rate, $10M to $50M in one quarter')]) + '</div>\n'
        f'<p style="font-size:28px;line-height:1.4;color:{BODY}">{B("Our read:")} agents still need names, certificates and DNS. GoDaddy co-develops agent discovery standards with Cisco, Google, Microsoft and Nvidia, and on 15 Oct opened hosting, email and commerce APIs to AI agents.</p>\n')
S.append(('ai', open_slide('ai', 'AI: threat and opportunity', 'AI cuts both ways for GoDaddy') + body +
          close_slide('Sources: Search Engine Land (SparkToro/Similarweb); Pew; Lovable; webhosting.today; IETF; GoDaddy Q2-26 call, 15 Oct.', 6)))

body = (f'<div style="display:flex;flex-direction:row;gap:64px">' +
        col_chart('Diluted shares, millions', ['2019', '2020', '2021', '2022', '2023', '2024', '2025', 'Q2 26'], [181.7, 168.6, 171.1, 161.5, 151.5, 145.3, 140.6, 127.0],
                  lambda v: f'{v:.0f}', colors=[BLUE3]*7 + [BLUE], height=300, bar=60) +
        col_chart('Buybacks, $B', ['2019', '2020', '2021', '2022*', '2023', '2024', '2025', 'H1 26'], [0.46, 0.54, 0.53, 1.30, 1.27, 0.72, 1.60, 0.83],
                  lambda v: f'{v:.2f}', colors=[BLUE]*8, height=300, bar=60) + '</div>\n' +
        stat_row([('~96%', 'Of 2022–25 FCF spent on buybacks', None), ('$1.33B', 'Authorisation left at June, ~10% of shares at $107', BLUE),
                  ('2.3x', 'FCF per share, 2021 to 2025', None)]))
S.append(('capital', open_slide('capital', 'Capital return', 'Nearly all free cash flow goes to buying back stock') + body +
          close_slide('*2022 buyback spans Jan 2022 to Jan 2023 per the company. Sources: GoDaddy 10-Ks and 10-Q (Jun 2026).', 7)))

pf = hbars('Price to free cash flow, 10 years', [('10-year high', 33.0, '', GREY), ('10-year median', 17.4, '', GREY),
                                                 ('10-year low', 6.4, '', BLUE3), ('Today (2026 guide)', 7.5, '', BLUE)],
           lambda v: f'{v:.1f}x', width=720, label_w=260, bar_w=330)
sc = table([(110, 'Case', 'left'), (None, 'Assumption', 'left'), (100, 'Multiple', 'right'), (120, 'Value', 'right'), (110, 'vs price', 'right')], [
    ['Bear', 'AI erodes add-ons; owner FCF falls 15%', '6x', '$60', f'<span style="color:{ORANGE}">−44%</span>'],
    ['Base', '2027E FCF ~$1.95B less $0.34B stock comp', '10x', '$140', f'<span style="color:{BLUE}">+31%</span>'],
    ['Bull', 'A&amp;C re-accelerates; buybacks continue', '14x', '$205', f'<span style="color:{BLUE}">+92%</span>'],
])
body = (f'<div style="display:flex;flex-direction:row;gap:64px">'
        f'<div style="width:720px;display:flex;flex-direction:column;gap:20px">{pf}'
        f'<p style="font-size:24px;line-height:1.4;color:{BODY}">GuruFocus data. EV/FCF is ~9x, less than half its 10-year median. Gen Digital’s reported approach was valued at about $12B.</p></div>'
        f'<div style="flex:1;display:flex;flex-direction:column;gap:20px">{lab("Scenarios on 2027E owner FCF per share")}{sc}'
        f'<p style="font-size:28px;line-height:1.4;color:{BODY}">{B("What the price implies:")} 0.8% perpetual growth in owner FCF at a 9.5% discount rate. Probability-weighted value (25/50/25): {B("$136, +28%")}.</p></div></div>\n')
S.append(('valuation', open_slide('valuation', 'Valuation', 'Near the cheapest it has been in a decade') + body +
          close_slide('Owner FCF per share: base $14.0 (2027E), bear $10.0, bull $14.9. Sources: GuruFocus (Oct 2026), consensus, our estimates.', 8)))

cal = [('29 Oct', 'Q3 2026 results, after the close'),
       ('1 Dec', 'Investor Night in Tempe: AI strategy and refreshed financial targets'),
       ('Open', 'Outcome of Gen Digital’s unsolicited approach'),
       ('Pending', 'Securities class action: lead plaintiff named after the 20 Oct deadline'),
       ('2027', 'New buyback authorisation; refinancing of 2027 notes')]
cl = ''.join(f'<div style="display:flex;flex-direction:row;gap:24px;padding:14px 0;border-bottom:1px solid {LINE}"><p style="width:140px;font-size:24px;font-weight:600;color:{BLUE}">{d}</p><p style="flex:1;font-size:24px;line-height:1.35;color:{BODY}">{e}</p></div>' for d, e in cal)
st = table([(None, 'Broker', 'left'), (240, 'Rating', 'left'), (120, 'Target', 'right')], [
    ['Wells Fargo', 'Underweight', '$76'], ['Cantor Fitzgerald', 'Neutral', '$90'], ['RBC (12 Oct)', 'Sector Perform', '$95'],
    ['Citi', 'Buy', '$105'], ['Baird', 'Outperform', '$120'], ['StoneX', 'Buy', '$140']])
body = (f'<div style="display:flex;flex-direction:row;gap:64px">'
        f'<div style="flex:1;display:flex;flex-direction:column;gap:8px">{lab("Catalyst calendar", BLUE)}{cl}</div>'
        f'<div style="width:680px;display:flex;flex-direction:column;gap:12px">{lab("The Street is split")}{st}'
        f'<p style="font-size:24px;line-height:1.4;color:{BODY}">RBC cut to Sector Perform on AI risk after a 38% rebound from the June low. Average target ~$107, about today’s price.</p></div></div>\n')
S.append(('catalysts', open_slide('catalysts', 'Catalysts', 'Three near-term triggers: Q3, Investor Night and Gen Digital') + body +
          close_slide('Sources: GoDaddy (Q3 date, 15 Oct release); FT via TIKR; RBC via Investing.com and Seeking Alpha; MarketBeat.', 9)))

rk = table([(400, 'Risk', 'left'), (None, 'What we watch', 'left'), (440, 'We would sell if', 'left')], [
    ['AI takes the website and marketing add-ons', 'Applications &amp; Commerce bookings (+7% in Q2)', 'A&amp;C growth falls below 5%'],
    ['Domain pricing weakens', 'Promotions; domains revenue growth (+5%)', 'Domains revenue declines'],
    ['The customer base shrinks', 'Customers (20.5M, flat)', 'Customers fall more than 3% a year'],
    ['Leverage meets higher rates', '2027 refinancing; net debt to EBITDA (~1.7x)', 'Leverage rises above 3x'],
    ['A value-destroying deal', 'Terms of any Gen Digital transaction', 'A mostly-stock deal at or below today’s price'],
])
body = rk + (f'\n<p style="font-size:28px;line-height:1.4;color:{BODY}">{B("Pre-mortem:")} if this fails, it will be because AI agents made the small-business website, and the add-ons around it, optional.</p>\n')
S.append(('risks', open_slide('risks', 'Risks', 'What would make us wrong, and when we would sell') + body +
          close_slide('For discussion only; not investment advice. Thresholds are our own.', 10)))

print(write_deck(ROOT, 'GoDaddy Deep Dive', S, {
    's1': {'description': 'Cover and investment summary', 'start': 'cover'},
    's2': {'description': 'The business and its track record', 'start': 'business'},
    's3': {'description': 'The bear case and the AI question', 'start': 'debate'},
    's4': {'description': 'Capital return, valuation, catalysts and risks', 'start': 'capital'}}))
