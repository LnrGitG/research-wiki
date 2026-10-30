"""Сверка emiss_34118_vvod (канон) с зеркалом ЕМИСС nsEDC по РФ.

Сравнивается одна и та же номенклатура: национальная строка из файла ЕМИСС
против строки канона с регионом `ru`. Отдельно печатается, сколько регионов
складывалось в агрегат и как он относится к национальной публикации — по
подписи канона `agg=sum_regions` видно, что значение РФ считается суммой
регионов, а не берётся из национальной строки источника.
"""
import csv
import gzip
import io
import ssl
import sys
import urllib.request

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
import db_tunnel

URL = ("https://761fae42-9959-46a6-80d9-09c7be333a14.selstorage.ru"
       "/fedstatru/data/csv/34118.csv.gz")
NOMEN_KEY = "жилые помещения в нежилых зданиях"
MONTHS = {m: i for i, m in enumerate(
    ["январь", "февраль", "март", "апрель", "май", "июнь", "июль",
     "август", "сентябрь", "октябрь", "ноябрь", "декабрь"], start=1)}


def mirror_national():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, context=ctx, timeout=120).read()
    rows = list(csv.reader(io.StringIO(gzip.decompress(raw).decode("utf-8-sig"))))
    years = rows[0][4:]
    out = {}
    for row in rows[1:]:
        if len(row) < 5 or not row[0].strip().startswith("643 "):
            continue
        if NOMEN_KEY not in row[1].lower():
            continue
        label = row[3].strip().lower()
        month_name = label.split()[-1]
        if month_name not in MONTHS:          # отсекаем накопительные итоги
            continue
        m = MONTHS[month_name]
        for y, v in zip(years, row[4:]):
            v = v.strip().replace(" ", "").replace(",", ".")
            if v and y.isdigit():
                out[(int(y), m)] = float(v)
    return out


def canon_national():
    conn = db_tunnel.connect()
    sql = """
    select extract(year from o.period_start)::int, extract(month from o.period_start)::int,
           sum(o.value), count(distinct o.region_id),
           sum(case when r.region_code = 'ru' then o.value end)
    from data.observation o
    join catalog.metric m on m.metric_id = o.metric_id
    join catalog.region r on r.region_id = o.region_id
    where m.metric_code = 'emiss_34118_vvod'
      and (o.sub_dimension::jsonb)->>'nomen' like %s
      and o.observation_status not in ('rejected', 'superseded')
      and (o.sub_dimension::jsonb)->>'period_name' not like '%%-%%'
    group by 1, 2
    """
    out = {}
    with conn.cursor() as cur:
        cur.execute(sql, (f"%{NOMEN_KEY}%",))
        for y, m, total, nreg, ru_sum in cur.fetchall():
            out[(y, m)] = (float(total), int(nreg), float(ru_sum) if ru_sum is not None else None)
    conn.close()
    return out


def main():
    mir = mirror_national()
    can = canon_national()
    print(f"зеркало: месяцев {len(mir)}, канон: месяцев {len(can)}")
    print("год-мес    зеркало(РФ)   канон сумма   РФ-строка   регионов   откл.%")
    worst = 0.0
    for key in sorted(set(mir) & set(can)):
        total, nreg, ru_sum = can[key]
        m = mir[key]
        diff = (total - m) / m * 100
        worst = max(worst, abs(diff))
        print(f"{key[0]}-{key[1]:02d}   {m:12.1f}   {total:11.1f}   "
              f"{(ru_sum if ru_sum is not None else float('nan')):10.1f}   "
              f"{nreg:8d}   {diff:+7.1f}")
    print(f"худшее отклонение суммы регионов от национальной строки: {worst:.1f}%")


if __name__ == "__main__":
    main()
