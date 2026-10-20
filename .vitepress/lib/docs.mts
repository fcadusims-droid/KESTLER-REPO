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
//     1. It is a Markdown file located either
//          a) at the REPOSITORY ROOT, or
//          b) directly inside a COLLECTION folder: a top-level folder that
//             contains an `index.md` (the collection's own page). A
//             collection is either one work in many documents (Resident Evil
//             Online), shown as one card, or a SHELF (`shelf: true` in its
//             index), a folder of separate works, each shown on its own.
//        Any other subfolder — one without an `index.md` — stays private,
//        and so does anything nested deeper inside a collection.
//     2. Its name is not in DEV_DENYLIST (README, LICENSE, config docs, ...).
//     3. Its front matter does NOT contain `publish: false` or `draft: true`
//        (on a collection's `index.md`, this hides the whole collection).
//
//   => A brand-new "New Universe.md" at the root is published automatically.
//   => A new file dropped into a collection folder joins that collection.
//   => A collection with no documents yet is not shown until it has one.
//   => A private note, a dev file, or anything flagged `publish: false`
//      is never built, never linked, and never indexed by search.
// ---------------------------------------------------------------------------

import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import matter from 'gray-matter'
import { outdatedLabel } from './outdated.mts'

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
  /** Path relative to the repo root, e.g. "One Blood.md" or "Saga/Part One.md" */
  file: string
  /** Route path without extension, e.g. "/One Blood" */
  link: string
  title: string
  description: string
  genre?: string
  /** Document type, e.g. "Worldbuilding", "Game Design Document", "Fanfiction". */
  category: string
  cover?: string
  order: number
  /** Set when the author marks the document as superseded: the date it dates from. */
  outdated?: string
  /** Inside a collection: the part the document belongs to, e.g. "01 · Lore". */
  section?: string
}

/** A folder of documents shown as one entry: a universe, a work, a game. */
export interface CollectionMeta extends DocMeta {
  kind: 'collection'
  /** Folder name, e.g. "Resident Evil Online" */
  dir: string
  /** The collection's documents, in reading order. */
  docs: DocMeta[]
  /** A shelf holds separate works (Fiction/, Fanfiction/, …), not one work. */
  shelf: boolean
}

export type LibraryItem = (DocMeta & { kind?: 'doc' }) | CollectionMeta

/** Canonical display order of the categories on the homepage and sidebar. */
export const CATEGORY_ORDER = [
  'Worldbuilding',
  'Fiction',
  'Fanfiction',
  'Game Design Document'
]

const DEFAULT_CATEGORY = 'Worldbuilding'

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
      /^<!--/.test(line) || // comment
      /^(Related|See also):/i.test(line) // cross-reference line
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

// Folders that are never collections, whatever they contain.
const NEVER_COLLECTIONS = new Set(['node_modules', 'public'])

function byOrder(a: DocMeta, b: DocMeta): number {
  return a.order - b.order || a.title.localeCompare(b.title)
}

/** Read one Markdown file into DocMeta, or null if it is private or unreadable. */
function readDoc(
  absPath: string,
  file: string,
  link: string,
  fallbackTitle: string,
  inherited: { category?: string; genre?: string } = {}
): DocMeta | null {
  let raw: string
  try {
    raw = fs.readFileSync(absPath, 'utf-8')
  } catch {
    return null
  }

  let data: Record<string, any> = {}
  let content = raw
  try {
    const parsed = matter(raw)
    data = parsed.data || {}
    content = parsed.content
  } catch {
    // Malformed front matter: treat the whole file as body, keep building.
    console.warn(`[archive] Could not parse front matter for "${file}" — publishing raw body.`)
  }

  // Privacy flags — the author can hide any document explicitly.
  if (data.publish === false || data.draft === true) return null

  const genre = data.genre ?? inherited.genre
  return {
    file,
    link,
    title: String(data.title || firstHeading(content) || fallbackTitle),
    description: String(data.description || firstParagraph(content) || ''),
    genre: genre ? String(genre) : undefined,
    category: String(data.category || inherited.category || DEFAULT_CATEGORY),
    cover: data.cover ? String(data.cover) : undefined,
    order: typeof data.order === 'number' ? data.order : 999,
    outdated: outdatedLabel(data.outdated),
    section: data.section ? String(data.section) : undefined
  }
}


/** Discover every publishable document at the repository root. */
export function discoverDocs(): DocMeta[] {
  const docs: DocMeta[] = []
  for (const entry of fs.readdirSync(ROOT, { withFileTypes: true })) {
    if (!entry.isFile() || !/\.md$/i.test(entry.name) || isDevFile(entry.name)) continue
    const doc = readDoc(
      path.join(ROOT, entry.name),
      entry.name,
      '/' + stripExt(entry.name),
      stripExt(entry.name)
    )
    if (doc) docs.push(doc)
  }
  return docs.sort(byOrder)
}

/**
 * Discover every collection: a top-level folder with an `index.md`.
 * The index's front matter describes the collection (title, description,
 * category, genre, cover, order); its documents inherit category and genre
 * unless they set their own. Empty collections are returned too — callers
 * decide whether to show them.
 */
export function discoverCollections(): CollectionMeta[] {
  const collections: CollectionMeta[] = []
  for (const entry of fs.readdirSync(ROOT, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue
    if (entry.name.startsWith('.') || NEVER_COLLECTIONS.has(entry.name)) continue
    const dirAbs = path.join(ROOT, entry.name)
    const indexAbs = path.join(dirAbs, 'index.md')
    if (!fs.existsSync(indexAbs)) continue

    const dir = entry.name
    const meta = readDoc(indexAbs, `${dir}/index.md`, `/${dir}/`, dir)
    if (!meta) continue // the whole collection is flagged private
    const shelf = readShelfFlag(indexAbs)

    const docs: DocMeta[] = []
    for (const child of fs.readdirSync(dirAbs, { withFileTypes: true })) {
      if (!child.isFile() || !/\.md$/i.test(child.name) || isDevFile(child.name)) continue
      const doc = readDoc(
        path.join(dirAbs, child.name),
        `${dir}/${child.name}`,
        `/${dir}/${stripExt(child.name)}`,
        stripExt(child.name),
        { category: meta.category, genre: meta.genre }
      )
      if (doc) docs.push(doc)
    }
    collections.push({ ...meta, kind: 'collection', dir, docs: docs.sort(byOrder), shelf })
  }
  return collections.sort(byOrder)
}

/**
 * A collection's documents split by `section`, in reading order: sections
 * appear in the order of their first document. Documents without a section
 * form one unnamed group.
 */
export function sectionsOf(docs: DocMeta[]): { section?: string; docs: DocMeta[] }[] {
  const groups: { section?: string; docs: DocMeta[] }[] = []
  for (const d of docs) {
    const g = groups.find((x) => x.section === d.section)
    if (g) g.docs.push(d)
    else groups.push({ section: d.section, docs: [d] })
  }
  return groups
}

function readShelfFlag(indexAbs: string): boolean {
  try {
    return matter(fs.readFileSync(indexAbs, 'utf-8')).data.shelf === true
  } catch {
    return false
  }
}

/** Collections that have at least one document — the ones the site shows. */
export function visibleCollections(): CollectionMeta[] {
  return discoverCollections().filter((c) => c.docs.length > 0)
}

/** Documents grouped by category, in canonical category order. */
export function groupByCategory(): { category: string; docs: LibraryItem[] }[] {
  // Root documents and collections share the grid: a collection is one entry,
  // and every work on a shelf is an entry of its own.
  const collections = visibleCollections()
  const docs: LibraryItem[] = [
    ...discoverDocs(),
    ...collections.filter((c) => !c.shelf),
    ...collections.filter((c) => c.shelf).flatMap((c) => c.docs)
  ].sort(byOrder)
  const seen = new Set<string>()
  const groups: { category: string; docs: LibraryItem[] }[] = []

  const pushGroup = (category: string) => {
    const items = docs.filter((d) => d.category === category)
    if (items.length) groups.push({ category, docs: items })
    seen.add(category)
  }

  for (const category of CATEGORY_ORDER) pushGroup(category)
  // Any custom categories the author invents later appear after the known ones.
  for (const d of docs) {
    if (!seen.has(d.category)) pushGroup(d.category)
  }
  return groups
}

/** Repo-relative paths of every Markdown file that is built as a page. */
export function publishedFiles(): Set<string> {
  const files = new Set<string>(['index.md']) // the homepage
  for (const d of discoverDocs()) files.add(d.file)
  for (const c of visibleCollections()) {
    files.add(c.file)
    for (const d of c.docs) files.add(d.file)
  }
  return files
}

/** Escape glob metacharacters so a file name like "Bible (3).md" matches itself. */
function literalGlob(p: string): string {
  return p.replace(/[\\()[\]{}*?!+@]/g, '\\$&')
}

/**
 * Every Markdown file in the repository that must be EXCLUDED from the build:
 * dev files, anything flagged private, every file in a non-collection folder,
 * anything nested inside a collection, and empty collections' index pages.
 * Returned as literal glob patterns so the files are never rendered as pages
 * nor added to the search index.
 */
export function excludedGlobs(): string[] {
  const published = publishedFiles()
  const excluded: string[] = []
  const walk = (rel: string) => {
    for (const entry of fs.readdirSync(path.join(ROOT, rel), { withFileTypes: true })) {
      const child = rel ? `${rel}/${entry.name}` : entry.name
      if (entry.isDirectory()) {
        if (entry.name === 'node_modules' || entry.name === '.git') continue
        walk(child)
      } else if (entry.isFile() && /\.md$/i.test(entry.name) && !published.has(child)) {
        excluded.push(literalGlob(child))
      }
    }
  }
  walk('')
  return excluded
}
