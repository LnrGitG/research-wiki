# -*- coding: utf-8 -*-
"""Независимый первоисточник: дневной ряд ключевой ставки cbr.ru/hd_base/KeyRate."""
import re
import sys

import requests

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}
sess = requests.Session()
# POST с диапазоном дат — hd_base отдаёт таблицу за период
r = sess.post("https://www.cbr.ru/hd_base/KeyRate/",
              headers=UA, timeout=60, verify=False,
              data={"UniDbQuery.Posted": "True",
                    "UniDbQuery.From": "01.09.2013",
                    "UniDbQuery.To": "25.09.2026"})
r.raise_for_status()
html = r.text
print("HTML:", len(html), "bytes")

# Таблица: <td>дд.мм.гггг</td><td>XX,XX</td>
rows = re.findall(r"<td>\s*(\d{2}\.\d{2}\.\d{4})\s*</td>\s*<td[^>]*>\s*([\d,]+)\s*</td>", html)
print("строк ряда:", len(rows))
if rows:
    print("первые:", rows[:3])
    print("последние:", rows[-3:])
    with open("/tmp/keyrate_series.txt", "w", encoding="utf-8") as f:
        for d, v in rows:
            f.write(f"{d};{v}\n")
    print("сохранено: /tmp/keyrate_series.txt")
else:
    # диагностика структуры
    i = html.find("Ключевая ставка")
    print("контекст:", html[i:i+500] if i >= 0 else "заголовок не найден")
    print("первые 1000:")
    print(html[:1000])