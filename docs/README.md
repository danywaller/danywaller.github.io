# Content maintenance

Use these guides to add, edit, hide, or remove the site's content:

- [Blog posts](posts.md)
- [Poems and poetry collections](poems.md)
- [Portfolio items](portfolio.md)
- [Publications](publications.md)
- [Career map locations and field work](career-map.md)

The files in `docs/` are repository documentation and are excluded from the built website.

## Shared structure

Content files start with YAML front matter between two `---` lines. The rest of the file is Markdown or HTML. Collection defaults in `_config.yml` select the layout and features such as the author sidebar and sharing links.

`_layouts/` controls full pages, `_includes/` controls repeated elements such as archive entries, and `_pages/` contains section landing pages. Add images to `images/` and downloadable files to `files/`.

Header links are configured in `_data/navigation.yml`. Add a link by copying an existing `title` and `url` entry under `main`, remove its entry to hide it, or reorder entries to change the order. Hiding a navigation link keeps the page accessible through its URL.

## Preview and publish

Run `./preview.sh` from the repository root, then open `http://localhost:4000`. Check both the section listing and the individual page. Restart the preview after editing `_config.yml` or a file in `_plugins/`.

For a build without starting the server:

```bash
bundle exec jekyll build
```

Commit and push the content changes to `master` to publish through `.github/workflows/deploy_pages.yml`. Changes to `docs/` do not appear on the website.

## Keep the CV in sync

The CV page reads `_data/cv.json`; editing a collection file does not automatically regenerate that JSON. After changing poems or publications, run the existing sync script if the CV should reflect those changes:

```bash
/Users/danywaller/code/venvs/webpae/bin/python scripts/sync_cv_json_from_site.py --input _pages/cv.md --output _data/cv.json --config _config.yml
```

This rebuilds multiple CV sections from `_pages/cv.md`, `_config.yml`, and the collections. Review the JSON changes before committing. The script reads Markdown portfolio items only; existing HTML portfolio items are not included by that importer.

Career map addresses are manual fields in `_data/cv.json`. The sync script preserves them only when the work or education entry's identifying fields still match. Follow the [career map guide](career-map.md) when changing those entries.
