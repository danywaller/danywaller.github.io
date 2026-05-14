#!/usr/bin/env python3
"""Generate publication markdown files from one or more BibTeX sources.

This script remains as a compatibility entry point for workflows that keep
separate BibTeX files for journals, proceedings, or books. It now shares the
same markdown-building code as `publications.py`, so both BibTeX entry points
produce the same front matter shape.
"""

from __future__ import annotations

from pathlib import Path

from generator_utils import (
    build_publication_markdown,
    build_publication_record_from_bib_entry,
    clean_value,
    parse_bibtex_entries,
    write_markdown,
)


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = SCRIPT_DIR.parent / "_publications"


# Each source can override the shared BibTeX defaults. The category field is
# what the site uses to group publications on the archive page.
publist = {
    "proceeding": {
        "file": "proceedings.bib",
        "venuekey": "booktitle",
        "venue-pretext": "In the proceedings of ",
        "collection": "publications",
        "category": "conferences",
        "permalink_prefix": "/publication/",
    },
    "journal": {
        "file": "pubs.bib",
        "venuekey": "journal",
        "venue-pretext": "",
        "collection": "publications",
        "category": "manuscripts",
        "permalink_prefix": "/publication/",
    },
}


def generate_source(source_name, source_config, output_dir):
    """Generate markdown for a configured BibTeX source."""
    source_path = SCRIPT_DIR / source_config["file"]
    if not source_path.exists():
        print(f"Skipped {source_name}: missing {source_path.name}")
        return

    for entry in parse_bibtex_entries(source_path):
        try:
            record = build_publication_record_from_bib_entry(entry, source_config)
            md_filename, markdown = build_publication_markdown(record)
            destination = write_markdown(output_dir, md_filename, markdown)
            print(f"Wrote {destination.name}")
        except KeyError as error:
            title = clean_value(entry["fields"].get("title")) or entry["key"]
            print(f"Skipped {title}: missing expected field {error}")


def main():
    """Run the generator for each configured BibTeX source."""
    for source_name, source_config in publist.items():
        generate_source(source_name, source_config, DEFAULT_OUTPUT_DIR)


if __name__ == "__main__":
    main()
