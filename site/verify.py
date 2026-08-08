"""
Post-build verification for dist/.

Checks the things that silently break on a content site and that a normal build
will not complain about: shipped JS, heading structure, table semantics, crawler
allowances, generated endpoints, and per-page metadata completeness.

Run after every build:  python verify.py
Exits non-zero if any page is incomplete.
"""

import pathlib
import re
import sys

DIST = pathlib.Path("dist")

if not DIST.exists():
    sys.exit("dist/ not found. Run `npm run build` first.")

html_files = sorted(DIST.rglob("*.html"))
js_files = list(DIST.rglob("*.js"))

print(f"HTML pages built : {len(html_files)}")
print(f"JS files shipped : {len(js_files)}  (zero is the goal)")
print()

home = (DIST / "index.html").read_text(encoding="utf-8")
print("--- home page ---")
print(f"size            : {len(home):,} bytes")
print(f"JSON-LD blocks  : {home.count('application/ld+json')}")
print(f"h1 / h2         : {len(re.findall(r'<h1', home))} / {len(re.findall(r'<h2', home))}")
print(f"real <table>    : {home.count('<table')}")
print(f"th scope=       : {home.count('th scope=')}")
print(f'canonical link  : {chr(34) + "canonical" + chr(34) in home}')
print(f"skip link       : {'skip-link' in home}")
print()

print("--- content present in raw HTML (the core AEO requirement) ---")
for probe in [
    "shortlist, not a ranking",
    "Answer Engine Optimization",
    "non-deterministic",
    "Month one is plumbing",
    "11%",
]:
    print(f"  {'OK  ' if probe in home else 'MISS'}  {probe}")
print()

print("--- generated endpoints ---")
for name in ["robots.txt", "llms.txt", "sitemap-index.xml", "favicon.svg"]:
    f = DIST / name
    size = f.stat().st_size if f.exists() else 0
    print(f"  {'OK  ' if f.exists() else 'MISS'}  {name:20} {size:>7,} bytes")
print()

robots = (DIST / "robots.txt").read_text(encoding="utf-8")
print("--- AI crawlers allowed in robots.txt ---")
for c in [
    "GPTBot",
    "OAI-SearchBot",
    "ClaudeBot",
    "PerplexityBot",
    "Google-Extended",
    "CCBot",
]:
    print(f"  {'OK  ' if c in robots else 'MISS'}  {c}")
print()

print("--- schema types across all pages ---")
types: dict[str, int] = {}
for f in html_files:
    for m in re.findall(r'"@type":"([A-Za-z]+)"', f.read_text(encoding="utf-8")):
        types[m] = types.get(m, 0) + 1
for t, n in sorted(types.items(), key=lambda x: -x[1]):
    print(f"  {t:22} {n}")
print()

print("--- every page: title, description, canonical, exactly one h1 ---")
failures = []
for f in html_files:
    text = f.read_text(encoding="utf-8")
    missing = []
    if "<title>" not in text:
        missing.append("title")
    if 'name="description"' not in text:
        missing.append("description")
    if 'rel="canonical"' not in text:
        missing.append("canonical")
    h1s = len(re.findall(r"<h1", text))
    if h1s != 1:
        missing.append(f"h1 count={h1s}")
    if missing:
        failures.append((f.relative_to(DIST).as_posix(), missing))

if failures:
    for path, missing in failures:
        print(f"  FAIL  {path}: {', '.join(missing)}")
    print()
    sys.exit(f"{len(failures)} page(s) incomplete")

print(f"  OK    all {len(html_files)} pages complete")
print()
print("Verification passed.")
