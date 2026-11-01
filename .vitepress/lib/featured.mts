import fs from 'node:fs'
import path from 'node:path'
import { ROOT, groupByCategory } from './docs.mts'

// Editorial introductions only. Excerpts are read from the published works at
// build time, so hiding a work also removes its sample from the homepage.
const selections = [
  {
    file: 'Worldbuilding/METAMIND.md',
    pitch: 'Humanity survives a pandemic through a cure that makes obedience biologically comfortable. Those immune to its behavioural effects must confront a peaceful world built on the loss of refusal.',
    format: 'Worldbuilding bible · Dystopian science fiction',
    stage: 'Development dossier',
    focus: 'Start here for an original speculative world presented through an inquiry, testimony and competing accounts.',
    sampleStart: 'Humanity was not conquered by soldiers, law, ideology, or machines.',
    sampleEnd: 'At the center of the architecture stood Lyber Vergießen,',
    fullLabel: 'Read the full dossier'
  },
  {
    file: 'Worldbuilding/ASPECTROS.md',
    pitch: 'In a world where souls reshape reality and stone retains human grief, a quiet historian records the people that histories of power leave behind.',
    format: 'Worldbuilding bible · Metaphysical fantasy',
    stage: 'World and character development',
    focus: 'Read next for an original fantasy cosmology told through the voice of Lótus, historian of Verdalis.',
    sampleStart: 'I am not a powerful man.',
    sampleEnd: 'This book is my attempt to set down the whole of it',
    fullLabel: 'Read the full world bible'
  },
  {
    file: 'Game Design Documents/ASTROPIRE.md',
    pitch: 'A stranded boy builds a machine workforce to steer an asteroid home. When those machines begin to wake up, every production decision becomes a question of obedience, care and freedom.',
    format: 'Game design document · Survival / Automation',
    stage: 'Game concept and systems design',
    focus: 'Explore how narrative themes become player decisions, production systems and consequences in an original game concept.',
    sampleStart: 'A twelve-year-old boy wakes from a failing cryogenic capsule',
    sampleEnd: '### 1.2 Design Pillars',
    fullLabel: 'Read the full game design'
  }
]

export function loadFeaturedWorks() {
  const published = new Map(groupByCategory().flatMap((g) => g.docs).map((doc) => [doc.file, doc]))
  return selections.flatMap((selection) => {
    const doc = published.get(selection.file)
    if (!doc) return []

    const source = fs.readFileSync(path.join(ROOT, selection.file), 'utf-8')
    const start = source.indexOf(selection.sampleStart)
    const end = source.indexOf(selection.sampleEnd, start)
    if (start < 0 || end <= start || source.indexOf(selection.sampleStart, start + 1) >= 0) {
      throw new Error(`[archive] Review the featured excerpt boundaries for "${selection.file}".`)
    }
    const sample = source.slice(start, end).trim()
    return [{
      file: doc.file,
      title: doc.title,
      link: doc.link,
      pitch: selection.pitch,
      format: selection.format,
      stage: selection.stage,
      focus: selection.focus,
      fullLabel: selection.fullLabel,
      paragraphs: sample.split(/\n\s*\n/).map((p) => p.replace(/\s+/g, ' ').trim()),
      minutes: Math.max(1, Math.ceil(sample.split(/\s+/).length / 200))
    }]
  })
}
