#!/usr/bin/env python3
"""Снятие оперативной линии ИКВ РФ (карточки 1421/1422) как дубля КЭП.

Решение владельца: 17.10.2026, ответ «Сними как дубль кэп».
Канон: kep1_63 (56187, млрд руб.) и kep1_6_y3 (56192, % к периоду) — КЭП 1.6.
Оперативные карточки iokmro/iokspo держат по 2 наблюдения (2026Q1, 2026Q2,
release 70, assessment_type='preliminary'), значения совпадают с КЭП точка
в точку: 6634.6 / 9586.0 и 85.7 / 93.4.

Что делает:
  1. дамп `attic/ikv_kep_supersede_before_<ts>.csv.gz` (карточки + строки);
  2. валидация: значения должны совпасть с КЭП на те же периоды — иначе СТОП;
  3. карточки → status='inactive', is_active=false, тег 'superseded',
     в description — путь к канону (по плану db-dedupe-plan-20261007, п. E);
  4. строки НЕ удаляются (vintage предварительной оценки, история решения);
  5. derived.metric_card — синхронный флаг статуса (кэш канона).

Запуск: APPLY=1 python3 scripts/supersede_ikv_operational.py
"""
import csv
import gzip
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as t  # noqa: E402

APPLY = os.environ.get("APPLY") == "1"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUP = (1421, 1422)          # iokmro, iokspo
CANON = (56187, 56192)      # kep1_63, kep1_6_y3

NOTE = ("Снята как дубль КЭП (канон: {canon}). Канал закрыт 17.10.2026 по решению "
        "владельца; 2 наблюдения (2026Q1–Q2, release 70, preliminary) сохранены как "
        "vintage предварительной оценки — значения идентичны КЭП. "
        "Вопрос: queries/db-dedupe-plan-20261007.md, п. E.")


def main():
    # ---------- 1. состояние до ----------
    cards = t.query_dict("SELECT metric_id, metric_code, status, is_active, description, tags "
                    "FROM catalog.metric WHERE metric_id = ANY(%s) ORDER BY metric_id",
                    (list(DUP),))
    canon_cards = t.query_dict("SELECT metric_id, metric_code, status, is_active "
                          "FROM catalog.metric WHERE metric_id = ANY(%s) ORDER BY metric_id",
                          (list(CANON),))
    rows = t.query_dict("""SELECT o.observation_id, o.metric_id, m.metric_code, o.region_id,
                             o.period_start, o.frequency_id, o.value, o.assessment_type,
                             o.release_id, o.sub_dimension, o.observation_status, o.created_at
                      FROM data.observation o JOIN catalog.metric m USING (metric_id)
                      WHERE o.metric_id = ANY(%s)
                      ORDER BY o.metric_id, o.period_start""", (list(DUP),))
    print("=== ДО: карточки-дубли ===")
    for c in cards:
        print("  ", c)
    print("=== ДО: канон КЭП ===")
    for c in canon_cards:
        print("  ", c)
    print("=== ДО: строки дублей (%d) ===" % len(rows))
    for r in rows:
        print("  ", r)

    if not APPLY:
        print("\n[сухой прогон] APPLY=1 для записи")
        return

    # ---------- 2. валидация: значения совпадают с КЭП ----------
    pairs = [(1421, 56187), (1422, 56192)]
    for dup_id, canon_id in pairs:
        for r in [x for x in rows if x["metric_id"] == dup_id]:
            hit = t.query_dict("""SELECT o.value FROM data.observation o
                             WHERE o.metric_id = %s AND o.region_id = %s
                               AND o.period_start = %s AND o.frequency_id = %s""",
                          (canon_id, r["region_id"], r["period_start"], r["frequency_id"]))
            vals = {v["value"] for v in hit}
            if not vals or float(r["value"]) not in {float(v) for v in vals}:
                raise SystemExit("СТОП: значение %s/%s (%s) не найдено в КЭП %s — %s"
                                 % (dup_id, r["period_start"], r["value"], canon_id, vals))
    print("\nвалидация пройдена: все строки дублей найдены в КЭП с тем же значением")

    # ---------- 3. дамп-точка возврата ----------
    attic = os.path.join(REPO, "attic")
    os.makedirs(attic, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    dump = os.path.join(attic, "ikv_kep_supersede_before_%s.csv.gz" % ts)
    with gzip.open(dump, "wt", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["kind", "metric_id", "metric_code", "status", "is_active", "description",
                    "observation_id", "region_id", "period_start", "frequency_id", "value",
                    "assessment_type", "release_id", "sub_dimension"])
        for c in cards:
            w.writerow(["metric", c["metric_id"], c["metric_code"], c["status"], c["is_active"],
                        c["description"], "", "", "", "", "", "", "", ""])
        for r in rows:
            w.writerow(["observation", r["metric_id"], r["metric_code"], "", "", "",
                        r["observation_id"], r["region_id"], r["period_start"], r["frequency_id"],
                        r["value"], r["assessment_type"], r["release_id"], r["sub_dimension"]])
    print("дамп: %s (%d строк)" % (dump, os.path.getsize(dump)))

    # ---------- 4. деактивация карточек ----------
    for dup_id, canon_id in pairs:
        code = [c["metric_code"] for c in cards if c["metric_id"] == dup_id][0]
        canon_code = [c["metric_code"] for c in canon_cards if c["metric_id"] == canon_id][0]
        n = t.execute("""UPDATE catalog.metric
                         SET status = 'inactive', is_active = false,
                             description = %s,
                             tags = (SELECT array_agg(DISTINCT x) FROM unnest(
                                       coalesce(tags,'{}') || ARRAY['superseded']) x)
                         WHERE metric_id = %s AND status <> 'inactive'""",
                      (NOTE.format(canon=canon_code), dup_id))
        print("карточка %s (%s): обновлено строк %s → канон %s (%s)" % (dup_id, code, n, canon_id, canon_code))
        t.execute("UPDATE derived.metric_card SET status = 'inactive' WHERE metric_id = %s", (dup_id,))

    # ---------- 5. сверка ----------
    print("\n=== ПОСЛЕ ===")
    for c in t.query_dict("SELECT metric_id, metric_code, status, is_active, tags "
                     "FROM catalog.metric WHERE metric_id = ANY(%s) ORDER BY metric_id",
                     (list(DUP),)):
        print("  ", c)
    n_rows = t.query_dict("SELECT count(*) n FROM data.observation WHERE metric_id = ANY(%s)",
                     (list(DUP),))[0]["n"]
    n_act = t.query_dict("SELECT count(*) n FROM catalog.metric WHERE status='active'")[0]["n"]
    n_card_act = t.query_dict("SELECT count(*) n FROM derived.metric_card WHERE status='active'")[0]["n"]
    print("  строк дублей сохранено: %s" % n_rows)
    print("  активных карточек в каталоге: %s" % n_act)
    print("  активных карточек в derived.metric_card: %s" % n_card_act)
    left = t.query_dict("""SELECT m.metric_code, m.status, count(o.*) n FROM catalog.metric m
                      LEFT JOIN data.observation o USING (metric_id)
                      WHERE m.metric_id = ANY(%s) GROUP BY 1,2 ORDER BY 1""", (list(DUP),))
    print("  проверка дублей:", left)
    print("  проверка канона:", t.query_dict(
        """SELECT m.metric_code, m.status, count(o.*) n FROM catalog.metric m
           LEFT JOIN data.observation o USING (metric_id)
           WHERE m.metric_id = ANY(%s) GROUP BY 1,2 ORDER BY 1""", (list(CANON),)))
    print("\nточка возврата: %s" % dump)


if __name__ == "__main__":
    main()
