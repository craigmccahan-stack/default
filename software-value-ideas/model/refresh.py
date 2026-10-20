"""Re-bases every price-driven number in the four decks to the 19 Oct 2026 close.
Fundamentals and scenario values are unchanged from final.py; only the price moves."""
R = 0.095
OLD = {'ADBE': 238.14, 'INTU': 289.07, 'GDDY': 98.18, 'FDS': 272.01, 'CRM': 227.61}
PX = {'ADBE': 247.09, 'INTU': 325.62, 'GDDY': 106.70, 'FDS': 303.36, 'CRM': 242.45}
Y2025 = {'ADBE': 238.14 / 0.68, 'INTU': 653.21, 'GDDY': 98.18 / 0.79}  # 2025 closes implied by the 6 Oct YTD figures; INTU per Motley Fool
D = {
 'ADBE': dict(sh=0.3892, nd=0.72, fcf=10.63, sbc=2.08),
 'INTU': dict(sh=0.2672, nd=0.50, fcf=8.66, sbc=2.06),
 'GDDY': dict(sh=0.127, nd=2.70, fcf=1.73, sbc=0.32),
 'FDS': dict(sh=0.03557, nd=1.20, fcf=0.7075, sbc=0.05),
 'CRM': dict(sh=0.823, nd=30.0, fcf=15.15, sbc=3.70),
}
SCEN = {'ADBE': (165, 340, 465), 'INTU': (210, 400, 525), 'GDDY': (60, 140, 205)}
pct = lambda v, p: round((v / p - 1) * 100)
for t, d in D.items():
    px = PX[t]; mc = px * d['sh']; ev = mc + d['nd']; own = d['fcf'] - d['sbc']
    g = (R * ev - own) / (ev + own)
    line = (f"{t}: px {px:.2f} ({(px / OLD[t] - 1) * 100:+.1f}% vs 6 Oct) mcap {mc:.2f} EV {ev:.2f} own {own:.2f} "
            f"yld {own / mc * 100:.2f}% g {g * 100:.2f}% P/FCF {mc / d['fcf']:.2f}x EV/FCF {ev / d['fcf']:.2f}x")
    if t in Y2025:
        line += f" YTD {(px / Y2025[t] - 1) * 100:+.1f}%"
    print(line)
    if t in SCEN:
        b, m, u = SCEN[t]
        pw = 0.25 * b + 0.5 * m + 0.25 * u
        print(f"   scen bear {b} {pct(b, px):+d}%  base {m} {pct(m, px):+d}%  bull {u} {pct(u, px):+d}%  PW ${pw:.0f} {pct(pw, px):+d}%")

a = PX['ADBE']; amc = a * 0.3892
print(f"ADBE: P/E on FY26 EPS guide $24.475 = {a / 24.475:.2f}x; $24.55B auth = {24.55 / amc * 100:.1f}% of mcap; $1B retires {1 / amc * 100:.2f}%")
i = PX['INTU']; imc = i * 0.2672
print(f"INTU: FY27 owner FCF yield {(8.23 - 2.02) / imc * 100:.2f}%; $7.9B auth = {7.9 / imc * 100:.1f}%; FY26 $6.8B returned = {6.8 / imc * 100:.1f}%; "
      f"div yield {1.38 * 4 / i * 100:.2f}%; at $300: yld {6.60 / (300 * 0.2672) * 100:.2f}% base {pct(400, 300):+d}%")
g_ = PX['GDDY']; gmc = g_ * 0.127
print(f"GDDY: P/FCF on 2026 guide {gmc / 1.80:.2f}x; $1.33B auth = {1.33 / gmc * 100:.1f}%; 95% of $1.8B retires {0.95 * 1.8 / gmc * 100:.1f}%/yr; "
      f"GuruFocus EV/FCF 8.6x -> {8.6 * (gmc + 2.7) / (98.18 * 0.127 + 2.7):.1f}x vs median {8.6 / 0.38:.1f}x")
print(f"IGV: 105.99 vs low 73.94 {(105.99 / 73.94 - 1) * 100:+.0f}%, vs peak 117.99 {(105.99 / 117.99 - 1) * 100:+.0f}%, YTD {(105.99 / (111.31 / 1.0534) - 1) * 100:+.1f}%")
print(f"SOX: 11316.34 YTD vs ~7084 base {(11316.34 / 7084 - 1) * 100:+.1f}%")
