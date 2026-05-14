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
- `type: "Poem"`
- `hyperlink`
- `venue`
- `date`
- `image`
- `images`

If `hyperlink` is present, poem templates render it as a small `learn more`
link in the poem subtitle rather than wrapping the poem title itself.

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
