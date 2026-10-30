#!/usr/bin/env python3
"""ДОМ.РФ: очистка sub_dimension от координат источника (30.10.2026).

Проблема. harmonize_4_domrf.py писал в sub_dimension служебный след парсера:
«разрез: <метка> | строка 6299 | ряд: stock | лист: 01_03_01». Номер строки
уникален для каждой записи, поэтому разрез не идентифицировал ряд как
временной: 774 896 строк релиза 3 дали 774 896 различных sub_dimension, и
агрегировать по разрезу было нечего — каждая точка выглядела отдельной серией.

Что делает скрипт. Переписывает sub_dimension в каноническую форму
«ряд: <dtype> | секция: <лист> | <метка разреза>», а координаты источника
(«строка N», имя листа) переносит в notes. Метка разреза (то, что раньше
стояло в «разрез:») сохраняется дословно: она различает классы застройщиков,
группы городов и подписи-продолжения, и без неё строки схлопнулись бы.

Обратимость. Перед правкой создаётся таблица
staging.domrf_subdim_backup_20261030 (observation_id, sub_dimension, notes).
Откат — один UPDATE ... FROM по этой таблице (команда печатается в отчёте).

Запуск:
    python3 domrf_fix_subdimension.py            # только замер
    python3 domrf_fix_subdimension.py --apply    # правка с бэкапом
"""
import argparse
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import connect  # noqa: E402

RELEASE_ID = 3          # старый перенос ДОМ.РФ (harmonize_4_domrf.py)
BACKUP = "staging.domrf_subdim_backup_20261030"

NEW_SUB = r"""
concat_ws(' | ',
  nullif('ряд: ' || btrim(substring(sub_dimension from 'ряд: ([^|]+?)( \||$)')), 'ряд: '),
  nullif('секция: ' || btrim(substring(sub_dimension from 'лист: (.*)$')), 'секция: '),
  nullif(btrim(substring(sub_dimension from 'разрез: (.*?)( \| |$)')), '')
)
"""

NEW_NOTES = r"""
nullif(concat_ws(' | ',
  nullif('строка ' || substring(sub_dimension from 'строка (\d+)'), 'строка '),
  nullif('лист: ' || btrim(substring(sub_dimension from 'лист: (.*)$')), 'лист: ')
), '')
"""

# Уже очищенные строки (в них есть «секция:») повторно не обрабатываем —
# иначе повторный прогон снял бы секцию и упал на уникальном индексе.
WHERE = ("release_id = %d and sub_dimension is not null"
         " and sub_dimension like '%%строка %%'"
         " and sub_dimension not like '%%секция:%%'") % RELEASE_ID


def measure(cur):
    """Сколько серий и групп получается после переписывания."""
    cur.execute(f"""
        with x as (
          select metric_id, region_id, period_start, value, {NEW_SUB} as new_sub
          from data.observation
          where {WHERE}
        )
        select count(*) as rows_,
               count(distinct new_sub) as series,
               count(*) filter (where new_sub is null) as без_разреза
        from x
    """)
    rows_, series, no_dim = cur.fetchone()

    cur.execute(f"""
        with x as (
          select metric_id, region_id, period_start, value, {NEW_SUB} as new_sub
          from data.observation
          where {WHERE}
        ),
        g as (
          select metric_id, region_id, period_start, new_sub,
                 count(*) n, count(distinct value) nv
          from x group by 1,2,3,4
        )
        select count(*) as groups,
               count(*) filter (where nv > 1) as конфликтов,
               coalesce(sum(n - nv) filter (where nv = 1), 0) as лишних_одинаковых
        from g
    """)
    groups, conflicts, duplicates = cur.fetchone()
    return dict(rows=rows_, series=series, no_dim=no_dim, groups=groups,
                conflicts=conflicts, duplicates=duplicates)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    conn = connect()
    cur = conn.cursor()
    cur.execute("set statement_timeout = '900s'")

    before = measure(cur)
    print("до правки:", before, flush=True)

    if not args.apply:
        cur.execute(f"select sub_dimension from data.observation where {WHERE} limit 3")
        for (sd,) in cur.fetchall():
            print("  пример:", sd[:160])
        print("\nзапуск с --apply внесёт правку")
        return

    t = time.time()
    cur.execute("select to_regclass(%s)", (BACKUP,))
    if cur.fetchone()[0] is None:
        cur.execute(f"""create table {BACKUP} as
            select observation_id, sub_dimension, notes
            from data.observation where {WHERE}""")
        conn.commit()
    else:
        print("снимок %s уже есть — переиспользую исходный" % BACKUP, flush=True)
    cur.execute(f"select count(*) from {BACKUP}")
    print("снимок в %s: %s строк (%.1f с)" % (BACKUP, cur.fetchone()[0], time.time() - t), flush=True)

    # Один проход, потому что стоит уникальный индекс по
    # (metric, region, period, frequency, assessment, sub_dimension, release)
    # и поэтапная правка упирается в него. Номер строки подставляется только
    # там, где после очистки под одним разрезом лежат разные значения:
    # это метрика 90 (лист ИЖС, 11 блоков по 4 строки) и ещё 86 групп.
    t = time.time()
    cur.execute(f"""
        with k as (
          select observation_id, metric_id, region_id, period_start, value,
                 {NEW_SUB} as new_sub,
                 {NEW_NOTES} as prov,
                 substring(sub_dimension from 'строка (\\d+)') as rowno
          from data.observation where {WHERE}
        ),
        g as (
          select k.*,
                 min(value) over w as vmin,
                 max(value) over w as vmax
          from k
          window w as (partition by metric_id, region_id, period_start, new_sub)
        )
        update data.observation o
        set sub_dimension = case
              when g.vmax is distinct from g.vmin then
                concat_ws(' | ', g.new_sub, 'строка ' || g.rowno)
              else g.new_sub end,
            notes = nullif(concat_ws(' | ',
                      nullif(coalesce(o.notes || ' | ', '') || coalesce(g.prov, ''), ''),
                      case when g.vmax is distinct from g.vmin
                           then 'разрез неоднозначен: номер строки сохранён как различие'
                      end), '')
        from g
        where o.observation_id = g.observation_id
    """)
    print("обрезано строк: %s (%.1f с)" % (cur.rowcount, time.time() - t), flush=True)
    conn.commit()

    # Остаток: строки с меткой «группа → подпись», у которых есть близнец
    # без метки с тем же значением. Это точные дубли, попавшие в базу дважды
    # из разных секций листа; гасим их статусом, данные не теряются.
    t = time.time()
    cur.execute(f"""
        update data.observation l
        set observation_status = 'superseded',
            notes = coalesce(l.notes || ' | ', '') || 'дубль секции: та же точка без метки разреза'
        where l.release_id = {RELEASE_ID}
          and l.observation_status not in ('rejected','superseded')
          and (l.sub_dimension like '% → %' or l.sub_dimension like '% #%')
          and exists (
            select 1 from data.observation c
            where c.release_id = {RELEASE_ID}
              and c.observation_status not in ('rejected','superseded')
              and c.metric_id = l.metric_id and c.region_id = l.region_id
              and c.period_start = l.period_start
              and c.frequency_id = l.frequency_id
              and c.assessment_type = l.assessment_type
              and c.value = l.value
              and c.sub_dimension not like '% → %'
              and c.sub_dimension not like '% #%')
    """)
    print("погашено точных дублей секции: %s (%.1f с)" % (cur.rowcount, time.time() - t), flush=True)
    conn.commit()

    # И помечаем то, что разобрать без первоисточника нельзя: рядом лежит
    # строка того же показателя с ДРУГИМ значением.
    cur.execute(f"""
        update data.observation l
        set notes = coalesce(l.notes || ' | ', '')
                    || 'разрез неоднозначен: рядом строка с другим значением, нужна сверка с листом'
        where l.release_id = {RELEASE_ID}
          and l.observation_status not in ('rejected','superseded')
          and (l.sub_dimension like '% → %' or l.sub_dimension like '% #%')
          and (l.notes is null or l.notes not like '%нужна сверка%')
          and exists (
            select 1 from data.observation c
            where c.release_id = {RELEASE_ID}
              and c.observation_status not in ('rejected','superseded')
              and c.metric_id = l.metric_id and c.region_id = l.region_id
              and c.period_start = l.period_start
              and c.frequency_id = l.frequency_id
              and c.assessment_type = l.assessment_type
              and c.value <> l.value
              and c.sub_dimension not like '% → %'
              and c.sub_dimension not like '% #%')
    """)
    print("помечено неоднозначных: %s" % cur.rowcount, flush=True)
    conn.commit()

    after = measure(cur)
    print("после правки:", after, flush=True)
    print("\nоткат:")
    print(f"  update data.observation o set sub_dimension = b.sub_dimension, notes = b.notes")
    print(f"    from {BACKUP} b where b.observation_id = o.observation_id;")


if __name__ == "__main__":
    main()
