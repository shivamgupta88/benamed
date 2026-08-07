# Be Named First — Business Documentation

Private working repository for an AI search visibility consultancy
(AEO / GEO) — benamedfirst.com

> **Keep this repository private.** It contains positioning, pricing strategy,
> client qualification criteria, outreach templates and revenue planning.

---

## Contents

| File | What it is |
|---|---|
| `Be-Named-First-Operations-Handbook.pdf` | The handbook, 50 pages, clickable contents. Read this. |
| `handbook.md` | Source for the PDF. **Also the file to paste into AI assistants as context.** |
| `prompt-set-dental-dubai.md` | 50-prompt measurement instrument, Dubai cosmetic dentistry |
| `linkedin-copy.md` | Copy-paste LinkedIn text: headline, About, company page, posts, DMs |
| `build_pdf.py` | Regenerates the PDF from `handbook.md` |

## Handbook sections

| § | Section |
|---|---|
| 0 | How to use this document (human + AI) |
| 1–2 | What the business is · positioning and language |
| 3 | Why this market exists now — verified data |
| 4 | **The ideal client** — 3-part test, verticals, geography, qualification rubric, vertical strategy |
| 5 | Services and pricing — tiers, public pricing policy, founding rate |
| 6 | **Expectations vs reality** — timelines, what we never promise, churn defence |
| 7 | Technical foundation — engines, crawlers, schema, off-site levers |
| 8 | **The prompt set** — methodology, run conditions, metric formulas |
| 9 | **Delivery** — Phase 0–4, step by step with time estimates |
| 10 | Reporting — audit and monthly report structure |
| 11 | **Client acquisition** — channels, outreach templates, volume maths |
| 12 | **Sales and closing** — call structure, scripted objection handling, terms |
| 13 | Targets and unit economics — capacity, 6-month ramp, cost base |
| 14 | Risk register |
| 15 | Team, tools and delegation |
| 16 | First 30 days — day by day |
| 17 | Integrity rules — binding |
| 18 | Sources — every statistic with its origin |
| 19–20 | Glossary · quick reference card |

## Regenerating the PDF

```bash
pip install markdown playwright
python build_pdf.py
```

Edit `handbook.md`, then rebuild. The clickable contents page regenerates
automatically and the build verifies that every link resolves to a heading.

Uses Microsoft Edge via Playwright, so no browser download is required on Windows.

## Ground rules carried through every document here

1. **No guarantees.** Not rankings, positions, citations, or outcome timelines.
   AI answers are non-deterministic.
2. **No fabrication.** No invented clients, results, testimonials, logos, or
   statistics.
3. **Every statistic is sourced.** Handbook §18 is the approved list.
4. **Estimates are labelled as estimates.** Hour figures, funnel rates and the
   revenue ramp are planning estimates, not measured results.

## Status

| Item | State |
|---|---|
| Name and domain | `benamedfirst.com` |
| Handbook | v1.0 complete |
| Prompt set | v1.0 — Dubai cosmetic dentistry, 50 prompts |
| Primary vertical | Cosmetic and implant dentistry, Dubai |
| Backup test | Med spas / aesthetics, Dubai — 60-day review |
| Scorecard template | Not built yet |
| First outreach | Pending |

Review quarterly. This market moves fast — re-verify §18 before using any figure
in a client-facing document.
