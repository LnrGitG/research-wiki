"""Чувствительность implied-ставки по правилу КПМ ДДКП (см. queries/model-sitrep-202610.md, разделы 3 и 5).

Правило (qpm_model.mod, строки 770-775):
    RS = 0.75*RS{-1} + 0.25*(RS_NEUTRAL + gamma2*E3_PIE4_DEV + 0.5*Y_GAP)
    E3_PIE4_MP = 0.75*E3(базовая, 3 кв. вперёд) + 0.25*E3(общая, 3 кв.)

Запуск: ~/.hermes/hermes-agent/venv/bin/python3 scripts/rule_sensitivity.py
Использовалось для раздела 5 «Калибровка по Резюме 23.09» (kanban t_08b8132f,
коммит c3ac7cd); при обновлении входов к 16.10/21.10 поправить словари base/hard.
Пометка: независимый расчёт, не связан с Банком России.
"""


def implied(rn, dev, gamma2, ygap, rs_prev=14.0, g1=0.75):
    return g1 * rs_prev + 0.25 * (rn + gamma2 * dev + 0.5 * ygap)


base = dict(dev=1.38, gamma2=1.5, ygap=0.0)   # базовый вход + калибровка большинства
hard = dict(dev=1.94, gamma2=1.9, ygap=0.5)   # hard-вход + калибровка меньшинства

print("== Сетка implied-ставки ==")
for rn in (8.0, 9.5, 10.5, 11.5):
    print(f"RN={rn}: base={implied(rn, **base):.2f} hard={implied(rn, **hard):.2f}")

print("\n== Разложение сдвига base->hard при RN=10.5 ==")
rn = 10.5
b0 = implied(rn, dev=1.38, gamma2=1.5, ygap=0.0)
b1 = implied(rn, dev=1.94, gamma2=1.5, ygap=0.0)
b2 = implied(rn, dev=1.94, gamma2=1.9, ygap=0.0)
b3 = implied(rn, dev=1.94, gamma2=1.9, ygap=0.5)
print(f"старт {b0:.2f}; +DEV(1.38->1.94): +{b1-b0:.3f}; +gamma2(1.5->1.9): +{b2-b1:.3f}; "
      f"+Y_GAP(0->0.5): +{b3-b2:.3f} (итог {b3:.2f})")
print(f"чистый вклад Y_GAP=+0.5: {0.25*0.5*0.5:.4f} п.п.; Y_GAP=+1.0: {0.25*0.5*1.0:.4f} п.п.")

print("\n== Вклад M2-аргумента меньшинства: эквивалент в DEV (gamma2=1.5) ==")
print(f"+0.3 п.п. ставки = DEV-эквивалент {0.3/1.5:.2f} п.п.; +0.5 п.п. = {0.5/1.5:.3f} п.п.")
print("Текущий DEV base=1.38 -> с M2-аргументом ~1.71; hard=1.94 -> ~2.24")

print("\n== Вилка implied по Резюме-калибровке (склонности, gamma2=1.5->1.9) ==")
lo = min(implied(rn, **base) for rn in (8.0, 9.5, 10.5, 11.5))
hi = max(implied(rn, **hard) for rn in (8.0, 9.5, 10.5, 11.5))
print(f"Вилка: {lo:.2f} (base, gamma2=1.5, RN=8.0) .. {hi:.2f} (hard, gamma2=1.9, RN=11.5)")
print("Обе ветви включают 14.00 в верхней части сетки RN -> удержание правилом не опровергается")