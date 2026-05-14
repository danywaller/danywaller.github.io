# Markdown generator scripts

This folder contains the helper scripts that generate publication markdown
files for the Jekyll site from BibTeX sources.

## Supported inputs

`publications.py`

- `.bib`

`pubsFromBib.py`

- One or more BibTeX files configured in the `publist` dictionary

## Default behavior

If you run the scripts without arguments from anywhere in the repository:

- `markdown_generator/publications.py` reads `markdown_generator/output.bib`
  and writes files into `_publications/`
- `markdown_generator/pubsFromBib.py` reads the configured BibTeX files from
  `markdown_generator/` and writes files into `_publications/`

## Usage examples

```bash
python3 markdown_generator/publications.py
python3 markdown_generator/publications.py files/bibtex1.bib --output-dir /tmp/publications
python3 markdown_generator/pubsFromBib.py
```

## Poems

Poems are hand-authored markdown files in `_poems/` rather than generated from
TSV input.

Common front matter fields:

- `title`
- `collection: poems`
- `type: unpublished`, `published`, or `submitted`
- `poem_collection: "Litany of the Spacefaring"` when the poem belongs on a collection subpage
- `permalink: /poems/litany-of-the-spacefaring/maven/` when you want a nested poem URL
- `hyperlink`
- `venue`
- `date`
- `image`
- `images`

If `hyperlink` is present, poem templates render it as a small `learn more`
link in the poem subtitle rather than wrapping the poem title itself.

`collection` should stay as `poems`, since that is the site-wide poem content
type. `poem_collection` is optional and only describes the nested collection
subpage. If `poem_collection` is omitted, the poem can live directly under
`/poems/`. If it is present, create a matching collection page and use a nested
poem permalink such as `/poems/litany-of-the-spacefaring/maven/`.

Poems marked `published` must include both `venue` and `date`. The Poetry page
lists collections, each collection subpage lists poem titles only, and the full
poem body is reserved for the individual poem page.

`image` should be a single filename from `/images/`.

`images` can be a list of filenames:

```yaml
images:
  - image-one.jpg
  - image-two.png
```

or a list of richer objects:

```yaml
images:
  - image_path: image-one.jpg
    alt: "Optional alt text"
    caption: "Optional caption"
```

## Notes

- The scripts escape a small set of YAML-sensitive characters before writing
  front matter.
- `publications.py` and `pubsFromBib.py` now share the same BibTeX markdown
  builder, so generated files have a consistent shape.
- BibTeX-generated publication files keep the existing numeric filename date
  prefix so regenerated URLs stay stable, but their front matter `date` now
  uses `YYYY-FullMonth` and ignores any BibTeX `day` value.
