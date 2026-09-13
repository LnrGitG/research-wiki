import pymupdf4llm, pathlib, gc

jobs = [
    ("raw/papers/nbp/nbp_ms143.pdf", "nbp_ms143_laszek_olszewski_2013"),
    ("raw/papers/nbp/nbp_ms206.pdf", "nbp_ms206_laszek_olszewski_2015"),
    ("raw/papers/nbp/nbp_ms132.pdf", "nbp_ms132_olszewski_2012"),
]
for src, dst in jobs:
    md = pymupdf4llm.to_markdown(src)
    pathlib.Path(f"papers/{dst}.md").write_text(md, encoding="utf-8")
    print(dst, len(md), "chars")
    gc.collect()