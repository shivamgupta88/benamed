# benamedfirst.com

Marketing site for Be Named First — an AI search visibility (AEO / GEO)
consultancy.

Built with **Astro**, fully static, deployed on **Netlify**.

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # -> dist/
python verify.py # post-build checks
```

---

## Why Astro rather than Next.js

The single hardest requirement for this particular site is that **every word of
content must be present in the raw HTML on first response**, because AI crawlers
are what the business is about. Astro ships **zero JavaScript by default**, so
that requirement is met structurally rather than by discipline.

Verified in the current build: **34 pages, 0 JS files shipped.**

The site also practises what it sells. It is the first reference implementation
of the work, so the audit checklist we apply to clients is applied here.

## Content lives in JSON, never in components

All copy is in `src/data/*.json`, typed in `src/types/content.ts`, and reached
through `src/lib/content.ts`. No component contains a content string.

| File | Drives |
|---|---|
| `site.json` | Brand tokens, contact, CTAs. Change the brand name in one place. |
| `navigation.json` | Header and footer navigation |
| `home.json` | Every home page section |
| `services.json` | All four services — also generates `/services/[slug]` |
| `process.json` | How it works, phases, leading indicators |
| `faqs.json` | FAQ page + home FAQ + FAQPage schema |
| `glossary.json` | Glossary index — also generates a page per term |
| `about.json` | About page |
| `legal.json` | Privacy and terms |
| `stats.json` | **Every statistic, with a mandatory source URL** |

`getStat()` throws at build time if a statistic is used without being declared in
`stats.json`. An unsourced number cannot reach production.

Adding a glossary term or a service means adding a JSON entry. No code changes,
and the new page is fully optimised automatically.

## Routes

```
/                                    Home
/services                            Hub
/services/ai-visibility-audit        Entry offer, main conversion page
/services/answer-engine-optimization
/services/generative-engine-optimization
/services/visibility-monitoring
/how-it-works                        Five phases + honest timeline
/glossary                            Index
/glossary/[slug]                     19 terms, one page each
/faq                                 Full FAQ
/about                               Founder, principles, transparency
/contact                             Netlify form
/thanks                              Form success (noindex)
/privacy  /terms
/404
```

Generated at build: `robots.txt`, `llms.txt`, `sitemap-index.xml`.

## AEO / GEO implementation

**Access**
- `robots.txt` explicitly allows 18 AI crawlers: GPTBot, OAI-SearchBot,
  ChatGPT-User, ClaudeBot, anthropic-ai, PerplexityBot, Google-Extended,
  Applebot-Extended, CCBot, Bingbot and others
- No content behind JavaScript, no cookie wall, no interstitial
- `llms.txt` generated from the content layer so it cannot drift out of sync

**Extractability**
- `AnswerBlock` enforces the answer-first pattern: heading, then a direct
  self-contained answer, then detail
- One `h1` per page, correct heading order — verified by `verify.py`
- Real `<table>` with `<th scope>`, never div grids
- FAQ built on `<details>` so answers are in the HTML without JS

**Structured data** — current build emits 17 schema types:
`ProfessionalService`, `WebSite`, `Person`, `Service`, `Offer`, `FAQPage`,
`Question`/`Answer`, `DefinedTerm`, `DefinedTermSet`, `HowTo`, `HowToStep`,
`BreadcrumbList`, `ItemList`, `ContactPage`.

**Glossary as a GEO play.** Nineteen terms, each on its own page with
`DefinedTerm` markup. Definitional content is disproportionately cited by
language models, so this is a deliberate lever rather than filler.

## Accessibility

- Skip link, semantic landmarks, visible focus states
- Keyboard-operable nav and FAQ with no JS
- 44px minimum touch targets
- `prefers-reduced-motion` and `prefers-color-scheme` respected
- Fluid type via `clamp()`, no horizontal scroll from 320px up

## Verification

`verify.py` runs against `dist/` and checks JS count, JSON-LD presence, heading
structure, table semantics, crawler allowances, generated endpoints, and that
every page has a title, description, canonical and exactly one `h1`.

It caught a real bug during development: ten pages were rendering `h2` as the
page title with no `h1`. Run it after every build.

## Deploying to Netlify

1. Push this repo to GitHub
2. Netlify → **Add new site** → **Import an existing project** → pick the repo
3. Settings are read from `netlify.toml`:
   - Build command `npm run build`
   - Publish directory `dist`
   - Node 22
4. Deploy
5. **Domain settings** → add `benamedfirst.com`, follow the DNS instructions
6. **Forms** — the contact form works with no backend via `data-netlify="true"`.
   Add a notification email under Forms → Settings so submissions reach you.

## Before going live

- [ ] Replace `bookingUrl` in `site.json` with a real calendar link
- [ ] Confirm `hello@benamedfirst.com` exists and receives mail
- [ ] Add real favicon and OG image assets (see the brand asset brief)
- [ ] Add a founder photograph to the About page
- [ ] Set the Netlify form notification email
- [ ] Re-run `verify.py`
- [ ] Run Lighthouse on mobile emulation
- [ ] Submit the sitemap in Google Search Console

## Content rules — binding

1. **No guarantees.** Not rankings, positions, citations or outcome timelines.
2. **No fabrication.** No invented clients, results, testimonials or logos. The
   site currently shows none, deliberately — there are no real ones yet.
3. **Every statistic carries a source.** Enforced at build time.
4. **No employer names.** The About page describes the founder's technical
   background without naming past employers.
