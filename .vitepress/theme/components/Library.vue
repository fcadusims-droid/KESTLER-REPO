<script setup lang="ts">
import { computed, ref } from 'vue'
import { withBase } from 'vitepress'
import { data as groups } from '../library.data.mts'

const query = ref('')
const activeCategory = ref<string>('All')

const totalCount = computed(() =>
  groups.reduce((n, g) => n + g.docs.length, 0)
)

const categories = computed(() => ['All', ...groups.map((g) => g.category)])

// Groups filtered by the active category chip and the text query.
const visibleGroups = computed(() => {
  const q = query.value.trim().toLowerCase()
  return groups
    .filter(
      (g) => activeCategory.value === 'All' || g.category === activeCategory.value
    )
    .map((g) => ({
      category: g.category,
      docs: g.docs.filter(
        (d) =>
          !q ||
          d.title.toLowerCase().includes(q) ||
          (d.description || '').toLowerCase().includes(q) ||
          (d.genre || '').toLowerCase().includes(q)
      )
    }))
    .filter((g) => g.docs.length > 0)
})

const nothing = computed(() => visibleGroups.value.length === 0)
</script>

<template>
  <div class="archive">
    <header class="archive-hero">
      <p class="archive-eyebrow">The Archive</p>
      <h1 class="archive-title">A library of fictional universes</h1>
      <p class="archive-sub">
        {{ totalCount }} original {{ totalCount === 1 ? 'work' : 'works' }} — worldbuilding bibles,
        stories, fanfiction and game design documents. Choose a universe to begin reading.
      </p>

      <div class="archive-controls">
        <input
          v-model="query"
          type="search"
          class="archive-search"
          placeholder="Search the library…"
          aria-label="Search the library"
        />
        <div class="archive-chips" role="tablist" aria-label="Filter by type">
          <button
            v-for="cat in categories"
            :key="cat"
            type="button"
            class="archive-chip"
            :class="{ active: activeCategory === cat }"
            @click="activeCategory = cat"
          >
            {{ cat }}
          </button>
        </div>
      </div>
    </header>

    <section v-for="group in visibleGroups" :key="group.category" class="archive-section">
      <h2 class="archive-section-title">
        {{ group.category }}
        <span class="archive-section-count">{{ group.docs.length }}</span>
      </h2>

      <ul class="archive-grid" role="list">
        <li v-for="doc in group.docs" :key="doc.file" class="archive-card">
          <a class="archive-card-link" :href="withBase(doc.link)">
            <div class="archive-cover" :class="{ 'has-image': doc.cover }">
              <img
                v-if="doc.cover"
                :src="withBase(doc.cover)"
                :alt="doc.title"
                loading="lazy"
              />
              <span v-else class="archive-cover-title">{{ doc.title }}</span>
            </div>
            <div class="archive-card-body">
              <div class="archive-tags">
                <span class="archive-badge" :data-cat="group.category">{{ group.category }}</span>
                <span v-if="doc.genre" class="archive-genre">{{ doc.genre }}</span>
              </div>
              <h3 class="archive-card-title">{{ doc.title }}</h3>
              <p v-if="doc.description" class="archive-card-desc">{{ doc.description }}</p>
              <span class="archive-card-cta">Open document →</span>
            </div>
          </a>
        </li>
      </ul>
    </section>

    <p v-if="nothing" class="archive-empty">
      No universes match your search.
    </p>
  </div>
</template>
