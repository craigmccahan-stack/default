"""Final scenario values used in all four decks (prices as of 6-7 Oct 2026)."""
R = 0.095
D = {
 # px, shares now (bn), net debt, trailing FCF, trailing SBC, FY+1 FCF, FY+1 SBC, FY+1 avg diluted shares
 'ADBE': dict(px=238.14, sh=0.3892, nd=0.72, fcf=10.63, sbc=2.08, fcf1=11.23, sbc1=2.25, sh1=0.372),
 'INTU': dict(px=289.07, sh=0.2672, nd=0.50, fcf=8.66, sbc=2.06, fcf1=8.23, sbc1=2.02, sh1=0.265),
 'GDDY': dict(px=98.18,  sh=0.127,  nd=2.70, fcf=1.73, sbc=0.32, fcf1=1.95, sbc1=0.34, sh1=0.115),
}
SC = {  # (multiple, owner FCF $bn, shares bn) ; None -> FY+1 base inputs
 'ADBE': {'bear': (8, (10.63-2.08)*0.90, 0.375), 'base': (14, None, None), 'bull': (18, 11.9-2.25, 0.372)},
 'INTU': {'bear': (10, 5.50, 0.265), 'base': (17, None, None), 'bull': (21, 8.6-2.02, 0.263)},
 'GDDY': {'bear': (6, (1.73-0.32)*0.85, 0.120), 'base': (10, None, None), 'bull': (14, 2.05-0.34, 0.115)},
}
for t, d in D.items():
    mc = d['px']*d['sh']; ev = mc + d['nd']; own = d['fcf']-d['sbc']
    g = (R*ev - own)/(ev + own)
    own1 = d['fcf1']-d['sbc1']; ops1 = own1/d['sh1']
    print(f"{t}: mcap {mc:.1f} EV {ev:.1f} EV/FCF {ev/d['fcf']:.1f}x ownFCF {own:.2f} yld {own/mc*100:.1f}% (EV {own/ev*100:.1f}%) g_impl {g*100:.1f}% | FY+1 own/sh {ops1:.2f} P/own1 {d['px']/ops1:.1f}x")
    for k,(m,o,s) in SC[t].items():
        o = own1 if o is None else o; s = d['sh1'] if s is None else s
        v = m*o/s
        print(f"   {k:4} {m:>2}x x ${o/s:6.2f} = ${v:6.1f} ({(v/d['px']-1)*100:+.0f}%)")
