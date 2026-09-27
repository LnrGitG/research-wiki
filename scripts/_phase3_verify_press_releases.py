"""Сверка дат заседаний dkp.meeting с пресс-релизами ЦБ.

Проверяемый факт: для даты-пятницы существование пресс-релиза вида
https://www.cbr.ru/press/pr/?file=ДДММГГГГ_133000key.htm (страница решения
весит больше 30 КБ, служебная заглушка — около 28 КБ).

Для каждой даты заседания 2018-2026 проверяются сама дата и три соседние
пятницы (±7, ±14 дней), чтобы отличить «дата неверна» от «эндпоинт не покрывает год».
"""
import sys, urllib.request, ssl, datetime

sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
URL = "https://www.cbr.ru/press/pr/?file=%s_133000key.htm"


def probe(d):
    url = URL % d.strftime("%d%m%Y")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=25, context=CTX) as r:
            body = r.read()
        return len(body) > 30000
    except Exception:
        return None


conn = connect()
cur = conn.cursor()
cur.execute("""SELECT m.meeting_id, m.meeting_date::text, m.decision_kind, d.action
FROM dkp.meeting m LEFT JOIN dkp.decision d USING(meeting_id)
WHERE m.meeting_date BETWEEN '2018-01-01' AND '2026-12-31' ORDER BY m.meeting_date""")
rows = cur.fetchall()
conn.close()

print("заседаний 2018-2026:", len(rows))
bad = []
for mid, ds, kind, action in rows:
    d = datetime.date.fromisoformat(ds)
    ok = probe(d)
    mark = {True: "OK", False: "НЕТ", None: "ошибка сети"}[ok]
    neighbours = ""
    if ok is not True:
        for delta in (7, -7, 14, -14):
            nd = d + datetime.timedelta(days=delta)
            if nd.weekday() == 4:
                r = probe(nd)
                if r:
                    neighbours += " %s✓" % nd.isoformat()
        bad.append((ds, kind, action, mark, neighbours.strip()))
    print("  %s %-11s %-11s %s%s" % (ds, kind, action or "-", mark, neighbours))
print()
print("проблемные (дата не подтверждена):", len(bad))
for b in bad:
    print("   ", b)