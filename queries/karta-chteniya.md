---
title: "Карта чтения — экономика жилья и ипотеки"
type: reading-map
created: 2026-07-27
updated: 2026-07-27
tags: [map, reading, housing-economics, roadmap]
---

# 🗺 Карта чтения: экономика жилья и ипотеки

> 182 статьи в 10 кластерах · 10 аннотаций-переводов · 17.6М символов

## 🔴 Приоритет 1 — Фундамент (читать обязательно)

Эти работы определяют язык и методологию всей отрасли. Без них остальное не понять.

| № | Статья | Аннотация | Кластер | Почему первой |
|---|--------|-----------|---------|---------------|
| 1 | [Mishkin 2007](papers/mishkin-2007-housing-monetary-transmission) | ✅ | Классические модели | 6 каналов трансмиссии — базовая карта всех механизмов |
| 2 | [Iacoviello 2005](papers/iacoviello-2005-house-prices) | ✅ | ДКП→жильё | DSGE с залоговыми ограничениями — основа современных моделей |
| 3 | [DiPasquale-Wheaton 1994](papers/dipasquale-wheaton-1994-housing-market-dynamics) | ✅ | Классические модели | Stock-flow модель — структура рынка |
| 4 | [Poterba 1984](papers/poterba-1984-tax-subsidies) | ✅ | Классические модели | User cost — формула стоимости владения |
| 5 | [Bernanke 2003](papers/Bernanke-Measuring-the-Effects-of-Monetary-Policy-FAVAR-approach-2003) | ✅ | FAVAR | FAVAR — метод измерения эффектов ДКП |
| 6 | [Saiz 2010](papers/saiz-2010-geographic-determinants-housing-supply) | ✅ | Предложение/регулирование | Эластичность предложения — главный параметр пузыря |

**Ссылки на полные обзоры:**
- [[reviews/klassicheskie-modeli-ekonomiki-zhilya]]
- [[reviews/dkp-transmissiya-na-rynok-zhilya]]
- [[reviews/favar-faktornye-modeli]]
- [[reviews/predlozhenie-i-regulirovanie-zhilya]]

---

## 🟡 Приоритет 2 — Методология прогнозирования

Для построения своих моделей. Читай по направлению:

### Факторные модели (ядро)
- [Rapach 2009](papers/Rapach-Differences-in-housing-price-forecastability-across-US-states-2009) — прогнозируемость по штатам
- [Bork 2012](papers/Bork-Housing-price-forecastability-A-factor-analysis-2012) — 3 фактора из 122 рядов
- [Ng 2025](papers/Ng.-A-Hierarchical-Factor-Analysis-of-US-Housing-Market-Dynamics) — иерархические факторы
- [Mattera 2025](papers/Mattera-Forecasting-house-price-growth-rates-with-factor-models-and-spatio-temporal-clustering-2025) — пространственно-временная кластеризация

### ML и нелинейные
- [Qiongwei Ye 2024](papers/Qiongwei-Ye-House-price-prediction-using-machine-learning-for-Ames-Iowa-2024) — машинное обучение
- [Plakandaras](papers/Plakandaras-Forecasting-the-U.S.-Real-House-Price-Index) — EEMD+Elastic Net+SVR

### Nowcasting и mixed-frequency
- [Koop 2019](papers/Koop-etal-JRSSA2019-UK-regional-nowcasting-using-a-mixed-frequency-Vector-Autoregressive) — MF-VAR
- [Tallman-Zaman 2020](papers/Tallman-Zaman-IJF-2020-Combining-survey-long-run-forecasts-and-nowcasts-with-BVAR) — энтропийный наклон
- [rbnz-2025-gdp-nowcasting-dfm](papers/rbnz-2025-gdp-nowcasting-dfm) — DFM from RBNZ

**Ссылки на полные обзоры:**
- [[reviews/prognozirovanie-cen-faktornye-podhody]]
- [[reviews/ml-ne-linearnye-modeli-dlya-prognozirovaniya]]
- [[reviews/nowcasting-i-mixed-frequency-modeli]]

---

## 🟢 Приоритет 3 — Контекст и приложения

Читай после изучения фундаментальных методов.

### Международная трансмиссия
- [Corsetti 2020](papers/Corsetti-One-Money-Many-Markets-Monetary-Transmission-and-Housing-Financing-in-the-Euro-Area-2020) | ✅ аннотация | Еврозона, ARM share и LTV
- [Bandt](papers/Bandt.-The-international-transmission-of-house) — глобальные факторы
- [Shu-hen-Chiang](papers/Shu-hen-Chiang-Navigating-shifting-tides-Time-varying-monetary-policy-spillovers-in-core-peripheral-) — spillover core-periphery

### Предложение и регулирование
- [Glaeser-Gyourko-Saiz 2008](papers/glaeser-gyourko-saiz-2008-housing-supply-bubbles) | ✅ аннотация | Пузыри и предложение
- [Mayer-Somerville 2000](papers/mayer-somerville-2000-land-regulation) — земельное регулирование
- [Baum-Snow-Duranton 2025](papers/baum-snow-duranton-2025-housing-supply-affordability) — доступность и предложение

### Отчёты ЦБ и макрофинансовая стабильность
- [Adrian 2020](papers/Adrian-Predicting-Downside-Risks-to-House-Prices-and-Macro-Financial-Stability-2020) — House-Prices-at-Risk
- [BoE 2026](papers/boe-2026-house-price-expectations) — ожидания жилья и инфляция
- [Harvard-JCHS 2024](papers/Harvard-JCHS-Americas-Rental-Housing-2024) — рынок аренды
- [Effects-of-a-Mortgage-Interest-Rate-Subsidy](papers/Effects-of-a-Mortgage-Interest-Rate-Subsidy-Evidence-from-Colombia) — субсидии в Колумбии

**Ссылки на полные обзоры:**
- [[reviews/mezhdunarodnaya-transmissiya-dkp-i-zhilya]]
- [[reviews/otchety-cb-i-regulyaciya]]

---

## 🇷🇺 Российский кластер (для вашего контекста)

| Статья | Аннотация | Кластер |
|--------|-----------|---------|
| [Жирнов 2025](papers/Массовая-льготная-ипотека-продлевать-нельзя-завершать) | — | Российские исследования |
| [Жирнов 2023](papers/Льготная-ипотека-дискриминация-или-дифференциация) | — | Российские исследования |
| [Гафарова 2023](papers/geterogennost-kanala-refinansirovaniya-ipoteki-v-rossiyskih-regionah) | — | Российские исследования |
| [Рощина-Илюнькина 2021](papers/Влияние-государственных-мер-по-поддержке-ипотечного-кредитования-на-доступность-жилья-в-России-регио) | — | Российские исследования |
| [Стерник 2018](papers/Стерник-С-Г-Стерник-Г-М-2018-Методика-прогнозирован-иод-локальном) | — | Российские исследования |
| [Зубарев 2022](papers/Zubarev-Otsenka-vliyaniya-globalqnykh-shokov-na-rossiyskuyu-ekonomiku-i-naukasting-VVP-v-ramkakh-fak) | — | Российские исследования |
| [Гармидер 2020](papers/Garmider.-Ispolzovanie-modeli-favar-dlya-prognozirovaniya-rossiyskih-makroekonomicheskih-ryadov) | — | Российские исследования |
| [Фокин 2023](papers/naukasting-i-prognozirovanie-osnovnyh-rossiyskih-makroekonomicheskih-pokazateley-s-pomoschyu-mfbvar-) | — | Российские исследования |
| АКРА 2025 | — | Российские исследования |
| Strategy Partners 2025 | — | Российские исследования |
| [NRA обзор 2024](papers/nra-obzor-zhilishhnoe-stroitelstvo-ijul-2024-2) | — | Российские исследования |
| [Sherpa 2024](papers/sherpa-2024-re-market-russia) | — | Российские исследования |
| [Колечков-Тимушев 2022](papers/otrasl-stroitelstva-v-regionah-rossii-sostoyanie-faktory-i-sledstviya) | — | Российские исследования |
| [Мельков 2023](papers/ЭФФЕКТ-КОНВЕРГЕНЦИИ-ЦЕН-КАК-ФАКТОР-НЕОДНОРОДНОСТИ) | — | Российские исследования |
| [Садковкин 2024](papers/ЭКОНОМИЧЕСКАЯ-ОЦЕНКА-ВЛИЯНИЯ-КРИЗИСОВ) | — | Российские исследования |
| [Бархота 2022](papers/Феномен-жилищной-инфляции-в-контексте-инвестиционных-потребностей-строительной-индустрии) | — | Российские исследования |
| [Sherpa Digital](papers/sherpa-digital-construction-russia) | ⚠️ дубликат | Российские исследования |

**Полный обзор:** [[reviews/rossiyskie-issledovaniya-rynka-zhilya]]

---

## 🔗 Связи между кластерами

```
                ┌──────────────────────────────────┐
                │   Mishkin 2007: 6 каналов          │
                │   → user cost, wealth, credit      │
                └──────────┬───────────────────────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
     User cost      Financial      Supply
     (Poterba)     accelerator    (Glaeser)
     1984          (Iacoviello)   2008
                      2005             │
            ┌──────────────┼──────────────┐
            │              │              │
        FAVAR         DSGE         Nowcasting
        (Bernanke)   (Iacoviello)  (Koop)
        2003          2005       2019
            │              │              │
            └──────────────┼──────────────┘
                           │
                    Forecasting
                    (factor models)
                    (Rapach, Bork)
                    (Mattera)
                           │
                           │
                    International
                    (Corsetti, Chiang)
                    (Bandt)
```

---

## 📊 Итоговая статистика

| Метрика | Значение |
|---------|----------|
| Полных текстов в `papers/` | **182** |
| Кластерных обзоров в `reviews/` | **9** (101 статья) |
| Аннотаций-переводов в `annotations/` | **10** |
| Общего объёма | **17.6М символов** |
| Кластеров | **10** |
| Русскоязычных статей | **~18** |

---

## 💡 Рекомендации по чтению

1. **Начни с Mishkin 2007** — 6 каналов трансмиссии дадут тебе карту всех механизмов
2. **Затем Iacoviello 2005** — покажет, как кредитные ограничения усиливают каждый канал
3. **Потом DiPasquale-Wheaton 1994** — даст структуру (stock-flow) для понимания рынка
4. **Далее по кластерам** — сначала `rossiyskie-issledovaniya-rynka-zhilya` (тебе ближе), потом `favar-faktornye-modeli` и `dkp-transmissiya-na-rynok-zhilya`
5. **Ссылки [[...]] работают в Obsidian** — тапай по названиям статей, чтобы открыть текст