---
title: "AI-кейс: ассистент ускоренного обзора научной литературы (AI Mindset)"
source_url: https://base.aimindset.org/_Automation/ai-implementation-cases/case-Express-Scientific-Literature-Review
date_read: 2026-08-25
type: ai_case_methodology
tags:
  - literature-review
  - ai-pipeline
  - semantic-search
  - citation-network
  - research-gaps
  - workflow-reference
related:
  - "[[karpeko_2026_quiet_inflation_expectations]]"
---

# AI-ассистент ускоренного обзора научной литературы

Источник: AI Mindset knowledge base, кейс от 21.08.2026 (~3 мин чтения).

## Суть кейса

Проблема: 8–15 часов на первичный обзор при входе в новую область; 40% исследователей
ограничиваются поверхностным анализом.

Заявленное решение: структурированная карта поля за 15–30 минут (500–1000+ публикаций).

## Конвейер из 4 этапов

1. **Поиск и анализ массива**: семантическая генерация поисковых стратегий (Claude) →
   мультибазовый поиск PubMed/arXiv/Scholar/Semantic Scholar → фильтрация по
   качеству/цитируемости/новизне → хронология направления.
2. **Структурный анализ**: извлечение концепций из абстрактов (ChatGPT) → кластеризация
   подтем → систематизация методологий → выявление противоречий.
3. **Сетевой анализ**: сеть цитирований публикаций и авторов → ранжирование ключевых
   авторов → эволюция концепций/смена парадигм → междисциплинарные пересечения.
4. **Обзор и рекомендации**: автогенерация отчёта с разделами → research gap анализ →
   методологические рекомендации → экспорт в Notion/Zotero/Mendeley (через Make).

## Инструменты кейса

Claude (анализ вопросов, семантика), ChatGPT (извлечение концепций), Make
(автоматизация поиска и экспорта); упоминаются также Elicit, Research Rabbit,
Scite, Undermind.

## Соотнесение с research-wiki

| Этап кейса | Что уже есть у нас | Разрыв |
|------------|--------------------|--------|
| Мультибазовый поиск | arxiv-skill, huggingface-hub, web_search (ограничен), CMWP/RANEPA вручную | нет Semantic Scholar/OpenAlex API в пайплайне |
| Извлечение и структурирование | academic-literature-ingest, batch-research-ingest, pymupdf4llm, .RU.md переводы | кластеризация подтем — только через vector-search (568 доков) |
| Сетевой анализ цитирований | catalog.yaml с related-ссылками, теги | нет графа цитирований (Semantic Scholar Citations API бесплатный) |
| Research gaps / обзор | queries/*.md пишутся вручную | LLM-генерация обзора поверх БД возможна |
| Экспорт | GitHub Pages (search/vector/viewer/data/dashboard) | интеграция с Zotero отсутствует |

## Практический вывод для нашего пайплайна

Минимальное усиление по образцу кейса:
1. **OpenAlex / Semantic Scholar API** (бесплатные) — метаданные + цитирования +
   референс-граф для статей из catalog.yaml;
2. построение citation-graph.json → визуализация на GitHub Pages (d3.js);
3. авторанжирование «ключевые авторы направления» для housing economics;
4. LLM-шаг «gap-анализ» поверх существующего векторного поиска.
