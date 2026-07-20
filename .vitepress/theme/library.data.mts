// Build-time data loader that feeds the homepage grid.
// Reuses the exact same discovery rules as the sidebar and the build exclusion,
// so the homepage, the navigation and the search index can never drift apart.
import { discoverDocs, type DocMeta } from '../lib/docs.mts'

declare const data: DocMeta[]
export { data }

export default {
  // Re-run discovery when any root Markdown file changes (dev HMR).
  watch: ['../../*.md'],
  load(): DocMeta[] {
    return discoverDocs()
  }
}
