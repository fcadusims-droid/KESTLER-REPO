import { loadFeaturedWorks } from '../lib/featured.mts'

declare const data: ReturnType<typeof loadFeaturedWorks>
export { data }

export default {
  watch: ['../../*.md', '../../*/*.md', '../lib/featured.mts'],
  load: loadFeaturedWorks
}
