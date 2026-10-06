# Poems and poetry collections

## Files and layout

- Source: `_poems/*.md`
- Full page: `_layouts/poem.html`
- Poetry index: `_pages/poems.html` at `/poems/`
- Listing entry: `_includes/archive-single-poem.html`
- Existing collection page: `_pages/litany-for-the-spacefaring.html`

Poem dates and publication details are separate from the automatic blog modification timestamps.

## Add an individual poem

Create `_poems/my-poem.md`:

```markdown
---
title: "My poem"
collection: poems
type: unpublished
permalink: /poems/my-poem/
date: 2026-10-06
---

First line
<br>
Second line
<br><br>
The next stanza
```

Without `poem_collection`, it appears under Individual Poems. Use `<br>` for deliberate line breaks and `<br><br>` for stanza breaks when ordinary Markdown spacing does not produce the desired layout.

`type` must be `unpublished`, `submitted`, or `published`. A published poem must have both `venue` and `date` for the CV importer. `hyperlink` adds a small “learn more” link. `image`, `image_alt`, and `image_caption` add a single image from `images/`. For multiple images:

```yaml
images:
  - image_path: my-image.png
    alt: "Description of the image"
    caption: "Optional caption"
```

## Add a poem to a collection

Set these fields on the poem:

```yaml
poem_collection: "My collection"
permalink: /poems/my-collection/my-poem/
```

Keep `collection: poems`. The `poem_collection` value groups poems within that collection; it does not replace the site's collection type.

For a new collection, create `_pages/my-collection.html`:

```liquid
---
layout: archive
title: "My collection"
permalink: /poems/my-collection/
author_profile: true
poem_collection: "My collection"
---

<p>A short introduction to the collection.</p>

{% assign collection_poems = site.poems | where: "poem_collection", page.poem_collection %}
{% for post in collection_poems reversed %}
  {% include archive-single-poem.html %}
{% endfor %}
```

The collection name must match exactly. The collection URL must use its slug, such as `My collection` → `my-collection`, because the Poetry page builds that link automatically. The collection appears once it has at least one poem.

## Edit or remove

Edit the poem's file to change its text, status, or metadata. To move it out of a collection, remove `poem_collection` and choose a standalone permalink. Add `redirect_from` for a previous URL if links should keep working.

Delete the poem's file to remove it from the site, then regenerate `_data/cv.json` using the command in [the maintenance index](README.md) if it is also listed on the CV. For a temporary hide, use `published: false`; this is a visibility flag distinct from `type: published`.

To remove a collection, move or delete its poems and delete its `_pages/` collection page. Remove manual links to that page. Deleting the landing page alone leaves a broken collection link while any poem still names the collection.
