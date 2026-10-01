#!/usr/bin/env python3
"""Download open-access PDFs cited in the CBR international-practice reference.

Target dir: raw/papers/ (symlink to YC Object Storage).
Verifies each file: HTTP 200, %PDF magic, non-trivial size, %%EOF trailer.
Idempotent: skips files already present and valid.

Notes on blocked sources (checked 01.10.2026):
- IMF wpiea2025109: www.imf.org sits behind Akamai and returns 403 to
  datacenter clients; the file is pulled from the Wayback Machine instead.
  The Wayback raw copy is served in two chunks (5 MiB + remainder), so the
  downloader issues a Range request for the tail and concatenates.
- Chen et al. (REPU China, 10.1016/j.ceqi.2023.02.003): gold OA but the PDF
  exists only on ScienceDirect, which is behind a Cloudflare captcha with no
  mirror (Unpaywall url_for_pdf = null). Not retrievable from this host.
"""
import os
import subprocess
import sys

DEST = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "raw", "papers")
)

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# (short_name, url)
SOURCES = [
    ("fsb-2020-suptech.pdf",
     "https://www.fsb.org/wp-content/uploads/P091020.pdf"),
    ("bis-project-ellipse-2022.pdf",
     "https://www.bis.org/publications/project-ellipse-integrated-regulatory-data-and-analytics-platform.pdf"),
    ("baker-bloom-davis-2016-epu-qje.pdf",
     "https://www.policyuncertainty.com/media/BakerBloomDavis.pdf"),
    ("ahir-bloom-furceri-2022-wui-nber-w29763.pdf",
     "https://www.nber.org/system/files/working_papers/w29763/w29763.pdf"),
    ("shapiro-sudhof-wilson-2020-news-sentiment-frbsf-wp2017-01.pdf",
     "https://www.frbsf.org/wp-content/uploads/wp2017-01.pdf"),
    ("pfeifer-marohl-2023-centralbankroberta-arxiv.pdf",
     "https://arxiv.org/pdf/2310.17691"),
    ("gambacorta-etal-2025-cb-lms-bis-wp1215.pdf",
     "https://www.bis.org/publications/working-paper-1215-cb-lms-language-models-central-banking.pdf"),
    ("dicastri-etal-2019-suptech-generations-fsi19.pdf",
     "https://www.bis.org/publications/fsi-insight-19-suptech-generations.pdf"),
    ("broeders-prenio-2018-suptech-fsi9.pdf",
     "https://www.bis.org/publications/fsi-insight-9-innovative-technology-financial-supervision-suptech-experience-early-users.pdf"),
    ("loughran-mcdonald-2011-liability-jf.pdf",
     "https://www.uts.edu.au/globalassets/sites/default/files/adg_cons2015_loughran-mcdonald-je-2011.pdf"),
]

# IMF working paper: primary URL is Akamai-blocked, use the Wayback raw copy.
IMF_NAME = "silva-moriya-veyrune-2025-imf-wp25-109.pdf"
IMF_WAYBACK = ("https://web.archive.org/web/20260606114643id_/"
               "https://www.imf.org/-/media/files/publications/wp/2025/"
               "english/wpiea2025109-print-pdf.pdf")

# Chen et al. — not retrievable (Cloudflare-only OA). Listed for the record.
BLOCKED = [("chen-etal-2023-repu-china.pdf",
            "https://doi.org/10.1016/j.ceqi.2023.02.003",
            "ScienceDirect Cloudflare captcha, no OA mirror")]


def is_valid_pdf(path):
    if not os.path.exists(path) or os.path.getsize(path) < 20000:
        return False
    with open(path, "rb") as f:
        head = f.read(5)
        f.seek(max(0, os.path.getsize(path) - 2048))
        tail = f.read()
    return head == b"%PDF-" and b"%%EOF" in tail


def curl(url, out, extra=None, timeout=140):
    cmd = ["curl", "-sSL", "--max-time", "120", "-A", UA,
           "-H", "Accept: application/pdf,*/*"]
    if extra:
        cmd += extra
    cmd += ["-o", out, "-w", "%{http_code} %{content_type} %{size_download}", url]
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def download(name, url):
    out = os.path.join(DEST, name)
    if is_valid_pdf(out):
        print(f"SKIP  {name} (already valid, {os.path.getsize(out)} B)")
        return True
    tmp = out + ".part"
    try:
        r = curl(url, tmp)
    except subprocess.TimeoutExpired:
        print(f"FAIL  {name}: timeout")
        return False
    if is_valid_pdf(tmp):
        os.replace(tmp, out)
        print(f"OK    {name}  {r.stdout.strip()}  size={os.path.getsize(out)}")
        return True
    meta = r.stdout.strip()
    print(f"FAIL  {name}  {meta}")
    if os.path.exists(tmp):
        os.remove(tmp)
    return False


def download_imf():
    """Wayback serves the raw copy in two chunks; fetch tail with Range."""
    out = os.path.join(DEST, IMF_NAME)
    if is_valid_pdf(out):
        print(f"SKIP  {IMF_NAME} (already valid, {os.path.getsize(out)} B)")
        return True
    head_p, tail_p = out + ".head", out + ".tail"
    try:
        r1 = curl(IMF_WAYBACK, head_p)
        n1 = os.path.getsize(head_p) if os.path.exists(head_p) else 0
        if n1 == 0 or open(head_p, "rb").read(5) != b"%PDF-":
            print(f"FAIL  {IMF_NAME}  head chunk: {r1.stdout.strip()}")
            return False
        # If the head chunk is already complete, done.
        if b"%%EOF" in open(head_p, "rb").read()[-2048:]:
            os.replace(head_p, out)
            print(f"OK    {IMF_NAME}  single chunk size={os.path.getsize(out)}")
            return True
        r2 = curl(IMF_WAYBACK, tail_p, extra=["-H", f"Range: bytes={n1}-"])
        n2 = os.path.getsize(tail_p) if os.path.exists(tail_p) else 0
        with open(out, "wb") as f:
            f.write(open(head_p, "rb").read())
            f.write(open(tail_p, "rb").read())
        for p in (head_p, tail_p):
            if os.path.exists(p):
                os.remove(p)
        if is_valid_pdf(out):
            print(f"OK    {IMF_NAME}  chunks {n1}+{n2} size={os.path.getsize(out)}")
            return True
        print(f"FAIL  {IMF_NAME}  assembled {n1 + n2} B, invalid")
        return False
    except subprocess.TimeoutExpired:
        print(f"FAIL  {IMF_NAME}: timeout")
        return False


def main():
    os.makedirs(DEST, exist_ok=True)
    ok = fail = 0
    for name, url in SOURCES:
        if download(name, url):
            ok += 1
        else:
            fail += 1
    if download_imf():
        ok += 1
    else:
        fail += 1
    for name, url, why in BLOCKED:
        if is_valid_pdf(os.path.join(DEST, name)):
            ok += 1
        else:
            fail += 1
            print(f"BLOCK {name}  {why}  ({url})")
    print(f"\n=== done: {ok} ok, {fail} unavailable, dest={DEST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())