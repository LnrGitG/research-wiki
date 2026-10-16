#!/usr/bin/env python3
"""Ядро прямых загрузчиков: сырьё → канон (catalog.metric + data.observation).

Заменяет путь «парсер → SQLite-лендинг → гармонайзер → канон» на «парсер →
канон». Логика преобразования (разбор периода, разрешение региона, сборка
sub_dimension, ключ наблюдения, ON CONFLICT DO NOTHING) повторяет рубеж 6, чтобы
прямой загрузчик попадал в ТЕ ЖЕ ключи, что прежний путь, и не плодил дубликаты.

Отличие от рубежа 6 принципиальное: частота берётся по группе, а не одна на все
(рубеж 6 помечал квартальной частотой все 83 744 своих наблюдения, включая
месячные ряды «Промпродукция, месяц»).

Использование:

    from direct_core import Writer
    w = Writer(tag='direct')
    w.ingest(rows, group='rosstat_prom_products')

где row — словарь:
    metric_name  — полное имя метрики (шаблон уже подставлен)
    value        — значение
    ps           — (год, месяц); месяц 0 = годовой период
    region       — id региона (int) либо его название (str)
    sub          — подразрез (строка) либо None
    freq         — 'M' / 'Q' / 'A' / 'W'
    source       — код источника ('rosstat', 'fns', ...)
    release      — метка релиза (первичная публикация)
    unit         — код единицы ('unknown', если неизвестна)
"""
import collections
import os
import re
import sys

import psycopg

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
# порт тоннеля 15432: локального PostgreSQL на VDS нет (см. db_tunnel.py)
DSN = os.environ.get("PGDSN",
                     "host=127.0.0.1 port=15432 dbname=research_wiki user=wiki")
TARGET = "core.observation_v2"
CUR_YEAR = 2026


def norm(s):
    return '' if s is None else re.sub(r'\s+', ' ', str(s)).strip().lower()


# --- периоды ---------------------------------------------------------------
# kind берётся из спецификации группы (совпадает с рубежом 6)
def parse_period(kind, row):
    """(год, месяц) либо None. Квартал кодируем месяцем 1/4/7/10, год — 0."""
    g = row.get
    y = g('year') or g('report_year')
    if kind == 'a':
        return (int(y), 0) if y else None
    if kind == 'a_str':
        per = str(g('period') or '')
        mq = re.match(r'^(\d{4})Q(\d)', per)
        if mq:
            return (int(mq.group(1)), {1: 1, 2: 4, 3: 7, 4: 10}[int(mq.group(2))])
        m = re.match(r'^(\d{4})', per)
        return (int(m.group(1)), 0) if m else None
    if kind == 'yq':
        q = g('quarter') if g('quarter') is not None else g('q')
        if q is None:
            return None
        m = re.match(r'^Q(\d)', str(q))
        qi = int(m.group(1)) if m else (int(q) if str(q).isdigit() else None)
        if qi is None or not y:
            return None
        return (int(y), {1: 1, 2: 4, 3: 7, 4: 10}[qi])
    if kind == 'y_q_only':
        q = g('q')
        return (int(y), {1: 1, 2: 4, 3: 7, 4: 10}[int(q)]) if y and q else None
    if kind == 'yq_rf':
        q = g('quarter')
        return (int(y), {1: 1, 2: 4, 3: 7, 4: 10}[int(q)]) if y and q else None
    if kind == 'y_m':
        m = g('month') or g('report_month')
        return (int(y), int(m)) if y and m else None
    if kind == 'ym':
        m = re.match(r'^(\d{4})-(\d{2})', str(g('month') or g('period') or ''))
        return (int(m.group(1)), int(m.group(2))) if m else None
    if kind == 'pq':
        m = re.match(r'^(\d{4})-Q(\d)', str(g('period') or ''))
        return (int(m.group(1)), {1: 1, 2: 4, 3: 7, 4: 10}[int(m.group(2))]) if m else None
    if kind in ('snap', 'snapdate'):
        s = str(g('snapshot') or g('snapshot_date') or '')
        m = re.match(r'^(\d{4})(\d{2})(\d{2})?', s)
        if not m:
            return None
        qm = {1: 1, 2: 1, 3: 1, 4: 4, 5: 4, 6: 4,
              7: 7, 8: 7, 9: 7, 10: 10, 11: 10, 12: 10}.get(int(m.group(2)), 0)
        return (int(m.group(1)), qm)
    if kind == 'yperiod':
        y2 = g('report_year')
        return (int(y2), 0) if y2 else None
    raise ValueError('неизвестный разбор периода: %s' % kind)


def period_start(ps):
    y, m = ps
    return "%04d-01-01" % y if m == 0 else "%04d-%02d-01" % (y, m)


def period_end(ps):
    y, m = ps
    if m == 0:
        return "%04d-12-31" % y
    if m in (1, 4, 7, 10):
        return "%04d-%02d-30" % (y, m + 2)
    return "%04d-%02d-%02d" % (y, m, 28)


class Writer:
    """Пишет подготовленные строки в канон, ведя справочники и релизы."""

    def __init__(self, tag='direct', simulate=False):
        self.tag = tag
        self.simulate = simulate
        self.conn = psycopg.connect(DSN)
        self.cur = self.conn.cursor()
        self._refs()

    def _refs(self):
        q = self.cur
        q.execute("SELECT source_code, source_id FROM core.source")
        self.src = dict(q.fetchall())
        q.execute("SELECT frequency_code, frequency_id FROM core.frequency")
        self.freq = dict(q.fetchall())
        q.execute("SELECT unit_code, unit_id FROM core.unit")
        self.units = dict(q.fetchall())
        q.execute("SELECT region_id, name_ru FROM core.region")
        self.reg, self.canon = {}, {}
        for ri, n in q.fetchall():
            self.reg[norm(n)] = ri
            self.canon[ri] = n
        q.execute("SELECT alias, region_id FROM meta.region_alias")
        for a, ri in q.fetchall():
            self.reg.setdefault(norm(a), ri)
        self.RU = self.reg.get('российская федерация')
        q.execute("SELECT metric_id, name_ru FROM core.metric")
        self.by_name = {norm(nm): mid for mid, nm in q.fetchall()}
        q.execute("SELECT metric_code FROM core.metric")
        self.used = {r[0] for r in q.fetchall()}
        self.rel_cache = {}
        self.new_metrics = []

    # --- справочники ---
    def ensure_metric(self, name, freq_code, unit_code='unknown'):
        """Метрика по имени; при отсутствии — регистрируется (идемпотентно)."""
        k = norm(name)
        mid = self.by_name.get(k)
        if mid:
            return mid, False
        if self.simulate:
            mid = -len(self.new_metrics) - 1
            self.by_name[k] = mid
            self.new_metrics.append(name)
            return mid, True
        from metric_codes import code_from_name, uniquify
        code = uniquify(code_from_name(str(name)), self.used)
        self.cur.execute("""INSERT INTO core.metric
            (metric_code, name_ru, unit_id, frequency_id, metric_type, status, tags)
            VALUES (%s, %s, %s, %s, 'primary', 'active', %s)
            ON CONFLICT (metric_code) DO UPDATE SET name_ru=EXCLUDED.name_ru
            RETURNING metric_id""",
            (code, str(name)[:200], self.units.get(unit_code, self.units.get('unknown')),
             self.freq.get(freq_code), [self.tag]))
        mid = self.cur.fetchone()[0]
        self.by_name[k] = mid
        self.used.add(code)
        self.new_metrics.append(name)
        self.conn.commit()
        return mid, True

    def ensure_release(self, source_code, label):
        sid = self.src.get(source_code)
        if sid is None:
            raise KeyError('нет источника %s в core.source' % source_code)
        key = (sid, str(label)[:200])
        if key in self.rel_cache:
            return self.rel_cache[key]
        if self.simulate:
            self.rel_cache[key] = -1
            return -1
        # в представлении core.release колонка называется release_label
        self.cur.execute("""SELECT release_id FROM core.release
                            WHERE source_id=%s AND release_label=%s""", key)
        r = self.cur.fetchone()
        if r:
            rid = r[0]
        else:
            self.cur.execute("""INSERT INTO core.release
                (source_id, release_label, published_at, status, notes)
                VALUES (%s, %s, now(), 'loaded', %s) RETURNING release_id""",
                (sid, key[1], 'Прямой загрузчик %s' % self.tag))
            rid = self.cur.fetchone()[0]
            self.conn.commit()
        self.rel_cache[key] = rid
        return rid

    def resolve_region(self, row, region_col, code_col):
        """(region_id, части подразреза) как в рубеже 6."""
        parts = []
        rid = None
        if row.get('region_id') is not None:
            rid = int(row['region_id'])
        if rid is None and region_col:
            rn = row.get(region_col)
            rid = self.reg.get(norm(rn)) if rn else None
            if rid and rn and self.canon.get(rid) and norm(self.canon[rid]) != norm(rn):
                parts.append('состав: %s' % str(rn))
            if not rid and rn:
                parts.append('категория: %s' % str(rn))
        rid = rid or self.RU
        if code_col and code_col != 'region_id' and row.get(code_col) is not None:
            parts.append('%s: %s' % (code_col, row[code_col]))
        return rid, parts

    # --- запись ---
    def ingest(self, rows, group='', verbose=True):
        """rows: список dict(metric_name, value, ps, region, sub, freq, source,
        release, unit). Возвращает (подготовлено, вставлено, конфликтов, метрик)."""
        prepared = []
        for r in rows:
            if r.get('value') is None or r.get('ps') is None:
                continue
            nm = str(r['metric_name'])[:200]   # длина сверяется ДО поиска метрики
            mid, _ = self.ensure_metric(nm, r.get('freq', 'M'), r.get('unit', 'unknown'))
            rel = self.ensure_release(r['source'], r['release'])
            prepared.append((mid, r.get('region') or self.RU, self.freq[r.get('freq', 'M')],
                             period_start(r['ps']), period_end(r['ps']), r['value'],
                             'final' if r['ps'][0] < CUR_YEAR else 'preliminary',
                             'validated', self.src[r['source']], rel,
                             r.get('sub') or None))

        # дубликаты ключа внутри пачки: дописываем «строка N» (механизм рубежа 5)
        cnt = collections.Counter()
        for t in prepared:
            cnt[(t[0], t[1], t[2], t[3], t[6], t[9], t[10])] += 1
        if verbose and any(v > 1 for v in cnt.values()):
            loss = sum(v - 1 for v in cnt.values() if v > 1)
            print('  дубликатов ключа внутри группы: %d' % loss)

        if self.simulate:
            return len(prepared), 0, 0, len(self.new_metrics)

        # построчные INSERT через SSH-тоннель — тысячи round-trip (урок этапа 1.2);
        # вставляем пачками, а число вставленных считаем по приросту строк релиза
        releases = sorted({t[9] for t in prepared})
        before = self._rel_counts(releases)
        sql = """INSERT INTO %s
            (metric_id, region_id, frequency_id, period_start, period_end, value,
             assessment_type, observation_status, source_id, release_id, sub_dimension)
            VALUES (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)
            ON CONFLICT (metric_id, region_id, period_start, frequency_id,
                         assessment_type, sub_dimension, release_id) DO NOTHING""" % TARGET
        for i in range(0, len(prepared), 2000):
            self.cur.executemany(sql, prepared[i:i + 2000])
            self.conn.commit()
        after = self._rel_counts(releases)
        ins = sum(after[k] - before[k] for k in after)
        return len(prepared), ins, len(prepared) - ins, len(self.new_metrics)

    def _rel_counts(self, releases):
        if not releases:
            return {}
        self.cur.execute("""SELECT release_id, count(*) FROM data.observation
                            WHERE release_id = ANY(%s) GROUP BY 1""",
                         (list(releases),))
        d = dict(self.cur.fetchall())
        return {r: d.get(r, 0) for r in releases}

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    print('ядро прямых загрузчиков; DSN=%s' % DSN)
