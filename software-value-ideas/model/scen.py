from model import CO, metrics, value
# Scenario definitions: (multiple, owner FCF next FY in $bn, avg shares bn)
S = {
 'ADBE': {'bear': (8, (10.60-2.08)*0.90, 0.375), 'base': (14, None, None), 'bull': (18, 11.9-2.25, 0.372)},
 'INTU': {'bear': (10, 5.50, 0.265), 'base': (17, None, None), 'bull': (21, 8.4-2.02, 0.263)},
 'GDDY': {'bear': (6, 1.40*0.85, 0.120), 'base': (11, None, None), 'bull': (14, 2.05-0.34, 0.116)},
 'FDS':  {'bear': (11, 0.60, 0.035), 'base': (17, None, None), 'bull': (21, 0.78-0.055, 0.0345)},
 'CRM':  {'bear': (10, 10.5, 0.81), 'base': (16, None, None), 'bull': (20, 12.5, 0.79)},
}
for t, sc in S.items():
    px = CO[t]['px']; out=[]
    for k in ('bear','base','bull'):
        mult, own, sh = sc[k]
        c = CO[t]
        own = own if own is not None else c['fcf1']-c['sbc1']
        sh = sh if sh is not None else c['sh1']
        v = mult*own/sh
        out.append(f"{k} ${v:6.0f} ({(v/px-1)*100:+5.0f}%) [{mult}x x ${own/sh:5.2f}]")
    m = metrics(t)
    print(t, f"px ${px}", ' | '.join(out))
