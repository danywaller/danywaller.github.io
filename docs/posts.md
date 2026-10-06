# Blog posts

## Files and layout

- Source: `_posts/YYYY-MM-DD-slug.md`
- Full page: `_layouts/single.html`
- Listings: `_includes/archive-single.html`
- Blog index: `_pages/year-archive.html` at `/year-archive/`, ordered by most recently modified
- Default URL: `/posts/<slug>/`, configured in the posts defaults in `_config.yml`

The filename still needs its date prefix because Jekyll uses it to identify posts, order them internally, and schedule future posts. Do not add a `date` field to the front matter. The filename date does not appear in the permalink or as a publication date on the page.

## Add a post

Create a file such as `_posts/2026-10-06-my-new-post.md`:

```markdown
---
title: "My new post"
excerpt: "A short description for listings and search previews."
permalink: /posts/my-new-post/
tags:
  - instrument genealogy
---

Write the article here.
```

An explicit `permalink` is optional; the default uses the filename's slug. Keep slugs unique and use lowercase words separated by hyphens. `categories`, `header.teaser`, and `header.image` are optional. Image filenames for the header are relative to `images/`.

Posts tagged `instrument genealogy` automatically appear on the Instrument Genealogy collection page at `/portfolio/instrument-genealogy/`, ordered by most recently modified. The portfolio index links to this collection as one item. Add or remove the tag to include or exclude a post. Blog posts are not currently linked from the header; add `/year-archive/` to `_data/navigation.yml` if desired.

## Automatic modified timestamp

`_plugins/post_modified.rb` sets `modified` during every build and local preview refresh. It uses the most recent commit that changed the Markdown file. For uncommitted edits or new files, it uses the file's modification time. Without Git, it also uses the file's modification time.

The build computes this metadata without rewriting the Markdown source. A front matter `modified` value is optional and is overridden automatically, so it does not need manual maintenance. On the deployed site, the timestamp changes after the edited file is committed, pushed, and rebuilt. Unrelated commits and repeated builds leave it unchanged.

The timestamp appears as `Modified:` below the article content, in UTC. The same value supplies search metadata, the feed's updated timestamp, and sitemap modification dates. `.github/workflows/deploy_pages.yml` fetches the full Git history so deployment can find each file's last edit.

## Edit, hide, or remove a post

Edit the Markdown body or front matter and preview the page. Keep the permalink stable when only the title changes. If a URL must change, preserve the previous address:

```yaml
redirect_from:
  - /posts/old-slug/
```

To hide a post, add `published: false` and `sitemap: false`. To keep a draft, move it into `_drafts/` and remove the filename's date prefix. Drafts can be previewed with `bundle exec jekyll serve --drafts -H localhost`. A future filename date keeps a post scheduled while `future: false` remains set in `_config.yml`.

To remove a post permanently, delete its file and remove any manually written links to its URL. Automatic tag, category, blog, and instrument genealogy listings update on the next build. Delete associated assets only if no other page uses them.
