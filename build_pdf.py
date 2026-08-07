"""
Build a print-quality PDF from handbook.md.

Pipeline: markdown -> styled HTML -> Edge (via Playwright) print-to-PDF.
Uses Edge because it ships with Windows, so no browser download is needed.
"""

import functools
import re
from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright

print = functools.partial(print, flush=True)

HERE = Path(__file__).parent
MD = HERE / "handbook.md"
HTML = HERE / "handbook.html"
PDF = HERE / "Be-Named-First-Operations-Handbook.pdf"

CSS = """
@page {
  size: A4;
  margin: 18mm 16mm 20mm 16mm;
}
@page :first { margin-top: 0; }

* { box-sizing: border-box; }

body {
  font-family: "Segoe UI", -apple-system, system-ui, sans-serif;
  font-size: 10.2pt;
  line-height: 1.55;
  color: #1a1d21;
  margin: 0;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

/* ---------- cover ---------- */
.cover {
  height: 252mm;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 0 4mm;
  page-break-after: always;
  border-top: 6px solid #c2410c;
}
.cover h1 {
  font-size: 34pt;
  line-height: 1.1;
  margin: 0 0 6mm 0;
  border: none;
  padding: 0;
  letter-spacing: -0.5pt;
}
.cover .sub { font-size: 14pt; color: #44494f; margin-bottom: 2mm; }
.cover .domain { font-size: 11pt; color: #c2410c; font-weight: 600; margin-bottom: 22mm; }
.cover .meta { font-size: 9.5pt; color: #6b7280; border-top: 1px solid #e5e7eb; padding-top: 4mm; }

/* ---------- headings ---------- */
h1 {
  font-size: 19pt;
  margin: 0 0 5mm 0;
  padding-bottom: 2.5mm;
  border-bottom: 2.5px solid #c2410c;
  page-break-before: always;
  page-break-after: avoid;
  letter-spacing: -0.3pt;
}
h1:first-of-type { page-break-before: avoid; }

h2 {
  font-size: 14pt;
  margin: 8mm 0 3mm 0;
  padding-bottom: 1.5mm;
  border-bottom: 1.5px solid #d1d5db;
  page-break-before: always;
  page-break-after: avoid;
  letter-spacing: -0.2pt;
}
h2:first-of-type { page-break-before: avoid; }

h3 {
  font-size: 11.5pt;
  margin: 6mm 0 2mm 0;
  color: #111827;
  page-break-after: avoid;
}
h4 {
  font-size: 10.4pt;
  margin: 4mm 0 1.5mm 0;
  color: #374151;
  page-break-after: avoid;
}

p { margin: 0 0 2.6mm 0; orphans: 3; widows: 3; }

/* ---------- tables ---------- */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 3mm 0 5mm 0;
  font-size: 8.8pt;
  page-break-inside: avoid;
}
thead { background: #1f2937; color: #fff; }
th {
  text-align: left;
  padding: 2mm 2.2mm;
  font-weight: 600;
  font-size: 8.6pt;
}
td {
  padding: 1.9mm 2.2mm;
  border-bottom: 0.5px solid #e5e7eb;
  vertical-align: top;
}
tbody tr:nth-child(even) { background: #f9fafb; }

/* ---------- lists ---------- */
ul, ol { margin: 0 0 3mm 0; padding-left: 6mm; }
li { margin-bottom: 1.4mm; }
li > ul, li > ol { margin-top: 1.4mm; }

/* ---------- code ---------- */
code {
  font-family: "Cascadia Mono", Consolas, monospace;
  font-size: 8.6pt;
  background: #f3f4f6;
  padding: 0.4mm 1.1mm;
  border-radius: 2px;
  color: #9a3412;
}
pre {
  background: #f9fafb;
  border: 0.5px solid #e5e7eb;
  border-left: 3px solid #c2410c;
  padding: 3mm;
  font-size: 8.4pt;
  line-height: 1.45;
  overflow-wrap: break-word;
  white-space: pre-wrap;
  page-break-inside: avoid;
  margin: 3mm 0;
}
pre code { background: none; padding: 0; color: #1f2937; }

/* ---------- blockquote (templates/scripts) ---------- */
blockquote {
  margin: 3mm 0;
  padding: 2.5mm 4mm;
  background: #fffbeb;
  border-left: 3px solid #d97706;
  font-size: 9.4pt;
  color: #292524;
  page-break-inside: avoid;
}
blockquote p { margin-bottom: 1.8mm; }
blockquote p:last-child { margin-bottom: 0; }

strong { font-weight: 600; color: #0f172a; }
em { color: #44494f; }

hr {
  border: none;
  border-top: 0.5px solid #e5e7eb;
  margin: 6mm 0;
}

a { color: #9a3412; text-decoration: none; word-break: break-all; }

/* ---------- table of contents ---------- */
.toc { page-break-after: always; }
.toc h2 { page-break-before: avoid; }
.toc-hint {
  font-size: 8.6pt;
  color: #6b7280;
  font-style: italic;
  margin-bottom: 5mm;
}
.toc-list {
  list-style: none;
  padding-left: 0;
  margin: 0;
  font-size: 10.4pt;
}
.toc-list li {
  margin-bottom: 0;
  border-bottom: 0.5px solid #f1f2f4;
}
.toc-list a {
  display: flex;
  align-items: baseline;
  gap: 3mm;
  padding: 2.1mm 1mm;
  color: #1a1d21;
  text-decoration: none;
}
.toc-num {
  flex: 0 0 8mm;
  font-weight: 600;
  color: #c2410c;
  font-variant-numeric: tabular-nums;
}
.toc-label { flex: 0 1 auto; }
.toc-dots {
  flex: 1 1 auto;
  border-bottom: 0.5px dotted #cbd0d6;
  transform: translateY(-1mm);
  min-width: 6mm;
}
"""


def slugify(text):
    """Match python-markdown's toc/attr_list slug style."""
    slug = text.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    return slug.strip("-")


def build_toc(md_text):
    """
    Build a clickable TOC linking to each '## N. Title' section.

    Returns (toc_html, anchor_map) where anchor_map maps heading text -> slug so
    the same ids can be injected into the rendered body.
    """
    items = re.findall(r"^## (\d+\..*)$", md_text, flags=re.MULTILINE)
    if not items:
        return "", {}

    anchor_map = {}
    rows = []
    for title in items:
        title = title.strip()
        slug = slugify(title)
        anchor_map[title] = slug

        # Split "4. The ideal client" into number + label for two-column layout.
        m = re.match(r"^(\d+)\.\s*(.*)$", title)
        num, label = (m.group(1), m.group(2)) if m else ("", title)

        rows.append(
            f'<li><a href="#{slug}">'
            f'<span class="toc-num">{num}</span>'
            f'<span class="toc-label">{label}</span>'
            f'<span class="toc-dots"></span>'
            f"</a></li>"
        )

    lis = "\n".join(rows)
    return (
        '<div class="toc"><h2>Contents</h2>'
        '<p class="toc-hint">Click any entry to jump to that section.</p>'
        f'<ul class="toc-list">{lis}</ul></div>',
        anchor_map,
    )


def inject_anchors(body_html, anchor_map):
    """Add matching id attributes to the rendered <h2> headings."""
    for title, slug in anchor_map.items():
        # python-markdown escapes &, <, > in heading text
        escaped = (
            title.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        )
        for variant in (escaped, title):
            needle = f"<h2>{variant}</h2>"
            if needle in body_html:
                body_html = body_html.replace(
                    needle, f'<h2 id="{slug}">{variant}</h2>', 1
                )
                break
    return body_html


def main():
    md_text = MD.read_text(encoding="utf-8")

    # Split the cover (everything before the first '---') from the body.
    parts = md_text.split("\n---\n", 1)
    cover_md, body_md = (parts[0], parts[1]) if len(parts) == 2 else ("", md_text)

    cover_html = f"""
    <div class="cover">
      <h1>Be Named First</h1>
      <div class="sub">Operations Handbook</div>
      <div class="sub" style="font-size:11pt">AI Search Visibility Consultancy</div>
      <div class="domain">benamedfirst.com</div>
      <div class="meta">
        Version 1.0 &nbsp;·&nbsp; August 2026<br>
        Internal reference document. Also intended as context for AI assistants.<br>
        Review quarterly &mdash; timelines, engine behaviour and pricing benchmarks shift.
      </div>
    </div>
    """

    md_engine = markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists", "attr_list"]
    )
    body_html = md_engine.convert(body_md)
    toc_html, anchor_map = build_toc(body_md)
    body_html = inject_anchors(body_html, anchor_map)

    # Verify every TOC link has a matching target.
    missing = [s for s in anchor_map.values() if f'id="{s}"' not in body_html]
    if missing:
        print(f"WARNING: {len(missing)} TOC link(s) have no target: {missing}")
    else:
        print(f"All {len(anchor_map)} TOC links resolved to a heading id")

    full = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>Be Named First - Operations Handbook</title>
<style>{CSS}</style></head>
<body>{cover_html}{toc_html}{body_html}</body></html>"""

    HTML.write_text(full, encoding="utf-8")
    print(f"HTML written: {HTML.name} ({len(full):,} chars)")

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        page = browser.new_page()
        page.goto(HTML.as_uri(), wait_until="load")
        page.pdf(
            path=str(PDF),
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template="<div></div>",
            footer_template=(
                '<div style="width:100%;font-size:7.5pt;color:#9ca3af;'
                'font-family:Segoe UI,sans-serif;padding:0 16mm;'
                'display:flex;justify-content:space-between;">'
                "<span>Be Named First &mdash; Operations Handbook v1.0</span>"
                '<span class="pageNumber"></span>'
                "</div>"
            ),
            margin={"top": "14mm", "bottom": "16mm", "left": "0", "right": "0"},
        )
        browser.close()

    size_kb = PDF.stat().st_size / 1024
    print(f"PDF written: {PDF.name} ({size_kb:,.0f} KB)")


if __name__ == "__main__":
    main()
