-- Схема карточки публикации (фаза 5 анализа корпуса).
--
-- Назначение: единая таблица метаданных корпуса первичных исследований и
-- публикаций research-wiki, с русскоязычными заголовками полей.
--
-- Размещение: БД research_wiki на ВМ YC, схема core. Ссылается на уже
-- существующие core.document и core.file_registry, не дублируя их поля.
--
-- Идемпотентность: CREATE TABLE IF NOT EXISTS + UPSERT по paper_code.
--
-- Поля соответствуют ТЗ владельца: название, ссылка на источник (DOI или
-- другая), выводы, источники и данные, методы, список литературы с
-- источниками и ссылками, ссылка на первичный PDF для загрузки.

BEGIN;

CREATE TABLE IF NOT EXISTS core.paper_card (
    -- Идентификация
    paper_code        text PRIMARY KEY,          -- код работы (stem файла вики)
    title_ru          text,                      -- название (рус.)
    title_orig        text,                      -- название в оригинале
    doc_type          text,                      -- статья / перевод / отчёт / препринт

    -- Источник
    source_url        text,                      -- ссылка на источник (DOI или иная)
    doi               text,                      -- DOI, если найден в тексте
    venue             text,                      -- издание / журнал / серия
    year              integer,                   -- год публикации
    authors           text,                      -- авторы (строка, как в тексте)
    authors_source    text,                      -- откуда взяты: frontmatter/label/byline/filename

    -- Содержание
    findings          text,                      -- выводы
    findings_source    text,                     -- section / abstract / пусто
    methods           text[],                    -- методы (массив канонических кодов)
    data_sources      text[],                    -- источники данных (массив)
    methods_text      text,                      -- фрагмент текста секции методов

    -- Библиография
    references_json   jsonb,                     -- список литературы:
                                                 -- [{текст, авторы, год, издание, doi, url}]
    n_references      integer,                   -- число записей в списке

    -- Первичный файл в хранилище (бакет wiki-research, YC Object Storage)
    file_path         text,                      -- путь в бакете: raw/papers/имя.pdf
    file_name         text,                      -- имя файла
    file_size_bytes   bigint,                    -- размер
    file_sha256       char(64),                  -- контрольная сумма
    presigned_url     text,                      -- подписанная ссылка (истекает 7 дней)
    file_match        text,                      -- способ связки: source_pdf/exact/prefix/none
    file_available    boolean,                   -- есть ли файл в хранилище

    -- Служебное
    wiki_page         text,                      -- путь страницы вики
    updated           timestamptz DEFAULT now(),
    created           timestamptz DEFAULT now(),
    source_note       text                       -- заметка о происхождении/качестве записи
);

COMMENT ON TABLE  core.paper_card IS
    'Карточка публикации: метаданные корпуса первичных исследований research-wiki';
COMMENT ON COLUMN core.paper_card.findings_source IS
    'Откуда текст выводов: section (настоящая секция) или abstract (резерв из аннотации)';
COMMENT ON COLUMN core.paper_card.references_json IS
    'Список литературы массивом объектов: {текст, авторы, год, издание, doi, url}';
COMMENT ON COLUMN core.paper_card.file_match IS
    'Способ связки с файлом: source_pdf, exact, prefix, ambiguous, none';
COMMENT ON COLUMN core.paper_card.authors_source IS
    'Источник авторов: frontmatter, label, byline, authors_line, filename';

-- Индексы
CREATE INDEX IF NOT EXISTS paper_card_year_idx       ON core.paper_card (year);
CREATE INDEX IF NOT EXISTS paper_card_doi_idx        ON core.paper_card (doi);
CREATE INDEX IF NOT EXISTS paper_card_type_idx       ON core.paper_card (doc_type);
CREATE INDEX IF NOT EXISTS paper_card_search_idx     ON core.paper_card
    USING gin (to_tsvector('russian',
        coalesce(title_ru,'') || ' ' || coalesce(title_orig,'') || ' ' ||
        coalesce(findings,'') || ' ' || coalesce(authors,'')));
CREATE INDEX IF NOT EXISTS paper_card_refs_idx       ON core.paper_card
    USING gin (references_json);
CREATE INDEX IF NOT EXISTS paper_card_methods_idx    ON core.paper_card
    USING gin (methods);

-- Витрина для DataLens: без служебных полей и без тяжёлого jsonb
CREATE OR REPLACE VIEW core.v_paper_card AS
SELECT paper_code,
       title_ru,
       title_orig,
       authors,
       year,
       venue,
       doc_type,
       source_url,
       doi,
       findings,
       array_to_string(methods, ', ')   AS methods,
       array_to_string(data_sources, ', ') AS data_sources,
       n_references,
       file_name,
       pg_size_pretty(file_size_bytes)  AS file_size,
       file_available,
       presigned_url
FROM core.paper_card;

COMMENT ON VIEW core.v_paper_card IS
    'Витрина карточек публикаций для DataLens (методы и данные — строкой)';

COMMIT;
