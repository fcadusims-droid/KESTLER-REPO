import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import { h, nextTick, onMounted, watch } from 'vue'
import { useRoute } from 'vitepress'
import mediumZoom from 'medium-zoom'

import Library from './components/Library.vue'
import Collection from './components/Collection.vue'
import Breadcrumbs from './components/Breadcrumbs.vue'
import BackToTop from './components/BackToTop.vue'
import OutdatedNotice from './components/OutdatedNotice.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      // Breadcrumbs above every document, then the notice on outdated ones.
      'doc-before': () => [h(Breadcrumbs), h(OutdatedNotice)],
      // Floating back-to-top button on every page.
      'layout-bottom': () => h(BackToTop)
    })
  },
  enhanceApp({ app }) {
    // Makes <Library /> usable from index.md.
    app.component('Library', Library)
    // Makes <Collection /> usable from a collection folder's index.md.
    app.component('Collection', Collection)
  },
  setup() {
    const route = useRoute()
    const enableZoom = () => {
      // Click-to-zoom on every content image (opt out with the `no-zoom` class).
      mediumZoom('.vp-doc img:not(.no-zoom)', {
        background: 'var(--vp-c-bg)',
        margin: 24
      })
    }
    onMounted(enableZoom)
    watch(
      () => route.path,
      () => nextTick(enableZoom)
    )
  }
} satisfies Theme
