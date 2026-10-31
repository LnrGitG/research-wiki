#!/usr/bin/env python3
"""Генератор синтетической фикстуры ответа ЕМИСС в формате SDMX.

Структура как у живого ответа: Code/Description в CodeLists, затем DataSets
с Series (SeriesKey, Attributes, пять Obs). Теги без namespace — так приходит
часть элементов ЕМИСС, на этом спотыкался первый разбор.

Пишется потоком, чтобы генератор не держал сотни мегабайт в памяти:

    python3 scripts/emiss_sdmx_fixture.py /tmp/sdmx_small.xml 30000
    python3 scripts/emiss_sdmx_fixture.py /tmp/sdmx_fixture.xml 200000
    python3 scripts/emiss_sdmx_fixture.py /tmp/sdmx_codes_after.xml 100 --codes-after
"""

import argparse


def main():
    ap = argparse.ArgumentParser(description="фикстура SDMX-ответа ЕМИСС")
    ap.add_argument("path", nargs="?", default="/tmp/sdmx_fixture.xml")
    ap.add_argument("series", nargs="?", type=int, default=200_000)
    ap.add_argument("--periods", type=int, default=5, help="точек на ряд")
    ap.add_argument("--codes", type=int, default=1000)
    ap.add_argument("--codes-after", action="store_true",
                    help="положить CodeLists после DataSets (проверка отложенных названий)")
    args = ap.parse_args()

    def write_codes(f):
        f.write('<CodeLists>\n<CodeList id="CL_OKATO">\n')
        for i in range(args.codes):
            f.write('<Code value="%03d"><Description>Регион %d</Description></Code>\n' % (i, i))
        f.write("</CodeList>\n</CodeLists>\n")

    with open(args.path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<message:Message xmlns:message="http://www.SDMX.org/resources/SDMXML/schemas/v1_0/message">\n')
        f.write("<Header><ID>x</ID><Prepared>2026-10-31</Prepared></Header>\n")
        if not args.codes_after:
            write_codes(f)
        f.write("<DataSets>\n<DataSet>\n")
        for i in range(args.series):
            f.write("<Series><SeriesKey>")
            f.write('<Value concept="s_OKATO" value="%03d"/>' % (i % args.codes))
            f.write('<Value concept="s_vozr" value="15-72"/>')
            f.write('<Value concept="s_pokaz" value="43062"/>')
            f.write("</SeriesKey><Attributes>")
            f.write('<Value concept="EI" value="тыс. человек"/>')
            f.write('<Value concept="PERIOD" value="год"/>')
            f.write("</Attributes>")
            for p in range(args.periods):
                f.write("<Obs><Time>%d</Time>" % (2017 + p))
                f.write('<ObsValue value="%d.%d"/>' % (i % 5000, p))
                f.write("</Obs>")
            f.write("</Series>\n")
        f.write("</DataSet>\n</DataSets>\n")
        if args.codes_after:
            write_codes(f)
        f.write("</message:Message>\n")

    print("готово:", args.path, args.series, "рядов ×", args.periods, "точек")


if __name__ == "__main__":
    main()
