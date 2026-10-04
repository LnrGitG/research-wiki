#!/usr/bin/env python3
import sys, re
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

rows = query("SELECT metric_code FROM core.metric WHERE metric_code !~ '^[a-z0-9_-]+$'")
codes = [r[0] for r in rows]
print("всего не проходящих:", len(codes))

# какие символы встречаются
bad = {}
for c in codes:
    for ch in c:
        if not re.match(r'[a-z0-9_-]', ch):
            bad[ch] = bad.get(ch, 0) + 1
print("\nзапрещённые символы:", sorted(bad.items(), key=lambda x: -x[1]))

print("\nпримеры:")
for c in codes[:15]:
    print("   ", c)

# сколько начинаются с заглавной / содержат кириллицу
print("\nс заглавной латинской:", sum(1 for c in codes if re.match(r'[A-Z]', c)))
print("с кириллицей:", sum(1 for c in codes if re.search(r'[а-яА-ЯёЁ]', c)))
print("с точкой:", sum(1 for c in codes if '.' in c))
print("с пробелом:", sum(1 for c in codes if ' ' in c))
print("с другими символами:", sum(1 for c in codes
      if re.search(r'[^a-zA-Z0-9_.\- а-яА-ЯёЁ]', c)))