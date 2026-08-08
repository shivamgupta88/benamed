import type { APIRoute } from 'astro';
import { site } from '../lib/content';

/**
 * robots.txt generated at build time.
 *
 * Every major AI crawler is explicitly allowed. This is the single highest
 * leverage line of configuration on the whole site - a disallow here makes the
 * site invisible to an entire engine no matter how good the content is.
 */
const AI_CRAWLERS = [
  'GPTBot',
  'OAI-SearchBot',
  'ChatGPT-User',
  'ClaudeBot',
  'anthropic-ai',
  'Claude-Web',
  'PerplexityBot',
  'Perplexity-User',
  'Google-Extended',
  'Applebot',
  'Applebot-Extended',
  'CCBot',
  'Bingbot',
  'Amazonbot',
  'meta-externalagent',
  'DuckAssistBot',
  'YouBot',
  'cohere-ai',
];

export const GET: APIRoute = () => {
  const body = [
    '# Be Named First',
    '# AI crawlers are explicitly welcome. That is rather the point.',
    '',
    'User-agent: *',
    'Allow: /',
    '',
    ...AI_CRAWLERS.flatMap((bot) => [`User-agent: ${bot}`, 'Allow: /', '']),
    `Sitemap: ${site.url}/sitemap-index.xml`,
    '',
  ].join('\n');

  return new Response(body, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
