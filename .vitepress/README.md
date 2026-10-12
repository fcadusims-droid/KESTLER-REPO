# How the Archive works (internal notes)

This folder turns the repository into a public reading website (**The Kestler
Archive**) using [VitePress](https://vitepress.dev). This file is internal — it
lives inside `.vitepress/`, so it is **never** published or indexed by search.

## The one rule that matters

**Git is the CMS.** You never edit the website by hand.

- Add a `Something.md` at the repository root → it becomes a page automatically.
- Edit any document and push → the site rebuilds and updates.
- Rename or delete a document → the site follows on the next push.

Every push to `main` triggers `.github/workflows/deploy.yml`, which builds the
site and publishes it to GitHub Pages. No manual step.

## What gets published (privacy by default)

A Markdown file is turned into a public page **only if all** of these are true:

1. It sits at the **repository root**, or directly inside a **collection
   folder** — a top-level folder with an `index.md` (see below). Files in any
   other subfolder, or nested deeper inside a collection, stay private.
2. Its name is not a known dev file (`README`, `LICENSE`, `CONTRIBUTING`, …).
3. Its front matter does **not** contain `publish: false` or `draft: true`.

So a new universe is public automatically, but a private note, a config file,
or anything you flag stays off the site — and out of the search index.

To hide a document, add this to the top of the file:

```yaml
---
publish: false
---
```

The rules live in one place: `.vitepress/lib/docs.mts`. The sidebar, the
homepage grid, the build exclusions and the search index all read from it, so
they can never disagree.

## Collections (folders)

A universe, work or game with many documents lives in its own folder:

```
Resident Evil Online/
  index.md        ← makes the folder a collection; its front matter describes it
  Part One.md     ← every .md here joins the collection automatically
  Part Two.md
```

- `index.md` front matter: `title`, `description`, `category`, `genre`,
  `cover`, `order` (same fields as a document). Its body is the collection page;
  put `<Collection />` where the document grid should appear.
- Documents inherit the collection's `category` and `genre` unless they set
  their own; `order` sorts them inside the collection.
- `section: "01 · Lore"` groups documents into parts: the collection page,
  the sidebar and Previous/Next all follow `order`, part by part.
- A document that cites another of the same collection by file name in code
  (`` `survival.md` ``) gets a link to it, labelled with its title.
- The homepage shows one card per collection; the sidebar shows the collection
  with its documents underneath; documents get a breadcrumb back to it.
- A collection with no documents yet is not built or shown.
- `publish: false` on the `index.md` hides the whole collection.
- A folder without `index.md` is private, as before.

## Outdated documents

`outdated: "2026-10-06"` (or `outdated: true`) in the front matter adds an
"Outdated" badge to the card and a notice at the top of the page. Set
`outdated_note` to replace the default sentence.

## Optional front matter

Every field is optional. Without it, the title comes from the first `# heading`
(or the filename) and the description from the first paragraph.

```yaml
---
title: One Blood
description: A dark fantasy universe.
genre: Dark Fantasy
cover: assets/oneblood.jpg   # relative to the repo root
order: 1                     # lower numbers sort first on the homepage
---
```

## Images

Reference images normally — `![](cover.png)` or `![](assets/cover.png)`. Paths
resolve relative to the Markdown file (the repo root). Drop the image anywhere
in the repo and it is bundled on build. Content images are click-to-zoom
(add the class `no-zoom` to opt a single image out).

## Local development

```bash
npm install
npm run docs:dev      # live preview at http://localhost:5173
npm run docs:build    # production build into .vitepress/dist
npm run docs:preview  # serve the production build locally
```

## If you rename the repository or use a custom domain

Update `BASE` (and `HOSTNAME`) at the top of `.vitepress/config.mts`, and the
`Sitemap:` line in `public/robots.txt`. Both can also be overridden at build
time with the `SITE_BASE` / `SITE_HOSTNAME` environment variables.

## One-time GitHub setup

In the repository: **Settings → Pages → Build and deployment → Source →
GitHub Actions**. After that, every push deploys automatically.
