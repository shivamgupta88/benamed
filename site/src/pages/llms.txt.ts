import type { APIRoute } from 'astro';
import { glossary, services, site, sortedTerms } from '../lib/content';

/**
 * llms.txt generated at build time from the content layer, so it never drifts
 * out of sync with the site.
 *
 * Honest caveat: adoption of this convention is not universal across engines
 * and its measured impact is not established the way structured data's is. It
 * is included because it is low cost and low risk, not because it is a primary
 * lever.
 */
export const GET: APIRoute = () => {
  const terms = sortedTerms();

  const body = `# ${site.brandName}

> ${site.shortDescription}

${site.brandName} is a specialist consultancy that makes businesses visible inside
AI-generated answers across ${site.engines.join(', ')}. The work has three parts:
measuring current visibility with a fixed and repeatable prompt set, fixing what
blocks it on-site and off-site, and reporting movement monthly per engine.

Founder: ${site.founderName}, ${site.founderRole}
Contact: ${site.contactEmail}
Website: ${site.url}

## Core positioning

An AI answer names three or four businesses and stops. There is no page two.
Businesses that are not in that set do not appear at all, and no analytics
product tells them it happened. There is no Search Console equivalent for AI
answers.

We make no guarantees about rankings, positions or citations, because AI answers
are non-deterministic: the same prompt can return different answers and different
cited sources on consecutive runs. We sell a documented process and transparent
measurement of what it produced.

## Services

${services
  .map(
    (s) => `### ${s.name}
${s.answer}
Price: ${s.price} (${s.priceNote})
Timeline: ${s.duration}
URL: ${site.url}/services/${s.slug}`
  )
  .join('\n\n')}

## Measurement method

- A fixed set of 40-50 prompts, written the way buyers actually phrase questions
- Three runs per prompt per engine, because outputs are non-deterministic
- Controlled conditions: logged out, no history, consistent location and timing
- Two metrics recorded: mention rate and citation share
- Reported per engine and never averaged, because cited-domain overlap between
  engines is roughly 11%
- The prompt set is frozen for the duration of an engagement so results stay
  comparable against the baseline

## Realistic timelines

- Days 1-7: crawler access and indexability corrected, verifiable in server logs
- Weeks 1-2: first mentions may appear, volatile
- Weeks 4-8: early movement, first mentions commonly land here
- Weeks 4-12: citations begin on lower-competition questions
- Months 3-6: repeat citations and consistent visibility across engines

## Who this serves

Cosmetic and implant dentistry, aesthetic clinics and med spas, and adjacent
high-value elective healthcare. The qualifying condition is that one new customer
is worth thousands rather than hundreds.

## Key pages

- Home: ${site.url}/
- Services: ${site.url}/services
- How it works: ${site.url}/how-it-works
- Glossary: ${site.url}/glossary
- FAQ: ${site.url}/faq
- About: ${site.url}/about
- Contact: ${site.url}/contact

## Definitions

${glossary.answer}

${terms.map((t) => `- ${t.term}: ${t.short} (${site.url}/glossary/${t.slug})`).join('\n')}
`;

  return new Response(body, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
