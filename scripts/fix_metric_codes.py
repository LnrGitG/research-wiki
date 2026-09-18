#!/usr/bin/env python3
"""
Косметика кодов: убрать суффиксы _N, появившиеся при повторных прогонах.

Когда рубеж перезапускается, а старые метрики удаляются как осиротевшие,
новые получают код с суффиксом (`vdpotr_2` вместо `vdpotr`), хотя базовый
код уже свободен. Скрипт возвращает базовые коды там, где это безопасно.

Запуск:  python3 fix_metric_codes.py [--apply]
"""
import os
import re
import sys

import psycopg

os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
DSN = os.environ.get("PGDSN", "host=localhost port=5432 dbname=research_wiki user=wiki")
APPLY = "--apply" in sys.argv

conn = psycopg.connect(DSN)
cur = conn.cursor()

cur.execute("SELECT metric_id, metric_code FROM core.metric")
used = {code: mid for mid, code in cur.fetchall()}

# ВАЖНО: шаблон '_[0-9]+$' ловит и осмысленные коды вида '01_01_01'
# (метрики ДОМ.РФ и панели). Их трогать нельзя. Чиним только метрики
# рубежа 6, чей базовый код свободен и не начинается с цифры.
cur.execute("""SELECT metric_id, metric_code, name_ru, tags FROM core.metric
               WHERE metric_code ~ '_[2-9]$'
                 AND tags @> ARRAY['stage6']
                 AND metric_code !~ '^[0-9]'
               ORDER BY metric_code""")
cands = [(m, c, n) for m, c, n, _ in cur.fetchall()]
print("метрик рубежа 6 с суффиксом _N (кандидаты): %d" % len(cands))

renames, skipped = [], []
for mid, code, name in cands:
    base = re.sub(r"_[0-9]+$", "", code)
    if base in used and used[base] != mid:
        skipped.append((code, base, "базовый код занят"))
        continue
    renames.append((mid, code, base))

print("\nможно переназвать: %d" % len(renames))
for mid, old, new in renames[:12]:
    print("   %-16s -> %s" % (old, new))
if len(renames) > 12:
    print("   ... и ещё %d" % (len(renames) - 12))
print("\nнельзя (базовый код занят): %d" % len(skipped))
for old, base, why in skipped[:6]:
    print("   %-16s (%s)" % (old, why))

# сколько наблюдений затронуто
nobs = 0
for mid, old, new in renames:
    cur.execute("SELECT count(*) FROM core.observation_v2 WHERE metric_id=%s", (mid,))
    nobs += cur.fetchone()[0]
print("\nнаблюдений у переназываемых метрик: %s" % format(nobs, ","))

if not APPLY:
    print("\nСУХОЙ ПРОГОН. Применить: python3 fix_metric_codes.py --apply")
    conn.close()
    sys.exit(0)

for mid, old, new in renames:
    cur.execute("UPDATE core.metric SET metric_code=%s WHERE metric_id=%s", (new, mid))
conn.commit()
print("\nпереназвано: %d" % len(renames))

cur.execute("SELECT count(*) FROM core.metric WHERE metric_code ~ '_[0-9]+$'")
print("осталось с суффиксом: %s" % cur.fetchone()[0])
cur.execute("SELECT count(*) FROM core.metric")
print("метрик всего: %s" % cur.fetchone()[0])
conn.close()
