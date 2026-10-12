<script setup lang="ts">
// Notice at the top of a document whose front matter carries `outdated`.
// Optional `outdated_note` replaces the default sentence.
import { computed } from 'vue'
import { useData } from 'vitepress'
import { outdatedLabel } from '../../lib/outdated.mts'

const { frontmatter } = useData()

const label = computed(() => outdatedLabel(frontmatter.value.outdated))
const note = computed(
  () =>
    (frontmatter.value.outdated_note as string) ||
    'This is an earlier version of the document. It is kept for reference and no longer reflects the current state of the project.'
)
</script>

<template>
  <aside v-if="label" class="outdated-notice" role="note">
    <strong>{{ label }}</strong>
    <span>{{ note }}</span>
  </aside>
</template>
