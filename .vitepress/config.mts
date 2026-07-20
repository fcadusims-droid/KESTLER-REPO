import { defineConfig, type HeadConfig } from 'vitepress'
import { discoverDocs, excludedGlobs } from './lib/docs.mts'

// ---------------------------------------------------------------------------
// Public site identity. Change SITE_* here (or via env) if the repo is renamed
// or moved to a custom domain — nothing else needs to be touched.
// ---------------------------------------------------------------------------
const SITE_NAME = 'The Kestler Archive'
const SITE_TAGLINE = 'An archive of original fictional universes.'
// GitHub Pages project site: https://<user>.github.io/<repo>/
// NOTE: the <repo> path segment is CASE-SENSITIVE on GitHub Pages. The CI
// workflow overrides these from the real repository name so they always match
// (see .github/workflows/deploy.yml); the defaults below are the local fallback.
const HOSTNAME = process.env.SITE_HOSTNAME || 'https://fcadusims-droid.github.io'
const BASE = process.env.SITE_BASE || '/KESTLER-REPO/'

// Discover the library once, at config load. Used to build the sidebar and to
// exclude everything that is not a public worldbuilding document.
const docs = discoverDocs()

const sidebar = [
  {
    text: 'The Library',
    items: docs.map((d) => ({ text: d.title, link: d.link }))
  }
]

export default defineConfig({
  title: SITE_NAME,
  description: SITE_TAGLINE,
  lang: 'en',
  base: BASE,

  // Dark theme is the default; the reader can still toggle to light.
  appearance: 'dark',

  // Clean URLs (/One Blood instead of /One Blood.html).
  cleanUrls: true,

  // Reader-oriented: no last-updated dates, no commit authors, no git metadata.
  lastUpdated: false,

  // Error handling: never fail the whole build on an odd/unsupported link.
  // A warning is printed instead so a new document is never blocked from publishing.
  ignoreDeadLinks: true,

  // Do NOT turn dev files or private documents into pages or index them.
  srcExclude: [
    ...excludedGlobs(),
    // Safety net: anything in a subfolder is private by default.
    '**/node_modules/**',
    '.github/**',
    '.vitepress/**',
    'public/**'
  ],

  // Native, automatic sitemap.xml.
  sitemap: {
    hostname: HOSTNAME.replace(/\/$/, '') + BASE
  },

  // Global SEO / social metadata.
  head: [
    ['meta', { name: 'theme-color', content: '#8b5cf6' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:site_name', content: SITE_NAME }],
    ['meta', { name: 'robots', content: 'index, follow' }]
  ],

  // Per-page Open Graph / Twitter tags, generated automatically from the page.
  transformHead({ pageData, siteConfig }) {
    const tags: HeadConfig[] = []
    const title =
      (pageData.frontmatter.title as string) ||
      pageData.title ||
      siteConfig.site.title
    const description =
      (pageData.frontmatter.description as string) ||
      pageData.description ||
      siteConfig.site.description
    const url =
      HOSTNAME.replace(/\/$/, '') +
      BASE +
      pageData.relativePath.replace(/(index)?\.md$/, '').replace(/\s/g, '%20')

    tags.push(['meta', { property: 'og:title', content: title }])
    tags.push(['meta', { property: 'og:description', content: description }])
    tags.push(['meta', { property: 'og:url', content: url }])
    tags.push(['meta', { name: 'twitter:title', content: title }])
    tags.push(['meta', { name: 'twitter:description', content: description }])
    tags.push(['link', { rel: 'canonical', href: url }])

    const cover = pageData.frontmatter.cover as string | undefined
    if (cover) {
      const abs = /^https?:\/\//.test(cover)
        ? cover
        : HOSTNAME.replace(/\/$/, '') + BASE + cover.replace(/^\//, '')
      tags.push(['meta', { property: 'og:image', content: abs }])
      tags.push(['meta', { name: 'twitter:image', content: abs }])
    }
    return tags
  },

  // Markdown rendering options (footnotes/tables/task-lists are on by default).
  markdown: {
    lineNumbers: true,
    image: {
      // Lazy-load images for performance.
      lazyLoading: true
    }
  },

  themeConfig: {
    siteTitle: SITE_NAME,

    // Minimal top navigation — no GitHub links, no external branding.
    nav: [{ text: 'The Library', link: '/' }],

    // Automatic left sidebar listing every universe (drives prev/next too).
    sidebar,

    // Automatic Table of Contents from the document headings, with active
    // section highlighting as you scroll.
    outline: {
      level: [2, 6],
      label: 'On this page'
    },

    // Local, static full-text search (MiniSearch). No external service.
    search: {
      provider: 'local',
      options: {
        detailedView: true
      }
    },

    docFooter: {
      prev: 'Previous',
      next: 'Next'
    },

    returnToTopLabel: 'Back to top',
    sidebarMenuLabel: 'Library',
    darkModeSwitchLabel: 'Appearance',
    lightModeSwitchTitle: 'Switch to light',
    darkModeSwitchTitle: 'Switch to dark',

    // No "Edit this page", no repo links, no social links — reader-only site.
    footer: {
      message: SITE_TAGLINE,
      copyright: `© ${new Date().getFullYear()} Johnny Kestler`
    }
  }
})
