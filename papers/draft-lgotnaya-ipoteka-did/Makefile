# Сборка статьи «Льготная ипотека как автономный источник спроса…»
#
# make tables  — пересобрать таблицы и рисунки из данных (Python + psycopg)
# make md      — knit R Markdown в markdown (knitr)
# make tex     — собрать LaTeX (pandoc + citeproc)
# make pdf     — собрать PDF (xelatex, два прохода для ссылок)
# make html    — HTML-версия (pandoc, без LaTeX)
# make all     — tables + pdf
#
# Требуется: R + knitr в ~/R/library; pandoc (в этом окружении —
# venv-пакет pypandoc_binary); TinyTeX в ~/.TinyTeX с пакетами
# caption, booktabs, float, amsmath, hyperref, geometry, graphics, xcolor,
# babel-russian, hyphen-russian.
#
# Примечание: rmarkdown в среде не собирается (пакет fs требует компиляции),
# поэтому сборка идёт через knitr + pandoc напрямую. Если rmarkdown доступен,
# достаточно `Rscript -e 'rmarkdown::render("paper.Rmd")'`.

R_LIB  := $(HOME)/R/library
PY     := $(HOME)/.hermes/hermes-agent/venv/bin/python3
PANDOC := $(HOME)/.hermes/hermes-agent/venv/lib/python3.11/site-packages/pypandoc/files/pandoc
XELATEX := $(HOME)/.TinyTeX/bin/x86_64-linux/xelatex
R      := R_LIBS_USER=$(R_LIB) Rscript
OPTS   := --citeproc --bibliography=refs.bib --include-in-header=preamble.tex \
          -V geometry:margin=2.5cm -V fontsize=11pt

.PHONY: all tables md tex pdf html clean

all: tables pdf

tables:
	$(PY) $(HOME)/personal/scripts/export_for_paper.py

md: tables
	$(R) -e '.libPaths(path.expand("~/R/library")); knitr::knit("paper.Rmd", output="paper.md")'

tex: md
	$(PANDOC) paper.md -s -o paper.tex $(OPTS)

pdf: tex
	$(XELATEX) -interaction=nonstopmode paper.tex > paper.pass1.log
	$(XELATEX) -interaction=nonstopmode paper.tex > paper.pass2.log

html: md
	$(PANDOC) paper.md -s -o paper.html $(OPTS)

clean:
	rm -f paper.md paper.tex paper.pdf paper.html paper.aux paper.log paper.out \
	      paper.toc paper.pass1.log paper.pass2.log