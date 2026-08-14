---
title: "AI Agents and Prompt Engineering in Econometric Coding"
authors: "Sebastian Galiani, Federico Ariel López, Raul A. Sosa"
year: 2026
publisher: "NBER"
type: working-paper
nber_id: w35588
doi: null
url: "https://www.nber.org/papers/w35588"
pdf: "raw/papers/nber_w35588_galiani_2026_ai_econometric_coding.pdf"
pages: 31
jel: [C18, C87]
tags: [AI, LLM, econometric-coding, agents, prompt-engineering, Stata, R, Python, benchmark, Claude, GPT, reproducibility, methodology]
created: 2026-08-14
updated: 2026-08-14
---

# AI Agents and Prompt Engineering in Econometric Coding

**NBER Working Paper No. 35588, August 2026**

**Authors:** Sebastian Galiani (Tulane University & NBER), Federico Ariel López (Universidad de San Andrés), Raul A. Sosa (Universidad de San Andrés)

**JEL:** C18, C87

## Аннотация

Исследование того, как LLM пишут код для эконометрического анализа. Сравниваются три измерения AI-ассистированного кодирования: статистическое ПО (Stata, R, Python), тип промпта (zero-shot vs few-shot), и уровень агентности — от чатбота, пишущего один скрипт, до агента, который исполняет и исправляет свой код.

На бенчмарке из 21 прикладной эконометрической задачи переход от чатбота к ограниченному агенту повышает успешность с **74% до 96%** при дополнительных ~8 центах за запуск.

## Ключевые результаты

| Параметр | Чатбот | One-repair | Ограниченный агент |
|----------|--------|------------|---------------------|
| Task success (zero-shot) | 67.3% | 81.3% | 94.9% |
| Task success (few-shot) | 81.6% | 85.1% | 96.5% |
| Task success (overall) | **74.4%** | **83.2%** | **95.7%** |
| Executability | 77.5% | 90.5% | 99.7% |
| Output correctness | 67.3% | 81.3% | 94.9% |

### Основные выводы

1. **Агентность > промпт-инжиниринг.** Переход от чатбота к агенту даёт +21.3 п.п. (p < 0.001), few-shot промпт — только +6.6 п.п. (p = 0.009).

2. **Промпт-инжиниринг и агентность — субституты.** Few-shot эффект падает с 14.3 п.п. (чатбот) до 1.6 п.п. (агент). Взаимодействие few-shot × constrained agent = −12.7 п.п. (p = 0.061).

3. **Stata хуже Python и R.** В zero-shot чатботе Stata на **33.3 п.п.** ниже Python (p = 0.005). Под агентом различия нивелируются: Python 88.7%, R 88.9%, Stata 75.7%.

4. **Стоимость.** Средняя стоимость запуска: $0.18 (чатбот) → $0.26 (агент). Incremental cost = $0.36 за дополнительный успешный запуск.

5. **Межмодельное сравнение.** Для Claude Sonnet 4.6 и GPT-5.4 (через Codex) few-shot улучшает чатбот значительно больше, чем агента — подтверждающая гипотезу субститутов.

## Методология

- **Бенчмарк:** 21 задача по прикладной эконометрике (линейная регрессия, DID, RDD, IV, панельные оценки, временные ряды)
- **Дизайн:** 3 ПО × 2 промпта × 3 уровня агентности = 18 условий, 5 повторений каждое = 1890 наблюдений (Claude Sonnet 4.6)
- **Оценка:** автоматический скоринг — исполнимость, корректность вывода, совпадение с эталоном в пределах допуска
- **Статистика:** кластеризация на уровне задачи, wild-cluster-bootstrap p-values (9999 репликаций)

## Связи

- `concepts/econometric-models-housing-market.md` — методология эконометрического моделирования
- Тема: AI-инструменты для эконометрических исследований; применимо к валидации кода в исследованиях жилищного рынка

## Примечание

Работа не связана напрямую с жилищным строительством, но важна для методологии: показывает, что AI-агенты с автономным исполнением кода значительно превосходят простую генерацию скриптов, что применимо к воспроизводимости эконометрических исследований (включая исследования рынка жилья).

## Аннотация (англ.)

We study how large language models write code for econometric analysis. We compare three dimensions of AI-assisted coding: statistical software (Stata, R, or Python), prompting (zero-shot versus few-shot), and the degree of agency, from a chatbot that writes a single script to an agent that executes and revises its own code. On a benchmark of applied econometric and statistical tasks, moving from the chatbot to the constrained agent raises task success from 74 to 96 percent, at about eight additional cents per run. For Claude Sonnet 4.6 and GPT-5.4 through Codex, few-shot prompting improves the chatbot far more than the constrained agent, indicating that prompting and agency act as substitutes. For these models, differences across statistical software are sizeable under the chatbot but largely disappear under the constrained agent.