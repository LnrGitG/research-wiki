---
title: MNB WP 2026/3 — Sentiment-based Financial Stress Index for Hungary
type: review
created: 2026-07-29
updated: 2026-07-29
tags: [review, sentiment-analysis, financial-stress, Hungary, MNB, CDS, Granger-causality, spillover]
paper_ref: papers/mnb-wp-2026-3-sentiment-financial-stress-index-hungary.md
---

# Обзор: MNB Working Papers 2026/3 — Sentiment-based Financial Stress Index for Hungary

**Авторы:** Beáta Horváth, Tamás Berki, Lívia Réka Ónozó, Csanád Temesvári (MNB)  
**Дата:** июль 2026  
**DOI/URL:** https://www.mnb.hu/letoltes/mnb-wp-2026-3-final-1.pdf

---

## 🎯 Суть вклада (one-liner)

Построен **SFSI (Sentiment-based Financial Stress Index)** для Венгрии на новостных текстах 2005–2020: булевый словарный алгоритм (co-occurrence двух наборов терминов) + LDA-фильтрация статей. Индекс **ведущий по отношению к CDS-спредам** (Granger p<0.001), объясняет **60% дисперсии ошибки прогноза CDS в долгосроке** (FEVD), доминирует в spillover-анализе на горизонтах h≥3 (62% при h=12). Дополняет FISS (MNB): FISS лучше на краткосроке (h≤3), SFSI — на средне/долгосроке (h≥3). Ключевое преимущество: **производится в real-time на любой частоте**.

---

## 📊 Методология: что нового

| Компонент | Решение | Почему важно |
|-----------|---------|--------------|
| **Источник** | 2 венгерских новостных портала, ~95 ст./день, 2005–2020 | Охватывает GFC, еврокризис, конверсию FX-кредитов, COVID |
| **Фильтрация** | LDA (16 топиков, 13 экономических) | Убирает шум (таблоиды, погода) — без LDA индекс крайне волатилен, низкий S/N |
| **Индексация** | Boolean co-occurrence: N_F × N_S на статью, потом mean | Не считает частоту терминов — ловит *доминирование нарратива* о кризисе в тексте |
| **Ключевые слова** | 2 набора: (1) финансовый кризис, (2) сегменты фин. системы | Экспертный отбор + двухстадийный ARMA-sensitivity отбор (убрали избыточные) |
| **Частота** | Любая (daily/weekly/monthly) | Real-time мониторинг — преимущество перед FISS (высокая частота, но с лагает по публикации) |

---

## 🔬 Эмпирика: главные результаты

### 1. Granger-причинность (Toda-Yamamoto)
| Направление | χ² | p-value | Вывод |
|-------------|-----|---------|-------|
| **SFSI → CDS** | 19.01 | 0.000 | **SFSI ведёт CDS** (1 месяц вперёд) |
| CDS → SFSI | 0.09 | 0.761 | Нет обратной причинности |
| FISS ↔ CDS | 16.20 / 7.67 | 0.001 / 0.054 | **Двунаправленно** |
| EPU EU ↔ CDS | 8.63 / 9.18 | 0.125 / 0.102 | Незначимо |
| GPRI HU ↔ CDS | 1.53 / 1.33 | 0.67 / 0.72 | Незначимо |

### 2. Generalized IRF (шок → CDS spread)
| Индекс | Мгновенный эффект | Пик | Горизонт пика | Затухание |
|--------|-------------------|-----|---------------|-----------|
| **SFSI** | +12–13 бп | **~30 бп** | **месяц 5** | ~24 мес. |
| FISS | чуть сильнее | ~25 бп | месяц 2 | месяц 10 |
| EPU EU | слабее | ~10 бп | месяц 2 | незначим с 5-го мес. |
| GPRI HU | — | незначим | — | — |

**Интерпретация:** SFSI даёт **устойчивый, накапливающийся эффект** — структурная информация, полезна для среднесрочного риск-менеджмента.

### 3. FEVD (доля дисперсии ошибки прогноза CDS)
| Горизонт | CDS (own) | **SFSI** | FISS | EPU | GPRI |
|----------|-----------|----------|------|-----|------|
| Краткосрочный | ~100% | 12% | — | — | — |
| 5 мес. | — | **40%** | — | — | — |
| Долгосрочный | **30%** | **60%** | ~15–20% | низко | низко |

→ SFSI становится **доминирующим драйвером** CDS-спреда в долгосроке.

### 4. Diebold-Yilmaz Spillover (directional → CDS)
| Индекс | h=1 | h=2 | h=3 | h=6 | h=12 |
|--------|-----|-----|-----|-----|------|
| FISS | 19.95 | 22.33 | 24.56 | 30.36 | 38.35 |
| **SFSI** | 13.00 | **22.70** | **31.32** | **48.54** | **61.96** |
| EPU EU | 2.59 | 3.12 | 3.63 | 4.90 | 6.49 |
| GPRI HU | 0.25 | 0.75 | 1.02 | 1.33 | 1.49 |
| **SFSI+FISS** | 24.45 | 33.99 | 41.91 | 56.67 | **67.21** |

- h=1: FISS чуть сильнее (краткосрочная чувствительность рынка)
- **h≥3: SFSI доминирует** — news sentiment передаёт системный стресс дольше
- Комбинация SFSI+FISS = **best of both worlds**

### 5. Dynamic (rolling 60m) spillover
- COVID-19: резкий скачок spillover во всех моделях
- На h=6: **SFSI становится главным передатчиком шоков** к FISS и CDS
- Эффект持久: долгая медийная атеншн + запаздывающие политические реакции

---

## 🎯 Валидация по кризисным эпизодам
SFSI ловит все ключевые события:
- 2007: Bear Stearns → SFSI spike || FX/capital markets
- 2008: Lehman → sharp spike
- 2009: HUF/EUR turbulence (FX exposure households)
- 2010: Greece junk downgrade → elevated SFSI
- 2011: Euro debt fears + CHF/HUF all-time high (CHF mortgages) → sustained rise
- 2011.09: Early FX loan repayment (banks bear losses) → peak end-2011
- 2014-15: Mandatory FX loan conversion → minor bump
- 2016: Brexit + US election
- 2020: COVID → high until early 2021

**Корреляция с FISS (эталон MNB на 19 hard-переменных): очень высокая по динамике.**

---

## 🛡️ Робастность
- Monte Carlo: удаление 10% / 40% статей (1000 симуляций) → макс. разница в тысячных долях
- Индекс **экстремально устойчив** к потере источника/статей

---

## ⚠️ Ограничения (авторы + свои)

1. **Только 2 источника** — узкая медиабаза, риск пропуска нарративов из других каналов (TV, соцсети, региональные СМИ)
2. **Нет декомпозиции на глобальный/региональный/страноспецифический стресс** — авторы сами отмечают: сильный глобальный фактор в CDS (Kocsis & Nagy, 2011)
3. **Булевый подход** не ловит контекст/ сарказм/ отрицание (но: интерпретируемость, отсутствие labelled data)
4. **Период заканчивается 2020** — нет пост-COVID, войны в Украине, инфляционного шока 2022–2024
5. **Венгерский язык** — словарь не переносим напрямую на другие страны (но методология — да)
6. **FISS vs SFSI complementarity** показана, но нет формальной комбинированной модели / nowcasting exercise

---

## 🔗 Связь с кластерами вики

| Кластер / Концепция | Связь |
|---------------------|-------|
| `concepts/econometric-housing-models` | SFSI → CDS → mortgage rates → housing stress transmission |
| `reviews/favar-faktornye-modeli` | FISS = factor-based stress index (Szendrei & Varga, 2017/2020); SFSI дополняет его soft-data измерением |
| `reviews/nowcasting-i-mixed-frequency-modeli` | SFSI — high-frequency / real-time indicator, применим в MIDAS / nowcasting |
| `reviews/ml-ne-linearnye-modeli` | Альтернатива: deep learning sentiment (BERT/finBERT) — авторы сознательно выбрали интерпретируемый Boolean |
| `reviews/mezhdunarodnaya-transmissiya-dkp-i-zhilya` | CDS spillover → international financial stress transmission to HU housing |

---

## 💡 Идеи для follow-up (для моей вики)

1. **Replicate SFSI для России** — те же 2-3 портала (РБК, Интерфакс, ТАСС?) + словарь на русском; сравнить с ЦБ РФ financial stress index
2. **Combine SFSI + FISS в MIDAS/BVAR nowcasting** для CDS / mortgage rates / house prices
3. **Decompose SFSI**: global vs local news topics (LDA topics → separate indices)
4. **High-frequency (daily/weekly) nowcasting** housing market stress during crises
5. **Non-linear / regime-switching VAR** — авторы упоминают в future work
6. **Cross-country CEE panel**: Poland, Czechia, Romania — same methodology, compare spillovers

---

## 📝 Статус в вики

- [x] PDF сохранён: `raw/papers/mnb-wp-2026-3.pdf`
- [x] Full markdown: `papers/mnb-wp-2026-3-sentiment-financial-stress-index-hungary.md`
- [x] Review создан: `reviews/mnb-wp-2026-3-sentiment-fsi-hungary.md` (this file)
- [ ] Добавить ссылки в `concepts/econometric-models-housing-market.md`
- [ ] Добавить в `reviews/favar-faktornye-modeli.md` (ссылка на FISS complementarity)
- [ ] Создать/обновить concept note: `concepts/sentiment-financial-stress-index.md`
- [ ] Commit & push to GitHub

---

## Цитата (BibTeX)

```bibtex
@techreport{horvath2026sentiment,
  title={Sentiment-based Financial Stress Index for Hungary},
  author={Horv\'ath, Be\'ata and Berki, Tam\'as and \'Onoz\'o, L\'ivia R\'eka and Temesv\'ari, Csan\'ad},
  institution={Magyar Nemzeti Bank},
  year={2026},
  number={2026/3},
  type={MNB Working Papers},
  url={https://www.mnb.hu/letoltes/mnb-wp-2026-3-final-1.pdf}
}
```