// Build-time data loader that feeds the homepage.
// Reuses the exact same discovery + grouping rules as the sidebar and the build
// exclusion, so the homepage, the navigation and the search index never drift.
import { groupByCategory, type DocMeta } from '../lib/docs.mts'

export interface LibraryGroup {
  category: string
  docs: DocMeta[]
}

declare const data: LibraryGroup[]
export { data }

export default {
  // Re-run discovery when any root Markdown file changes (dev HMR).
  watch: ['../../*.md'],
  load(): LibraryGroup[] {
    return groupByCategory()
  }
}
