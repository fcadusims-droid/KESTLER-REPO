<script setup lang="ts">
import { computed, ref } from 'vue'
import { withBase } from 'vitepress'
import { data as groups } from '../library.data.mts'
import { data as featured } from '../featured.data.mts'

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
          (d.genre || '').toLowerCase().includes(q) ||
          // A collection matches when any of its documents does.
          (d.kind === 'collection' &&
            d.docs.some((c) => c.title.toLowerCase().includes(q)))
      )
    }))
    .filter((g) => g.docs.length > 0)
})

const nothing = computed(() => visibleGroups.value.length === 0)
</script>

<template>
  <div class="archive">
    <header class="archive-hero">
      <p class="archive-eyebrow">Portfolio</p>
      <h1 class="archive-title">João Vitor Perazzolo</h1>
      <p class="archive-aka">aka <strong>Johnny Kestler</strong></p>
      <p class="archive-sub">
        Writer and worldbuilder. {{ totalCount }} {{ totalCount === 1 ? 'work' : 'works' }} — worldbuilding
        bibles, original stories, fanfiction and game design documents.
        Begin with three selected original projects, or explore the full library.
      </p>
      <nav class="archive-entry-links" aria-label="Choose where to start">
        <a href="#selected-work" class="archive-primary-link">Start with selected work</a>
        <a href="#library">Browse all {{ totalCount }} works</a>
        <a href="#contact">Development &amp; collaboration</a>
      </nav>
    </header>

    <section v-if="featured.length" id="selected-work" class="archive-featured" aria-labelledby="selected-title">
      <p class="archive-eyebrow">A reading path</p>
      <h2 id="selected-title" class="archive-section-title">Three ways into the work</h2>
      <p class="archive-section-intro">
        Start with a dystopian dossier, step into a resonant fantasy world, then
        see how story becomes game design. Each introduction includes an excerpt
        from the existing document and a link to the full work.
      </p>
      <ol class="archive-featured-grid">
        <li v-for="(work, index) in featured" :key="work.file" class="archive-featured-card">
          <p class="archive-featured-number">0{{ index + 1 }} · Original project</p>
          <h3>{{ work.title }}</h3>
          <p class="archive-featured-pitch">{{ work.pitch }}</p>
          <dl class="archive-work-facts">
            <div><dt>Format</dt><dd>{{ work.format }}</dd></div>
            <div><dt>Stage</dt><dd>{{ work.stage }}</dd></div>
          </dl>
          <p class="archive-featured-focus">{{ work.focus }}</p>
          <a class="archive-card-cta" :href="withBase(work.link)">{{ work.fullLabel }} →</a>
          <details class="archive-sample">
            <summary>Read an excerpt <span>· {{ work.minutes }} min</span></summary>
            <div class="archive-sample-text">
              <p v-for="(paragraph, i) in work.paragraphs" :key="i">{{ paragraph }}</p>
              <a :href="withBase(work.link)">Continue with {{ work.title }} →</a>
            </div>
          </details>
        </li>
      </ol>
    </section>

    <section id="contact" class="archive-contact" aria-labelledby="contact-title">
      <div>
        <p class="archive-eyebrow">Development &amp; collaboration</p>
        <h2 id="contact-title">Discuss an original project</h2>
        <p>
          For development, adaptation or narrative design enquiries, contact
          Johnny Kestler. Mention the project, your organisation and the kind
          of collaboration you have in mind.
        </p>
      </div>
      <a class="archive-primary-link" href="mailto:johnnykestler@hotmail.com">johnnykestler@hotmail.com ↗</a>
    </section>

    <section id="library" aria-labelledby="library-title">
      <h2 id="library-title" class="archive-section-title">Explore the complete library</h2>
      <p class="archive-section-intro">
        Original worlds, fiction and game concepts sit alongside unofficial,
        non-commercial fan projects. Filter by type or search titles, genres and descriptions.
      </p>
      <div class="archive-controls">
        <input
          v-model="query"
          type="search"
          class="archive-search"
          placeholder="Search the portfolio…"
          aria-label="Search the portfolio"
        />
        <div class="archive-chips" role="group" aria-label="Filter by type">
          <button
            v-for="cat in categories"
            :key="cat"
            type="button"
            class="archive-chip"
            :class="{ active: activeCategory === cat }"
            :aria-pressed="activeCategory === cat"
            @click="activeCategory = cat"
          >
            {{ cat }}
          </button>
        </div>
      </div>

      <section v-for="group in visibleGroups" :key="group.category" class="archive-section">
        <h3 class="archive-section-title">
          {{ group.category }}
          <span class="archive-section-count">{{ group.docs.length }}</span>
        </h3>

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
                  <span v-if="doc.outdated" class="archive-outdated">{{ doc.outdated }}</span>
                  <span v-if="doc.kind === 'collection'" class="archive-genre">
                    Collection · {{ doc.docs.length }}
                    {{ doc.docs.length === 1 ? 'document' : 'documents' }}
                  </span>
                </div>
                <h4 class="archive-card-title">{{ doc.title }}</h4>
                <p v-if="doc.description" class="archive-card-desc">{{ doc.description }}</p>
                <span class="archive-card-cta">
                  {{ doc.kind === 'collection' ? 'Open collection →' : 'Open document →' }}
                </span>
              </div>
            </a>
          </li>
        </ul>
      </section>

      <p v-if="nothing" class="archive-empty">
        No universes match your search.
      </p>
    </section>

    <footer class="archive-colophon" role="contentinfo">
      <h2 class="archive-colophon-title">On authorship</h2>
      <p>
        The original works in this portfolio are created by
        <strong>João Vitor Perazzolo</strong>, who writes as
        <strong>Johnny Kestler</strong>. Fan works are unofficial and
        non-commercial: their underlying franchises, settings, characters and
        trademarks belong to their respective rights holders. Johnny Kestler
        created the original contributions made for those fan works.
      </p>
      <p>
        The documents were developed with <strong>Claude</strong>, an AI assistant
        by Anthropic, from the author's concepts and creative direction.
        The website was built with AI assistance.
      </p>
    </footer>
  </div>
</template>
