# Johnny Kestler — Archive

Original worldbuilding, fiction, fanfiction and game design documents by
**Johnny Kestler** (João Vitor Perazzolo), published as a static site straight
from this repository.

## The archive

Every Markdown file at the root of this repository is a work, and every work
becomes a page automatically. There is no index to maintain and no build step to
run by hand: push a new `.md` and it is published, titled and searchable on the
next deploy.

**Privacy is the default.** A file is published only if it sits at the root, is
not a development file, and does not carry `publish: false` or `draft: true` in
its front matter. Anything inside a subfolder stays private — which is why the
engine below never appears in the library.

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

## Kestlerium

`kestlerium/` holds a living world that runs on the real Brasília clock: if it
is 9pm on a Tuesday here, it is 9pm on the same Tuesday there, and it is night.
A visitor opens the page and sees the present moment — nothing starts when they
arrive, and the world keeps going after they close the tab.

It is a small village going about ordinary life: routines, encounters, gossip
that arrives distorted, people who believe wrong versions of what they saw. The
point is not the map — it is what you cannot see by looking.

The engine is Python 3.11 with no dependencies, and **no paid model is involved
in any part of it.** Its own documentation lives in `kestlerium/README.md`, and
none of it is published to the archive.

There is a door to it on the homepage. It is a door, not a landing page: the
archive stays an archive unless you choose to walk through.

## Author

**Johnny Kestler** — worldbuilder and author.

## Licence

All rights reserved — see `LICENCE`. Reading here is welcome; reuse is not
granted by default.
