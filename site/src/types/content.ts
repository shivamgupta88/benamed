/** Types for every JSON file in src/data. Content never lives in components. */

export interface NavLink {
  label: string;
  href: string;
}

export interface Site {
  brandName: string;
  domain: string;
  url: string;
  tagline: string;
  shortDescription: string;
  metaDescription: string;
  contactEmail: string;
  bookingUrl: string;
  founderName: string;
  founderRole: string;
  locale: string;
  engines: string[];
  primaryCta: NavLink;
  secondaryCta: NavLink;
}

export interface Navigation {
  header: NavLink[];
  footer: { heading: string; links: NavLink[] }[];
}

export interface Stat {
  id: string;
  value: string;
  label: string;
  source: string;
  sourceUrl: string;
}

export interface StatsFile {
  note: string;
  stats: Stat[];
}

export interface TableBlock {
  caption: string;
  columns: string[];
  rows: string[][];
}

export interface Point {
  title: string;
  body: string;
}

export interface Home {
  hero: { eyebrow: string; headline: string; subhead: string; note: string };
  problem: { heading: string; answer: string; points: Point[] };
  disciplines: {
    heading: string;
    answer: string;
    comparison: TableBlock;
    closing: string;
  };
  measurement: {
    heading: string;
    answer: string;
    method: string[];
    closing: string;
  };
  honesty: {
    heading: string;
    answer: string;
    timeline: TableBlock;
    closing: string;
  };
  audience: {
    heading: string;
    answer: string;
    verticals: string[];
    notFor: string;
  };
  finalCta: { heading: string; body: string };
}

export interface ProcessStep {
  step: string;
  detail: string;
}

export interface Service {
  slug: string;
  name: string;
  badge: string;
  summary: string;
  price: string;
  priceNote: string;
  duration: string;
  answer: string;
  deliverables: string[];
  inScope?: string[];
  outOfScope?: string[];
  note: string;
  process: ProcessStep[];
}

export interface ServicesFile {
  hub: { heading: string; answer: string };
  services: Service[];
  pricingNote: string;
}

export interface Phase {
  number: string;
  name: string;
  timing: string;
  answer: string;
  steps: string[];
  outcome: string;
}

export interface ProcessFile {
  heading: string;
  answer: string;
  phases: Phase[];
  leadingIndicators: { heading: string; answer: string; items: Point[] };
}

export interface FaqItem {
  q: string;
  a: string;
}

export interface FaqFile {
  heading: string;
  answer: string;
  groups: { name: string; items: FaqItem[] }[];
}

export interface GlossaryTerm {
  slug: string;
  term: string;
  short: string;
  long: string;
  related: string[];
}

export interface GlossaryFile {
  heading: string;
  answer: string;
  terms: GlossaryTerm[];
}

export interface AboutFile {
  heading: string;
  answer: string;
  founder: { name: string; role: string; bio: string[] };
  principles: { heading: string; items: Point[] };
  transparency: { heading: string; answer: string; body: string };
}

export interface LegalDoc {
  heading: string;
  updated: string;
  answer: string;
  sections: { title: string; body: string }[];
}

export interface LegalFile {
  privacy: LegalDoc;
  terms: LegalDoc;
}
