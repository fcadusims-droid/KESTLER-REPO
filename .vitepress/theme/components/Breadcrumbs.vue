<script setup lang="ts">
import { computed } from 'vue'
import { useData, withBase } from 'vitepress'

const { page, frontmatter } = useData()

const title = computed(
  () => (frontmatter.value.title as string) || page.value.title || 'Document'
)
// Hidden on the homepage (which has no meaningful breadcrumb trail).
const isHome = computed(() => page.value.relativePath === 'index.md')
</script>

<template>
  <nav v-if="!isHome" class="breadcrumbs" aria-label="Breadcrumb">
    <a :href="withBase('/')">The Library</a>
    <span class="breadcrumbs-sep">/</span>
    <span class="breadcrumbs-current">{{ title }}</span>
  </nav>
</template>
