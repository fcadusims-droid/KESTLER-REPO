<script setup lang="ts">
// The document grid of a collection page. Placed in a folder's index.md as
// <Collection />; it lists every published document in that folder.
import { computed } from 'vue'
import { useData, withBase } from 'vitepress'
import { data as collections } from '../collections.data.mts'

const { page } = useData()

const collection = computed(() => {
  const dir = page.value.relativePath.split('/')[0]
  return collections.find((c) => c.dir === dir)
})
</script>

<template>
  <div v-if="collection" class="collection">
    <p class="collection-count">
      {{ collection.docs.length }}
      {{ collection.docs.length === 1 ? 'document' : 'documents' }}
    </p>
    <ul class="archive-grid" role="list">
      <li v-for="doc in collection.docs" :key="doc.file" class="archive-card">
        <a class="archive-card-link" :href="withBase(doc.link)">
          <div class="archive-cover" :class="{ 'has-image': doc.cover }">
            <img v-if="doc.cover" :src="withBase(doc.cover)" :alt="doc.title" loading="lazy" />
            <span v-else class="archive-cover-title">{{ doc.title }}</span>
          </div>
          <div class="archive-card-body">
            <div class="archive-tags">
              <span class="archive-badge" :data-cat="doc.category">{{ doc.category }}</span>
              <span v-if="doc.genre" class="archive-genre">{{ doc.genre }}</span>
              <span v-if="doc.outdated" class="archive-outdated">{{ doc.outdated }}</span>
            </div>
            <h3 class="archive-card-title">{{ doc.title }}</h3>
            <p v-if="doc.description" class="archive-card-desc">{{ doc.description }}</p>
            <span class="archive-card-cta">Open document →</span>
          </div>
        </a>
      </li>
    </ul>
  </div>
</template>
