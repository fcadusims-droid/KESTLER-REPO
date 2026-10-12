<script setup lang="ts">
// A thin bar at the top of a work that fills as the reader goes down it.
// Shown on documents only, never on the homepage.
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useData, useRoute } from 'vitepress'

const { frontmatter, page } = useData()
const route = useRoute()
const progress = ref(0)

const isDoc = computed(
  () => frontmatter.value.layout !== 'page' && page.value.relativePath !== 'index.md'
)

function update() {
  const el = document.documentElement
  const max = el.scrollHeight - el.clientHeight
  progress.value = max > 0 ? Math.min(1, Math.max(0, el.scrollTop / max)) : 0
}

onMounted(() => {
  update()
  window.addEventListener('scroll', update, { passive: true })
  window.addEventListener('resize', update, { passive: true })
})
onBeforeUnmount(() => {
  window.removeEventListener('scroll', update)
  window.removeEventListener('resize', update)
})
watch(() => route.path, () => requestAnimationFrame(update))
</script>

<template>
  <div
    v-if="isDoc"
    class="reading-progress"
    :style="{ width: '100%', transform: `scaleX(${progress})` }"
    aria-hidden="true"
  />
</template>
