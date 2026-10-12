<script setup lang="ts">
// The document grid of a collection page. Placed in a folder's index.md as
// <Collection />; it lists every published document in that folder, grouped
// by `section` when the documents declare one, in reading order.
import { computed } from 'vue'
import { useData, withBase } from 'vitepress'
import { data as collections } from '../collections.data.mts'

const { page } = useData()

const collection = computed(() => {
  const dir = page.value.relativePath.split('/')[0]
  return collections.find((c) => c.dir === dir)
})

const sections = computed(() => {
  const groups: { section?: string; docs: typeof collection.value.docs }[] = []
  for (const d of collection.value?.docs || []) {
    const g = groups.find((x) => x.section === d.section)
    if (g) g.docs.push(d)
    else groups.push({ section: d.section, docs: [d] })
  }
  return groups
})

// "01 · Lore" → "part-01-lore": a valid, stable anchor for the outline.
const anchor = (section: string) =>
  'part-' + section.toLowerCase().normalize('NFKD').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')

const first = computed(() => collection.value?.docs[0])
</script>

<template>
  <div v-if="collection" class="collection">
    <p class="collection-count">
      {{ collection.docs.length }}
      {{ collection.docs.length === 1 ? 'document' : 'documents' }}
      <template v-if="sections.length > 1"> · {{ sections.length }} parts</template>
    </p>
    <p v-if="first && collection.docs.length > 1 && !collection.shelf" class="collection-start">
      Start reading:
      <a :href="withBase(first.link)">{{ first.title }} →</a>
    </p>

    <section v-for="group in sections" :key="group.section || '_'" class="collection-part">
      <h2 v-if="group.section" :id="anchor(group.section)" class="collection-part-title">
        {{ group.section }}
      </h2>
      <ol class="collection-list">
        <li v-for="doc in group.docs" :key="doc.file" class="collection-item">
          <a :href="withBase(doc.link)">
            <span class="collection-item-title">{{ doc.title }}</span>
            <span v-if="doc.outdated" class="archive-outdated">{{ doc.outdated }}</span>
            <span v-if="doc.description" class="collection-item-desc">{{ doc.description }}</span>
          </a>
        </li>
      </ol>
    </section>
  </div>
</template>
