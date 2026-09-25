# -*- coding: utf-8 -*-
"""Контроль лестницы: сырые значения ряда на спорных датах."""
import datetime
import re
import sys

import requests
import urllib3

urllib3.disable_warnings()

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}
r = requests.post("https://www.cbr.ru/hd_base/KeyRate/",
                  headers=UA, timeout=120, verify=False,
                  data={"UniDbQuery.Posted": "True",
                        "UniDbQuery.From": "01.09.2013",
                        "UniDbQuery.To": "25.09.2026"})
rows = re.findall(r"<td>\s*(\d{2}\.\d{2}\.\d{4})\s*</td>\s*<td[^>]*>\s*([\d,]+)\s*</td>", r.text)
series = {datetime.datetime.strptime(d, "%d.%m.%Y").date(): float(v.replace(",", "."))
          for d, v in rows}
print(f"точек: {len(series)}")

# Контрольные даты: (дата, ожидание из общедоступной хроники, подозрение)
controls = [
    ("2014-12-11", "9.5"), ("2014-12-12", "9.5 или 10.5?"), ("2014-12-15", "10.5"),
    ("2014-12-16", "17.0"), ("2014-12-17", "17.0"),
    ("2015-04-30", "14.0"), ("2015-05-05", "12.5"),
    ("2015-06-08", "12.5"), ("2015-06-09", "12.5 или 11.5?"), ("2015-06-16", "11.5"),
    ("2022-09-16", "8.0"), ("2022-09-19", "8.0 или 7.5?"),
    ("2022-10-28", "8.0 или 7.5?"), ("2022-10-31", "7.5"),
    ("2022-02-25", "9.5"), ("2022-02-28", "20.0"),
    ("2022-05-26", "14.0"), ("2022-05-27", "14.0 или 11.0?"), ("2022-05-30", "11.0"),
    ("2023-08-15", "12.0"), ("2023-08-14", "8.5"),
    ("2014-02-28", "5.5"), ("2014-03-03", "7.0"),
]
for ds, expect in controls:
    d = datetime.date.fromisoformat(ds)
    v = series.get(d)
    # ближайший рабочий день с данными
    if v is None:
        probe = d
        for _ in range(7):
            probe += datetime.timedelta(days=1)
            if probe in series:
                break
        v = series.get(probe)
        print(f"{ds}: нет данных, ближайший {probe} = {v} (ожидалось: {expect})")
    else:
        print(f"{ds}: {v} (ожидалось: {expect})")