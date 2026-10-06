# Publications

## Files and layout

- Source: `_publications/*.md`
- Index: `_pages/publications.html` at `/publications/`
- Listing entry: `_includes/archive-single.html`
- Full local page: `_layouts/single.html`
- Category labels: `publication_category` in `_config.yml`

The index groups entries under Books, Journal Articles, or Conference Proceedings and lists each group in reverse collection order. Publication dates remain publication metadata; the blog timestamp changes do not apply to this collection.

## Add a publication manually

Create `_publications/2026-10-06-my-paper.md`:

```yaml
---
title: "My paper"
collection: publications
category: manuscripts
permalink: /publication/2026-10-06-my-paper
date: "2026-10-06"
publication_date: "October 2026"
author_summary: 'First Author, <strong>C. D. Waller</strong>, et al.'
venue: "Journal name"
doi: "10.xxxx/example"
paperurl: "https://doi.org/10.xxxx/example"
external_url: "https://doi.org/10.xxxx/example"
citation: 'Full publication citation.'
---
```

Replace the example DOI and links with real values. Use `books`, `manuscripts`, or `conferences` for `category`; an unconfigured category will be omitted by the grouped index. To add another category, define its key and `title` under `publication_category` in `_config.yml`.

`date` is a machine-readable date, while `publication_date` is the displayed label and can include a conference date range. `author_summary` is the short author list shown on the website; `citation` is the complete reference used by the CV importer. The Markdown body can be empty or contain an abstract and additional details.

Publication titles link to `external_url`, falling back to `paperurl`. Omit both when the title should link to its local publication page. Optional download fields include `slidesurl` and `bibtexurl`.

## Generate from BibTeX

The generator workflow is described in `markdown_generator/readme.md`. From the repository root:

```bash
/Users/danywaller/code/venvs/webpae/bin/python markdown_generator/publications.py
```

By default it reads `markdown_generator/output.bib` and writes `_publications/`. `markdown_generator/pubsFromBib.py` uses its configured `publist` instead. Review generated changes before committing, especially URLs and manually curated details.

Keep BibTeX source records consistent with manual publication edits if you plan to regenerate those files.

## Edit or remove

Edit the front matter to change an entry's metadata. Preserve the permalink so existing links continue working. Update the source BibTeX record too when that file is generated.

Delete the Markdown file to remove the entry from the site, and remove its BibTeX record if a generator would recreate it. To hide a publication temporarily, add `published: false`. The current CV importer reads source Markdown directly, including hidden files, so review or remove any corresponding JSON entry when hiding a publication.

After adding or removing publications, regenerate `_data/cv.json` with the sync command in [the maintenance index](README.md) to update the separate CV list. Review the JSON and any manual links to the old publication URL.
