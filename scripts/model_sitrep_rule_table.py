#!/usr/bin/env python3
"""Sitrep t_a95e2d05: точный пересчёт таблицы implied для трёх сценариев."""
G1, W, TAR = 0.75, 0.75, 4.0

def implied(e3c, e3h, g2, ygap, rn, rs_prev=14.0):
    mp = W * e3c + (1 - W) * e3h
    dev = mp - TAR
    rs = G1 * rs_prev + (1 - G1) * (rn + g2 * dev + 0.5 * ygap)
    return round(rs, 2), round(mp, 2), round(dev, 2)

scen = {
    "base": (5.25, 5.75, 1.5, 0.0),
    "hard": (5.75, 6.50, 1.9, 0.5),
    "stuck": (6.50, 7.00, 1.9, 0.5),
}
print("RN:      8.00   9.50  10.50  11.50")
for name, (e3c, e3h, g2, ygap) in scen.items():
    vals = [implied(e3c, e3h, g2, ygap, rn) for rn in (8.0, 9.5, 10.5, 11.5)]
    mp = vals[0][1]; dev = vals[0][2]
    row = "  ".join(f"{v[0]:5.2f}" for v in vals)
    print(f"{name:>5} MP={mp} DEV={dev}: {row}")

# Обратная задача: DEV, оправдывающий удержание 14.00 при Y_GAP=0
print("\nОбратная задача (RS=14, Y=0):")
for g2 in (1.5, 1.9):
    devs = []
    for rn in (8.0, 9.5, 10.5, 11.5):
        dev = (14.0 - rn) / g2
        devs.append((rn, round(dev, 2), round(dev + TAR, 2)))
    print(f"  gamma2={g2}: (RN, DEV, MP):", devs)