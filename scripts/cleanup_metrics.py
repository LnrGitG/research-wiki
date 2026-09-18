#!/usr/bin/env python3
"""
Приборка метрик: осиротевшие, вытесненные и уродливые коды.

Три класса:

1. ОСИРОТЕВШИЕ С ЖИВЫМ БЛИЗНЕЦОМ — код остался от прежней попытки
   гармонизации, данные у близнеца с тем же названием. Удаляются.
   Пример: `rke`, `rke_2` пустые, `rke_3` (32714 наблюдений) — живой.

2. ВЫТЕСНЕННЫЕ — старые коды МСФО (`rev`, `ebi`, `ocf`…) без данных после
   того, как рубеж 6 создал метрики с именами «МСФО девелоперов: X».
   Удаляются; освободившиеся коды используются для чистого переименования.

3. УРОДЛИВЫЕ КОДЫ — `mdo_2`, `mdr_2`… где суффикс возник из-за занятого
   базового кода (mdo/mdr принадлежат метрикам ЦБ). Переименовываются в
   читаемые с сохранением префикса md.

Запуск:  python3 cleanup_metrics.py [--apply]
"""
import os
import re
import sys

import psycopg

os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
DSN = os.environ.get("PGDSN", "host=localhost port=5432 dbname=research_wiki user=wiki")
APPLY = "--apply" in sys.argv

# Чистое переименование: убрать суффикс, сохранив смысловой префикс
RENAMES = {
    "mdo_2": "mdocf",     # МСФО девелоперов: ocf (mdo занят метрикой ЦБ)
    "mdr_2": "mdrev",     # МСФО девелоперов: revenue (mdr занят метрикой ЦБ)
    "mdr_3": "mdroe",     # МСФО девелоперов: roe
    "mdr_4": "mdroa",     # МСФО девелоперов: roa
    "vdpotr_2": "vdpotr",  # свободный базовый код
}

conn = psycopg.connect(DSN)
cur = conn.cursor()


def norms(s):
    return re.sub(r"\s+", " ", s or "").strip().lower()


def nobs(mid):
    cur.execute("SELECT count(*) FROM core.observation_v2 WHERE metric_id=%s", (mid,))
    return cur.fetchone()[0]


# карта живых метрик по имени
cur.execute("""SELECT m.metric_id, m.metric_code, m.name_ru, m.tags,
                      (SELECT count(*) FROM core.observation_v2 o WHERE o.metric_id=m.metric_id)
               FROM core.metric m""")
allm = cur.fetchall()
alive_by_name = {}
for mid, code, nm, tg, n in allm:
    if n > 0:
        alive_by_name.setdefault(norms(nm), []).append((mid, code, n))

orphans = [(mid, code, nm, tg) for mid, code, nm, tg, n in allm if n == 0]
print("осиротевших метрик: %d\n" % len(orphans))

to_delete, to_keep = [], []
for mid, code, nm, tg in orphans:
    twins = alive_by_name.get(norms(nm))
    if twins:
        to_delete.append((mid, code, nm, "есть живой близнец %s" % [t[1] for t in twins]))
    else:
        to_keep.append((mid, code, nm, tg))

# вытесненные старые коды МСФО (без данных, заменены метриками «МСФО девелоперов: X»)
SUPERSEDED = {"ase", "cap", "ebi", "nde", "npe", "nee", "ocf", "opp", "rev", "roa", "roe"}
# прочие: вытесненные новой гармонизацией или мусорные
EXTRA = {"itzdrrm": "вытеснена itzdr/itizdrpm (рубеж 6)",
         "ksd": "вытеснена ksdrk/ksddrk",
         "mts": "вытеснена mtsrk",
         "iokmrrkri": "дубль iokmrrk",
         "pok": "мусорное имя «показатель 35»",
         # названия различаются лишь сноской «1)» или обрезкой — данные у близнеца
         "vdpzdcn": "дубль vdpzdcn_2 (в названии лишняя сноска «1)»)",
         "trsvpzd": "дубль trsvpzd_2",
         # вытеснены рубежом 5: та же таблица housing_prices_regional
         # перенесена как tkzg (Цена 1 кв. м жилья, годовая), 2919 строк
         "tprzr": "вытеснена tkzg (цены первичного рынка, 2919 строк)",
         "tsrzr": "вытеснена tkzg (цены вторичного рынка)",
         # источник отсутствует: в staging нет строк с «темп роста»
         "trsvpzd": "источник отсутствует (в staging нет строк с «темп роста»)"}

for mid, code, nm, tg in to_keep:
    if code in SUPERSEDED:
        to_delete.append((mid, code, nm, "вытеснена метрикой «МСФО девелоперов: %s»" % nm))
    elif code in EXTRA:
        to_delete.append((mid, code, nm, EXTRA[code]))

print("К УДАЛЕНИЮ: %d" % len(to_delete))
for mid, code, nm, why in to_delete:
    print("   %-16s %-52s %s" % (code, str(nm)[:52], why))

kept = [k for k in to_keep if not any(d[0] == k[0] for d in to_delete)]
print("\nОСТАВИТЬ (уникальные, без близнеца и не вытеснённые): %d" % len(kept))
for mid, code, nm, tg in kept:
    print("   %-16s %-52s %s" % (code, str(nm)[:52], tg))

# переименования
used = {}
cur.execute("SELECT metric_id, metric_code FROM core.metric")
for mid, code in cur.fetchall():
    used[code] = mid

# Метрики, на которые ссылается legacy-таблица core.observation (рубеж 3),
# удалить нельзя из-за внешнего ключа. Она устарела (325 из 327 метрик
# дублируются в observation_v2), но её судьба — отдельное решение.
cur.execute("""SELECT DISTINCT metric_id FROM core.observation""")
legacy_ids = {r[0] for r in cur.fetchall()}
blocked = [d for d in to_delete if d[0] in legacy_ids]
to_delete = [d for d in to_delete if d[0] not in legacy_ids]
if blocked:
    print("НЕ УДАЛЯЮ (ссылки из legacy core.observation — нужно решение по таблице):")
    for mid, code, nm, why in blocked:
        cur.execute("SELECT count(*) FROM core.observation WHERE metric_id=%s", (mid,))
        print("   %-14s %-50s legacy-строк=%s" % (code, str(nm)[:50], cur.fetchone()[0]))

del_ids = {d[0] for d in to_delete}
renames = []
for old, new in RENAMES.items():
    mid = used.get(old)
    if not mid:
        continue
    if new in used and used[new] not in del_ids:
        print("\nПРОПУСК %s -> %s: код занят" % (old, new))
        continue
    renames.append((mid, old, new))

print("\nПЕРЕИМЕНОВАНИЯ: %d" % len(renames))
for mid, old, new in renames:
    print("   %-16s -> %-16s (наблюдений %s)" % (old, new, format(nobs(mid), ",")))

if not APPLY:
    print("\nСУХОЙ ПРОГОН. Применить: python3 cleanup_metrics.py --apply")
    conn.close()
    sys.exit(0)

# удаляем: сначала метрики, потом осиротевшие релизы источника, если пусты
for mid, code, nm, why in to_delete:
    cur.execute("DELETE FROM core.metric WHERE metric_id=%s", (mid,))
conn.commit()
print("\nудалено метрик: %d" % len(to_delete))

for mid, old, new in renames:
    cur.execute("UPDATE core.metric SET metric_code=%s WHERE metric_id=%s", (new, mid))
conn.commit()
print("переименовано: %d" % len(renames))

cur.execute("SELECT count(*) FROM core.metric")
print("метрик всего: %s" % cur.fetchone()[0])
cur.execute("""SELECT count(*) FROM core.metric m WHERE NOT EXISTS (
    SELECT 1 FROM core.observation_v2 o WHERE o.metric_id=m.metric_id)""")
print("осиротевших осталось: %s" % cur.fetchone()[0])
cur.execute("SELECT count(*) FROM core.observation_v2")
print("наблюдений: %s" % format(cur.fetchone()[0], ","))
conn.close()
