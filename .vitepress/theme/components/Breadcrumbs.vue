<script setup lang="ts">
import { computed } from 'vue'
import { useData, withBase } from 'vitepress'
import { data as collections } from '../collections.data.mts'

const { page, frontmatter } = useData()

const title = computed(
  () => (frontmatter.value.title as string) || page.value.title || 'Document'
)
// Hidden on the homepage (which has no meaningful breadcrumb trail).
const isHome = computed(() => page.value.relativePath === 'index.md')

// A document inside a collection folder gets the collection as a middle crumb.
// On the collection's own page (its index.md) there is no middle crumb.
const parent = computed(() => {
  const parts = page.value.relativePath.split('/')
  if (parts.length < 2 || parts[parts.length - 1] === 'index.md') return null
  return collections.find((c) => c.dir === parts[0]) || null
})
</script>

<template>
  <nav v-if="!isHome" class="breadcrumbs" aria-label="Breadcrumb">
    <a :href="withBase('/')">Portfolio</a>
    <span class="breadcrumbs-sep">/</span>
    <template v-if="parent">
      <a :href="withBase(parent.link)">{{ parent.title }}</a>
      <span class="breadcrumbs-sep">/</span>
    </template>
    <span class="breadcrumbs-current">{{ title }}</span>
  </nav>
</template>
