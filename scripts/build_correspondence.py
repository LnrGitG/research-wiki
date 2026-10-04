#!/usr/bin/env python3
"""Таблицы соответствия для контекстного поиска + функция resolve_metric.

Создаёт:
  catalog.topic             — темы макроанализа
  catalog.metric_topic      — привязка показателя к теме
  catalog.metric_alias      — синонимы (то, чем говорит контекст сессии)
  catalog.metric_region_scope — охват показателя по территории
  catalog.source_endpoint   — точка публикации и расписание опроса
  catalog.resolve_metric()  — поиск показателя по слову

Наполнение — на ядре показателей, которые реально встречаются в записках;
расширять по мере использования, а не заливать все 16 тысяч сразу.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

DDL = [
 ("catalog.topic", """CREATE TABLE IF NOT EXISTS catalog.topic (
        topic_id serial PRIMARY KEY,
        topic_code text UNIQUE NOT NULL,
        name_ru text NOT NULL,
        parent_id int REFERENCES catalog.topic(topic_id),
        description text)"""),
 ("catalog.metric_topic", """CREATE TABLE IF NOT EXISTS catalog.metric_topic (
        metric_id int NOT NULL REFERENCES catalog.metric(metric_id),
        topic_id int NOT NULL REFERENCES catalog.topic(topic_id),
        weight numeric DEFAULT 1,
        PRIMARY KEY (metric_id, topic_id))"""),
 ("catalog.metric_alias", """CREATE TABLE IF NOT EXISTS catalog.metric_alias (
        alias_id serial PRIMARY KEY,
        metric_id int NOT NULL REFERENCES catalog.metric(metric_id),
        alias text NOT NULL,
        lang text DEFAULT 'ru',
        alias_type text DEFAULT 'synonym',
        weight numeric DEFAULT 1,
        created_by text DEFAULT 'manual')"""),
 ("catalog.metric_region_scope", """CREATE TABLE IF NOT EXISTS catalog.metric_region_scope (
        metric_id int NOT NULL REFERENCES catalog.metric(metric_id),
        scope text NOT NULL,
        region_id int REFERENCES catalog.region(region_id),
        note text)"""),
 ("catalog.source_endpoint", """CREATE TABLE IF NOT EXISTS catalog.source_endpoint (
        endpoint_id serial PRIMARY KEY,
        source_id int NOT NULL REFERENCES catalog.source(source_id),
        url text NOT NULL,
        kind text NOT NULL,
        poll_cron text,
        parser_script text,
        is_active boolean DEFAULT true,
        last_checked_at timestamptz,
        last_hash text,
        note text)"""),
 ("индекс триграмм на синонимы",
  "CREATE INDEX IF NOT EXISTS ix_metric_alias_trgm ON catalog.metric_alias USING gin (alias gin_trgm_ops)"),
 ("индекс триграмм на имена",
  "CREATE INDEX IF NOT EXISTS ix_metric_name_trgm ON catalog.metric USING gin (name_ru gin_trgm_ops)"),
 ("индекс по коду",
  "CREATE INDEX IF NOT EXISTS ix_metric_alias_lower ON catalog.metric_alias (lower(alias))"),
]
for label, sql in DDL:
    try:
        execute(sql)
        print(f"OK  {label}")
    except Exception as e:
        print(f"ERR {label}: {str(e)[:160]}")

# ---------- темы ----------
TOPICS = [
    ("inflation", "Инфляция и цены", None),
    ("dku", "Денежно-кредитные условия", None),
    ("demand", "Спрос и потребление", None),
    ("output", "Выпуск и разрыв выпуска", None),
    ("labour", "Рынок труда", None),
    ("credit", "Кредит и долг", None),
    ("budget", "Бюджет и субсидии", None),
    ("external", "Внешний сектор и курс", None),
    ("housing", "Жильё и ипотека", None),
    ("regions", "Региональный разрез", None),
]
print("\n--- темы ---")
for code, name, parent in TOPICS:
    try:
        execute("""INSERT INTO catalog.topic (topic_code, name_ru, parent_id)
                   VALUES (%s, %s, %s) ON CONFLICT (topic_code) DO NOTHING""",
                (code, name, parent))
    except Exception as e:
        print("ERR", code, str(e)[:120])
print("   тем:", query("SELECT count(*) FROM catalog.topic")[0][0])

# ---------- синонимы и темы по ядру показателей ----------
SEED = {
 "kep1_14":     ("inflation", ["инфляция", "ИПЦ", "рост цен", "индекс потребительских цен",
                               "инфляция м/м", "потребительские цены"]),
 "kep1_14_s":   ("inflation", ["инфляция с исключением", "базовая инфляция"]),
 "kep3_52":     ("inflation", ["ИПЦ на конец периода", "инфляция год к году"]),
 "vvpi":        ("output",    ["ИФО ВВП", "динамика ВВП", "рост ВВП"]),
 "vvp":         ("output",    ["ВВП по использованию", "структура ВВП"]),
 "kep1_12":     ("output",    ["ВВП", "валовый внутренний продукт", "объём ВВП"]),
 "kep1_12_m":   ("demand",    ["оборот розничной торговли", "розница", "потребление"]),
 "kep4_17":     ("labour",    ["безработица", "уровень безработицы", "безработные"]),
 "kep4_2":      ("labour",    ["зарплата", "заработная плата", "номинальная зарплата"]),
 "snz":         ("labour",    ["среднемесячная зарплата", "средняя зарплата"]),
 "ippsm":       ("output",    ["промпроизводство", "индекс промышленного производства",
                               "ИПП", "промышленность"]),
 "y477050015":  ("credit",    ["инвестиции", "инвестиции в основной капитал", "ИКВ"]),
 "kep1_7":      ("demand",    ["СМР", "строительно-монтажные работы", "строительство"]),
}
print("\n--- синонимы и темы ---")
added_a = added_t = 0
for code, (topic, aliases) in SEED.items():
    mid = query("SELECT metric_id FROM catalog.metric WHERE metric_code=%s", (code,))
    if not mid:
        print(f"   пропуск {code}: нет в каталоге")
        continue
    mid = mid[0][0]
    try:
        execute("""INSERT INTO catalog.metric_topic (metric_id, topic_id, weight)
                   SELECT %s, topic_id, 1 FROM catalog.topic WHERE topic_code=%s
                   ON CONFLICT DO NOTHING""", (mid, topic))
        added_t += 1
    except Exception as e:
        print(f"   ERR темы {code}: {str(e)[:100]}")
    for a in aliases:
        try:
            execute("""INSERT INTO catalog.metric_alias (metric_id, alias, alias_type)
                       VALUES (%s, %s, 'synonym')""", (mid, a))
            added_a += 1
        except Exception as e:
            print(f"   ERR синонима {code}/{a}: {str(e)[:100]}")
print(f"   синонимов добавлено: {added_a}, тем привязано: {added_t}")
print("   всего синонимов:", query("SELECT count(*) FROM catalog.metric_alias")[0][0])
print("   всего связей с темами:", query("SELECT count(*) FROM catalog.metric_topic")[0][0])