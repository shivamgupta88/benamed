/**
 * Typed access to the JSON content layer.
 *
 * Components import from here, never from the JSON files directly, so the
 * shape of the content is validated in one place.
 */

import siteJson from '../data/site.json';
import navigationJson from '../data/navigation.json';
import homeJson from '../data/home.json';
import servicesJson from '../data/services.json';
import processJson from '../data/process.json';
import faqsJson from '../data/faqs.json';
import glossaryJson from '../data/glossary.json';
import aboutJson from '../data/about.json';
import legalJson from '../data/legal.json';
import statsJson from '../data/stats.json';

import type {
  AboutFile,
  FaqFile,
  GlossaryFile,
  GlossaryTerm,
  Home,
  LegalFile,
  Navigation,
  ProcessFile,
  Service,
  ServicesFile,
  Site,
  Stat,
  StatsFile,
} from '../types/content';

export const site = siteJson as Site;
export const navigation = navigationJson as Navigation;
export const home = homeJson as Home;
export const servicesFile = servicesJson as ServicesFile;
export const processFile = processJson as ProcessFile;
export const faqs = faqsJson as FaqFile;
export const glossary = glossaryJson as GlossaryFile;
export const about = aboutJson as AboutFile;
export const legal = legalJson as LegalFile;
export const statsFile = statsJson as StatsFile;

export const services: Service[] = servicesFile.services;

/** Look up one service by slug. Throws at build time if the slug is wrong. */
export function getService(slug: string): Service {
  const found = services.find((s) => s.slug === slug);
  if (!found) {
    throw new Error(
      `Unknown service slug "${slug}". Available: ${services
        .map((s) => s.slug)
        .join(', ')}`
    );
  }
  return found;
}

/** Look up one glossary term by slug. */
export function getTerm(slug: string): GlossaryTerm {
  const found = glossary.terms.find((t) => t.slug === slug);
  if (!found) {
    throw new Error(`Unknown glossary term "${slug}"`);
  }
  return found;
}

/** Glossary terms sorted alphabetically for index display. */
export function sortedTerms(): GlossaryTerm[] {
  return [...glossary.terms].sort((a, b) => a.term.localeCompare(b.term));
}

/** Fetch a sourced statistic by id. Throws if it is not in stats.json. */
export function getStat(id: string): Stat {
  const found = statsFile.stats.find((s) => s.id === id);
  if (!found) {
    throw new Error(
      `Unknown stat "${id}". Every statistic must be declared in stats.json with a source.`
    );
  }
  return found;
}

/** Every FAQ flattened, for building FAQPage structured data. */
export function allFaqs() {
  return faqs.groups.flatMap((g) => g.items);
}

/** Absolute URL for canonicals, sitemaps and structured data. */
export function absoluteUrl(path: string): string {
  const clean = path === '/' ? '' : path.replace(/\/$/, '');
  return `${site.url}${clean}`;
}
