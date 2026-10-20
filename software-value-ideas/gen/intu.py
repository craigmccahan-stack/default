import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from deep import *

ROOT = os.path.join(HERE, '..', 'decks', 'intuit')
B = lambda t: f'<b style="color:{INK}">{t}</b>'
S = []

S.append(('cover', cover(dict(name='Intuit', ticker='INTU',
    tagline='The small-business ledger at 10x free cash flow, priced as if AI ends its growth',
    cover_stats=[('$326', 'Share price, 19 Oct', PAPER), ('$400', 'Base-case value, +23%', '#8DB6E3'),
                 ('7.6%', 'Owner FCF yield', PAPER), ('$87B', 'Market cap', PAPER)]))))

body = (f'<div style="display:flex;flex-direction:row;gap:64px;flex:1">'
        f'<div style="flex:1;display:flex;flex-direction:column;gap:24px">{lab("Our thesis", BLUE)}' +
        points([f'{B("The engine is QuickBooks, not TurboTax.")} The business platform is 54% of revenue and grew 18%; QBO Accounting +23%.',
                f'{B("TurboTax shrinks in units, not dollars.")} Units −2% to 39.0M, revenue +7%; assisted TurboTax Live is 53% of it.',
                f'{B("Margins are stepping up.")} A 17% workforce cut lifts the FY27 GAAP operating margin to ~32%, up 440bp.',
                f'{B("Priced for 1.8% growth forever,")} against guidance of 9–10% revenue growth and high-teens EPS growth.']) +
        f'<p style="font-size:28px;font-weight:600;color:{BLUE};background:#E4ECF5;padding:14px 20px">Long, half size; add below $300. Base $400 (+23%); bear $210 (−36%).</p></div>' +
        key_card([('Market cap · EV', '$87B · $88B'), ('Owner FCF, FY26', '$6.6B'), ('Owner FCF yield', '7.6%'), ('Growth priced in', '1.8% a year')],
                 [('Bear', 210, -36), ('Base', 400, 23), ('Bull', 525, 61)], 326) + '</div>\n')
S.append(('summary', open_slide('summary', 'Investment summary', 'A best-in-class platform at a distressed multiple') + body +
          close_slide('Owner FCF = FCF minus stock comp. Scenarios: 10x, 17x and 21x owner FCF per share. Sources: Intuit FY26 8-K and 10-K.', 2)))

mix = hbars('FY26 revenue by segment, $B', [
    ('Global Business Solutions', 12.9, '+16% · QBO Online Ecosystem $9.9B, +19%', BLUE),
    ('TurboTax', 5.3, '+7% · Live (assisted) ~53%', BLUE2),
    ('Credit Karma', 2.6, '+20%', BLUE2),
    ('ProTax', 0.65, '+4%', GREY)], lambda v: f'${v:.1f}B', width=1040, label_w=330, bar_w=300)
ai = ''.join(
    f'<div style="display:flex;flex-direction:column;gap:4px;padding:14px 0;border-bottom:1px solid {LINE}">'
    f'<p style="font-family:{SERIF};font-size:36px;font-weight:600;color:{INK}">{v}</p><p style="font-size:24px;color:{BODY}">{k}</p></div>'
    for v, k in [('$225B+', 'Online payment volume, up 30%'), ('8.9M', 'Online Ecosystem customers; revenue per customer +15%'),
                 ('+28%', 'Mid-market customers (QBO Advanced and IES)'), ('~4x', 'Intuit Enterprise Suite run-rate, now $145M+')])
body = (f'<div style="display:flex;flex-direction:row;gap:56px">'
        f'<div style="width:1040px;display:flex;flex-direction:column;gap:36px">{mix}'
        f'<p style="font-size:28px;line-height:1.4;color:{BODY}">{B("Why it is durable:")} QuickBooks holds the ledger, payroll and payment data of millions of small firms and is the default tool of their accountants. AI agents need that data to act.</p></div>'
        f'<div style="flex:1;display:flex;flex-direction:column;background:{CARD};border:1px solid {LINE};padding:28px 32px">{lab("The QuickBooks flywheel", BLUE)}{ai}</div></div>\n')
S.append(('business', open_slide('business', 'The business', 'Small-business software is 60% of Intuit, and still growing fast') + body +
          close_slide('FY26 ended 31 Jul 2026; revenue $21.4B. Sources: Intuit FY26 8-K, Q4 FY26 earnings script, PYMNTS.', 3)))

yrs = ['FY19', 'FY20', 'FY21', 'FY22', 'FY23', 'FY24', 'FY25', 'FY26']
body = (f'<div style="display:flex;flex-direction:row;gap:64px">' +
        col_chart('Revenue, $B', yrs, [6.78, 7.68, 9.63, 12.73, 14.37, 16.29, 18.83, 21.40], lambda v: f'{v:.1f}', colors=[BLUE3]*7 + [BLUE2], height=330, bar=60) +
        col_chart('Free cash flow, $B', yrs, [2.17, 2.36, 3.20, 3.73, 4.84, 4.69, 6.12, 8.66], lambda v: f'{v:.1f}', colors=[BLUE]*7 + [BLUE2], height=330, bar=60) +
        '</div>\n' +
        stat_row([('18%', 'Revenue CAGR, FY19–26', None), ('22%', 'FCF CAGR, FY19–26', None),
                  ('42%', 'Non-GAAP operating margin, FY26', None), ('4x', 'Free cash flow since FY19', BLUE)]))
S.append(('history', open_slide('history', 'Track record', 'Seven years of 18% compound growth') + body +
          close_slide('FCF = operating cash flow minus capex; FY26 includes a one-off cash-tax benefit. Sources: Intuit filings, StockAnalysis.', 4)))

rows = [
    ['AI agents will file taxes for free', 'AI costs ~$0.12 a return vs ~$162 of TurboTax revenue per return (Goldman). No AI entrant has disclosed real volume; TurboTax’s share of self-prepared e-files slipped ~2 points to ~59%.', f'<span style="color:{ORANGE}">Real pressure on DIY pricing; Intuit is cutting entry prices and offers free Credit Karma Tax.</span>'],
    ['Growth has peaked', 'FY27 revenue guided +9–10%, from 14%; the 3-year platform target was cut to 10–15% from 15–20%. GBS is still guided +13–14%.', f'<span style="color:{BLUE}">Slower but double-digit, at a price that assumes 1.8%.</span>'],
    ['AI-native rivals will disrupt QuickBooks', 'Xero grew 31% with Melio; Basis and Rillet raised $100M each. Intuit: mid-market customers +28%; it is buying Sequence, an AI-native billing tool (15 Oct).', f'<span style="color:{BLUE}">The fight is in the mid-market, where Intuit’s distribution is hard to copy.</span>'],
    ['FY26 cash flow was flattered', 'True: immediate R&amp;D expensing cut cash taxes. Consensus FY27 FCF is $8.2B, down ~5%.', f'<span style="color:{BLUE}">Even on normalised FCF the owner yield is ~7%.</span>'],
]
body = table([(340, 'What bears say', 'left'), (None, 'What the data shows', 'left'), (440, 'Our read', 'left')], rows)
body += f'<p style="font-size:28px;line-height:1.4;color:{BODY}">{B("Net:")} the bears are right that do-it-yourself tax is under pressure, and wrong that it defines Intuit.</p>'
S.append(('debate', open_slide('debate', 'The bear case', 'Four bear arguments, tested against the numbers') + body + '\n' +
          close_slide('Sources: Goldman Sachs via Yahoo (2 Jun 2026); IRS filing-season statistics; Intuit FY26 results and Investor Day; Xero FY26.', 5)))

# 6 focus: how much is really at risk
segs = [('Business platform and other GBS', 12.9, BLUE, '60%'), ('TurboTax Live', 2.8, BLUE2, '13%'), ('TurboTax DIY', 2.5, ORANGE, '12%'),
        ('Credit Karma', 2.6, BLUE3, '12%'), ('ProTax', 0.65, GREY, '3%')]
tot = sum(v for _, v, _, _ in segs)
bar = ''.join(f'<div style="width:{round(v / tot * 1664)}px;height:72px;background:{c}"></div>' for _, v, c, _ in segs)
legend = ''.join(f'<div style="display:flex;flex-direction:row;gap:12px;align-items:center"><div style="width:24px;height:24px;background:{c}"></div>'
                 f'<p style="font-size:24px;color:{BODY}">{n} <b style="color:{INK}">{p}</b></p></div>' for n, v, c, p in segs)
tiles = ''.join(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:6px;background:{CARD};border:1px solid {LINE};padding:24px 28px">'
    f'<p style="font-family:{SERIF};font-size:56px;font-weight:600;line-height:1.05;color:{c}">{v}</p><p style="font-size:24px;line-height:1.35;color:{BODY}">{k}</p></div>'
    for v, k, c in [('~12%', 'of revenue is do-it-yourself tax, the part most exposed to AI agents', ORANGE),
                    ('~6%', 'revenue hit in Goldman’s bear case: 20% of filers fully on AI by 2030', INK),
                    ('0', 'IRS Direct File returns in 2026; the free government option was not offered', BLUE)])
body = (f'<div style="display:flex;flex-direction:column;gap:20px">{lab("FY26 revenue, $21.4B")}'
        f'<div style="display:flex;flex-direction:row;gap:0">{bar}</div>'
        f'<div style="display:flex;flex-direction:row;flex-wrap:wrap;gap:16px 40px">{legend}</div></div>\n'
        f'<div style="display:flex;flex-direction:row;gap:32px">{tiles}</div>\n'
        f'<p style="font-size:28px;line-height:1.4;color:{BODY}">{B("Our read:")} even a severe AI-tax scenario costs Intuit about 6% of revenue. A share price down 50% this year discounts far more than that.</p>\n')
S.append(('exposure', open_slide('exposure', 'TurboTax and AI', 'How much of Intuit is really at risk from AI tax agents?') + body +
          close_slide('Live ~53% of TurboTax revenue (Zacks); DIY is the rest. Goldman case: TurboTax ~18% below FY25. Sources: IRS, Intuit.', 6)))

body = (f'<div style="display:flex;flex-direction:row;gap:64px">' +
        col_chart('Buybacks, $B', ['FY20', 'FY21', 'FY22', 'FY23', 'FY24', 'FY25', 'FY26'], [0.32, 1.0, 1.9, 2.0, 2.0, 2.8, 5.5],
                  lambda v: f'{v:.1f}', colors=[BLUE]*6 + [BLUE2], height=290, bar=64) +
        col_chart('Diluted shares, millions', yrs, [264, 264, 273, 284, 283, 284, 283, 277],
                  lambda v: f'{v:.0f}', colors=[BLUE3]*7 + [BLUE], height=290, bar=60,
                  note='Shares rose with the stock-funded Credit Karma and Mailchimp deals; FY26 is the first real decline.') + '</div>\n' +
        stat_row([('$6.8B', 'Returned in FY26, ~80% of FCF', None), ('$7.9B', 'Buyback authorisation left, ~9% of market cap', BLUE),
                  ('$1.38', 'Quarterly dividend, up 15%; ~1.7% yield', None)]))
S.append(('capital', open_slide('capital', 'Capital return', 'Buybacks doubled in FY26 and now shrink the share count') + body +
          close_slide('Sources: Intuit 8-Ks and 10-Ks (FY20–FY26); Macrotrends (diluted shares).', 7)))

pf = hbars('Price to free cash flow', [('FY21', 46.3, '', GREY), ('FY22', 34.1, '', GREY), ('FY23', 29.9, '', GREY),
                                       ('FY24', 39.1, '', GREY), ('FY25', 36.0, '', BLUE3), ('Today', 10.0, '', BLUE)],
           lambda v: f'{v:.1f}x', width=700, label_w=140, bar_w=440)
sc = table([(110, 'Case', 'left'), (None, 'Assumption', 'left'), (100, 'Multiple', 'right'), (120, 'Value', 'right'), (110, 'vs price', 'right')], [
    ['Bear', 'TurboTax loses share; owner FCF falls to $5.5B', '10x', '$210', f'<span style="color:{ORANGE}">−36%</span>'],
    ['Base', 'Consensus FY27 FCF of $8.2B, less $2.0B stock comp', '17x', '$400', f'<span style="color:{BLUE}">+23%</span>'],
    ['Bull', 'TurboTax stabilises; platform grows 15%', '21x', '$525', f'<span style="color:{BLUE}">+61%</span>'],
])
body = (f'<div style="display:flex;flex-direction:row;gap:64px">'
        f'<div style="width:700px;display:flex;flex-direction:column;gap:20px">{pf}'
        f'<p style="font-size:24px;line-height:1.4;color:{BODY}">Fiscal year-end multiples (TickerLeague). Today: market cap ÷ FY26 FCF. EV/FCF has a 13-year median of 29.8x (GuruFocus).</p></div>'
        f'<div style="flex:1;display:flex;flex-direction:column;gap:20px">{lab("Scenarios on FY27E owner FCF per share")}{sc}'
        f'<p style="font-size:28px;line-height:1.4;color:{BODY}">{B("What the price implies:")} 1.8% perpetual growth in owner FCF at a 9.5% discount rate. Probability-weighted value (25/50/25): {B("$384, +18%")}. Below $300, base-case upside is back above 30%.</p></div></div>\n')
S.append(('valuation', open_slide('valuation', 'Valuation', 'From 36x free cash flow to 10x in fifteen months') + body +
          close_slide('Owner FCF per share: base $23.4 (FY27E), bear $20.8, bull $25.0. Sources: TickerLeague, GuruFocus, MarketScreener consensus.', 8)))

cal = [('~19 Nov', 'Q1 FY27: first quarter with stock comp in non-GAAP and Mailchimp shown separately'),
       ('By 31 Oct', 'Restructuring substantially complete'),
       ('Jan–Apr 2027', 'First AI-native TurboTax season; lower entry prices; free Credit Karma Tax'),
       ('Late Feb', 'Q2 FY27 and early tax-season read'),
       ('Pending', 'Sequence deal closes: AI billing for mid-market customers'),
       ('Ongoing', '$7.9B buyback authorisation; quarterly dividend')]
cl = ''.join(f'<div style="display:flex;flex-direction:row;gap:24px;padding:14px 0;border-bottom:1px solid {LINE}"><p style="width:180px;font-size:24px;font-weight:600;color:{BLUE}">{d}</p><p style="flex:1;font-size:24px;line-height:1.35;color:{BODY}">{e}</p></div>' for d, e in cal)
st = table([(None, 'Broker', 'left'), (240, 'Rating', 'left'), (120, 'Target', 'right')], [
    ['Goldman Sachs', 'Sell', '$276'], ['Piper Sandler', 'Underweight', '$290'], ['JPMorgan', 'Neutral', '$331'],
    ['BofA', 'Neutral', '$360'], ['Evercore ISI', 'Outperform', '$400'], ['Mizuho', 'Outperform', '$430']])
body = (f'<div style="display:flex;flex-direction:row;gap:64px">'
        f'<div style="flex:1;display:flex;flex-direction:column;gap:8px">{lab("Catalyst calendar", BLUE)}{cl}</div>'
        f'<div style="width:680px;display:flex;flex-direction:column;gap:12px">{lab("The Street has capitulated")}{st}'
        f'<p style="font-size:24px;line-height:1.4;color:{BODY}">At least five downgrades since June and no upgrades since August. Targets set since August run $290–430.</p></div></div>\n')
S.append(('catalysts', open_slide('catalysts', 'Catalysts', 'The 2027 tax season is the decisive test') + body +
          close_slide('Q1 date is an estimate. Sources: Intuit; broker actions via MarketBeat, SentiSense, Investing.com (Jun–Oct 2026).', 9)))

rk = table([(400, 'Risk', 'left'), (None, 'What we watch', 'left'), (440, 'We would sell if', 'left')], [
    ['TurboTax DIY share loss speeds up', '2027 season units; share of IRS self-prepared e-files', 'Units fall more than 5%'],
    ['QuickBooks growth leans on price', 'Online Ecosystem customers (+3%) vs revenue per customer', 'Online Ecosystem growth below 12%'],
    ['The mid-market push stalls', 'IES run-rate; mid-market customers', 'IES growth below 50%'],
    ['Cost cuts do not stick', 'FY27 GAAP operating margin (~32% guide)', 'The margin guide is cut'],
    ['Free government filing returns', 'IRS Direct File status', 'A free federal option relaunched at scale'],
])
body = rk + (f'\n<p style="font-size:28px;line-height:1.4;color:{BODY}">{B("Pre-mortem:")} if this fails, it will be because AI made tax filing a free utility faster than Intuit could move filers to assisted and money products.</p>\n')
S.append(('risks', open_slide('risks', 'Risks', 'What would make us wrong, and when we would sell') + body +
          close_slide('For discussion only; not investment advice. Thresholds are our own.', 10)))

print(write_deck(ROOT, 'Intuit Deep Dive', S, {
    's1': {'description': 'Cover and investment summary', 'start': 'cover'},
    's2': {'description': 'The business and its track record', 'start': 'business'},
    's3': {'description': 'The bear case and TurboTax exposure', 'start': 'debate'},
    's4': {'description': 'Capital return, valuation, catalysts and risks', 'start': 'capital'}}))
