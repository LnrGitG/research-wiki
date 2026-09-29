# Сценарии работы с БД v2 через корпоративный pgAdmin (database.mlcluster.ru)

**Роль для коллег: `viewer`** — только чтение (SELECT) на 11 схем.
Подключение: host `89.169.168.214`, port 5432, database **`research_wiki`**
(подчёркивание!), user `viewer`, SSL mode `require`, пароль — у держателя
секрета (не публикуется, `DB_VIEWER_PASSWORD` в ~/.hermes/.env на VPS).

Метка: **«Независимый расчёт, не связанный с Банком России».**

---

## Сценарий 1. Инвентаризация: что есть в базе

Карта таблиц по объёму:
```sql
SELECT schemaname, table_name, n_live_tup
FROM pg_stat_user_tables WHERE schemaname IN ('core','derived','v2','staging')
ORDER BY n_live_tup DESC LIMIT 20;
```
Ожидаемо: core.observation_v2 ≈ 5,48 млн; core.metric ≈ 16 313.

Каталог источников:
```sql
SELECT s.source_code, count(*) AS n_obs, max(o.period_start)::date AS last_period
FROM core.observation_v2 o JOIN core.source s ON s.source_id = o.source_id
GROUP BY 1 ORDER BY n_obs DESC;
```

## Сценарий 2. Свежесть данных (перед совещанием)

```sql
SELECT s.source_code,
       max(o.period_start)::date AS last_period,
       CURRENT_DATE - max(o.period_start)::date AS age_days
FROM core.observation_v2 o JOIN core.source s ON s.source_id = o.source_id
WHERE o.period_start < CURRENT_DATE
GROUP BY 1 ORDER BY age_days DESC;
```
Пороги тревоги (из datalens-db-health-dashboard-20260928.md): 45 / 120 / 400 дней.
Плановые значения на 29.09: cbr ~29, iminfin ~5, fns ~59; фейлы: rosreestr 181,
smartlab 181, worldbank 636.

## Сценарий 3. Региональная разведка (Отделения)

Все показатели по своему региону с начала года:
```sql
SELECT m.name_ru, m.metric_code, o.period_start::date, o.value
FROM core.observation_v2 o
JOIN core.metric m ON m.metric_id = o.metric_id
JOIN core.region r ON r.region_id = o.region_id
WHERE r.name_ru ILIKE '%Башкортостан%'
  AND o.period_start >= DATE '2026-01-01'
  AND o.sub_dimension = ''
  AND o.observation_status <> 'rejected'
ORDER BY o.period_start, m.name_ru;
```
Совет: `SET search_path TO core, public;` — можно писать таблицы без префикса.

Рейтинг региона внутри своего федерального округа (ввод жилья):
```sql
SELECT r.name_ru, o.value,
       RANK() OVER (PARTITION BY fd.region_id ORDER BY o.value DESC) AS rank_fo
FROM core.observation_v2 o
JOIN core.metric m ON m.metric_id = o.metric_id
JOIN core.region r ON r.region_id = o.region_id
JOIN core.region fd ON fd.region_id = r.parent_id
WHERE m.metric_code = 'rosstat_housing_total_m' AND r.level = 'region'
  AND o.period_start = (SELECT max(period_start)
                        FROM core.observation_v2 o2
                        WHERE o2.metric_id = m.metric_id AND o2.region_id = o.region_id)
ORDER BY rank_fo;
```

## Сценарий 4. Ипотека/кредитование (ДКП, факт-чек)

Ключевые коды: `irz`/`vmd` — ставки ИЖК; `zkf`/`zyi` — задолженность
физлиц/итого; `vhdt` — выдачи. Динамика к прошлому году:
```sql
SELECT m.metric_code, fd.name_ru AS district, o.period_start::date, o.value,
       o.value / lag(o.value, 12) OVER (PARTITION BY m.metric_id, fd.region_id
                                        ORDER BY o.period_start) - 1 AS yoy
FROM core.observation_v2 o
JOIN core.metric m ON m.metric_id = o.metric_id
JOIN core.region r ON r.region_id = o.region_id
JOIN core.region fd ON fd.region_id = r.parent_id
WHERE m.metric_code IN ('zkf','vhdt') AND fd.level = 'federal_district'
  AND o.period_start >= DATE '2025-01-01'
ORDER BY m.metric_code, fd.name_ru, o.period_start;
```
Внимание: нули в `vmd`/`izhk_rate_fx` — это отсутствие валютных выдач
(с ~2025-03), не ставка; `virtr` нулевые — тоже отсутствие выдач.

## Сценарий 5. Выгрузка результата

Query Tool → кнопка Download (CSV) → файл тянется в Excel/презентацию.
Для регулярных (еженедельных) выгрузок просить default-агента настроить
сценарий скриптом, а не руками.

## Сценарий 6. Что НЕ нужно делать

- Писать без префикса схему при пустом search_path — запрос упадёт
  («relation does not exist»); сначала `SET search_path TO core, public;`
- Искать схемы `public` — её нет; 11 рабочих схем перечислены выше.
- Пытаться писать/создавать: вернётся «permission denied» — это задумано.
- Делиться подключением под одним паролем — лучше запросить отдельную роль
  через default-агента (роль + личный пароль).

---

## Связанные материалы

- Паспорт региона (веб-витрина): https://lnrgitg.github.io/research-wiki/passport.html
- Спецификация датасетов DataLens: data/datalens_datasets.yaml
- Отчёт о сборке DataLens: queries/datalens-api-build-20260929.md
- Каталог метрик (векторный поиск): docs/data.html / scripts/metric_search.py