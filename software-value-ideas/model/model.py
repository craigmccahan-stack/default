"""Valuation model for the software value deck. All $ in billions except per-share.
Owner FCF = free cash flow minus stock-based compensation (treats SBC as a real cost).
Prices as of 6-7 Oct 2026. Inputs carry their source in research/*.md.
"""
R = 0.095  # discount rate for reverse DCF (10y UST 5.3% + ~4.2% ERP)

CO = {
    # ticker: price, shares (bn, current), net debt, FCF (TTM/FY base), SBC (base), next-FY FCF, next-FY SBC, next-FY avg shares, rev growth (next FY), durability score (0-4)
    'ADBE': dict(name='Adobe', px=238.14, sh=0.3892, nd=0.72, fcf=10.60, sbc=2.08, fcf1=11.23, sbc1=2.25, sh1=0.372, g=0.09, dur=3.0),
    'INTU': dict(name='Intuit', px=289.07, sh=0.2672, nd=0.50, fcf=8.60, sbc=2.00, fcf1=8.00, sbc1=2.02, sh1=0.263, g=0.095, dur=3.5),
    'GDDY': dict(name='GoDaddy', px=98.18, sh=0.127, nd=2.70, fcf=1.73, sbc=0.33, fcf1=1.92, sbc1=0.34, sh1=0.116, g=0.06, dur=2.5),
    'FDS': dict(name='FactSet', px=272.01, sh=0.03557, nd=1.20, fcf=0.7075, sbc=0.05, fcf1=0.75, sbc1=0.055, sh1=0.0345, g=0.055, dur=2.0),
    'CRM': dict(name='Salesforce', px=227.61, sh=0.823, nd=30.0, fcf=15.15, sbc=3.70, fcf1=15.05, sbc1=3.60, sh1=0.80, g=0.07, dur=2.5),
}

def metrics(t):
    c = CO[t]
    mc = c['px'] * c['sh']
    ev = mc + c['nd']
    own = c['fcf'] - c['sbc']
    own1 = c['fcf1'] - c['sbc1']
    y = own / mc
    y_ev = own / ev
    # Gordon: EV = OFCF*(1+g)/(R-g)  =>  g = (R*EV - OFCF)/(EV + OFCF)
    g_impl = (R * ev - own) / (ev + own)
    ops1 = own1 / c['sh1']
    return dict(mc=mc, ev=ev, own=own, y=y, y_ev=y_ev, g_impl=g_impl, ev_fcf=ev / c['fcf'], ops1=ops1,
                p_own1=c['px'] / ops1)

def value(t, mult, own1=None):
    """Equity value per share = multiple x next-FY owner FCF per share."""
    c = CO[t]
    o = (own1 if own1 is not None else c['fcf1'] - c['sbc1'])
    return mult * o / c['sh1']

if __name__ == '__main__':
    print(f"{'tkr':5} {'mcap':>7} {'EV':>7} {'EV/FCF':>7} {'ownFCF':>7} {'yld':>6} {'yldEV':>6} {'g_impl':>7} {'ops1':>7} {'P/own1':>7}")
    for t in CO:
        m = metrics(t)
        print(f"{t:5} {m['mc']:7.1f} {m['ev']:7.1f} {m['ev_fcf']:7.1f} {m['own']:7.2f} {m['y']*100:5.1f}% {m['y_ev']*100:5.1f}% {m['g_impl']*100:6.1f}% {m['ops1']:7.2f} {m['p_own1']:7.1f}")
