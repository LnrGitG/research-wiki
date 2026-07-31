---
title: Glaeser & Gyourko (2018) — The Economic Implications of Housing Supply
type: review
created: 2026-07-31
updated: 2026-07-31
tags: [review, housing-supply, regulation, housing-wealth, spatial-misallocation, JEP]
paper_ref: papers/glaeser-gyourko-2018-housing-supply-jep.md
---

# Обзор: Glaeser & Gyourko (2018) — The Economic Implications of Housing Supply

**Авторы:** Edward Glaeser (Harvard), Joseph Gyourko (Wharton)  
**Журнал:** Journal of Economic Perspectives, 32(1), 3–30  
**DOI:** `10.1257/jep.32.1.3`  
**Год:** 2018

---

## 🎯 Суть (one-liner)

Классический обзор экономики предложения жилья в США: методология **P/MPPC** (price-to-minimum-profitable-production-cost = Tobin's q для жилья) → классификация рынков на три типа (эластичный / неэластичный / убывающий) → последствия для богатства домохозяйств и пространственного размещения труда.

---

## 📊 Методология

### MPPC (Minimum Profitable Production Cost)
```
MPPC = (Land + ConstructionCosts) × EntrepreneurialProfit (1.17)
```
- **Construction costs:** RSMeans данные, economy-quality home, 2000 ft²
- **Land:** 20% от физической стоимости (правило большого пальца от застройщиков)
- **EP:** 17% gross margin (на основе портфелей публичных homebuilders)

### Три типа рынков (по P/MPPC)

| Тип | Пример | P/MPPC | Характеристика |
|-----|--------|--------|----------------|
| **Эластичный** (growing, elastic) | Atlanta | ~1.0 | Конкуренция строителей держит цену ≈ MPPC; объём строительства волатилен, цена — нет |
| **Неэластичный** (growing, inelastic) | San Francisco | 2.84 (2013) | Регулирование → supply curve наклонная; спрос → рост цен, а не объёмов; связь P/MPPC↔permits разорвана |
| **Убывающий** (declining) | Detroit | <1.0 | Спрос упал, жильё durable → цены ниже MPPC; новое строительство ≈ 0 |

---

## 🔬 Ключевые результаты

### 1. Распределение P/MPPC по рынкам США (2013)
- **73.6%** домов оценены ≈ или ниже MPPC (P/MPPC ≤ 1.25)
- **26.4%** — дорогое жильё (P/MPPC > 1.25), из них **10.2%** — более чем вдвое дороже MPPC
- All-time high в 2005: 53.3% домов > 1.25 MPPC (28% — >2×)
- **Метро с P/MPPC > 2 (2013):** Los Angeles, Oxnard-Ventura, San Francisco
- **1.25–2:** Baltimore, Boston, Denver, New York, San Diego, Seattle, Washington DC

### 2. Динамика 1985–2013
- **1985:** 6.4% метро с P/MPPC > 1.25 (только CA + HI)
- **2007 (пик бума):** 48.5% метро > 1.25
- **2013:** 15.9% — всё ещё выше 1985 года (долгосрочный тренд)
- **Рост дисперсии цен:** хвост распределения цен стал значительно длиннее (Gyourko, Mayer, Sinai 2013 — «superstar cities»)

### 3. Эффекты богатства
- 40% роста капитала/ВВП (Piketty 2014) = жильё; 83% роста частного капитала/дохода = жильё
- **Выигравшие:** старшие когорты (55–74), богатые, владевшие жильём до введения ограничений
- **Проигравшие:** молодые, арендаторы, покупатели после 2000
- **SCF 1983 vs 2013:** housing net worth выросла только у 95-й и 99-й перцентилей старших когорт; медианный домовладелец 35–44 лет в 2013 имел **$6,000** equity vs **$55,799** в 1983 (!)
- **Перераспределение от покупателей к продавцам**, а не чистый рост благосостояния

### 4. Пространственная аллокация труда
- **Hsieh & Moretti (2017):** GDP мог бы быть на **9% выше**, если бы Сан-Франциско, Сан-Хосе и Нью-Йорк строили как median-метро
- **Критика:** эластичность спроса на труд Cobb-Douglas (7.5) завышает оценки; при эмпирических эластичностях (Beaudry et al. 2014: 0.3–1.0) → **0.7–2% GDP**
- **Итог:** даже 2% GDP — существенная величина; нижняя граница потерь от регулирования ≈ **2% национального выпуска**
- **Оговорка:** не учтены negative externalities строительства, гетерогенность человеческого капитала, amenities

---

## 🛡️ Сильные стороны

- **Простая, прозрачная методология** P/MPPC — интуитивно понятный аналог Tobin's q
- **Трёхтиповая классификация** рынков (Detroit / Atlanta / San Francisco) — педагогически сильный приём
- **Честная критика** собственных оценок: Hsieh-Moretti 9% → 0.7–2% при реалистичных допущениях
- **Связь с Piketty/Rognlie** — помещает обсуждение в контекст макроэкономики богатства
- **Данные:** AHS микро + RSMeans + SCF — три независимых источника

---

## ⚠️ Ограничения

1. **США только** — неясно, насколько методология применима к другим странам (особенно с централизованным планированием)
2. **2013 — последний год данных** — не покрывает пост-COVID всплеск цен (2020–2023)
3. **Качество жилья** — RSMeans economy quality может занижать реальную стоимость; при luxury — лишь 6% дорогих домов, что меняет выводы
4. **Причинность** — «регулирование → цены» спорна из-за эндогенности (cross-section, нет инструментов)
5. **Negative externalities строительства** — авторы признают, что не оценивают их количественно
6. **Human capital** — не учтена гетерогенность навыков при оценке misallocation
7. **Gyourko-Saiz-Summers WRLURI** — единственный индекс регулирования, но он основан на опросах 2006 г.

---

## 🔗 Связь с кластерами вики

| Кластер / Концепт | Связь |
|-------------------|-------|
| `reviews/predlozhenie-i-regulirovanie-zhilya` | **Прямое дополнение** — эта статья должна быть головной в обзоре. Даёт unified framework (P/MPPC) и макроэкономические следствия |
| `reviews/klassicheskie-modeli-ekonomiki-zhilya` | Tobin's q для жилья — прямая аналогия с Topel-Rosen 1988 |
| `reviews/otchety-cb-i-regulyaciya` | Wealth effects + spatial misallocation — связь с макрофинансовой стабильностью |
| `reviews/rossiyskie-issledovaniya-rynka-zhilya` | Методология P/MPPC применима к российским регионам: Москва / СПб как San Francisco, регионы как Detroit/Atlanta |
| `concepts/econometric-models-housing-market` | Добавлен метод Price-to-Cost Ratio (Tobin's q) в таблицу |
| `papers/glaeser-gyourko-2003-building-restrictions` | Ранняя версия методологии |
| `papers/saiz-2010-geographic-determinants-housing-supply` | Geography vs regulation как факторы supply |

---

## 💡 Идеи для follow-up

1. **Реплицировать P/MPPC для России** — Росстат (цены), RSMeans-аналог (КО-Инвест?), land share
2. **Оценить misallocation труда в РФ** — Москва/СПб как San Francisco, регионы как Detroit
3. **Проверить wealth effect по SCF-аналогу** — RLMS-HSE, с фокусом на старшие когорты
4. **Обновить данные до 2024** — пост-COVID цены; связь с льготной ипотекой
5. **Сравнить с Glaeser-Gyourko 2003 и 2005** — эволюция методологии

---

## 📝 Статус в вики

- [x] PDF скопирован: `raw/papers/glaeser-gyourko-2018-housing-supply-jep.pdf`
- [x] Full markdown: `papers/glaeser-gyourko-2018-housing-supply-jep.md`
- [x] Review: `reviews/glaeser-gyourko-2018-housing-supply-review.md`
- [ ] Обновить `reviews/predlozhenie-i-regulirovanie-zhilya.md` (добавить ссылку)
- [ ] Обновить `concepts/econometric-models-housing-market.md`
- [ ] Commit & push to GitHub

## Цитата (BibTeX)

```bibtex
@article{glaeser2018economic,
  title={The Economic Implications of Housing Supply},
  author={Glaeser, Edward and Gyourko, Joseph},
  journal={Journal of Economic Perspectives},
  volume={32},
  number={1},
  pages={3--30},
  year={2018},
  doi={10.1257/jep.32.1.3}
}
```