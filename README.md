# João Vitor Perazzolo — aka Johnny Kestler

The writing portfolio of **João Vitor Perazzolo**, who writes as
**Johnny Kestler**: worldbuilding bibles, original stories, fanfiction and game
design documents, published as a static site straight from this repository.

## The site

Every Markdown file at the root of this repository is a work, and every work
becomes a page automatically. There is no index to maintain and no build step to
run by hand: push a new `.md` and it is published, titled and searchable on the
next deploy.

**Privacy is the default.** A file is published only if it sits at the root, is
not a development file, and does not carry `publish: false` or `draft: true` in
its front matter. Anything inside a subfolder stays private and never appears
in the portfolio.

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
