# Спека: перезагрузка базы данных «жилищный рынок РФ» (v2)

**Дата:** 2026-09-21
**Статус:** проект на утверждение владельца
**Контекст:** решение владельца (21.09.2026) — «создать базу заново… много шумных
слишком детализированных показателей, следить за которыми очень затратно.
Наполнять постепенно, верифицируя каждый исходный файл».

---

## 0. Диагноз: почему v1 не выдержала

Три базы накопили 3,2 млн строк, из которых полезная плотность ниже 20%:

| База | Строк | Главная проблема |
|---|---|---|
| rosstat_construction.db (SQLite) | 1,95 млн | 60% объёма — domrf_indicators; 24% маргинальных блоков (ДДУ нежилые, паркинги, КРТ-сток); 14,4 тыс. точных дублей; 6,8 тыс. «регионов»-мусора (годы вместо субъектов) |
| cbr_mortgage_monthly (SQLite) | 175 тыс. | 91% валютных строк после 2022 = нули; разнобой имён регионов (347 вариантов в observations) |
| research_wiki (PG) | 2,28 млн obs | 2 440 метрик из одного конвейера; 732 tiny (1–2 точки), 601 stale, 699 unknown-единиц; 223 дубль-пары, из которых 192 псевдо |

Уроки каталогизации (этапы 1–3, протокол catalog-stage1-protocol-20260921.md)
показали корень: **метрики заводились из файлов, а не из потребностей анализа**.
Каждый лист каждого XLSX становился рядом; фильтрация «шум/ядро» откладывалась
на потом и стала дороже, чем была бы отсечка на входе.

**Решение:** новая БД с входным фильтром (allowlist доменов), per-file верификацией
и полным метаданным контуром. Старые базы остаются как архив (read-only) —
они источник для переноса ядра; никакого разрушения.

## 1. Принципы (мировая практика)

За образцы приняты: FRED/MDB (качество фацетов), DBnomics (dimension map),
SDMX (меры/атрибуты/размерности), World Bank WDI (иерархия агрегатов),
Eurostat (свежесть/статусы ревизий), IMF SDMX-CLI (эджер-загрузчик).

1. **Allowlist на входе, не карантин на выходе.** Домен-каталог из ~60 метрик
   ядра; всё вне его требует явного решения владельца. Цель — 1 000–2 000 obs
   на метрику, а не 30 000 «на всякий случай».
2. **Один факт — одна строка, с прокси-ключами источника.**
   `observation(metric, region, period, frequency, value)` + наблюдаемая
   неизменяемость: ревизии не перезаписывают значение, а добавляют версию.
3. **Версионность через vintage.** Каждый запуск загрузки = `run_id` со снимком
   source-файла (sha256, дата публикации, дата загрузки). Ряды с историей
   ревизий читаются `AS OF` любой прошлой загрузки.
4. **Гармонизация на входе.** Единый справочник регионов, единиц, частот;
   конверсия в канонические единицы (млн руб., руб/м², шт.) при загрузке,
   а не при анализе.
5. **Качество — измеримое поле, не комментарий.** Флаги по строке: outlier,
   revision, imputed, provisional, break_in_series.

## 2. Схема БД (PostgreSQL, research_wiki_v2)

```sql
-- ============ СПРАВОЧНИКИ ============
CREATE TABLE source (           -- организации-публикаторы
  source_id     SMALLSERIAL PRIMARY KEY,
  source_code   TEXT UNIQUE,            -- 'rosstat', 'cbr', 'domrf', 'eiszs', 'fnso'...
  name_ru       TEXT NOT NULL,
  access_url    TEXT,
  access_method TEXT                    -- 'api'|'scrape'|'file'|'manual'
);

CREATE TABLE dataset (          -- конкретный продукт источника (файл/выгрузка/раздел)
  dataset_id    SERIAL PRIMARY KEY,
  source_id     SMALLINT NOT NULL REFERENCES source,
  dataset_code  TEXT UNIQUE,            -- 'vfs-0420218', 'domrf-price-index', 'kep-1'
  name_ru       TEXT NOT NULL,
  release_url   TEXT,
  schedule      TEXT,                   -- регламент публикации ('monthly+14d')
  is_active     BOOLEAN DEFAULT TRUE
);

CREATE TABLE region (
  region_id     SMALLINT PRIMARY KEY,
  region_code   TEXT UNIQUE,            -- ОКАТО/ОКТМО канонический
  name_ru       TEXT NOT NULL,
  level         TEXT NOT NULL,          -- 'rf'|'federal_district'|'region'
  parent_id     SMALLINT REFERENCES region,
  oktmo TEXT, okato TEXT, iso_code TEXT,
  valid_from DATE, valid_to DATE        -- история переименований/созданий
);

CREATE TABLE unit (
  unit_id       SMALLSERIAL PRIMARY KEY,
  unit_code     TEXT UNIQUE,            -- 'mln_rub','rub_m2','count','pct','index_100'
  name_ru       TEXT NOT NULL,
  dim           TEXT                    -- 'money','area','count','ratio','index','time'
);

CREATE TABLE frequency (
  frequency_id  SMALLSERIAL PRIMARY KEY,
  freq_code     TEXT UNIQUE,            -- 'M','Q','A','W'
  name_ru       TEXT NOT NULL,
  periods_per_year SMALLINT
);

-- ============ КАТАЛОГ МЕТРИК (ядро ~60, расширяемо) ============
CREATE TABLE domain (           -- тематические домены
  domain_id     SMALLSERIAL PRIMARY KEY,
  domain_code   TEXT UNIQUE,            -- 'supply','demand','prices','credit','demography',
                                -- 'firms','budget','macro_input','search_leads'
  name_ru       TEXT NOT NULL,
  parent_id     SMALLINT REFERENCES domain
);

CREATE TABLE metric (
  metric_id     SERIAL PRIMARY KEY,
  metric_code   TEXT UNIQUE,            -- 'smr_full_m', 'ikv_rf_q', 'cbr_izhk_rate_m'
  name_ru       TEXT NOT NULL,
  name_en       TEXT,
  definition_ru TEXT,                   -- методология источника своими словами
  domain_id     SMALLINT NOT NULL REFERENCES domain,
  parent_metric_id  INT REFERENCES metric,   -- подчинённость (ИЖС → ввод всего)
  relation_type TEXT,                   -- 'is_part_of'|'derived_from'|'complement'
  unit_id       SMALLINT NOT NULL REFERENCES unit,
  frequency_id  SMALLINT NOT NULL REFERENCES frequency,
  is_aggregate  BOOLEAN DEFAULT FALSE,  -- РФ/ФО = агрегат субъектов
  priority      TEXT DEFAULT 'core'     -- 'core'|'extended'|'context'
);

CREATE TABLE metric_dataset_map (       -- метрика может приходить из нескольких датасетов
  metric_id     INT REFERENCES metric,
  dataset_id    INT REFERENCES dataset,
  native_code   TEXT,                   -- как показатель назван у источника (id ЕМИСС и т.п.)
  native_unit   TEXT,                   -- единица в оригинале
  scale_factor  NUMERIC DEFAULT 1,      -- коэффициент пересчёта в каноническую единицу
  PRIMARY KEY (metric_id, dataset_id)
);

-- ============ ЗАГРУЗКИ И ВЕРСИОННОСТЬ ============
CREATE TABLE load_run (
  run_id        SERIAL PRIMARY KEY,
  dataset_id    INT NOT NULL REFERENCES dataset,
  loaded_at     TIMESTAMPTZ DEFAULT now(),
  source_file   TEXT,                   -- путь исходника
  file_sha256   CHAR(64),               -- снапшот исходника
  source_published_at DATE,             -- дата публикации на источнике (важно: не дата в файле!)
  parser_version TEXT,                  -- git-хеш парсера
  status        TEXT CHECK (status IN ('ok','partial','failed','verified')),
  rows_parsed   INT, rows_inserted INT, rows_rejected INT,
  notes         TEXT
);

CREATE TABLE load_check (               -- верификация каждого файла (ручная, до/после)
  check_id      SERIAL PRIMARY KEY,
  run_id        INT REFERENCES load_run,
  check_kind    TEXT,        -- 'spot_value'|'row_count'|'hash_series'|'region_count'
  check_detail  JSONB,       -- {"cell":"B3","expected":..., "got":...}
  passed        BOOLEAN,
  checked_by    TEXT DEFAULT 'agent', checked_at TIMESTAMPTZ DEFAULT now()
);

-- ============ ДАННЫЕ ============
CREATE TABLE observation (
  obs_id        BIGSERIAL PRIMARY KEY,
  metric_id     INT NOT NULL REFERENCES metric,
  region_id     SMALLINT NOT NULL REFERENCES region,
  frequency_id  SMALLINT NOT NULL REFERENCES frequency,
  period_start  DATE NOT NULL,
  period_end    DATE,
  value         NUMERIC(20,4),          -- каноническая единица
  value_native  NUMERIC(20,4),          -- как в источнике (для аудита)
  run_id        INT NOT NULL REFERENCES load_run,   -- версии: разные run → разные строки
  is_current    BOOLEAN DEFAULT TRUE,   -- активная версия (последний run)
  quality_flags TEXT[] DEFAULT '{}',    -- 'outlier','revision','imputed','break','provisional'
  UNIQUE (metric_id, region_id, frequency_id, period_start, run_id)
);
CREATE INDEX obs_current_idx ON observation (metric_id, region_id, period_start) WHERE is_current;
CREATE INDEX obs_series_idx  ON observation (metric_id, region_id, run_id);

CREATE TABLE series_revision (          -- ревизии задним числом: сравнение run'ов
  metric_id INT, region_id SMALLINT, period_start DATE,
  prev_run_id INT, prev_value NUMERIC, new_run_id INT, new_value NUMERIC,
  abs_change NUMERIC, pct_change NUMERIC,
  detected_at TIMESTAMPTZ DEFAULT now(),
  PRIMARY KEY (metric_id, region_id, period_start, new_run_id)
);

CREATE TABLE freshness (                -- витрина актуальности (пересчёт pg_cron)
  metric_id INT PRIMARY KEY,
  last_obs_at DATE, obs_count INT,
  freshness TEXT CHECK (freshness IN ('fresh','lagging','stale')),
  expected_next DATE,
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- ============ ВИТРИНЫ ============
CREATE VIEW v_core_panel AS             -- панель ядра для моделирования
SELECT m.metric_code, r.name_ru AS region, f.freq_code, o.period_start, o.value, o.quality_flags
FROM observation o JOIN metric m USING (metric_id) JOIN region r USING (region_id)
JOIN frequency f USING (frequency_id)
WHERE o.is_current AND m.priority = 'core';

CREATE VIEW v_freshness_board AS        -- дашборд актуальности
SELECT m.metric_code, fr.freshness, fr.last_obs_at, fr.obs_count, d.dataset_code
FROM freshness fr JOIN metric m USING (metric_id)
JOIN metric_dataset md ON md.metric_id = m.metric_id
JOIN dataset d USING (dataset_id);
```

Ключевые отличия от текущей БД: metric содержит **методологию и подчинённость**
вместо плоских фацетов; observation хранит **run_id** (история ревизий вместо
перезаписи); отдельные load_run/load_check — аудируемый конвейер; всё
нормализовано, никаких 583-мегабайтных широких таблиц.

## 3. Ядро доменов (allowlist первого наполнения, ~60 метрик)

| Домен | Метрики ядра | Источники |
|---|---|---|
| demand (ввод/СМР) | СМР РФ мес./кв., ввод РФ мес./кв., ИФО стр., ИКВ, ВНОК | Росстат КЭП, ЕМИСС |
| supply (регионы) | ввод по 85 рег. (мес., кв.), ввод ИЖС, застройки | Росстат |
| prices | ИЦЖ (первичка/вторичка руб/м²), индекс ДОМ.РФ (база 100), ДДУ-цены | Росстат, ДОМ.РФ |
| transactions | количество ДДУ РФ, сделки Росреестра (отдельный контур) | ДОМ.РФ, Росреестр |
| credit | выдача ИЖК объём/кол-во, ставка ПВР, задолженность (4 ряда, не 158!) | ЦБ 0420218 |
| developers | выручка/прибыль застройщиков, HHI регионов | ФНС, СПАРК |
| budget/subsidies | субсидии СП, кассовое исполнение | Минфин, казначейство |
| search_leads | композит Wordstat S2–S5 | Яндекс |
| macro_input | ключевая ставка, ИПЦ, ВВП стр., доходы нас., демография | ЦБ, Росстат |

Фильтры первого дня: без инвалютных рядов после 2022 (91% нулей), без
vmns-подчинённых (карантин по решению владельца), без ДДУ нежилые/паркинги/КРТ
прогнозы, без срезов «в т.ч. по годам разрешения».

## 4. Интеллектуальный загрузчик

Архитектура (пакет `loader/` в research-wiki-private):

```
loader/
  registry.py      # dataset registry: YAML-карточки источников
  parsers/         # по одному модулю на dataset: parse_<code>.py
  verify.py        # этап верификации: sha256, спот-значения, счётчики
  normalize.py     # регионы/единицы/частоты → канон, масштабные коэффициенты
  ingest.py        # запись: новый run_id, дедуп в run, обновление is_current
  revisions.py     # diff между run'ами → series_revision + флаг revision
  cli.py           # loader ingest <dataset_code> [--file X] [--verify-only]
```

Порядок работы загрузчика на файл (весь путь ≤5 минут на файл):

1. **Реестр.** Карточка `datasets/vfs-0420218.yaml`: url, листы, маппинг
   лист→(metric, срез), единицы, расписание. Добавление источника = YAML + парсер.
2. **Верификация (обязательный рубеж).** sha256 совпал с реестром или это
   документированное обновление; спот-значения 3 ячеек против ожиданий;
   счётчик строк в диапазоне; Белгородская область как контрольный регион
   (значения сверены с ручной выгрузкой из этого протокола).
3. **Нормализация.** Регион → region_id (только канонические имена, иначе
   reject); единица → каноническая с scale_factor; период → period_start/period_end;
   отрицательные/нули-валюта после 2022 → фильтр по правилам карточки.
4. **Инжест.** INSERT в новый run_id; строки, отличающиеся от прошлого run,
   → series_revision с флагом `revision` в quality_flags нового run.
5. **Отчёт.** JSON: rows_parsed/inserted/rejected, ревизии, спот-чеки —
   в load_check и в stdout. `partial`/`failed` не поднимают is_current.

Парсеры переписываются под карточку: read_only openpyxl (потоково, не в память),
pyarrow для крупных CSV, батч-insert COPY (не построчный INSERT) — целевой
прогон файла ЦБ 02_18: <30 с против минут у старого конвейера.

## 5. План миграции (поэтапный, верифицируемый)

| Этап | Что | Верификация | Оценка |
|---|---|---|---|
| M0 | Схема v2 в отдельной PG-схеме `v2` на той же БД ВМ | DDL применён, витрины пустые | 0,5 ч |
| M1 | Реестр: 12 датасетов ядра (КЭП, ЕМИСС 34118, ДОМ.РФ price-index, ЦБ 0420218, Минфин, ФНС, Wordstat) | карточки в YAML + review | 1 сессия |
| M2 | Парсеры ядра + загрузка 5 приоритетных (КЭП, 34118, price-index, ЦБ, Wordstat) | спот-чеки, счётчики | 2–3 сессии |
| M3 | Ревизии + freshness + дашборд | pg_cron job | 1 сессия |
| M4 | Остальные домены, витрины, DataLens | сверка с v1 по ядру | по мере |

**Правило переноса:** ничего не копируется bulk'ом из v1 — только через
загрузчик из исходных файлов. Исключение: регионы/единицы (справочники) можно
перенести скриптом с последующей сверкой. Каждая загрузка = отдельный run_id,
значит полный откат = смена is_current.

**Точки остановки для владельца:** после M0 (схема), после M1 (реестр: состав
~60 метрик ядра — ключевой рубеж), после M2 (первые данные в витрине).

## 6. Риски и предохранители

- **Несовпадение спот-чеков** → run остаётся partial, данные не видны в витрине;
  ручное вскрытие до ретрая.
- **Расширение каталога** — только через PR-модель: карточка метрики + обоснование;
  никаких листов-«на всякий случай».
- **Росреестр** — по принятому решению живёт вне основной БД (rosreestr_separate.db);
  в v2 для него лишь ссылочный dataset без observation.
- **Старая БД не удаляется** — read-only архив; v2 заполняется параллельно;
  мостовые запросы через foreign data wrapper, если потребуется сверка.

## 7. Проверяемые гипотезы

- Г1: allowlist ~60 метрик ядра покрывает ≥90% строк существующих спецификаций
  (specs/, bridge, MIDAS) без потери функциональности — проверка на этапе M1
  прогоном спек через view v_core_panel.
- Г2: верифицированная загрузка снизит долю ложных дублей с ~30% (этап 1 v1)
  до <5% — метрика: dupes_found / total на контрольном переносе.
- Г3: время полной перезагрузки ядра <30 минут против многодневного ручного
  конвейера v1 — замер на M2.