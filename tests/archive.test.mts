import assert from 'node:assert/strict'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'
import { test, type TestContext } from 'node:test'

const repo = fileURLToPath(new URL('../', import.meta.url))

async function fixture(t: TestContext, files: Record<string, string> = {}) {
  const cache = path.join(repo, '.vitepress/cache')
  fs.mkdirSync(cache, { recursive: true })
  const root = fs.mkdtempSync(path.join(cache, 'publication-test-'))
  t.after(() => fs.rmSync(root, { recursive: true, force: true }))
  fs.cpSync(path.join(repo, '.vitepress/lib'), path.join(root, '.vitepress/lib'), { recursive: true })
  const write = (file: string, content: string) => {
    const dest = path.join(root, file)
    fs.mkdirSync(path.dirname(dest), { recursive: true })
    fs.writeFileSync(dest, content)
  }
  write('index.md', '# Portfolio')
  for (const [file, content] of Object.entries(files)) write(file, content)
  const docs = await import(pathToFileURL(path.join(root, '.vitepress/lib/docs.mts')).href)
  const featured = await import(pathToFileURL(path.join(root, '.vitepress/lib/featured.mts')).href)
  return { root, write, ...docs, ...featured }
}

test('the catalogue and exclusions follow publication flags and folder depth', async (t) => {
  const f = await fixture(t, {
    'Visible.md': '# Visible\n\nA public work.',
    'Hidden.md': '---\npublish: false\n---\n# Hidden',
    'Draft.md': '---\ndraft: true\n---\n# Draft',
    'README.md': '# Development notes',
    'Shelf/index.md': '---\nshelf: true\n---\n# Shelf',
    'Shelf/Story.md': '# Story',
    'Shelf/Draft.md': '---\ndraft: true\n---\n# Draft',
    'Shelf/nested/Notes.md': '# Notes',
    'Unlisted/Notes.md': '# Notes',
    'HiddenCollection/index.md': '---\npublish: false\n---\n# Hidden collection',
    'HiddenCollection/Secret.md': '# Secret',
    'narrativelean/index.md': '# Accidental collection',
    'narrativelean/Notes.md': '# Development notes',
    'tests/index.md': '# Accidental collection',
    'tests/Fixture.md': '# Test fixture'
  })
  assert.deepEqual([...f.publishedFiles()].sort(), ['Shelf/Story.md', 'Shelf/index.md', 'Visible.md', 'index.md'])
  const excluded = f.excludedGlobs()
  for (const file of ['Hidden.md', 'Draft.md', 'README.md', 'Shelf/Draft.md', 'Shelf/nested/Notes.md', 'Unlisted/Notes.md', 'HiddenCollection/Secret.md', 'narrativelean/index.md', 'tests/Fixture.md']) {
    assert.ok(excluded.includes(file), `${file} must be excluded`)
  }
  assert.deepEqual(f.groupByCategory().flatMap((g: any) => g.docs.map((d: any) => d.file)).sort(), ['Shelf/Story.md', 'Visible.md'])
})

for (const file of ['Broken.md', 'Shelf/index.md', 'Shelf/Broken.md']) {
  test(`invalid YAML in ${file} stops discovery instead of publishing raw text`, async (t) => {
    const f = await fixture(t, { 'Shelf/index.md': '# Shelf', [file]: '---\ndraft: true\ntitle: [unfinished\n---\nDO NOT PUBLISH' })
    assert.throws(() => f.publishedFiles(), (error: Error) => error.message.includes(file) && error.message.includes('Build stopped'))
    assert.throws(() => f.publishedFiles(), /Build stopped/, 'repeated discovery must still reject invalid metadata')
  })
}

for (const flag of ['publish', 'draft']) {
  for (const value of ['"false"', 'null', '[]']) {
    test(`${flag}: ${value} is rejected rather than interpreted as a public document`, async (t) => {
      const f = await fixture(t, { 'Ambiguous.md': `---\n${flag}: ${value}\n---\n# Ambiguous` })
      assert.throws(() => f.publishedFiles(), /must be true or false, without quotes/)
    })
  }
}

const works = ['Worldbuilding/METAMIND.md', 'Worldbuilding/ASPECTROS.md', 'Game Design Documents/ASTROPIRE.md']
function featuredFiles() {
  return Object.fromEntries([
    ['Worldbuilding/index.md', '---\nshelf: true\ncategory: Worldbuilding\n---\n# Worlds'],
    ['Game Design Documents/index.md', '---\nshelf: true\ncategory: Game Design Document\n---\n# Games'],
    ...works.map((file) => [file, fs.readFileSync(path.join(repo, file), 'utf-8')])
  ])
}

test('all three featured excerpts come from the actual published source documents', async (t) => {
  const f = await fixture(t, featuredFiles())
  const selected = f.loadFeaturedWorks()
  assert.deepEqual(selected.map((d: any) => d.title), ['MetaMind', 'Aspectros', 'ASTROPIRE'])
  for (const doc of selected) {
    const source = fs.readFileSync(path.join(f.root, doc.file), 'utf-8').replace(/\s+/g, ' ')
    assert.ok(source.includes(doc.paragraphs.join(' ')), `${doc.title}: excerpt must remain verbatim`)
    assert.ok(f.publishedFiles().has(doc.file))
    assert.ok(doc.minutes >= 1)
  }
})

test('excluding a featured document or shelf removes its excerpt from the homepage data', async (t) => {
  const f = await fixture(t, featuredFiles())
  const source = fs.readFileSync(path.join(f.root, works[0]), 'utf-8')
  f.write(works[0], source.replace('---\n', '---\ndraft: true\n'))
  assert.deepEqual(f.loadFeaturedWorks().map((d: any) => d.title), ['Aspectros', 'ASTROPIRE'])
  f.write('Worldbuilding/index.md', '---\npublish: false\n---\n# Worlds')
  assert.deepEqual(f.loadFeaturedWorks().map((d: any) => d.title), ['ASTROPIRE'])
})

test('a changed excerpt boundary requires review rather than silently taking another passage', async (t) => {
  const f = await fixture(t, featuredFiles())
  const source = fs.readFileSync(path.join(f.root, works[0]), 'utf-8')
  f.write(works[0], source.replace('Humanity was not conquered by soldiers, law, ideology, or machines.', 'Changed opening.'))
  assert.throws(() => f.loadFeaturedWorks(), /Review the featured excerpt boundaries/)
})
