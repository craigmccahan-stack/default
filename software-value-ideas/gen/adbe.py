import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from deep import *

ROOT = os.path.join(HERE, '..', 'decks', 'adobe')
B = lambda t: f'<b style="color:{INK}">{t}</b>'
S = []

# 1 cover
S.append(('cover', cover(dict(name='Adobe', ticker='ADBE',
    tagline='A 9% owner cash yield on the creative and document standard, priced as if growth has ended',
    cover_stats=[('$247', 'Share price, 19 Oct', PAPER), ('$340', 'Base-case value, +38%', '#8DB6E3'),
                 ('8.9%', 'Owner FCF yield', PAPER), ('$96B', 'Market cap', PAPER)]))))

# 2 summary
body = (f'<div style="display:flex;flex-direction:row;gap:64px;flex:1">'
        f'<div style="flex:1;display:flex;flex-direction:column;gap:24px">{lab("Our thesis", BLUE)}' +
        points([f'{B("Growth is intact.")} Q3 FY26 revenue +13%, total ARR +11% to $27.5B, AI-first ARR above $650M and up 150%.',
                f'{B("The fear is in the price.")} At 10x FY26 EPS the stock implies 0.6% perpetual owner-FCF growth.',
                f'{B("Cash comes back to owners.")} $24.6B of buyback capacity is 26% of the market cap; shares are down 20% since FY19.',
                f'{B("A reset is coming.")} A new CEO from 1 Dec and the FY27 guide in December can re-anchor expectations.']) +
        f'<p style="font-size:28px;font-weight:600;color:{BLUE};background:#E4ECF5;padding:14px 20px">Long. Base case $340 (+38%); bear case $165 (−33%).</p></div>' +
        key_card([('Market cap · EV', '$96B · $97B'), ('Owner FCF, trailing', '$8.5B'), ('Owner FCF yield', '8.9%'), ('Growth priced in', '0.6% a year')],
                 [('Bear', 165, -33), ('Base', 340, 38), ('Bull', 465, 88)], 247) + '</div>\n')
S.append(('summary', open_slide('summary', 'Investment summary', 'A compounding cash machine priced for decline') + body +
          close_slide('Owner FCF = FCF minus stock comp. Scenarios: 8x, 14x and 18x FY27E owner FCF per share. Sources: Adobe filings.', 2)))

# 3 business
mix = hbars('Q3 FY26 revenue by customer group, $B', [
    ('Creative &amp; Marketing Pros', 4.65, '+13% y/y', BLUE),
    ('Business Pros &amp; Consumers', 1.91, '+16% y/y', BLUE2),
    ('Non-subscription', 0.20, 'services, other', GREY)], lambda v: f'${v:.2f}B', width=1000, label_w=380, bar_w=380)
ai = ''.join(
    f'<div style="display:flex;flex-direction:column;gap:4px;padding:14px 0;border-bottom:1px solid {LINE}">'
    f'<p style="font-family:{SERIF};font-size:36px;font-weight:600;color:{INK}">{v}</p><p style="font-size:24px;color:{BODY}">{k}</p></div>'
    for v, k in [('$650M+', 'AI-first ARR, up 150% y/y'), ('~1B', 'Monthly active users across Adobe'),
                 ('100M+', 'Creative freemium users, up 70% y/y'), ('+40%', 'Firefly ARR growth, quarter on quarter')])
body = (f'<div style="display:flex;flex-direction:row;gap:64px">'
        f'<div style="width:1000px;display:flex;flex-direction:column;gap:36px">{mix}'
        f'<p style="font-size:28px;line-height:1.4;color:{BODY}">{B("Why it is durable:")} PDF and the Creative Cloud file formats are industry standards; '
        f'enterprise marketing teams run content supply chains on Adobe; and commercially safe, indemnified AI matters to large customers.</p></div>'
        f'<div style="flex:1;display:flex;flex-direction:column;background:{CARD};border:1px solid {LINE};padding:28px 32px">{lab("Where AI already pays", BLUE)}{ai}</div></div>\n')
S.append(('business', open_slide('business', 'The business', 'Two customer groups, both still growing double digits') + body +
          close_slide('Sources: Adobe Q3 FY26 8-K (10 Sep 2026) and earnings call. Total Q3 revenue $6.76B.', 3)))

# 4 history
yrs = ['FY19', 'FY20', 'FY21', 'FY22', 'FY23', 'FY24', 'FY25', 'FY26E']
rev = [11.17, 12.87, 15.79, 17.61, 19.41, 21.51, 23.77, 26.60]
fcf = [4.03, 5.31, 6.88, 7.40, 6.94, 7.87, 9.85, 10.63]
body = (f'<div style="display:flex;flex-direction:row;gap:64px">' +
        col_chart('Revenue, $B', yrs, rev, lambda v: f'{v:.1f}', colors=[BLUE3]*7 + [BLUE2], height=330, bar=60) +
        col_chart('Free cash flow, $B', yrs[:-1] + ['TTM'], fcf, lambda v: f'{v:.1f}', colors=[BLUE]*7 + [BLUE2], height=330, bar=60) +
        '</div>\n' +
        stat_row([('13%', 'Revenue CAGR, FY19–25', None), ('16%', 'FCF CAGR, FY19–25', None),
                  ('46%', 'Non-GAAP operating margin, FY25', None), ('−20%', 'Diluted shares since FY19', BLUE)]))
S.append(('history', open_slide('history', 'Track record', 'Seven years of compounding, through two AI scares') + body +
          close_slide('FY26E revenue = guidance midpoint; TTM FCF to Aug 2026. Sources: Adobe 8-Ks and 10-Ks; StockAnalysis.', 4)))

# 5 debate
rows = [
    ['Generative AI commoditises creative tools', 'Revenue +13% and ARR +11% in Q3. Firefly now hosts 30+ outside models, including Google’s and OpenAI’s.', f'<span style="color:{BLUE}">Adobe is the workflow layer, and is already selling AI on top.</span>'],
    ['Canva and Figma take the market', 'Both grow faster (Canva ~35%, Figma ~39%), but Adobe added ~$2.8B of revenue this year, ~70% of Canva’s entire ARR.', f'<span style="color:{BLUE}">A bigger market, not a zero-sum one.</span>'],
    ['Net new ARR −36% means growth is rolling over', 'Driven by the freemium push and deferred price rises; total ARR still +11%, RPO +8%. Q4 is the seasonal peak.', f'<span style="color:{ORANGE}">The metric to watch. The FY27 guide is the test.</span>'],
    ['Leadership turmoil', 'CFO left in June; CEO Narayen hands over on 1 Dec to Anil Chakravarthy, ex-CEO of Informatica.', f'<span style="color:{ORANGE}">Risk of a kitchen-sink guide; also a chance to reset.</span>'],
]
body = table([(380, 'What bears say', 'left'), (None, 'What the data shows', 'left'), (440, 'Our read', 'left')], rows)
body += f'<p style="font-size:28px;line-height:1.4;color:{BODY}">{B("Net:")} two of the four bear arguments are contradicted by reported numbers; the other two get tested by the FY27 guide in December.</p>'
S.append(('debate', open_slide('debate', 'The bear case', 'Four bear arguments, tested against the numbers') + body + '\n' +
          close_slide('Sources: Adobe Q3 FY26 8-K and call; Canva via SaaStr; Figma Q2 2026 results; Adobe 8-K (2 Sep 2026).', 5)))

# 6 focus: AI competition
ch = table([(220, 'Challenger', 'left'), (260, 'Scale', 'left'), (None, 'What stands out', 'left')], [
    ['Canva', '~$4B ARR, ~35% growth', '265M monthly users; private valuation marked down ~17% from peak'],
    ['Figma', '$1.46B FY26 guide, +39%', 'Shares fell 15% on its Q2 margin outlook'],
    ['Google', 'Nano Banana, Veo 3.1', 'Gemini app downloads +331% as Firefly fell 68% (Oct 2025)'],
    ['OpenAI', 'gpt-image-2, Sora 2', 'Near-perfect text in images; 2K output'],
])
tiles = ''.join(
    f'<div style="display:flex;flex-direction:column;gap:4px;background:{CARD};border:1px solid {LINE};padding:20px 24px">'
    f'<p style="font-family:{SERIF};font-size:36px;font-weight:600;color:{BLUE}">{v}</p><p style="font-size:24px;line-height:1.35;color:{BODY}">{k}</p></div>'
    for v, k in [('30+', 'outside models inside Firefly, rivals included'), ('$650M+', 'AI-first ARR, up 150%'),
                 ('+45%', 'GenStudio for performance marketing, q/q'), ('$1.87B', 'Semrush, closed April: AI search for marketers')])
body = (f'<div style="display:flex;flex-direction:row;gap:56px">'
        f'<div style="flex:1;display:flex;flex-direction:column;gap:12px">{lab("The challengers", ORANGE)}{ch}</div>'
        f'<div style="width:620px;display:flex;flex-direction:column;gap:12px">{lab("Adobe’s response", BLUE)}'
        f'<div style="display:grid;grid-template-columns:repeat(2, 1fr);gap:16px">{tiles}</div></div></div>\n'
        f'<p style="font-size:28px;line-height:1.4;color:{BODY}">{B("Our read:")} the threat is real at the low end of the market; at the professional and enterprise end, Adobe is turning models into features it can charge for.</p>\n')
S.append(('competition', open_slide('competition', 'AI competition', 'The challengers are real; Adobe is adapting faster than feared') + body +
          close_slide('Sources: SaaStr, CurvedTrading (Canva); Figma Q2 2026; Cryptopolitan (app data); Oakgen; Adobe filings and MAX 2025.', 6)))

# 7 capital return
body = (f'<div style="display:flex;flex-direction:row;gap:64px">' +
        col_chart('Diluted shares, millions', ['FY19', 'FY20', 'FY21', 'FY22', 'FY23', 'FY24', 'FY25', 'Q3 26'], [492, 485, 481, 471, 459, 450, 427, 395],
                  lambda v: f'{v:.0f}', colors=[BLUE3]*7 + [BLUE], height=330, bar=60) +
        col_chart('Buybacks, $B', ['FY19', 'FY20', 'FY21', 'FY22', 'FY23', 'FY24', 'FY25', '9M 26'], [2.75, 3.05, 3.95, 6.55, 4.40, 9.50, 11.28, 6.82],
                  lambda v: f'{v:.1f}', colors=[BLUE]*8, height=330, bar=60) + '</div>\n' +
        stat_row([('$41.5B', 'Bought back FY19–25, 86% of FCF', None), ('$24.6B', 'Authorisation left, 26% of market cap', BLUE),
                  ('~1.0%', 'Of the company retired per $1B at $247', None)]))
S.append(('capital', open_slide('capital', 'Capital return', 'Buybacks are shrinking the share count about 8% a year') + body +
          close_slide('Sources: Adobe 10-Ks and 10-Q (Aug 2026); Macrotrends (diluted shares); $25B authorisation runs to April 2030.', 7)))

# 8 valuation
vt = ''.join(
    f'<div style="display:flex;flex-direction:column;gap:6px;background:{CARD};border:1px solid {LINE};padding:22px 26px">'
    f'<p style="font-family:{SERIF};font-size:56px;font-weight:600;line-height:1.05;color:{c}">{v}</p><p style="font-size:24px;line-height:1.35;color:{BODY}">{k}</p></div>'
    for v, k, c in [('10.1x', 'Forward P/E on FY26 EPS guidance', BLUE), ('9.1x', 'Enterprise value to trailing FCF', BLUE),
                    ('44x', '10-year average trailing P/E', INK), ('11 of 67', 'Quarters since 2000 below 20x forward P/E; 9 saw gains a year later', INK)])
pe = f'<div style="display:grid;grid-template-columns:repeat(2, 1fr);gap:16px">{vt}</div>'
sc = table([(110, 'Case', 'left'), (None, 'Assumption', 'left'), (100, 'Multiple', 'right'), (120, 'Value', 'right'), (110, 'vs price', 'right')], [
    ['Bear', 'Owner FCF falls 10%; AI erodes pricing', '8x', '$165', f'<span style="color:{ORANGE}">−33%</span>'],
    ['Base', 'Consensus FY27 FCF of $11.2B, less stock comp', '14x', '$340', f'<span style="color:{BLUE}">+38%</span>'],
    ['Bull', 'ARR growth back above 12%; buybacks continue', '18x', '$465', f'<span style="color:{BLUE}">+88%</span>'],
])
body = (f'<div style="display:flex;flex-direction:row;gap:64px">'
        f'<div style="width:760px;display:flex;flex-direction:column;gap:20px">{lab("Then and now")}{pe}</div>'
        f'<div style="flex:1;display:flex;flex-direction:column;gap:20px">{lab("Scenarios on FY27E owner FCF per share")}{sc}'
        f'<p style="font-size:28px;line-height:1.4;color:{BODY}">{B("What the price implies:")} 0.6% perpetual growth in owner FCF at a 9.5% discount rate. Probability-weighted value (25/50/25): {B("$328, +33%")}.</p></div></div>\n')
S.append(('valuation', open_slide('valuation', 'Valuation', 'Adobe’s lowest valuation since at least 2000') + body +
          close_slide('Owner FCF per share: base $24.1 (FY27E), bear $20.5, bull $25.9. Sources: Offside Research, FullRatio, consensus, our estimates.', 8)))

# 9 catalysts and street
cal = [('10–12 Nov', 'Adobe MAX, Miami Beach: Firefly, agentic assistants'), ('1 Dec', 'Anil Chakravarthy takes over as CEO'),
       ('Mid-Dec', 'Q4 FY26 results and the first FY27 guide'), ('2H 2026', 'Topaz Labs acquisition closes'),
       ('Ongoing', 'Buybacks of ~$2.3B a quarter; a permanent CFO')]
cl = ''.join(f'<div style="display:flex;flex-direction:row;gap:24px;padding:14px 0;border-bottom:1px solid {LINE}"><p style="width:160px;font-size:24px;font-weight:600;color:{BLUE}">{d}</p><p style="flex:1;font-size:24px;line-height:1.35;color:{BODY}">{e}</p></div>' for d, e in cal)
st = table([(None, 'Broker', 'left'), (240, 'Rating', 'left'), (120, 'Target', 'right')], [
    ['Goldman Sachs', 'Sell', '$220'], ['Wells Fargo (12 Oct)', 'Underweight', '$225'], ['Morgan Stanley', 'Underweight', '$240'],
    ['Citi', 'Neutral', '$250'], ['HSBC (13 Oct)', 'Hold', '$267'], ['RBC', 'Outperform', '$315']])
body = (f'<div style="display:flex;flex-direction:row;gap:64px">'
        f'<div style="flex:1;display:flex;flex-direction:column;gap:8px">{lab("Catalyst calendar", BLUE)}{cl}</div>'
        f'<div style="width:700px;display:flex;flex-direction:column;gap:12px">{lab("The Street is sceptical")}{st}'
        f'<p style="font-size:24px;line-height:1.4;color:{BODY}">Two more downgrades in October: Wells Fargo to Underweight, HSBC to Hold. Consensus target ~$275. Expectations are low into the reset.</p></div></div>\n')
S.append(('catalysts', open_slide('catalysts', 'Catalysts', 'The next eight weeks reset the story') + body +
          close_slide('Sources: Adobe (MAX, 8-K 2 Sep 2026); broker actions via Seeking Alpha, TIKR, StreetInsider, Admiral Markets (Jul–Oct 2026).', 9)))

# 10 risks
rk = table([(400, 'Risk', 'left'), (None, 'What we watch', 'left'), (460, 'We would sell if', 'left')], [
    ['Net new ARR keeps shrinking', 'Q4 net new ARR; FY27 ARR guide', 'FY27 ARR growth is guided below 8%'],
    ['Creative pricing comes under pressure', 'Mix shift to cheaper plans; Creative subscription growth', 'Creative &amp; Marketing growth falls below 8%'],
    ['The new CEO overpays for AI', 'M&amp;A announcements', 'A large deal at more than 20x revenue'],
    ['AI compute costs squeeze margins', 'Non-GAAP operating margin', 'Margin guided below 42%'],
    ['The leadership gap drags on', 'Permanent CFO appointment', 'No permanent CFO by mid-2027'],
])
body = rk + (f'\n<p style="font-size:28px;line-height:1.4;color:{BODY}">{B("Pre-mortem:")} if this fails, it will be because generative AI cut the value of a creative seat faster than Adobe could sell AI on top of it.</p>\n')
S.append(('risks', open_slide('risks', 'Risks', 'What would make us wrong, and when we would sell') + body +
          close_slide('For discussion only; not investment advice. Thresholds are our own.', 10)))

order = write_deck(ROOT, 'Adobe Deep Dive', S, {
    's1': {'description': 'Cover and investment summary', 'start': 'cover'},
    's2': {'description': 'The business and its track record', 'start': 'business'},
    's3': {'description': 'The bear case and AI competition', 'start': 'debate'},
    's4': {'description': 'Capital return, valuation, catalysts and risks', 'start': 'capital'}})
print(order)
