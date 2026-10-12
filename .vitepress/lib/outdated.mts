// Pure helper shared by the build (lib/docs.mts) and the browser
// (OutdatedNotice.vue): no Node imports here.

/** `outdated: true` or `outdated: 2026-10-06` (quoted or not) → a label, else undefined. */
export function outdatedLabel(value: unknown): string | undefined {
  if (value === undefined || value === null || value === false) return undefined
  if (value === true) return 'Outdated'
  const d = value instanceof Date ? value : new Date(String(value))
  if (Number.isNaN(d.getTime())) return 'Outdated'
  const when = d.toLocaleDateString('en-GB', { month: 'long', year: 'numeric', timeZone: 'UTC' })
  return `Outdated · ${when}`
}
