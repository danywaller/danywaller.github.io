#!/usr/bin/env python3
"""Generate publication markdown files from a mixed BibTeX source.

This script mirrors the `PubsFromBib.ipynb` workflow: it reads a single mixed
BibTeX file, lets the shared generator infer journal articles vs conference
proceedings from each entry's BibTeX type, and writes publication markdown into
`../_publications`.
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


publist = {
    "mixed": {
        "file": "output.bib",
        "collection": "publications",
        "permalink_prefix": "/publication/",
    },
}


def generate_source(source_name, source_config, output_dir):
    """Generate markdown for a configured BibTeX source."""
    source_path = SCRIPT_DIR / source_config["file"]
    record_config = {key: value for key, value in source_config.items() if key != "file"}

    if not source_path.exists():
        print(f"Skipped {source_name}: missing {source_path.name}")
        return

    for entry in parse_bibtex_entries(source_path):
        try:
            record = build_publication_record_from_bib_entry(entry, record_config)
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
