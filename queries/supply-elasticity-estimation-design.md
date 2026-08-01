---
title: "Дизайн исследования: Оценка эластичности предложения жилья на российских данных"
type: "research-design"
status: "draft"
date: "2026-08-01"
author: "Hermes Agent"
tags: ["housing-supply-elasticity", "russia", "research-design", "econometrics", "urban-economics"]
related_papers:
  - "baum-snow-han-2024-microgeography-housing-supply"
  - "saiz-2010-geographic-determinants-housing-supply"
  - "glaeser-gyourko-2018-housing-supply-jep"
  - "caldera-johansson-2013-price-responsiveness-housing-supply-oecd"
  - "hilber-vermeulen-2016-supply-constraints-england"
  - "aastveit-albuquerque-anundsen-2023"
  - "gorback-keys-2023"
related_data:
  - "eiszhk_construction_permits"
  - "eiszhk_construction_stock"
  - "eiszhk_volume_finished"
  - "cbr_mortgage_new_loans"
  - "domrf_housing_starts"
  - "rosstat_regional_accounts"
---

# Дизайн исследования: Оценка эластичности предложения жилья в России

## 1. Исследуемые вопросы

### Основной вопрос
**Какова эластичность предложения жилья в России на национальном, региональном и внутригородском уровнях, и как она меняется во времени (2015–2026)?**

### Подвопросы
1. **Межрегиональная вариация:** Чем объясняется разброс эластичности между регионами (топография, регуляция, доступность земли, структура девелоперов)?
2. **Внутригородская вариация (микрогеография):** Как эластичность меняется с расстоянием до центра, плотностью застройки, топографией (по методу Baum-Snow & Han 2024)?
3. **Структурные сдвиги:** Как изменение доли малых девелоперов (22% → 27% в разрешениях, новость Urban 2026) и рост ИЖС влияют на агрегатную эластичность?
4. **Временная динамика:** Падает ли эластичность со временем (как в США: Saiz 2.6 → 1.3, Baum-Snow & Han 0.5)?
5. **Политические импликации:** Как эластичность медирует передачу монетарной политики через ипотечный канал (Andaloussi et al. 2024)?

---

## 2. Обзор литературы: методологические подходы

| Подход | Ключевые работы | Применимость к России |
|--------|----------------|----------------------|
| **Cross-section (Saiz 2010)** | Saiz (2010), Hilber & Vermeulen (2016) | Базовый бенчмарк, нужны инструменты |
| **Panel / Long diffs** | Aastveit et al. (2023), Cosman et al. (2018) | Есть панель регионов 2015–2026 |
| **Microgeography (tract-level)** | Baum-Snow & Han (2024), Büchler et al. (2021) | Требует трактовые данные (ЕИСЖС + Росстат) |
| **Structural / Model-based** | Glaeser & Gyourko (2018), Caldera & Johansson (2013) | P/MPPC, user cost model |
| **IV: Bartik + commuting** | Baum-Snow & Han (2024) | Есть матрица перемещений (Росстат) |
| **IV: Geography/Topography** | Saiz (2010), Gorback & Keys (2023) | DEM,坡度, вода — доступны |
| **IV: Regulation indices** | Hilber & Vermeulen (2016), Gyourko & Molloy (2014) | Нужен российский аналог WRLURI |

---

## 3. Доступные данные в базе

### 3.1. Количественные данные (Parquet в `data/processed/`)

| Источник | Переменные | Частота | География | Годы |
|----------|-----------|---------|-----------|------|
| **ЕИСЖС (13 файлов)** | Разрешения, ввод, фонд строящегося, ДДУ, цены, ИЖС | Месяц | 85 субъектов + ФО + РФ | 2015–2026 |
| **ЦБ РФ** | Новые ипотечные кредиты (объём, кол-во, по валютам), курсы USD/EUR | Месяц | 96 регионов | 2019–2026 |
| **ДОМ.РФ (CSV)** | Ввод жилья, реализация квартир, цены | Квартал/Месяц | Регионы (ручной экспорт) | 2024+ |
| **Росстат (планируется)** | ВВП региональный, население, доходы, занятость, инвестиции в ЖКХ | Год/Квартал | 85 субъектов | 2015–2026 |

### 3.2. Пространственные единицы

| Уровень | Единиц | Источник границ | Примечание |
|---------|--------|-----------------|------------|
| **Субъекты РФ** | 85 | Росстат | Основной для панельного анализа |
| **Города/Районы** | ~1,100 | Росстат / ЕИСЖС (по кодам ОКТМО) | Для внутригородской вариации |
| **Переписные участки (тракты)** | ~50к+ | Росстат 2020 | Требует привязки ЕИСЖС к ОКТМО |
| **Квартиры/Участки (микро)** | — | ЕИСЖС (проектные декларации) | Для hedonic price indices |

### 3.3. Инструментальные переменные (доступны/собираемы)

| IV | Источник | Статус |
|----|----------|--------|
| **Bartik-шоки через матрицу перемещений** | Росстат (перемещения 2010/2020) + отраслевая занятость | 🟡 Требует сборки |
| **Топография: %평плоской земли, elevation range, water** | SRTM/ASTER DEM (30м) | 🟢 Готово (скачать) |
| **Доступность земли: % застроено, расстояние до границы** | ЕИСЖС (фонд строящегося) + сателлит | 🟡 Частично |
| **Регуляция: региональные нормы застройки, ПЗЗ** | Градостроительные кодексы субъектов | 🔴 Требует ручного сбора |
| **Исторические: население 1989/2002/2010/2020** | Росстат переписи | 🟢 Готово |
| **Доля малых девелоперов / ИЖС в вводе** | ЕИСЖС + новость Urban | 🟢 Готово |

---

## 4. Методологические спецификации

### 4.1. Уровень 1: Межрегиональная панель (Saiz-style)

```stata
* Long-difference 2015→2026 или панель с FE
Δln(Housing_Stock_rt) = α + β Δln(Price_rt) + γ X_rt + μ_r + λ_t + ε_rt

* IV: Bartik_shock_rt (отраслевая занятость 2015 × нац. рост отрасли)
* Контролы: доходы, население, ипотечные ставки (ЦБ РФ), доля ИЖС, доля малых девелоперов
```

**Ожидаемый результат:** эластичность по регионам (0.3–2.5), регрессия β на характеристики регионов.

### 4.2. Уровень 2: Внутригородская микрогеография (Baum-Snow & Han 2024)

```python
# Уравнение предложения на уровне тракта i в регионе r
Δln(Q_irt) = γ_ir × Δln(P_irt) + ε_irt

# Гетерогенность γ_ir:
γ_ir = γ_0 + γ_1 × CBD_dist_ir + γ_2 × Developed_Share_ir
       + γ_3 × Flat_Share_ir + γ_4 × Slope_ir
       + γ_5 × Small_Dev_Share_ir + γ_6 × IZH_Share_ir
       + γ_7 × Regulation_Index_r + u_ir

# IV: Simulated Bartik через commuting matrix (как в Baum-Snow & Han)
# First stage: Δln(P_irt) = π_0 + π_1 × Simulated_RMA_Shock_irt + controls
```

**Требует:** привязка ЕИСЖС к трактам (ОКТМО → тракт), матрица перемещений.

### 4.3. Уровень 3: Структурная / P-MPPC (Glaeser & Gyourko 2018)

```python
# Price-to-Cost ratio (Tobin's q для жилья)
P/MPPC = Price_per_sqm / (Construction_Cost_per_sqm + Land_Cost_per_sqm)

# Construction cost: Росстат (индексы стоимости строительства) + локальные коэффициенты
# Land cost: остаточный метод или аукционы за землю
# P/MPPC > 1 → regulatory constraint / supply inelasticity
# Панель по городам/районам 2015–2026
```

### 4.4. Уровень 4: User Cost Model (Himmelberg, Mayer & Sinai 2005)

```python
User_Cost = r_rf + τ × (r_m + τ_prop) + δ + γ - g^e + ρ
# r_rf: безрисковая ставка (ОФЗ)
# r_m: ипотечная ставка (ЦБ РФ по регионам)
# τ: налоговая ставка (НДФЛ 13%/15%)
# δ: износ (2.5%/год)
# γ: обслуживание (1–2%)
# g^e: ожидаемый рост цен (адаптивные ожидания или сервеи)
# ρ: риск-премия

# Imputed_Rent = Price / User_Cost
# Imputed_Rent / Actual_Rent → индикатор переоценки
# Панель по городам
```

---

## 5. План реализации (поэтапный)

### Этап 1: Подготовка данных (1–2 недели)
- [ ] Скачать DEM (SRTM 30м) для России → посчитать %плоской земли, elevation range, water bodies по регионам/городам
- [ ] Собрать матрицу перемещений (Росстат 2010/2020) → построить Bartik-шоки
- [ ] Привязать ЕИСЖС к ОКТМО/трактам (коды в данных есть)
- [ ] Собрать региональные индексы регуляции (минимум: макс. этажность, ПЗЗ, парковка) — опрос/парсинг кодексов
- [ ] Дополнить Росстат: ВВП на душу, доходы, население, занятость по субъектам 2015–2026

### Этап 2: Базовые оценки (1 неделя)
- [ ] Saiz-style cross-section: long-diff 2015→2026 по 85 регионам
- [ ] Панель с FE: эластичность по регионам + тест на устойчивость
- [ ] P/MPPC по крупным городам (топ-30 по населению)
- [ ] User Cost model по тем же городам

### Этап 3: Микрогеография (2–3 недели)
- [ ] Агрегация ЕИСЖС до трактов (или городских округов, если тракты недоступны)
- [ ] Построение матрицы перемещений тракт-тракт (гравитационная модель на основе расстояний/дорог)
- [ ] IV оценка γ_ir с гетерогенностью по CBD_dist, developed_share, flat_share, slope
- [ ] Декомпозиция: new construction vs redevelopment vs renovation (как Baum-Snow & Han)

### Этап 4: Структурные сдвиги (1 неделя)
- [ ] Включение `small_dev_share_permits` и `izh_share_completions` в уравнение предложения
- [ ] Counterfactual: какая бы была эластичность при структуре 2021 г.?
- [ ] Роль ВПК-стимула: interaction `defense_spending × small_dev_share`

### Этап 5: Политический анализ (1 неделя)
- [ ] Передача монетарной политики: `Δrate → Δmortgage → Δprice` медируется через `γ_r`
- [ ] Симуляция: эффект снижения ставки на 1 п.п. в регионах с высокой/низкой эластичностью
- [ ] Welfare: deadweight loss от регуляции (как Baum-Snow & Han для Opportunity Zones)

---

## 6. Ожидаемые вклады

| Вклад | Новизна для России |
|-------|-------------------|
| **Первые тракт-уровневые эластичности** | Нет работ с микрогеографией для РФ |
| **Динамика 2015–2026** | Покрывает цикл: рост → пандемия → ипотечный бум →紧缩 |
| **Роль ИЖС и малых девелоперов** | Уникальные данные Urban + ЕИСЖС |
| **Связь с монетарной политикой** | Andaloussi et al. (2024) контекст для РФ |
| **Открытые данные и код** | Reproducible pipeline в research-wiki |

---

## 7. Риски и митигация

| Риск | Вероятность | Митигация |
|------|-------------|-----------|
| Нет трактовых границ / привязки ЕИСЖС | 🟡 Средняя | Использовать городские округа / районы (ОКТМО) как fallback |
| Нет регионального индекса регуляции (WRLURI-аналог) | 🔴 Высокая | 1) Собрать минимальный набор (этажность, ПЗЗ) 2) Использовать топографию как прокси 3) IV через исторические данные |
| ЕИСЖС не покрывает все города | 🟢 Низкая | Покрытие 85 субъектов, основные города есть |
| Эндогенность цен (simultaneity) | 🔴 Высокая | IV: Bartik + topography + historical instruments |
| Структурный срыв 2022 г. (санкции, миграция) | 🔴 Высокая | Включить dummy/post-2022 trend, разбить выборку |

---

## 8. Связь с существующей базой знаний

### Концепты для обновления
- `concepts/econometric-models-housing-market.md` — добавить строки: Microgeography IV, Russian Regional Panel, IZH Supply Elasticity
- `concepts/data-sources-housing-econometrics.md` — документировать ЕИСЖС, ЦБ РФ, Дом.РФ как готовые источники

### Рецензии для написания
- `reviews/russian-housing-supply-elasticity-overview.md` — обзор методов и результатов
- `reviews/baam-snow-han-2024-application-russia.md` — адаптация методологии

### Данные для инжестора (новые источники в `catalog.yaml`)
```yaml
- id: "dem_russia_srtm"
  name: "SRTM DEM Russia (topography)"
  type: "remote_raster"
  format: "geotiff"
  url: "https://srtm.csi.cgiar.org/srtmdata/"
  variables: ["slope", "elevation_range", "flat_share", "water_share"]
  geography: "russia_30m"
  schedule: "once"

- id: "rosstat_commuting_matrix"
  name: "Матрица перемещений населения (Перепись 2020)"
  type: "local_file"
  format: "xlsx"
  path: "data/raw/rosstat/commuting_2020.xlsx"
  schedule: "once"

- id: "regional_regulation_index"
  name: "Региональный индекс регуляции застройки"
  type: "manual_construct"
  format: "csv"
  path: "data/raw/regulation/regional_regulation_index.csv"
  variables: ["max_floor", "far_limit", "parking_norm", "green_space_norm", "pzz_strictness"]
  schedule: "annual"
```

---

## 9. Следующие шаги (immediate)

1. **Скачать SRTM DEM** для России и вычислить топографические переменные по регионам/городам
2. **Запросить/найти матрицу перемещений** Росстат 2020 (или построить гравитационную на расстояниях)
3. **Начать сбор региональной регуляции** — минимум топ-30 городов
4. **Запустить базовую Saiz-style регрессию** на имеющихся панельных данных (ЕИСЖС + ЦБ РФ + Росстат региональные аккаунты)
5. **Написать скрипт `scripts/estimate_supply_elasticity.py`** с модульной структурой для 4 уровней оценки

---

## 10. Референции (ключевые для реализации)

```bibtex
@article{saiz2010geographic,
  title={The geographic determinants of housing supply},
  author={Saiz, Albert},
  journal={Quarterly Journal of Economics},
  volume={125}, number={3}, pages={1253--1296}, year={2010}
}

@article{baum2024microgeography,
  title={The microgeography of housing supply},
  author={Baum-Snow, Nathaniel and Han, Lu},
  journal={Journal of Political Economy},
  volume={132}, number={6}, year={2024}
}

@article{glaeser2018housing,
  title={Housing supply and housing policy},
  author={Glaeser, Edward L and Gyourko, Joseph},
  journal={Journal of Economic Perspectives},
  volume={32}, number={1}, pages={3--30}, year={2018}
}

@article{caldera2013price,
  title={The price responsiveness of housing supply in OECD countries},
  author={Caldera, Aida and Johansson, Åsa},
  journal={Journal of Housing Economics},
  volume={22}, number={3}, pages={231--249}, year={2013}
}

@article{andaloussi2024housing,
  title={Housing markets and monetary policy},
  author={Andaloussi, Mehdi Benatiya and Biljanovska, Nina and De Stefani, Alessia},
  journal={Finance and Development},
  volume={61}, number={4}, pages={48--51}, year={2024}
}

@article{himmelberg2005assessing,
  title={Assessing high house prices: Bubbles, fundamentals and misperceptions},
  author={Himmelberg, Charles and Mayer, Christopher and Sinai, Todd},
  journal={Journal of Economic Perspectives},
  volume={19}, number={4}, pages={67--92}, year={2005}
}
```

---

## Приложение: Структура репозитория для проекта

```
research-wiki/
├── scripts/
│   ├── estimate_supply_elasticity.py      # Основной скрипт (4 уровня)
│   ├── prepare_topography.py              # SRTM → переменные по регионам/трактам
│   ├── build_bartik_instruments.py        # Матрица перемещений → Bartik shocks
│   ├── collect_regulation_index.py        # Парсинг/ручной ввод регуляции
│   └── query.py                           # Уже есть: SQL + NL к DuckDB
├── data/
│   ├── raw/
│   │   ├── srtm_russia/                   # DEM файлы
│   │   ├── rosstat/commuting_2020.xlsx
│   │   └── regulation/regional_regulation_index.csv
│   └── processed/
│       ├── supply_elasticity_region.parquet
│       ├── supply_elasticity_tract.parquet
│       └── p_mpcp_city.parquet
├── concepts/
│   ├── econometric-models-housing-market.md
│   └── data-sources-housing-econometrics.md
├── reviews/
│   ├── russian-housing-supply-elasticity-overview.md
│   └── baum-snow-han-2024-application-russia.md
└── queries/
    └── supply-elasticity-estimation-plan.md (этот файл)
```

---

*Документ создан автоматически на основе накопленной базы знаний. Требует ревью и доработки перед запуском.*