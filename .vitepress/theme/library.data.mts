// Build-time data loader that feeds the homepage.
// Reuses the exact same discovery + grouping rules as the sidebar and the build
// exclusion, so the homepage, the navigation and the search index never drift.
import { groupByCategory, type LibraryItem } from '../lib/docs.mts'

export interface LibraryGroup {
  category: string
  docs: LibraryItem[]
}

declare const data: LibraryGroup[]
export { data }

export default {
  // Re-run discovery when any root or collection Markdown file changes (dev HMR).
  watch: ['../../*.md', '../../*/*.md'],
  load(): LibraryGroup[] {
    return groupByCategory()
  }
}
