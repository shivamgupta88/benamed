# Prompt Set v1.0 — Cosmetic & Implant Dentistry, Dubai

**Vertical:** Cosmetic and implant dentistry
**Market:** Dubai, UAE
**Count:** 50 prompts
**Created:** August 2026
**Status:** Active baseline instrument

---

## Rules — read before every run

**This set is frozen.** Once a client signs off, it does not change during the
engagement. Baseline comparison is the entire product. New prompts go into a new
version (v1.1), documented separately, and reported as an addition — never merged
retroactively into the baseline.

**Conditions, identical every single run:**

| Condition | Setting |
|---|---|
| Runs per prompt per engine | **3** (LLM outputs are non-deterministic) |
| Session | Logged out, no history, fresh/incognito profile |
| Location | Dubai, UAE — VPN exit set and noted |
| Language | English |
| Day and time | Same weekday, similar time of day each cycle |
| Engines | ChatGPT · Perplexity · Google AI Overviews · Gemini · Claude |

**Total data points per full cycle:** 50 prompts × 3 runs × 5 engines = **750**

**Screenshot rule:** capture every result where the client is absent and a
competitor is present. These are simultaneously your sales assets and your report
evidence.

**Placeholders:** replace `[CLINIC]` with the client's clinic name and
`[AREA]` with their neighbourhood (Jumeirah, Business Bay, Al Barsha, Downtown,
Deira, Dubai Marina, JLT, DIFC).

---

## Category A — Category discovery (15 prompts, 30%)

Highest commercial intent. These are people choosing a provider right now. Expect
the lowest baseline visibility and the strongest emotional reaction from prospects
when they see the results.

| ID | Prompt |
|---|---|
| A01 | best cosmetic dentist in Dubai |
| A02 | best dental implant clinic in Dubai |
| A03 | who is the best dentist for veneers in Dubai |
| A04 | top rated dental clinics in Dubai |
| A05 | best Invisalign provider in Dubai |
| A06 | recommend a good cosmetic dentist in Dubai |
| A07 | best teeth whitening clinic in Dubai |
| A08 | most trusted dental implant surgeon in Dubai |
| A09 | best smile makeover clinic in Dubai |
| A10 | where should I get veneers done in Dubai |
| A11 | best paediatric dentist in Dubai |
| A12 | top dental clinics in [AREA] Dubai |
| A13 | best full mouth reconstruction dentist in Dubai |
| A14 | which Dubai dental clinic has the best reviews |
| A15 | best English speaking dentist in Dubai for expats |

## Category B — Comparison (10 prompts, 20%)

Mid-funnel. Buyer is evaluating options and is highly receptive to a cited source.
Comparison content is disproportionately extractable, so this category often moves
first after AEO work.

| ID | Prompt |
|---|---|
| B01 | veneers vs Invisalign for crooked teeth which is better |
| B02 | dental implants vs bridges cost and longevity |
| B03 | composite vs porcelain veneers pros and cons |
| B04 | Invisalign vs traditional braces for adults |
| B05 | how much do dental implants cost in Dubai vs Turkey |
| B06 | is dental treatment in Dubai cheaper than the UK |
| B07 | Zoom whitening vs laser whitening which lasts longer |
| B08 | single implant vs full arch which do I need |
| B09 | Dubai vs Abu Dhabi for dental implants |
| B10 | private vs insurance dental care in Dubai worth it |

## Category C — Problem-led (12 prompts, 25%)

Top of funnel, highest volume, lowest competition. **These move fastest and are
your month-two proof.** Target these first in implementation.

| ID | Prompt |
|---|---|
| C01 | how do I fix a gap between my front teeth |
| C02 | what can I do about severely stained teeth |
| C03 | I have a missing molar what are my options |
| C04 | how do I fix a chipped front tooth |
| C05 | my gums are receding what treatment do I need |
| C06 | how long do dental implants take to heal |
| C07 | are veneers permanent and do they damage teeth |
| C08 | what causes teeth to look yellow even after brushing |
| C09 | can I get implants if I have bone loss |
| C10 | how do I fix crooked teeth without braces as an adult |
| C11 | is dental implant surgery painful and what is recovery like |
| C12 | how much should a smile makeover cost |

## Category D — Brand-direct (8 prompts, 15%)

Tests whether the engines know the client as an entity at all. A zero-mention
baseline here indicates an entity-resolution problem, which is a Phase 1 fix, not
a content problem.

| ID | Prompt |
|---|---|
| D01 | is [CLINIC] a good dental clinic |
| D02 | [CLINIC] Dubai reviews |
| D03 | tell me about [CLINIC] |
| D04 | [CLINIC] dental implants cost |
| D05 | who are the dentists at [CLINIC] |
| D06 | is [CLINIC] worth the price |
| D07 | [CLINIC] vs other dental clinics in Dubai |
| D08 | where is [CLINIC] located and what treatments do they offer |

## Category E — Local and qualified (5 prompts, 10%)

Narrow, high-intent, and easiest to win. Good early wins for reporting.

| ID | Prompt |
|---|---|
| E01 | dentist near [AREA] Dubai open on weekends |
| E02 | emergency dentist Dubai available today |
| E03 | affordable cosmetic dentist in Dubai with payment plans |
| E04 | dental clinic in Dubai that accepts [insurance provider] |
| E05 | female dentist in Dubai for cosmetic treatment |

---

## Competitor set

Select **three** named competitors at kickoff, confirmed in writing by the client.
Track them across every prompt.

| Slot | Selection rule |
|---|---|
| Competitor 1 | The one the client names as their main rival |
| Competitor 2 | The clinic appearing most often in your Stage 1 spot checks |
| Competitor 3 | The clinic ranking highest in conventional Google results for A01–A03 |

Competitor 2 matters most for the report. It is frequently a clinic the client has
never considered a threat — which makes the finding land harder.

---

## Metrics

**Mention rate** = runs where client is named ÷ total runs × 100
**Citation share** = runs where client is cited with a link ÷ total runs × 100

Report **per engine**, never averaged. Cited-domain overlap between engines is
roughly 11%, so a blended figure is meaningless.

**Per engine, per cycle:** 50 prompts × 3 runs = 150 runs.
If the client is named in 30 of 150 ChatGPT runs → mention rate 20%.
If cited with a link in 12 of those → citation share 8%.

---

## Expected baseline

From typical patterns in under-optimised local markets. **Estimates for
expectation-setting, not measured results.**

| Category | Expected baseline mention rate | Notes |
|---|---|---|
| A — Category discovery | 0–10% | Usually near zero. This is the shock in the report. |
| B — Comparison | 0–15% | Generic sources dominate |
| C — Problem-led | 5–20% | Where quick wins live |
| D — Brand-direct | 20–60% | Should be high. If low, entity problem. |
| E — Local qualified | 0–15% | Thin competition, winnable fast |

**Diagnostic signal:** if Category D is also near zero, the engines do not recognise
the clinic as an entity at all. That is a Phase 1 access and entity-consistency
problem, and it is the fastest thing to fix.

---

## Outreach mini-audit — 5 prompts only

For Stage 1 qualification across a 25-prospect list, do not run the full set. Run
these five, on ChatGPT + Perplexity + AI Overviews only. About 4 minutes per
prospect.

| Use | Prompt |
|---|---|
| 1 | A01 — best cosmetic dentist in Dubai |
| 2 | A02 — best dental implant clinic in Dubai |
| 3 | A05 — best Invisalign provider in Dubai |
| 4 | A12 — top dental clinics in [AREA] Dubai |
| 5 | C12 — how much should a smile makeover cost |

Prompt 4 is the most persuasive in outreach because it is their own neighbourhood —
it is unarguably their market.

Screenshot every gap. That screenshot is the outreach email.

---

## Adapting for the med spa backup test

Roughly 60–70% carries over. Substitute the treatment vocabulary:

| Dental term | Med spa equivalent |
|---|---|
| cosmetic dentist | aesthetic clinic / med spa |
| veneers | dermal fillers |
| dental implants | laser treatment / body contouring |
| Invisalign | Botox / injectables |
| smile makeover | full facial rejuvenation |
| teeth whitening | skin brightening / peels |

Category structure, proportions, run methodology, and metrics stay identical.
Budget 45–60 minutes to adapt.

---

## Version log

| Version | Date | Change |
|---|---|---|
| 1.0 | Aug 2026 | Initial set, 50 prompts, Dubai cosmetic/implant dentistry |
