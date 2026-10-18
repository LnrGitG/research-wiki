#!/usr/bin/env python3
"""Обновление 18.10.2026: implied-ставка по правилу КПМ ДДКП после сентябрьских данных.

RS = 0.75*RS{-1} + 0.25*(RS_NEUTRAL + gamma2*(E3_PIE4_MP - 4) + 0.5*Y_GAP)
E3_PIE4_MP = 0.75*E3(базовая, 3к27) + 0.25*E3(общая, 3к27)

Изменение против прогона 24.09: базовая E3 для 3к27 повышена с 5,25 до 5,50,
общая — с 5,75 до 6,00. Основание: сентябрьская базовая инфляция 5,47% г/г
(+0,10 п.п.) и 6,0% с.к.г. (август 5,9%) — дезинфляция не ускорилась,
медианный и трендовый показатели снижаются слабо. Hard и застревание без изменений.
"""
import json
import os

G1, W, TARGET = 0.75, 0.75, 4.0
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "data", "rule_grid_20261018.json")
RS_PREV = 14.0
RN_GRID = (8.0, 9.5, 10.5, 11.5)

SCEN = [
    # label, E3core, E3head, gamma2, Y_GAP
    ("Базовый (24.09)", 5.25, 5.75, 1.5, 0.0),
    ("Базовый (обновл.)", 5.50, 6.00, 1.5, 0.0),
    ("Hard", 5.75, 6.50, 1.9, 0.5),
    ("Застревание 5–6%+", 6.50, 7.00, 1.9, 0.5),
]

def implied(e3c, e3h, g2, gap, rn):
    mp = W * e3c + (1 - W) * e3h
    dev = mp - TARGET
    rs = G1 * RS_PREV + (1 - G1) * (rn + g2 * dev + 0.5 * gap)
    return round(mp, 2), round(dev, 2), round(rs, 2)

out = []
print(f"{'сценарий':<20}{'MP':>6}{'DEV':>6}{'g2':>5}{'GAP':>5}", end="")
for rn in RN_GRID:
    print(f"{'RN=' + str(rn):>9}", end="")
print()
for label, c, h, g2, gap in SCEN:
    mp, dev, _ = implied(c, h, g2, gap, RN_GRID[0])
    row = dict(scenario=label, e3_core=c, e3_head=h, e3_mp=mp, dev=dev, gamma2=g2, y_gap=gap)
    print(f"{label:<20}{mp:>6.2f}{dev:>6.2f}{g2:>5}{gap:>5}", end="")
    for rn in RN_GRID:
        _, _, rs = implied(c, h, g2, gap, rn)
        print(f"{rs:>9.2f}", end="")
        row[f"rn_{rn}"] = rs
    print()
    out.append(row)

print("\nОбратная задача: какой E3_PIE4_MP оправдывает RS=14,00 при Y_GAP=0")
for rn in RN_GRID:
    for g2 in (1.5, 1.9):
        mp_req = TARGET + (RS_PREV - rn) / g2
        print(f"  RN={rn:<5} g2={g2}: MP_треб = {mp_req:.2f}%  (DEV={mp_req - TARGET:.2f})")

json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("\nsaved", OUT)
