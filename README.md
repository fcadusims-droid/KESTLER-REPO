# João Vitor Perazzolo — aka Johnny Kestler

The writing portfolio of **João Vitor Perazzolo**, who writes as
**Johnny Kestler**: worldbuilding bibles, original stories, fanfiction and game
design documents, published as a static site straight from this repository.

## The site

Every Markdown file at the root of this repository is a work, and every work
becomes a page automatically. There is no index to maintain and no build step to
run by hand: push a new `.md` and it is published, titled and searchable on the
next deploy.

**Privacy is the default.** A file is published only if it sits at the root (or
directly inside a collection folder, below), is not a development file, and does
not carry `publish: false` or `draft: true` in its front matter. Any other
subfolder stays private and never appears in the portfolio.

**Collections.** A universe, work or game with several documents gets its own
folder. A top-level folder becomes a collection when it contains an `index.md`;
every `.md` dropped into it then joins the collection, with one card on the
homepage and its own page listing the documents. A collection stays hidden
until it has at least one document. Example: `Resident Evil Online/`. Inside a
collection, `order` sets the reading order and `section: "01 · Lore"` groups
documents into parts.

```yaml
# Resident Evil Online/index.md
---
title: Resident Evil Online
description: One line for the homepage card.
category: Fanfiction        # its documents inherit category and genre
genre: Survival Horror
---

<Collection />
```

**Outdated documents.** Add `outdated: "2026-10-06"` (or `outdated: true`) to the
front matter: the card gets an "Outdated" badge and the page opens with a
notice. `outdated_note` replaces the default sentence.

Front matter drives the presentation:

```yaml
---
title: "One Blood"
description: "A dark-fantasy worldbuilding bible…"
genre: "Dark Fantasy"
category: "Worldbuilding"
order: 1
---
```

`category` groups the work on the homepage and in the sidebar; `order` sorts it
within the group. Both are optional — a file with no front matter is still
published, using its filename as the title.

## Author

**João Vitor Perazzolo**, aka **Johnny Kestler** — writer and worldbuilder.

Every universe, character and story here is the author's original creation.
The documents and the site were written and built with Claude, an AI assistant
by Anthropic, working from the author's own concepts, worlds and direction.

## Licence

All rights reserved — see `LICENCE`. Reading here is welcome; reuse is not
granted by default.
