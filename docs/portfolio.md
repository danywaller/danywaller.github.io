# Portfolio items

## Files and layout

- Source: `_portfolio/*.html` or `_portfolio/*.md`
- Full page: `_layouts/single.html`
- Portfolio index: `_pages/portfolio.html` at `/portfolio/`
- Listing entry: `_includes/archive-single.html`

The Portfolio page lists every item in `site.portfolio`, with a divider between entries. Existing items use HTML, but Jekyll also accepts Markdown. Default URLs are `/portfolio/<filename>/`.

## Add an item

Create `_portfolio/my-project.md`:

```markdown
---
title: "My project"
excerpt: "A short description for the portfolio listing."
collection: portfolio
permalink: /portfolio/my-project/
---

## About the project

Describe the project, its results, and any relevant links.

![Project image]({{ '/images/my-project.png' | relative_url }})
```

Copy an existing `.html` item instead if its HTML structure is a better starting point. Images and videos belong in `images/`; downloadable reports belong in `files/`. The `excerpt` can contain HTML when a listing needs an image. `header.teaser` adds a teaser to grid listings and `header.image` adds a full-page header image.

## Add a group of blog posts

`_portfolio/instrument-genealogy.html` adds one Instrument Genealogy item to `/portfolio/`. That item links to `/portfolio/instrument-genealogy/`, which automatically collects all published blog posts tagged `instrument genealogy`, ordered by most recently modified. Add or remove that tag on a post to change its membership; no separate portfolio item is needed for each post.

To create another group, add a portfolio file with its own front matter and this body:

```liquid
{% assign project_posts = site.tags['my project tag'] | sort: 'modified' | reverse %}
{% for post in project_posts %}
  {% include archive-single.html %}
{% else %}
  <p>Project posts are coming soon.</p>
{% endfor %}
```

Add the exact tag `my project tag` to the relevant posts. The posts themselves stay in `_posts/`.

## Edit, hide, or remove

Edit an item's source file to change its title, excerpt, or body. Preserve its permalink, or add `redirect_from` when changing it. To hide an item temporarily, add `published: false`. Delete its source file to remove it from the automatic portfolio list and remove any manual links to its URL.

Deleting a portfolio page that groups blog posts keeps those posts available at their own URLs. Remove tags from posts only if they should also leave the tag archive.

The CV sync script reads only `_portfolio/*.md`; it currently omits the existing HTML items. If a Markdown item appears on the CV, regenerate `_data/cv.json` after adding or removing it and review the resulting changes as described in [the maintenance index](README.md).
