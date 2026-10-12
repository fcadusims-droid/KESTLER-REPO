// Build-time data loader for collection pages and breadcrumbs: every folder
// with an index.md and at least one published document.
import { visibleCollections, type CollectionMeta } from '../lib/docs.mts'

declare const data: CollectionMeta[]
export { data }

export default {
  watch: ['../../*/*.md'],
  load(): CollectionMeta[] {
    return visibleCollections()
  }
}
