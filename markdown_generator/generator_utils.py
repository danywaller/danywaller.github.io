#!/usr/bin/env python3
"""Shared helpers for the markdown generator scripts.

The original repository shipped a few small one-off scripts that produced
publication and talk markdown. This module keeps the same lightweight feel,
but centralises the pieces that are still shared across those scripts:

- escaping front matter content
- assembling markdown files in the site's expected format
- parsing BibTeX entries
- normalising BibTeX date fields
"""

from __future__ import annotations

import math
from pathlib import Path
import re


HTML_ESCAPE_TABLE = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
}

MONTH_LOOKUP = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}
MONTH_NAME_BY_NUMBER = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

DEFAULT_PUBLICATION_COLLECTION = "publications"
DEFAULT_PUBLICATION_CATEGORY = "manuscripts"
DEFAULT_PUBLICATION_PERMALINK = "/publication/"
ALLOWED_POEM_TYPES = {"unpublished", "published", "submitted"}
DEFAULT_BIBTEX_SOURCE = {
    "venuekey": "journal",
    "venue-pretext": "",
    "collection": DEFAULT_PUBLICATION_COLLECTION,
    "category": DEFAULT_PUBLICATION_CATEGORY,
    "permalink_prefix": DEFAULT_PUBLICATION_PERMALINK,
}
BIBTEX_SOURCE_BY_ENTRY_TYPE = {
    "article": DEFAULT_BIBTEX_SOURCE,
    "book": {
        "venuekey": "publisher",
        "venue-pretext": "",
        "collection": DEFAULT_PUBLICATION_COLLECTION,
        "category": "books",
        "permalink_prefix": DEFAULT_PUBLICATION_PERMALINK,
    },
    "inbook": {
        "venuekey": "publisher",
        "venue-pretext": "",
        "collection": DEFAULT_PUBLICATION_COLLECTION,
        "category": "books",
        "permalink_prefix": DEFAULT_PUBLICATION_PERMALINK,
    },
    "inproceedings": {
        "venuekey": "booktitle",
        "venue-pretext": "In the proceedings of ",
        "collection": DEFAULT_PUBLICATION_COLLECTION,
        "category": "conferences",
        "permalink_prefix": DEFAULT_PUBLICATION_PERMALINK,
    },
    "conference": {
        "venuekey": "booktitle",
        "venue-pretext": "In the proceedings of ",
        "collection": DEFAULT_PUBLICATION_COLLECTION,
        "category": "conferences",
        "permalink_prefix": DEFAULT_PUBLICATION_PERMALINK,
    },
    "proceedings": {
        "venuekey": "booktitle",
        "venue-pretext": "In the proceedings of ",
        "collection": DEFAULT_PUBLICATION_COLLECTION,
        "category": "conferences",
        "permalink_prefix": DEFAULT_PUBLICATION_PERMALINK,
    },
}


def clean_value(value):
    """Return a stripped string for a table or BibTeX value."""
    if value is None:
        return ""

    if isinstance(value, float) and math.isnan(value):
        return ""

    return str(value).strip()


def html_escape(text):
    """Escape the small set of characters that commonly break YAML strings."""
    return "".join(HTML_ESCAPE_TABLE.get(character, character) for character in clean_value(text))


def normalize_category(value, default=DEFAULT_PUBLICATION_CATEGORY):
    """Normalise a publication category key for use in Jekyll front matter."""
    category = clean_value(value).lower().replace(" ", "-")
    return category or default


def strip_bibtex_markup(value):
    """Remove simple BibTeX formatting markers from a field."""
    return clean_value(value).replace("{", "").replace("}", "").replace("\\", "")


def make_url_slug(value):
    """Create a file-safe slug from a title-like string."""
    clean_title = strip_bibtex_markup(value).replace(" ", "-")
    slug = re.sub(r"\[.*\]|[^a-zA-Z0-9_-]", "", clean_title)
    return slug.replace("--", "-").strip("-")


def normalize_month(value, default=""):
    """Normalise a BibTeX month field into a two-digit month string."""
    text = clean_value(value).strip("{}").lower()
    if not text:
        return default

    if text.isdigit():
        month_number = int(text)
        if 1 <= month_number <= 12:
            return f"{month_number:02d}"
        return default

    if text in MONTH_LOOKUP:
        return f"{MONTH_LOOKUP[text]:02d}"

    short_text = text[:3]
    if short_text in MONTH_LOOKUP:
        return f"{MONTH_LOOKUP[short_text]:02d}"

    return default


def month_number_to_name(value):
    """Convert a two-digit month string into a full month name."""
    text = clean_value(value)
    if not text or not text.isdigit():
        return ""

    return MONTH_NAME_BY_NUMBER.get(int(text), "")


def build_bibtex_publication_dates(fields):
    """Build stable filename and front matter dates from BibTeX fields.

    The generated markdown keeps the existing numeric filename date format so
    regenerated publication URLs do not churn. The front matter date uses the
    full month name from the BibTeX entry and intentionally omits the day.
    """
    pub_year = clean_value(fields.get("year")) or "1900"
    raw_month = clean_value(fields.get("month"))
    pub_month = normalize_month(raw_month, default="01")

    filename_date = f"{pub_year}-{pub_month}-01"
    front_matter_date = pub_year

    if raw_month:
        month_name = month_number_to_name(pub_month)
        if month_name:
            front_matter_date = f"{pub_year}-{month_name}"

    return filename_date, front_matter_date


def write_markdown(output_dir, filename, content):
    """Write a generated markdown file to disk."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    destination = output_path / Path(filename).name
    destination.write_text(content, encoding="utf-8")
    return destination


def split_top_level_items(text, separator=","):
    """Split a BibTeX string on top-level separators only."""
    items = []
    current = []
    brace_depth = 0
    quote_open = False
    previous_character = ""

    for character in text:
        if character == '"' and previous_character != "\\":
            quote_open = not quote_open
        elif not quote_open and character == "{":
            brace_depth += 1
        elif not quote_open and character == "}" and brace_depth > 0:
            brace_depth -= 1

        if character == separator and not quote_open and brace_depth == 0:
            item = "".join(current).strip()
            if item:
                items.append(item)
            current = []
        else:
            current.append(character)

        previous_character = character

    tail = "".join(current).strip()
    if tail:
        items.append(tail)

    return items


def strip_bibtex_wrappers(value):
    """Remove a single pair of outer BibTeX braces or quotes."""
    text = clean_value(value)
    if len(text) >= 2 and text[0] == "{" and text[-1] == "}":
        return text[1:-1]
    if len(text) >= 2 and text[0] == '"' and text[-1] == '"':
        return text[1:-1]
    return text


def parse_bibtex_author_names(author_field):
    """Parse a BibTeX author string into display names."""
    authors = []
    for author in split_author_field(author_field):
        clean_author = strip_bibtex_markup(author)
        if "," in clean_author:
            parts = [part.strip() for part in clean_author.split(",") if part.strip()]
            if len(parts) >= 2:
                authors.append(" ".join(parts[1:] + [parts[0]]).strip())
                continue
        authors.append(clean_author)

    return [author for author in authors if author]


def split_author_field(author_field):
    """Split a BibTeX author list on top-level `and` separators."""
    authors = []
    current = []
    brace_depth = 0
    quote_open = False
    text = clean_value(author_field)
    index = 0

    while index < len(text):
        character = text[index]

        if character == '"':
            quote_open = not quote_open
        elif not quote_open and character == "{":
            brace_depth += 1
        elif not quote_open and character == "}" and brace_depth > 0:
            brace_depth -= 1

        if (
            not quote_open
            and brace_depth == 0
            and text[index:index + 5].lower() == " and "
        ):
            author = "".join(current).strip()
            if author:
                authors.append(author)
            current = []
            index += 5
            continue

        current.append(character)
        index += 1

    author = "".join(current).strip()
    if author:
        authors.append(author)

    return authors


def parse_bibtex_entries(input_path):
    """Parse a BibTeX file with a lightweight standard-library parser."""
    text = Path(input_path).read_text(encoding="utf-8")
    entries = []
    index = 0

    while index < len(text):
        at_index = text.find("@", index)
        if at_index == -1:
            break

        type_start = at_index + 1
        open_index = type_start
        while open_index < len(text) and text[open_index] not in "{(":
            open_index += 1

        entry_type = text[type_start:open_index].strip().lower()
        if not entry_type:
            index = at_index + 1
            continue

        if open_index >= len(text):
            break

        opening_character = text[open_index]
        closing_character = "}" if opening_character == "{" else ")"

        close_index = find_matching_character(text, open_index, opening_character, closing_character)
        if close_index == -1:
            break

        body = text[open_index + 1:close_index].strip()
        index = close_index + 1

        if entry_type in {"comment", "preamble", "string"}:
            continue

        body_parts = split_top_level_items(body)
        if not body_parts:
            continue

        entry_key = clean_value(body_parts[0])
        fields = {}
        for field_text in body_parts[1:]:
            if "=" not in field_text:
                continue

            field_name, field_value = field_text.split("=", 1)
            fields[clean_value(field_name).lower()] = strip_bibtex_wrappers(field_value)

        entries.append(
            {
                "type": entry_type,
                "key": entry_key,
                "fields": fields,
                "authors": parse_bibtex_author_names(fields.get("author", "")),
            }
        )

    return entries


def find_matching_character(text, start_index, opening_character, closing_character):
    """Find the matching closing character for a BibTeX block."""
    depth = 0
    quote_open = False
    previous_character = ""

    for index in range(start_index, len(text)):
        character = text[index]

        if character == '"' and previous_character != "\\":
            quote_open = not quote_open

        if quote_open:
            previous_character = character
            continue

        if character == opening_character:
            depth += 1
        elif character == closing_character:
            depth -= 1
            if depth == 0:
                return index

        previous_character = character

    return -1


def get_bibtex_source_config(entry_type, overrides=None):
    """Return the output settings for a BibTeX entry type."""
    source_config = dict(BIBTEX_SOURCE_BY_ENTRY_TYPE.get(entry_type, DEFAULT_BIBTEX_SOURCE))
    if overrides:
        source_config.update(overrides)

    return source_config


def build_publication_record_from_bib_entry(entry, source_config=None):
    """Convert a BibTeX entry into the shared publication record format."""
    fields = entry["fields"]
    config = get_bibtex_source_config(entry["type"], source_config)

    pub_date, front_matter_date = build_bibtex_publication_dates(fields)
    pub_year = clean_value(fields.get("year")) or "1900"

    title = strip_bibtex_markup(fields["title"])
    venue_key = config["venuekey"]
    venue = config["venue-pretext"] + strip_bibtex_markup(fields[venue_key])
    url_slug = make_url_slug(title)

    author_names = entry.get("authors", [])
    if author_names:
        citation = ",  ".join(author_names)
        citation += f', "{title}." {venue}, {pub_year}.'
    else:
        citation = f'"{title}." {venue}, {pub_year}.'

    paper_url = clean_value(fields.get("url"))
    excerpt = clean_value(fields.get("note"))
    scholar_query = re.sub(r"\s+", "+", title)

    return {
        "bib_id": entry["key"],
        "title": title,
        "pub_date": pub_date,
        "front_matter_date": front_matter_date,
        "url_slug": url_slug,
        "venue": venue,
        "citation": citation,
        "excerpt": excerpt,
        "paper_url": paper_url,
        "collection": config["collection"],
        "category": config["category"],
        "permalink_prefix": config["permalink_prefix"],
        "scholar_query": scholar_query,
    }


def build_publication_markdown(record):
    """Build a publication markdown file from a normalised record."""
    pub_date = clean_value(record["pub_date"])
    front_matter_date = clean_value(record.get("front_matter_date")) or pub_date
    url_slug = clean_value(record["url_slug"])
    html_filename = f"{pub_date}-{url_slug}".replace("--", "-")
    md_filename = f"{html_filename}.md"

    collection = clean_value(record.get("collection")) or DEFAULT_PUBLICATION_COLLECTION
    category = normalize_category(record.get("category"))
    permalink_prefix = clean_value(record.get("permalink_prefix")) or DEFAULT_PUBLICATION_PERMALINK
    title = html_escape(record["title"])
    venue = html_escape(record["venue"])
    citation = html_escape(record["citation"])
    excerpt = html_escape(record.get("excerpt"))
    paper_url = clean_value(record.get("paper_url"))
    slides_url = clean_value(record.get("slides_url"))
    bibtex_url = clean_value(record.get("bibtex_url"))

    lines = [
        "---",
        f'title: "{title}"',
        f"collection: {collection}",
        f"category: {category}",
        f"permalink: {permalink_prefix}{html_filename}",
    ]

    if excerpt:
        lines.append(f"excerpt: '{excerpt}'")

    lines.extend(
        [
            format_publication_date_front_matter(front_matter_date),
            f"venue: '{venue}'",
        ]
    )

    if paper_url:
        lines.append(f"paperurl: '{paper_url}'")

    if slides_url:
        lines.append(f"slidesurl: '{slides_url}'")

    if bibtex_url:
        lines.append(f"bibtexurl: '{bibtex_url}'")

    lines.extend(
        [
            f"citation: '{citation}'",
            "---",
        ]
    )

    body = []

    if paper_url:
        body.append(f'[Access paper here]({paper_url}){{:target="_blank"}}')

    if excerpt:
        body.append(excerpt)

    if not paper_url:
        scholar_query = clean_value(record.get("scholar_query"))
        if scholar_query:
            body.append(
                "Use "
                f'[Google Scholar](https://scholar.google.com/scholar?q={scholar_query})'
                '{:target="_blank"} for the full citation'
            )

    markdown = "\n".join(lines)
    if body:
        markdown += "\n" + "\n\n".join(body) + "\n"
    else:
        markdown += "\n"

    return md_filename, markdown


def format_publication_date_front_matter(value):
    """Format a publication date for YAML front matter."""
    text = clean_value(value)
    if re.search(r"[A-Za-z]", text):
        return f'date: "{text}"'
    return f"date: {text}"


def build_talk_markdown(record):
    """Build a poem markdown file from a normalised record."""
    url_slug = clean_value(record["url_slug"])
    md_filename = f"{url_slug}.md"

    title = html_escape(record["title"])
    poem_type = clean_value(record.get("type")).lower() or "unpublished"
    poem_collection = clean_value(record.get("poem_collection"))
    hyperlink = clean_value(record.get("hyperlink")) or clean_value(record.get("talk_url"))
    venue = html_escape(record.get("venue"))
    talk_date = clean_value(record.get("date"))
    description = html_escape(record.get("description"))

    if poem_type not in ALLOWED_POEM_TYPES:
        raise ValueError("Poem type must be unpublished, published, or submitted.")

    if poem_type == "published" and (not venue or not talk_date):
        raise ValueError("Published poems must include both venue and date.")

    lines = [
        "---",
        f'title: "{title}"',
        "collection: poems",
        f"type: {poem_type}",
    ]

    if poem_collection:
        lines.append(f'poem_collection: "{html_escape(poem_collection)}"')

    if hyperlink:
        lines.append(f"hyperlink: {hyperlink}")

    if venue:
        lines.append(f'venue: "{venue}"')

    if talk_date:
        lines.append(f"date: {talk_date}")

    lines.append("---")

    body = []
    if description:
        body.append(description)

    markdown = "\n".join(lines)
    if body:
        markdown += "\n" + "\n\n".join(body) + "\n"
    else:
        markdown += "\n"

    return md_filename, markdown
