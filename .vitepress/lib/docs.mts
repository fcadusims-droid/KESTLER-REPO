// ---------------------------------------------------------------------------
// Automatic worldbuilding-document discovery.
//
// This is the single source of truth for "what is publishable".
// It is imported by the VitePress config (to build the sidebar and to exclude
// non-public files from the build) and mirrors the rules used by the homepage
// data loader, so the site, the navigation and the search index always agree.
//
// PUBLISHING RULE (privacy by default):
//   A file is published as a page ONLY IF ALL of the following are true:
//     1. It is a Markdown file located at the REPOSITORY ROOT (not in a
//        subfolder). Anything you drop into a subfolder stays private.
//     2. Its name is not in DEV_DENYLIST (README, LICENSE, config docs, ...).
//     3. Its front matter does NOT contain `publish: false` or `draft: true`.
//
//   => A brand-new "New Universe.md" at the root is published automatically.
//   => A private note, a dev file, or anything flagged `publish: false`
//      is never built, never linked, and never indexed by search.
// ---------------------------------------------------------------------------

import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import matter from 'gray-matter'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
// lib/ -> .vitepress/ -> repository root
export const ROOT = path.resolve(__dirname, '..', '..')

// Development / infrastructure Markdown that must never reach the public site.
// Matching is case-insensitive.
const DEV_DENYLIST = new Set(
  [
    'README.md',
    'CONTRIBUTING.md',
    'LICENSE.md',
    'LICENCE.md',
    'CHANGELOG.md',
    'SECURITY.md',
    'CODE_OF_CONDUCT.md',
    'AUTHORS.md',
    'index.md' // the generated homepage
  ].map((n) => n.toLowerCase())
)

export interface DocMeta {
  /** Original file name, e.g. "One Blood.md" */
  file: string
  /** Route path without extension, e.g. "/One Blood" */
  link: string
  title: string
  description: string
  genre?: string
  cover?: string
  order: number
}

function stripExt(name: string): string {
  return name.replace(/\.md$/i, '')
}

function firstHeading(md: string): string | null {
  const m = md.match(/^\s*#\s+(.+?)\s*#*\s*$/m)
  return m ? cleanInline(m[1]) : null
}

/** Remove common inline Markdown so titles/descriptions read as plain text. */
function cleanInline(s: string): string {
  return s
    .replace(/!\[[^\]]*\]\([^)]*\)/g, '') // images
    .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1') // links -> text
    .replace(/[*_`~]/g, '') // emphasis / code marks
    .replace(/\s+/g, ' ')
    .trim()
}

/** First real prose paragraph (skips headings, quotes, rules, lists, tables). */
function firstParagraph(md: string): string {
  const lines = md.split(/\r?\n/)
  const buf: string[] = []
  for (const raw of lines) {
    const line = raw.trim()
    if (!line) {
      if (buf.length) break
      continue
    }
    if (
      /^#{1,6}\s/.test(line) || // heading
      /^>/.test(line) || // blockquote
      /^([-*_])\1{2,}$/.test(line.replace(/\s/g, '')) || // hr
      /^([-*+]|\d+[.)])\s/.test(line) || // list item
      /^\|/.test(line) || // table
      /^```/.test(line) || // fence
      /^<!--/.test(line) // comment
    ) {
      if (buf.length) break
      continue
    }
    buf.push(line)
  }
  const text = cleanInline(buf.join(' '))
  if (text.length <= 200) return text
  return text.slice(0, 197).replace(/\s+\S*$/, '') + '…'
}

export function isDevFile(name: string): boolean {
  return DEV_DENYLIST.has(name.toLowerCase())
}

/** Discover every publishable worldbuilding document at the repository root. */
export function discoverDocs(): DocMeta[] {
  const entries = fs.readdirSync(ROOT, { withFileTypes: true })
  const docs: DocMeta[] = []

  for (const entry of entries) {
    if (!entry.isFile()) continue
    if (!/\.md$/i.test(entry.name)) continue
    if (isDevFile(entry.name)) continue

    let raw: string
    try {
      raw = fs.readFileSync(path.join(ROOT, entry.name), 'utf-8')
    } catch {
      continue
    }

    let data: Record<string, any> = {}
    let content = raw
    try {
      const parsed = matter(raw)
      data = parsed.data || {}
      content = parsed.content
    } catch {
      // Malformed front matter: treat the whole file as body, keep building.
      console.warn(`[archive] Could not parse front matter for "${entry.name}" — publishing raw body.`)
    }

    // Privacy flags — the author can hide any document explicitly.
    if (data.publish === false || data.draft === true) continue

    const title = String(data.title || firstHeading(content) || stripExt(entry.name))
    const description = String(data.description || firstParagraph(content) || '')

    docs.push({
      file: entry.name,
      link: '/' + stripExt(entry.name),
      title,
      description,
      genre: data.genre ? String(data.genre) : undefined,
      cover: data.cover ? String(data.cover) : undefined,
      order: typeof data.order === 'number' ? data.order : 999
    })
  }

  docs.sort((a, b) => a.order - b.order || a.title.localeCompare(b.title))
  return docs
}

/**
 * Every root-level Markdown file that must be EXCLUDED from the build
 * (dev files + anything flagged private). Returned as glob patterns so the
 * files are never rendered as pages nor added to the search index.
 */
export function excludedGlobs(): string[] {
  const published = new Set(discoverDocs().map((d) => d.file))
  const excluded: string[] = []
  for (const entry of fs.readdirSync(ROOT, { withFileTypes: true })) {
    if (!entry.isFile() || !/\.md$/i.test(entry.name)) continue
    if (entry.name === 'index.md') continue // homepage stays
    if (!published.has(entry.name)) excluded.push(entry.name)
  }
  return excluded
}
