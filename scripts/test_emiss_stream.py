#!/usr/bin/env python3
"""Проверка потокового разбора и потоковой загрузки SDMX без сети.

Живой ЕМИСС отдаёт 403 с датацентр-адресов, поэтому проверяются две части,
которые от источника не зависят:

  * download(sink=...) пишет ответ кусками в файл и не собирает blob;
  * load() качает в файл (save_raw или временный), разбирает оттуда,
    возвращает те же поля и убирает временный файл;
  * parse_sdmx принимает и путь, и bytes (совместимость со старым вызовом);
  * названия s_OKATO/s_vozr доезжают, если CodeLists идут после DataSets.

    python3 scripts/test_emiss_stream.py
"""

import io
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import emiss_loader  # noqa: E402

SMALL_XML = """<?xml version="1.0" encoding="UTF-8"?>
<message:Message xmlns:message="http://www.SDMX.org/resources/SDMXML/schemas/v1_0/message">
<DataSets><DataSet>
<Series><SeriesKey><Value concept="s_OKATO" value="001"/><Value concept="s_vozr" value="15-72"/></SeriesKey><Attributes><Value concept="EI" value="тыс."/></Attributes><Obs><Time>2020</Time><ObsValue value="1 234,5"/></Obs></Series>
<Series><SeriesKey><Value concept="s_OKATO" value="002"/></SeriesKey><Obs><Time>2021</Time><ObsValue value="7"/></Obs><Obs><Time>2022</Time><ObsValue value="нет"/></Obs></Series>
</DataSet></DataSets>
<CodeLists><CodeList id="CL">
<Code value="001"><Description>Регион 1</Description></Code>
<Code value="002"><Description>Регион 2</Description></Code>
</CodeList></CodeLists>
</message:Message>
"""
SMALL = SMALL_XML.encode("utf-8")


class FakeResponse:
    def __init__(self, payload, ctype="application/xml"):
        self._buf = io.BytesIO(payload)
        self.headers = {"Content-Type": ctype}

    def read(self, n=-1):
        return self._buf.read(n)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class FakeOpener:
    def __init__(self, payload):
        self.payload = payload
        self.read_sizes = []

    def open(self, req, timeout=None):
        return FakeResponse(self.payload)


class StreamParseTest(unittest.TestCase):
    def test_parse_from_path(self):
        fd, path = tempfile.mkstemp(suffix=".xml")
        os.write(fd, SMALL)
        os.close(fd)
        try:
            data = emiss_loader.Emiss.parse_sdmx(path)
        finally:
            os.remove(path)
        self.assertEqual(len(data["rows"]), 2)
        self.assertEqual(data["rows"][0]["value"], 1234.5)
        self.assertEqual(data["rows"][0]["s_OKATO_name"], "Регион 1")
        # второй ряд: две точки, последняя с нечисловым значением
        self.assertIsNone(data["rows"][1]["value"])
        self.assertEqual(data["rows"][1]["value_raw"], "нет")
        # CodeLists идут после DataSets — название должно доехать вторым проходом
        self.assertEqual(data["rows"][1]["s_OKATO_name"], "Регион 2")

    def test_parse_accepts_bytes(self):
        data = emiss_loader.Emiss.parse_sdmx(SMALL)
        self.assertEqual(len(data["rows"]), 2)
        self.assertEqual(data["rows"][0]["time"], "2020")


class StreamDownloadTest(unittest.TestCase):
    def test_download_to_sink_does_not_return_blob(self):
        e = emiss_loader.Emiss.__new__(emiss_loader.Emiss)
        e.base = "https://example.invalid"
        e.timeout = 5
        fake = FakeOpener(SMALL)
        e.opener = fake
        meta = {"filters": {"0": {"indicator": True, "values": {"1": {"title": "x"}}}},
                "token_name": "t", "token": "v", "indicator_id": "1",
                "left": [], "top": [], "filter_object_ids": []}
        fd, path = tempfile.mkstemp(suffix=".xml")
        os.close(fd)
        try:
            got = e.download(meta, [], fmt="sdmx", sink=path)
            self.assertIsNone(got)
            with open(path, "rb") as fh:
                self.assertEqual(fh.read(), SMALL)
            self.assertEqual(len(e.parse_sdmx(path)["rows"]), 2)
        finally:
            os.remove(path)


class LoadToFileTest(unittest.TestCase):
    def test_load_streams_to_temp_and_cleans_up(self):
        e = emiss_loader.Emiss.__new__(emiss_loader.Emiss)
        e.meta = lambda ind: {"filters": {}}
        e.select = lambda meta, wanted: []
        seen = {}

        def fake_download(meta, selected, fmt="sdmx", sink=None):
            seen["sink"] = sink
            with open(sink, "wb") as fh:
                fh.write(SMALL)
            return None

        e.download = fake_download
        before = set(os.listdir(tempfile.gettempdir()))
        data = e.load("1")
        self.assertEqual(len(data["rows"]), 2)
        self.assertEqual(data["bytes"], len(SMALL))
        self.assertTrue(seen["sink"].endswith(".xml"))
        self.assertFalse(os.path.exists(seen["sink"]))
        self.assertEqual(before - set(os.listdir(tempfile.gettempdir())), set())

    def test_save_raw_is_kept(self):
        e = emiss_loader.Emiss.__new__(emiss_loader.Emiss)
        e.meta = lambda ind: {"filters": {}}
        e.select = lambda meta, wanted: []

        def fake_download(meta, selected, fmt="sdmx", sink=None):
            with open(sink, "wb") as fh:
                fh.write(SMALL)
            return None

        e.download = fake_download
        fd, path = tempfile.mkstemp(suffix=".xml")
        os.close(fd)
        try:
            data = e.load("1", save_raw=path)
            self.assertEqual(data["bytes"], len(SMALL))
            self.assertTrue(os.path.exists(path))
            self.assertEqual(os.path.getsize(path), len(SMALL))
        finally:
            os.remove(path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
