---
title: "Research Radar 2026-09-14: недельный обзор свежей литературы"
created: 2026-09-14
type: query
tags: [research-radar, weekly, housing-supply, monetary-policy, mortgage, nowcasting]
sources: [nber, ssrn, arxiv, philadelphia-fed, bis]
confidence: high
---

# Research Radar — 2026-09-14 (окно 7–14 сентября 2026)

Поиск по фокусу [[hypotheses.yaml]] и [[queries/literature-gap-map]]:
housing supply elasticity, mortgage subsidy, ДКП-трансмиссия, макропруденциальные
лимиты, nowcasting по search-данным, финансовое здоровье девелоперов, escrow/project
finance. Источники: NBER (сентябрьские w-papers), SSRN, arXiv econ.GN/econ.EM,
Philly Fed, BIS, ЦБ РФ. Окно жёсткое — 7 дней; улов скромный, но реальный.

## Новое в литературе

| # | Работа | Метод | Ключевой результат | Статус к гипотезам | URL |
|---|--------|-------|--------------------|--------------------|-----|
| 1 | **Graybill & Mangum 2026** (Philly Fed WP 26-33/R, rev. сентябрь 2026): *Is Mortgage Lock-In Responsible for Housing Market Tightness?* | Survival-модели housing tenures + калибровка search-and-matching модели (транзакционные данные Cotality) | Покупки чувствительнее к ипотечной ставке, чем предложения к lock-in: снижение ставки увеличит объёмы сделок, но **не** снимет тайтнесс; lock-in сокращает листинги и сделки | **Косвенно поддерживает X-003** (асимметрия ДКП): ставка действует через спрос сильнее, чем через предложение — аналог «сдерживание сильнее смягчения» на микроданных | [WP 26-33](https://www.philadelphiafed.org/-/media/FRBP/Assets/working-papers/2026/wp26-33.pdf) |
| 2 | **D'Amico, Soltas & Wang 2026** (сентябрь 2026): *Where Is Housing Slow to Build, And Is It Getting Slower?* | Измерение временных дюраций permitting и development стандартизированных проектов, 60 городов США, 2000– | Разложение длительности проекта на permitting/development; тренд замедления строительства по городам | **Нейтрально к H-002, релевантно пробелу №1** (эластичность предложения): дюрации как фрикцион предложения — потенциальный контролер в SPARK-панели | [PDF](https://evansoltas.com/papers/Durations_DSW2026.pdf) |
| 3 | **Berry 2026** (arXiv:2609.06308, 5 сент. 2026): *Housing Price Appreciation, Housing Affordability, and the Spatial Restructuring of Toronto Commuting* | OLS/квадратичные регрессии + Global/Local Moran's I, 23 CMA Онтарио 2016–2021 | Рост цен жилья не коррелирует с приростом маятниковой commuting (R²=.045, p=.331) — региональный рынок растёт без пропорционального роста поездок | Нейтрально; региональная дифференциация (контекст H-005) | [arXiv](https://arxiv.org/abs/2609.06308) |
| 4 | **BIS 2026** (WP 1375, 3 сент. 2026): *Zombie firms in emerging Asia* (Avdjiev, Hardy, Jager) | Firm-bank linked данные 10 азиатских EME, 2005–2021 | Зомби-фирмы: внутренние и кросс-бордер импликации (soft budget constraints, кредитные искажения) | **Методологический референс для H-002/H-008** (финансовое здоровье фирм → поведение; зомби-классификация как робастность к нашему финансовому ограничению Net Debt/EBITDA) | [BIS WP 1375](https://www.bis.org/publications/working-paper-1375-zombie-firms-emerging-asia-domestic-and-cross-border-implications) |

Дополнительно зафиксированы сентябрьские NBER w-papers (w35696 Hachem — loan rates
как incentive-инструменты в банковском principal-agent, релевантно каналу кредитного
рирования; w35704 Amann–Gorodnichenko–Talavera — allocative productivity в войне,
методологический референс для firm-level разрушения аллокативной эффективности), но
прямой связи с реестром гипотез нет — не включены в основной список.

## Влияние на гипотезы

- **X-003 (асимметрия ДКП) — пополнен evidence_for, статус не менялся**:
  Graybill & Mangum 2026 дают микрообоснование асимметрии — эластичность покупок
  по ставке (−0.10…−0.46 в IV-спецификациях) превышает эластичность листингов к
  lock-in; т.е. ужесточение сжимает рынок сильнее, чем смягчение расширяет
  ( buyers more sensitive than sellers). Для РФ-кейса это усиливает мотивировку
  регионального proxy-подхода (DiD по доле льготной ипотеки) из next_check.
- Остальные гипотезы (H-001…H-010) — **без изменений**: работ прямо по
  escrow-механике РФ, wordstat-nowcasting строительства или firm-level эластичности
  под финансовыми ограничениями за окно не найдено. Пробел №1 (firm-level
  эластичность) и №2 (escrow как exogenous shock) остаются незакрытыми — это
  подтверждает уникальность нашего вклада.

## Новые пробелы/идеи

1. **Lock-in как аналог эскроу-заморозки?** Механизм Graybill–Mangum (ставка
   сброса условий при транзакции) структурно похож на наш escrow-release:
   в обоих случаях фиксированные условия контракта создают экзогенный во времени
   барьер/высвобождение ликвидности. Возможная идея: методологический перенос
   survival-моделей tenures на эскроу-балансы девелоперов (когда проект «созревает»
   для release). Связь: [[queries/supply-elasticity-estimation-design]], H-003.
2. **Дюрации проектов как leading indicator СМР?** D'Amico–Soltas–Wang измеряют
   permitting/development lag'и — если аналог доступен по ЕИСЖС (сроки от старта
   продаж до ввода), это может улучшить H-006 (mixed-frequency блок) через
   «construction pipeline» фичу. Проверяемость: наличие проектных дат в ЕИСЖС.
3. **Зомби-девелоперы**: BIS 1375 даёт готовую методологию зомби-классификации
   (HK-подход) на firm-bank данных — прямой кандидат на контрол-переменную
   в H-002 (не только leverage, но и «зомби-статус» как альтернативная мера
   финансовой слабости). Связь: [[queries/microdata-macroeconomic-research-review]].

## Связи

- [[hypotheses.yaml]] — реестр (X-003 обновлён)
- [[queries/literature-gap-map]] — пробелы №1–№3 подтверждены как открытые
- [[queries/vnok-nowcasting-design]] — H-007/H-008 без новостей
- [[concepts/zhilischnaya-inflyaciya]] — индексные противоречия X-002 без новых работ

^[Скан: NBER сентябрьские листинги, SSRN Real Estate/Household Finance, arXiv econ.GN/econ.EM 2026-09, Philly Fed WP, BIS WP; дата проверки 2026-09-14]