# Каталог базы данных rosstat_construction.db

**Файл:** `data/rosstat_construction.db` (SQLite, ~757 МБ)
**Создан:** 2026-08-19
**Записей всего:** ~1 215 000+

---

## Сводная таблица

| # | Таблица | Записей | Период | Уровень | Источник |
|---|---------|---------|--------|---------|----------|
| 1 | `domrf_indicators` | 1 135 888 | 2020–2026 (мес.) | 85+ рег. | ДОМ.РФ |
| 2 | `observations` | 50 293 | 1990–2026 | 85+ рег. | Росстат folder/14458 |
| 3 | `housing_prices_quarterly` | 7 886 | 2016–2026 (кв.) | 102 рег. | Росстат info-stat 10-05 |
| 4 | `unfinished_construction_regional` | 6 970 | 2000–2024 | 97 рег. | Pril_Region_Pokaz 2025 |
| 5 | `housing_prices_regional` | 2 919 | 2000–2023 | 96 рег. | Stroit_Pril_2024 3.2 |
| 6 | `building_completions_regional` | 2 367 | 2000–2024 | 96 рег. | Pril_Region_Pokaz 2025 |
| 7 | `materials_production_fd` | 748 | 2016–2023 | 8 ФО | Stroit_Pril_2024 8 |
| 8 | `construction_employment` | 358 | 2010–2024 | 85 рег. | Trud_2025 + Stroit_2024 |
| 9 | `indicators` | 54 | — | (метаданные) | Росстат folder/14458 |
| 10 | `materials_production_rf` | 179 | 2017–2023 | РФ | Stroit_2024 8.1 |
| 11 | `materials_import` | 114 | 2015–2021 | РФ | Stroit_2024 8.6 |
| 12 | `materials_capacity_utilization` | 109 | 2017–2023 | РФ | Stroit_2024 8.5 |
| 13 | `construction_machinery` | 696 | 2020–2023 | 85 рег. | Stroit_Pril_2024 2.11 |
| 14 | `machinery_production` | 56 | 2017–2023 | РФ | Stroit_2024 2.26 |
| 15 | `machinery_import` | 30 | 2015–2021 | РФ | Stroit_2024 8.6 |

---

## 1. `domrf_indicators` — ДОМ.РФ (1 135 888 записей)

**Источник:** `raw/domrf/` (9 XLSX, 8.2 МБ) с https://наш.дом.рф/аналитика/статистические_ряды

### Схема

```sql
CREATE TABLE domrf_indicators (
    id INTEGER PRIMARY KEY,
    file_name TEXT,          -- исходный XLSX файл
    sheet_name TEXT,          -- лист в XLSX
    indicator_code TEXT,      -- код показателя (номер листа)
    indicator_name TEXT,      -- название показателя
    region_name TEXT,         -- регион (85+ субъектов + ФО + РФ)
    date TEXT,                -- дата (YYYY-MM-DD, помесячно)
    value REAL,                -- значение
    unit TEXT,                -- единица (шт., м², руб., %)
    data_type TEXT,           -- тип данных (см. ниже)
    source TEXT,              -- 'ДОМ.РФ статистические ряды'
    updated_at TEXT
);
```

### Типы данных (`data_type`)

| data_type | Записей | Показателей | Регионов | Описание |
|-----------|---------|-------------|----------|----------|
| `stock` | 356 400 | 45 | 99 | МКД сток: строящиеся, проданные, непроданные |
| `flow` | 312 840 | 39 | 99 | Проекты: ввод в действие (поток по месяцам) |
| `ddu_nonres` | 118 292 | 9 | 108 | ДДУ нежилые + машино-места (регионы/застройщики) |
| `stock_krt` | 82 368 | 24 | 99 | МКД КРТ (комплексное развитие территорий) |
| `ddu` | 40 392 | 6 | 99 | ДДУ: кол-во, площадь, цена (214-ФЗ + 215-ФЗ) |
| `permits_stock` | 38 640 | 5 | 125 | **Разрешения на строительство** (сток, накопленные) |
| `sales_meters` | 35 200 | 1 | 112 | Реализация квартир, м² |
| `sales_pct` | 33 216 | 1 | 112 | Реализация квартир, % |
| `permits_flow` | 31 408 | 4 | 100 | **Разрешения на строительство** (поток, выданные за мес.) |
| `readiness` | 17 777 | 1 | 6 | Уровень строительной готовности |
| `ddu_parking` | 13 464 | 1 | 99 | ДДУ машино-места: кол-во действующих |
| `ddu_parking_area` | 13 464 | 1 | 99 | ДДУ машино-места: площадь |
| `ddu_parking_price` | 13 464 | 1 | 99 | ДДУ машино-места: цена |
| `ddu_nonres_area` | 13 464 | 1 | 99 | ДДУ нежилых: площадь |
| `ddu_nonres_price` | 13 464 | 1 | 99 | ДДУ нежилых: цена |
| `sales` | 1 178 | 1 | 7 | РФ сводный (реализация) |
| `mortgage` | 852 | 13 | 1 | Ипотечное жилищное кредитование (ИЖК) |
| `summary` | 5 | 1 | 4 | Сводные показатели |

### Ключевые показатели (РФ)

| Показатель | data_type | Дата начала | Дата конца | Значение нач. | Значение кон. |
|-----------|-----------|-------------|-----------|----------------|---------------|
| Кол-во МКД с РНС (сток) | permits_stock | 2025-01 | 2026-08 | 17 695 | **20 727** |
| Площадь МКД с РНС (сток) | permits_stock | 2025-01 | 2026-08 | 239,5M м² | **303,3M м²** |
| Кол-во МКД с РНС (поток/мес.) | permits_flow | 2024-01 | 2026-07 | 370 | **320** |
| ДДУ действующие (214-ФЗ) | ddu | 2021-01 | 2026-08 | 747 199 | **771 617** |
| ДДУ площадь (214-ФЗ) | ddu | 2021-01 | 2026-08 | 42,0M м² | **36,5M м²** |
| ДДУ цена (214-ФЗ) | ddu | 2021-01 | 2026-08 | 3,75 трлн | **8,01 трлн** |
| Строящееся жильё | stock | 2020-01 | 2026-08 | 107,5M м² | **120,1M м²** |
| Продано ( stock) | stock | 2020-01 | 2026-08 | 43,9M м² | — |
| ИЖК траншей (год) | mortgage | 2024 | 2026 | 384 711 | 17 057 |

### SQL-запросы

```sql
-- Разрешения на строительство по регионам (последний месяц)
SELECT region_name, indicator_name, value, date
FROM domrf_indicators
WHERE data_type = 'permits_stock'
  AND date = (SELECT MAX(date) FROM domrf_indicators WHERE data_type = 'permits_stock')
ORDER BY value DESC LIMIT 20;

-- ДДУ по регионам ( динамика)
SELECT region_name, date, value
FROM domrf_indicators
WHERE data_type = 'ddu'
  AND indicator_name LIKE '%Количество действующих%214%'
  AND region_name IN ('Российская Федерация', 'г. Москва', 'Московская область')
ORDER BY region_name, date;

-- Ввод в действие МКД по месяцам (РФ)
SELECT date, indicator_name, value
FROM domrf_indicators
WHERE data_type = 'flow'
  AND region_name = 'Российская Федерация'
  AND indicator_name LIKE '%Количество многоквартирных домов%'
ORDER BY date;
```

---

## 2. `observations` — Росстат folder/14458 (50 293 записей)

**Источник:** 35 XLSX/XLS файлов из https://rosstat.gov.ru/folder/14458

### Схема

```sql
CREATE TABLE observations (
    id INTEGER PRIMARY KEY,
    indicator_id INTEGER,    -- FK → indicators.id
    region_name TEXT,        -- регион
    row_label TEXT,          -- метка строки (доп. разбивка)
    period TEXT,             -- период (год или диапазон)
    period_type TEXT,        -- 'annual' | 'monthly'
    value REAL,               -- числовое значение
    value_str TEXT,          -- текстовое значение
    source_file TEXT,        -- исходный файл
    updated_at TEXT
);
```

### Категории показателей (таблица `indicators`, 54 шт.)

| Категория | Кол-во | Примеры показателей |
|-----------|--------|---------------------|
| `housing_input_operational` | 19 | Ввод жилья (оперативные данные, помесячно) |
| `housing_input_regions` | 15 | Ввод жилья по регионам (годовые ряды) |
| `unfinished_construction` | 7 | Незавершённое строительство |
| `construction_works` | 3 | Объём работ по ВЭД «Строительство» |
| `housing_per_1000` | 1 | Ввод жилья на 1000 чел. |
| `housing_cost` | 1 | Стоимость 1 м² жилья |
| `housing_construction` | 1 | Ввод жилья всего |
| `cost_structure` | 1 | Структура затрат на строительство |
| `construction_by_ownership` | 1 | Ввод по формам собственности |
| `capacity_utilization` | 1 | Загрузка мощностей строительных организаций |
| `buildings_input` | 1 | Ввод зданий (жилые + нежилые) |
| `nonresidential_buildings` | 1 | Ввод нежилых зданий по типам |
| `production_capacity` | 1 | Ввод производственных мощностей |
| `social_facilities_culture` | 1 | Ввод объектов культуры |

---

## 3. `housing_prices_quarterly` — Цены на жильё (7 886 записей)

**Источник:** Росстат info-stat-06-2026, 10-05 «Цены на первичном и вторичном рынках жилья»

```sql
CREATE TABLE housing_prices_quarterly (
    id INTEGER PRIMARY KEY,
    region_name TEXT,        -- 102 региона
    year INTEGER,            -- 2016–2026
    quarter INTEGER,         -- 1–4
    market TEXT,              -- 'primary' | 'secondary'
    price_per_sqm REAL,       -- руб./м²
    unit TEXT,
    source TEXT,
    updated_at TEXT
);
```

---

## 4. `housing_prices_regional` — Годовые цены (2 919 записей)

**Источник:** Stroit_Pril_2024, лист 3.2

```sql
CREATE TABLE housing_prices_regional (
    id INTEGER PRIMARY KEY,
    region_name TEXT,        -- 96 регионов
    year INTEGER,            -- 2000–2023
    market TEXT,              -- 'primary' | 'secondary'
    price_per_sqm REAL,       -- тыс. руб./м²
    unit TEXT,
    source TEXT,
    updated_at TEXT
);
```

---

## 5. `building_completions_regional` — Ввод зданий (2 367 записей)

**Источник:** Pril_Region_Pokaz_2025, Раздел 14 (листы 14.2.1, 14.2.2)

```sql
CREATE TABLE building_completions_regional (
    id INTEGER PRIMARY KEY,
    region_name TEXT,        -- 96 регионов
    year INTEGER,            -- 2000–2024
    indicator TEXT,          -- 'buildings_completed_count' | 'buildings_completed_area'
    value REAL,               -- шт. или тыс. м²
    unit TEXT,
    source TEXT,
    updated_at TEXT
);
```

---

## 6. `unfinished_construction_regional` — Незавершённое строительство (6 970 записей)

**Источник:** Pril_Region_Pokaz_2025, Раздел 14 (листы 14.7, 14.8)

```sql
CREATE TABLE unfinished_construction_regional (
    id INTEGER PRIMARY KEY,
    region_name TEXT,        -- 97 регионов
    year INTEGER,            -- 2000–2024
    indicator TEXT,          -- 'unfinished_buildings_count' | 'unfinished_houses_count' | 'unfinished_houses_area'
    value REAL,
    unit TEXT,
    source TEXT,
    updated_at TEXT
);
```

---

## 7. `construction_employment` — Занятость в строительстве (358 записей)

**Источник:** Trud_2025 R_9_pril + Stroit_2024 R-2-3 + Ejegodnik_2025 R_05

```sql
CREATE TABLE construction_employment (
    id INTEGER PRIMARY KEY,
    region_name TEXT,        -- 85 регионов
    year INTEGER,            -- 2010–2024
    employment_thousands REAL,  -- тыс. чел.
    share_of_total_pct REAL,     -- доля от общей занятости, %
    source TEXT,
    updated_at TEXT
);
```

---

## 8. `construction_machinery` — Парк строительной техники (696 записей)

**Источник:** Stroit_Pril_2024 R_10_2_4_pril, лист 2.11

```sql
CREATE TABLE construction_machinery (
    id INTEGER PRIMARY KEY,
    region_name TEXT,        -- 85 регионов
    year INTEGER,            -- ~2021, ~2023 (2 среза)
    machine_type TEXT,       -- 'excavators' | 'bulldozers' | 'cranes' | 'loaders'
    count_total INTEGER,     -- кол-во, шт.
    pct_expired_service REAL, -- % с истекшим сроком службы
    pct_foreign_made REAL,   -- % импортных
    source TEXT,
    updated_at TEXT
);
```

---

## 9. `materials_production_rf` — Производство материалов РФ (179 записей)

**Источник:** Stroit_2024, табл. 8.1–8.2

```sql
CREATE TABLE materials_production_rf (
    id INTEGER PRIMARY KEY,
    year INTEGER,            -- 2017–2023
    product_name TEXT,       -- 27 продуктов (цемент, ж/б, кирпич, стекло, и т.д.)
    value REAL,
    unit TEXT,
    source TEXT
);
```

---

## 10. `materials_production_fd` — Производство материалов по ФО (748 записей)

**Источник:** Stroit_Pril_2024 R_10_8_pril (13 листов)

```sql
CREATE TABLE materials_production_fd (
    id INTEGER PRIMARY KEY,
    year INTEGER,            -- 2016–2023
    federal_district TEXT,   -- 8 ФО
    product_name TEXT,       -- 13 продуктов
    value REAL,
    unit TEXT,
    source TEXT
);
```

---

## 11. `materials_capacity_utilization` — Загрузка мощностей (109 записей)

**Источник:** Stroit_2024, табл. 8.5

```sql
CREATE TABLE materials_capacity_utilization (
    id INTEGER PRIMARY KEY,
    year INTEGER,            -- 2017–2023
    product_name TEXT,       -- 17 продуктов
    utilization_pct REAL,    -- % загрузки
    source TEXT
);
```

---

## 12. `materials_import` — Импорт материалов (114 записей)

**Источник:** Stroit_2024, табл. 8.6

```sql
CREATE TABLE materials_import (
    id INTEGER PRIMARY KEY,
    year INTEGER,            -- 2015–2021
    product_name TEXT,       -- 19 продуктов
    value REAL,
    unit TEXT,
    source TEXT
);
```

---

## 13. `machinery_production` — Производство техники (56 записей)

**Источник:** Stroit_2024, табл. 2.26

```sql
CREATE TABLE machinery_production (
    id INTEGER PRIMARY KEY,
    year INTEGER,            -- 2017–2023
    product_name TEXT,       -- 8 продуктов (краны башенные, экскаваторы, и т.д.)
    value REAL,
    unit TEXT,
    source TEXT
);
```

---

## 14. `machinery_import` — Импорт техники (30 записей)

**Источник:** Stroit_2024, табл. 8.6

```sql
CREATE TABLE machinery_import (
    id INTEGER PRIMARY KEY,
    year INTEGER,            -- 2015–2021
    product_name TEXT,       -- 5 продуктов
    value REAL,
    unit TEXT,
    source TEXT
);
```

---

## Источники данных

| Источник | Файлы | Период | Уровень |
|----------|-------|--------|---------|
| **ДОМ.РФ** (наш.дом.рф) | 9 XLSX, 8.2 МБ | 2020–2026 | 85+ рег., помес. |
| **Росстат** folder/14458 | 35 XLSX | 1990–2026 | 85+ рег. |
| **Росстат** folder/11109 | 112 XLSX/DOC/PDF | 2026 | 85 рег. |
| **Росстат** folder/210 (ежегодники) | DOCX/XLSX | 2000–2025 | 85 рег. |
| Stroit_2024 «Строительство в России» | DOCX | 2015–2023 | РФ + 85 рег. |
| Stroit_Pril_2024 | XLSX | 2000–2023 | 85 рег. |
| Stroit_2022 (PDF) | PDF | 2020–2021 | РФ |
| Stroit_Pril_2022 | XLSX | ~2021 | 85 рег. |
| Pril_Region_Pokaz_2025 | XLSX | 2000–2024 | 85 рег. |
| Ejegodnik_2025 | DOCX | 2022–2024 | РФ |
| Trud_2025 / Pril_Trud_2025 | XLSX/DOCX | 2010–2024 | 85 рег. |

---

## Индексы

```sql
-- domrf_indicators
CREATE INDEX idx_domrf_region ON domrf_indicators(region_name);
CREATE INDEX idx_domrf_date ON domrf_indicators(date);
CREATE INDEX idx_domrf_indicator ON domrf_indicators(indicator_code);
CREATE INDEX idx_domrf_file ON domrf_indicators(file_name);

-- observations
CREATE INDEX idx_obs_indicator ON observations(indicator_id);
CREATE INDEX idx_obs_region ON observations(region_name);
```

---

## Обновление

```bash
# Обновление данных Росстат (folder/14458)
python scripts/update_rosstat.py --priority 3   # ежемесячно
python scripts/update_rosstat.py --priority 2   # ежеквартально
python scripts/update_rosstat.py --rebuild      # раз в год

# Импорт ДОМ.РФ (ручной, после скачивания XLSX из браузера)
# 1. Скачать файлы с https://наш.дом.рф/аналитика/статистические_ряды
# 2. Поместить в raw/domrf/
# 3. Запустить импорт (см. код в session history)
```