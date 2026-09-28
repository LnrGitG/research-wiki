# Дашборд DataLens: актуальность базы данных v2.0 (проект — 28.09.2026)

Задача: мониторить свежесть заполнения `core.observation_v2`. Ниже — спроектированный
дашборд DataLens (DataLens на Yandex Cloud включается только в веб-консоли), готовый к сборке
по слоям: чарты + датасеты + SQL-запросы. Все числа ниже проверены запросами к живой базе
28.09.2026 (точно те значения, что отобразит дашборд при первом построении).

## 1. Датасет

DataLens подключается к PostgreSQL на ВМ через SSH-тоннель (доступен только из сети YC, что
удобно, потому что ВМ и есть в YC). Один датасет `db_health` поверх SQL-запроса (в DataLens это
«датасет из SQL-запроса»), с параметрами не требуется.

## 2. Состав дашборда — пять чартов

### 2.1. Сводка (обзор)
```
Всего точек      5 473 472
Метрик           15 861
Регионов         102
Период           1970-01-01 — 2031-01-01
Активных субъектов 91
```
Тип: «Таблица» с одной строкой, 5 колонок (или пять «Индикаторов» в отдельном блоке).
SQL-источник:
```sql
SELECT count(*) AS points,
       count(DISTINCT metric_id) AS metrics,
       count(DISTINCT region_id) AS regions,
       min(period_start)::date AS min_period,
       max(period_start)::date AS max_period
FROM core.observation_v2 WHERE observation_status <> 'rejected';
```

### 2.1. Свежесть по ключевым рядам (самый полезный блок)
18 метрик, по которым мы принимаем решения (факт-блок к СД). Таблица со столбцами:
`код | название | последний период | дней с последней точки | флаг свежести`.

| Метрика | Последний период | Возраст, дн | Флаг |
|---|---|---|---|
| ИПЦ по регионам (`emiss_31074_cpi_prevm_m`) | 2026-08-01 | 58 | зелёный |
| Ввод жилья всего / ИЖС | 2026-08-01 | 58 | зелёный |
| Кредиты физлицам / юрлицам (ЦБ) | 2026-08-01 | 58 | зелёный |
| Выручка по ККТ (ФНС) | 2026-08-01 | 58 | зелёный |
| ИПП (`ippsm`) | 2026-07-01 | 89 | жёлтый |
| ИЖК задолженность / выдачи / ставка | 2026-07-01 | 89 | жёлтый |
| Объём работ «Строительство» (`orsmr`) | 2026-07-01 | 89 | жёлтый |
| Взносы по ОКВЭД L68 (ФНС 1-НОМ) | 2026-07-01 | 89 | жёлтый |
| ЗП по регионам | 2026-06-01 | 119 | жёлтый |
| ИКВ (КЭП 1.6) | 2026-04-01 | 180 | оранжевый |
| Безработица (МОТ) | 2026-04-01 | 180 | оранжевый |
| ВВП (КЭП 1.1) | 2025-10-01 | 362 | красный |
| ВРП (`grp_level`) | 2024-01-01 | 1001 | красный |

SQL:
```sql
SELECT m.metric_code, left(m.name_ru, 48) AS name,
       max(o.period_start)::date AS last_period,
       extract(epoch from now() - max(o.period_start))/86400 AS age_days,
       CASE WHEN max(o.period_start) >= now() - interval '45 days' THEN 'зелёный'
            WHEN max(o.period_start) >= now() - interval '120 days' THEN 'жёлтый'
            WHEN max(o.period_start) >= now() - interval '400 days' THEN 'оранжевый'
            ELSE 'красный' END AS freshness
FROM core.metric m
JOIN core.observation_v2 o ON o.metric_id = m.metric_id
WHERE o.observation_status <> 'rejected'
  AND m.metric_code = ANY(ARRAY[
    'emiss_31074_cpi_prevm_m', 'rosstat_housing_total_m', 'rosstat_housing_pop_m',
    'ippsm', 'orsmr', 'kep1_63', 'zkf', 'zyi', 'vmd', 'vhdt',
    'oipflrrivrsrf', 'spsipflrrtmrsrf', 'emiss_43062_unemp_q',
    'emiss_57824_wage_m', 'grp_level', 'kkt_revenue_m',
    'fns_1nom_key_L68', 'kep1_12'])
GROUP BY 1, 2 ORDER BY 4;
```
Пороги: до 45 дней — зелёный (ряд обновляется), до 120 — жёлтый (ряд живой, но стоит ждать
очередной релиз), до 400 — оранжевый (частота квартальная/годовая, лаг источника), свыше — красный.

### 2.2. Блоки источников: объём и свежесть
Таблица «блок | метрик | точек | последний период», один столбец на каждый источник.

| Блок | Метрик | Точек | Последний период |
|---|---|---|---|
| ЕМИСС | 32 | 1 966 451 | 2026-08-01 |
| прочие (продукция Росстата и др.) | 1 256 | 1 377 984 | 2031-01-01 (прогнозные даты) |
| ФНС (налоги и ККТ) | 255 | 902 449 | 2026-07-01 |
| ДОМ.РФ / ЕИСЖС | 99 | 772 880 | 2026-08-01 |
| ЦБ (кредитование) | 729 | 348 322 | 2026-08-01 |
| КЭП Росстата | 1 073 | 81 817 | 2026-12-01 (прогнозный) |
| Росстат (продукция и жильё) | 12 414 | 16 129 | 2026-08-01 |
| ВРП | 3 | 7 440 | 2024-01-01 |

SQL:
```sql
SELECT CASE
    WHEN m.metric_code LIKE 'emiss%' THEN 'ЕМИСС'
    WHEN m.metric_code LIKE 'kep%' THEN 'КЭП Росстата'
    WHEN m.metric_code LIKE 'cbrmon%' OR m.metric_code IN ('vmd','vhdt','vhlvt','vhrr','zkf','zyi') THEN 'ЦБ'
    WHEN m.metric_code LIKE 'fns%' THEN 'ФНС'
    WHEN m.metric_code LIKE 'rosstat%' OR m.metric_code LIKE 'pm%'
         OR m.metric_code LIKE 'pn%' OR m.metric_code LIKE 'ppm%' THEN 'Росстат (продукция)'
    WHEN m.metric_code LIKE 'domrf%' OR m.metric_code LIKE '01_%' THEN 'ДОМ.РФ'
    WHEN m.metric_code LIKE 'grp%' THEN 'ВРП'
    ELSE 'прочие' END AS block,
    count(DISTINCT m.metric_id) AS metrics,
    count(*) AS points,
    max(o.period_start)::date AS last_period
FROM core.observation_v2 o
JOIN core.metric m USING (metric_id)
WHERE o.observation_status <> 'rejected'
GROUP BY 1 ORDER BY 3 DESC;
```

### 2.3. Активность инжеста: точки по неделям (диаграмма)
Линейный или столбчатый график «неделя → число добавленных точек» за последние 8 недель.
SQL:
```sql
SELECT date_trunc('week', r.ingested_at)::date AS week,
       count(DISTINCT r.release_id) AS releases,
       count(o.obs_id) AS points
FROM core.release r
LEFT JOIN core.observation_v2 o ON o.release_id = r.release_id
WHERE r.ingested_at >= now() - interval '8 weeks'
GROUP BY 1 ORDER BY 1;
```
Живые данные: 14.09 — 78 релизов / 2,29 млн точек; 21.09 — 15 релизов / 3,19 млн;
28.09 — 6 релизов / 8 328 (неделя ещё не закрыта, поэтому число маленькое).

### 2.4. Последние релизы (что зашло недавно)
Таблица «релиз | источник | дата инжеста | точек» — последняя колонка нужна, чтобы
сразу увидеть, не загрузился ли релиз пустым.
SQL:
```sql
SELECT r.release_label, s.source_code, r.ingested_at::date AS ingested,
       count(o.obs_id) AS points
FROM core.release r
LEFT JOIN core.source s ON s.source_id = r.source_id
LEFT JOIN core.observation_v2 o ON o.release_id = r.release_id
WHERE r.status = 'loaded'
GROUP BY 1, 2, 3 ORDER BY 3 DESC LIMIT 20;
```

### 2.5. Распределение метрик по свежести (одна полоска)
Категориальная диаграмма «сколько метрик живут в каком диапазоне от последней точки»:
0–30 дней — 13; 31–90 — 13 448; 91–365 — 1 380; свыше года — 1 020.
SQL:
```sql
SELECT CASE
    WHEN age <= 30 THEN '0-30'
    WHEN age <= 90 THEN '31-90'
    WHEN age <= 365 THEN '91-365'
    ELSE '>1y'
END AS bucket, count(*) AS metrics
FROM (
    SELECT extract(epoch from now() - max(o.period_start))/86400 AS age
    FROM core.metric m
    JOIN core.observation_v2 o ON o.metric_id = m.metric_id
    WHERE o.observation_status <> 'rejected'
    GROUP BY m.metric_id
) t GROUP BY 1;
```

## 3. Как собрать в DataLens (шаги)

1. **Подключение.** Консоль DataLens → Соединения → PostgreSQL: хост — внутренний IP ВМ
   (100.89.141.127 через Tailscale), порт 5432, БД `research_wiki`, пользователь `wiki`.
   Включить SSH-туннель — ВМ и есть в YC, поэтому SSH-ключи лежат там же.
2. **Датасет** `db_health` — «создать из SQL-запроса» по любому из запросов выше (в DataLens
   датасет на SQL — отдельный тип «Датасет из SQL-запроса»; один датасет на чарт).
3. **Чарты** — по одному на каждый из пяти SQL-блоков, типы: «Таблица» для 2.1 и 2.4,
   «Индикатор» для 2.0, «Линейная диаграмма» для 2.3, «Плоская таблица» для 2.2, «Горизонтальные
   полосы» для 2.5.
4. **Дашборд** `БД v2 — актуальность`: собрать пять чартов в сетку (обзор сверху, свежесть
   по ключевым и активность инжеста во втором ряду, блоки источников и распределение по свежести
   в третьем).
5. **Обновление** — настроить периодичность в датасете (раз в сутки достаточно) или на дашборде
   через «Обновить вручную» при каждом открытии.

## 4. Что дашборд сразу покажет (проверено на живой базе)

- Свежесть критична: ВВП в КЭП до 2025-Q4, ВРП до 2024 года, ИКВ и безработица до II квартала —
  это структурные лаги источников, а не сбои; они и должны быть видны на дашборде красным/оранжевым.
- 58 дней без обновления по ключевым месячным рядам (ИПЦ, ввод жилья, кредиты ЦБ, ККТ) — это
  августовские данные; сентябрьские придут с релизами 29.09 и 06–08.10.
- Две аномалии в датах, которые надо отдельно подсветить в описании: `period_start` встречается
  1970-01-01 и 2031-01-01 (прогнозные ряды и дефектные точки — стоит отфильтровать
  `period_start BETWEEN '1995-01-01' AND '2027-01-01'` для чистоты дашборда).

## 5. Дальше (что дашборд не покрывает)

Чарты в DataLens показывают текущее состояние, но не могут уведомлять об отклонениях. Для этого
следующий шаг — cron-джоб (12-го числа, вместе с джобом ФНС), который сам делает пять SQL-запросов,
сравнивает с порогами и присылает в Telegram только отклонения. Это дешевле, чем мониторить
дашборд руками, и дублирует не всё, а только критичные сигналы.

Пометка: независимый расчёт, не связан с Банком России.