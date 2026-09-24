#!/usr/bin/env python3
"""Sitrep t_a95e2d05: implied ключевая ставка по правилу КПМ ДДКП.

RS = gamma1*RS{-1} + (1-gamma1)*(RS_NEUTRAL + gamma2*E3_PIE4_DEV + gamma3*Y_GAP)
E3_PIE4_MP = w*E3(базовая) + (1-w)*E3(общая); DEV = MP - 4; w=0.75
gamma1=0.75; gamma2=1.5 (hard 1.9); gamma3=0.5
"""
import itertools, json

G1, W, TARIFF = 0.75, 0.75, 4.0
RS_CUR = 14.0

def implied(e3_core, e3_head, gamma2, y_gap, rs_neutral, rs_prev=RS_CUR):
    e3_mp = W * e3_core + (1 - W) * e3_head
    dev = e3_mp - TARIFF
    return round(G1 * rs_prev + (1 - G1) * (rs_neutral + gamma2 * dev + 0.5 * y_gap), 2), round(dev, 2)

# Сетка: E3 базовая/общая (середина 2027), gamma2, Y_GAP, RS_NEUTRAL
print("=== implied RS: сетка сценариев ===")
header = f"{'E3core':>6} {'E3head':>6} {'MP':>5} {'g2':>4} {'Y_GAP':>5} {'RN 9.5':>7} {'RN 10.5':>7} {'RN 11.5':>7}"
print(header)
rows_out = []
for e3c, e3h in [(4.5, 5.0), (5.0, 5.5), (5.5, 6.0), (6.0, 6.5), (6.5, 7.0)]:
    for g2 in (1.5, 1.9):
        for ygap in (0.0, 0.5):
            vals = []
            for rn in (9.5, 10.5, 11.5):
                rs, dev = implied(e3c, e3h, g2, ygap, rn)
                vals.append(rs)
            mp = round(W * e3c + (1 - W) * e3h, 2)
            print(f"{e3c:>6} {e3h:>6} {mp:>5} {g2:>4} {ygap:>5} {vals[0]:>7} {vals[1]:>7} {vals[2]:>7}")
            rows_out.append(dict(e3_core=e3c, e3_head=e3h, e3_mp=mp, gamma2=g2,
                                 y_gap=ygap, rs_n95=vals[0], rs_n105=vals[1], rs_n115=vals[2]))

# Базовый сценарий sitrep: E3core=5.25, E3head=5.75, Y_GAP=0 (закрыт), RN=10.0
rs_base, dev_base = implied(5.25, 5.75, 1.5, 0.0, 10.0)
# Hard: gamma2=1.9, дезинфляция медленнее: E3core=5.75, E3head=6.25, Y_GAP=+0.5, RN=11.5
rs_hard, dev_hard = implied(5.75, 6.5, 1.9, 0.5, 11.5)
# Hawk-ish: устойчивая инфляция застряла 5.5-6 => E3 6.5/7
rs_hawk, dev_hawk = implied(6.5, 7.0, 1.9, 0.5, 10.5)
print("\nБазовый:", rs_base, "DEV:", dev_base)
print("Hard:", rs_hard, "DEV:", dev_hard)
print("Застревание (hawk):", rs_hawk, "DEV:", dev_hawk)

with open("/home/lnr/.hermes/kanban/boards/macro/workspaces/t_a95e2d05/rule_grid.json", "w") as f:
    json.dump(rows_out, f, ensure_ascii=False, indent=1)
print("saved rule_grid.json")

# Справочно: реальная розница и ИКВ из первичных данных
cpi_26 = {6: 5.98, 7: 5.98}  # г/г июнь-июль (бюллетень ЦБ, расчёты по Росстату)
ret_nom = {6: 107.3, 7: 105.3}  # kep1_12_y2
for m in (6, 7):
    real = (ret_nom[m] / (100 + cpi_26[m]) - 1) * 100
    print(f"розница {m}.2026: номинал +{ret_nom[m]-100:.1f}% г/г, реальная ~{real:+.1f}% г/г")
ikv = {"1к26": (6634.6, 6905.7), "2к26": (9586.0, 9009.0)}
for k, (a, b) in ikv.items():
    print(f"ИКВ {k}: {a:.0f} vs {b:.0f} год назад = {(a/b-1)*100:+.1f}% г/г (номинал)")