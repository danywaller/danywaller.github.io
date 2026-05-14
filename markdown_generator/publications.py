#!/usr/bin/env python3
"""Generate publication markdown files from a BibTeX source.

This script is the single-file BibTeX entry point for the publication
generator. It reads one `.bib` file, converts each entry into the site's
publication front matter shape, and writes the markdown files into
`../_publications`.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from generator_utils import (
    build_publication_markdown,
    build_publication_record_from_bib_entry,
    clean_value,
    parse_bibtex_entries,
    write_markdown,
)


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT_PATH = SCRIPT_DIR / "output.bib"
DEFAULT_OUTPUT_DIR = SCRIPT_DIR.parent / "_publications"


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input_path",
        nargs="?",
        default=str(DEFAULT_INPUT_PATH),
        help="Input BibTeX file. Defaults to markdown_generator/output.bib.",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Directory where markdown files should be written.",
    )
    return parser.parse_args()


def generate_from_bibtex(input_path, output_dir):
    """Generate publication markdown from a standard BibTeX file."""
    for entry in parse_bibtex_entries(input_path):
        try:
            record = build_publication_record_from_bib_entry(entry)
            md_filename, markdown = build_publication_markdown(record)
            destination = write_markdown(output_dir, md_filename, markdown)
            print(f"Wrote {destination.name}")
        except KeyError as error:
            title = clean_value(entry["fields"].get("title")) or entry["key"]
            print(f"Skipped {title}: missing expected field {error}")


def main():
    """Run the generator."""
    args = parse_args()
    input_path = Path(args.input_path).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()

    if not input_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_path}")

    if input_path.suffix.lower() != ".bib":
        raise ValueError("Publication generation now supports BibTeX input only.")

    generate_from_bibtex(input_path, output_dir)


if __name__ == "__main__":
    main()
