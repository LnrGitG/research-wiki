#!/usr/bin/env python3
"""Поиск рабочей точки ЦБ по дневному ряду ключевой ставки.

Проверяются три пути:
  1. XML_key_rate.asp — старый XML-эндпоинт ЦБ (если жив);
  2. hd_base/KeyRate — страница с POST UniDbQuery (источник из навыка);
  3. универсальный API dataservice — датасета ставки там, судя по дереву,
     нет, но проверим поиск по названию.
Без записи в базу.
"""
import json
import ssl
import urllib.parse
import urllib.request

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
UA = {"User-Agent": "Mozilla/5.0"}


def fetch(url, data=None, headers=None):
    h = dict(UA)
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, data=data, headers=h)
    with urllib.request.urlopen(req, timeout=90, context=CTX) as r:
        return r.status, r.read()


print("=== 1. XML_key_rate.asp (годовой диапазон) ===")
try:
    st, body = fetch("https://www.cbr.ru/scripts/XML_key_rate.asp"
                     "?date_req1=01/01/2026&date_req2=04/10/2026")
    text = body.decode("utf-8", "ignore")
    print("   код:", st, "| байт:", len(body))
    print("   начало:", text[:300].replace("\n", " "))
except Exception as e:
    print("   недоступен:", str(e)[:180])

print("\n=== 2. hd_base/KeyRate: страница ===")
try:
    st, body = fetch("https://www.cbr.ru/hd_base/KeyRate/")
    text = body.decode("utf-8", "ignore")
    print("   код:", st, "| байт:", len(body))
    for marker in ("UniDbQuery", "date_req", "keyrate", "KeyRate"):
        print(f"   содержит «{marker}»:", marker in text)
except Exception as e:
    print("   недоступен:", str(e)[:180])

print("\n=== 3. hd_base/KeyRate: POST UniDbQuery за 2026 ===")
try:
    form = urllib.parse.urlencode({
        "UniDbQuery.Posted": "True",
        "UniDbQuery.From": "01.01.2026",
        "UniDbQuery.To": "04.10.2026",
    }).encode()
    st, body = fetch("https://www.cbr.ru/hd_base/KeyRate/", data=form,
                     headers={"Content-Type": "application/x-www-form-urlencoded"})
    text = body.decode("utf-8", "ignore")
    print("   код:", st, "| байт:", len(body))
    import re
    rows = re.findall(r"(\d{2}\.\d{2}\.\d{4})</td>\s*<td[^>]*>([\d,]+)", text)
    print("   распознано пар дата/значение:", len(rows))
    for r in rows[:3]:
        print("      ", r)
    for r in rows[-3:]:
        print("      ", r)
except Exception as e:
    print("   ошибка:", str(e)[:200])

print("\n=== 4. поиск в универсальном API по слову ===")
try:
    st, body = fetch("https://www.cbr.ru/dataservice/publications")
    nodes = json.loads(body.decode("utf-8", "ignore"))
    hit = [n for n in nodes if "ставк" in (n.get("category_name") or "").lower()]
    print("   узлов со словом «ставк»:", len(hit))
    for n in hit[:6]:
        print("      ", n.get("id"), n.get("category_name")[:70])
except Exception as e:
    print("   ошибка:", str(e)[:160])