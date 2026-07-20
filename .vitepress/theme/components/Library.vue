<script setup lang="ts">
import { computed, ref } from 'vue'
import { withBase } from 'vitepress'
import { data as docs } from '../library.data.mts'

const query = ref('')

const filtered = computed(() => {
  const q = query.value.trim().toLowerCase()
  if (!q) return docs
  return docs.filter(
    (d) =>
      d.title.toLowerCase().includes(q) ||
      (d.description || '').toLowerCase().includes(q) ||
      (d.genre || '').toLowerCase().includes(q)
  )
})

function initials(title: string): string {
  return title
    .split(/\s+/)
    .filter(Boolean)
    .slice(0, 2)
    .map((w) => w[0])
    .join('')
    .toUpperCase()
}
</script>

<template>
  <div class="archive">
    <header class="archive-hero">
      <p class="archive-eyebrow">The Archive</p>
      <h1 class="archive-title">A library of fictional universes</h1>
      <p class="archive-sub">
        {{ docs.length }} original {{ docs.length === 1 ? 'work' : 'works' }} — worldbuilding bibles,
        design documents and chronicles. Choose a universe to begin reading.
      </p>
      <div class="archive-filter">
        <input
          v-model="query"
          type="search"
          placeholder="Filter the library…"
          aria-label="Filter the library"
        />
      </div>
    </header>

    <ul class="archive-grid" role="list">
      <li v-for="doc in filtered" :key="doc.file" class="archive-card">
        <a class="archive-card-link" :href="withBase(doc.link)">
          <div class="archive-cover" :class="{ 'has-image': doc.cover }">
            <img
              v-if="doc.cover"
              :src="withBase(doc.cover)"
              :alt="doc.title"
              loading="lazy"
            />
            <span v-else class="archive-cover-fallback">{{ initials(doc.title) }}</span>
          </div>
          <div class="archive-card-body">
            <span v-if="doc.genre" class="archive-genre">{{ doc.genre }}</span>
            <h2 class="archive-card-title">{{ doc.title }}</h2>
            <p v-if="doc.description" class="archive-card-desc">{{ doc.description }}</p>
            <span class="archive-card-cta">Open document →</span>
          </div>
        </a>
      </li>
    </ul>

    <p v-if="filtered.length === 0" class="archive-empty">
      No universes match “{{ query }}”.
    </p>
  </div>
</template>
