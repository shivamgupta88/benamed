import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://benamedfirst.com',

  // Fully static output. Every page is real HTML on first response, which is
  // the single hardest requirement for AI crawlers and answer extraction.
  output: 'static',

  integrations: [sitemap()],

  build: {
    inlineStylesheets: 'auto',
  },

  compressHTML: true,

  // Trailing slashes off so canonical URLs stay consistent across the site
  // and in structured data.
  trailingSlash: 'never',
});
