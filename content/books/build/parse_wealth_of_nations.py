"""
Parse Adam Smith's Wealth of Nations into per-book originals JSON files.

Structure: 5 Books + Introduction, 32 chapters, some with PART subdivisions.
Non-dialogue prose treatise -- paragraph-based segmentation.

Segmentation rules:
- Each paragraph (blank-line-delimited block) = 1 thought
- Merge: paragraph < 60 words with neighbor (cap 450 combined)
- Split: paragraph > 400 words at argumentative pivots or sentence boundaries
- Table blocks (price data) preserved as single thoughts
"""

import json
import re
import os

BUILD_DIR = os.path.dirname(__file__)
SOURCE = os.path.join(BUILD_DIR, '..', 'Adam Smith - Wealth of Nations')
OUTPUT_DIR = BUILD_DIR

ROMAN_MAP = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6,
             'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10, 'XI': 11}

BOOK_RE = re.compile(r'^BOOK\s+([IVX]+)\.\s*$')
CHAPTER_RE = re.compile(r'^CHAPTER\s+([IVX]+)\.\s*$')
PART_RE = re.compile(r'^PART\s+([IVX]+)[.\s]')
INTRO_RE = re.compile(r'^INTRODUCTION[\s.]*$')
# Table line: starts with a year (4 digits) or spaces + digits in £/s/d columns
TABLE_RE = re.compile(r'^\s*\d{4}\s+\d|^\s+\d+\)\s+\d|^\s+Average\s+\d|^\s+Total\s+\d')
# Chapter title line (ALL CAPS, follows CHAPTER line)
TITLE_RE = re.compile(r'^OF\s|^THAT\s|^HOW\s|^CONCLUSION\s')


def roman_to_int(s):
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
    result = 0
    for i, c in enumerate(s):
        if i + 1 < len(s) and vals[c] < vals[s[i + 1]]:
            result -= vals[c]
        else:
            result += vals[c]
    return result


def word_count(text):
    return len(text.split())


def is_table_line(line):
    """Check if a line looks like part of a price/data table."""
    stripped = line.strip()
    if not stripped:
        return False
    # Lines with £ s d header
    if re.match(r'^\s*\xa3\s+s\s+d', stripped) or re.match(r'.*\xa3\s+s\s+d', stripped):
        return True
    # Year + numbers pattern
    if re.match(r'^\d{4}\s+\d', stripped):
        return True
    # Indented number columns (continuation rows)
    if re.match(r'^\s+\d+\s+\d+\s+\d', stripped):
        return True
    # Average/Total rows
    if re.match(r'^\s*(Average|Total)\s+\d', stripped):
        return True
    # Divisor rows like "64) 129  13  6"
    if re.match(r'^\s*\d+\)\s+\d', stripped):
        return True
    # Column header lines with multiple spaces between items
    if re.match(r'^\s+in each year|^\s+prices in|^\s+each year in', stripped):
        return True
    return False


def try_split(text):
    """Split a long paragraph at argumentative pivots or sentence boundaries."""
    pivot_pattern = (
        r'(?<=[.;])\s+(?=(?:'
        r'But |Now |Again |Further |On the other hand|However |Yet |'
        r'For |Hence |Therefore |Moreover |Similarly |In like manner |'
        r'Nor |And so |It follows |The reason is |This is why |'
        r'In the |The |Such |We |Suppose |Take |Then |'
        r'Secondly|Thirdly|Fourthly|Fifthly|'
        r'It is |There is |There are |'
        r'If |When |Where |Though |Whether ))'
    )

    parts = re.split(pivot_pattern, text)

    if len(parts) == 1:
        sentences = re.split(r'(?<=[.])\s+', text)
        if len(sentences) >= 4:
            mid = len(sentences) // 2
            part1 = ' '.join(sentences[:mid])
            part2 = ' '.join(sentences[mid:])
            if word_count(part1) >= 50 and word_count(part2) >= 50:
                return [part1, part2]
        return [text]

    result = []
    current = parts[0]
    for part in parts[1:]:
        if word_count(current) < 100:
            current = current + ' ' + part
        else:
            result.append(current)
            current = part
    result.append(current)

    # Recursively split any still-long parts
    final = []
    for r in result:
        if word_count(r) > 400:
            final.extend(try_split_at_sentence(r))
        else:
            final.append(r)
    return final


def try_split_at_sentence(text):
    """Fallback split at sentence boundary near midpoint."""
    sentences = re.split(r'(?<=[.])\s+', text)
    if len(sentences) < 2:
        return [text]
    mid_words = word_count(text) // 2
    cumulative = 0
    best_split = len(sentences) // 2
    best_dist = float('inf')
    for i, sent in enumerate(sentences[:-1]):
        cumulative += word_count(sent)
        dist = abs(cumulative - mid_words)
        if dist < best_dist and cumulative >= 50:
            best_split = i + 1
            best_dist = dist
    part1 = ' '.join(sentences[:best_split])
    part2 = ' '.join(sentences[best_split:])
    return [part1, part2]


def segment_paragraphs(paragraphs):
    """Apply merge/split rules to convert paragraphs into thoughts."""
    # First pass: split long paragraphs
    raw = []
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        wc = word_count(para)
        if wc > 400:
            raw.extend(try_split(para))
        else:
            raw.append(para)

    # Second pass: merge short paragraphs
    thoughts = []
    i = 0
    while i < len(raw):
        para = raw[i]
        wc = word_count(para)

        if wc < 60:
            # Try merging forward
            if i + 1 < len(raw):
                merged = para + '\n\n' + raw[i + 1]
                if word_count(merged) <= 450:
                    thoughts.append(merged)
                    i += 2
                    continue
            # Try merging backward
            if thoughts:
                merged = thoughts[-1] + '\n\n' + para
                if word_count(merged) <= 450:
                    thoughts[-1] = merged
                    i += 1
                    continue
            thoughts.append(para)
        else:
            thoughts.append(para)
        i += 1

    # Third pass: deduplicate consecutive identical
    deduped = []
    for t in thoughts:
        if not deduped or t != deduped[-1]:
            deduped.append(t)

    return deduped


def parse_text():
    """Parse the full text into a structured hierarchy."""
    with open(SOURCE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print(f"Total lines: {len(lines)}")

    # Skip header (lines 1-4) and TOC (lines 5-47)
    # Find where actual content starts: "INTRODUCTION AND PLAN OF THE WORK." after TOC
    content_start = 0
    toc_found = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        # The TOC starts at line 5 with "INTRODUCTION AND PLAN OF THE WORK."
        # The actual content starts at the SECOND occurrence (line 48)
        if stripped == 'INTRODUCTION AND PLAN OF THE WORK.':
            if toc_found:
                content_start = i
                break
            toc_found = True

    print(f"Content starts at line {content_start + 1}")

    # Parse into sections: intro, then books with chapters
    # Structure: list of books, each book has chapters, each chapter has paragraphs
    books = {}  # book_num -> {chapters: {ch_num -> {paragraphs: [], part_info: []}}}

    current_book = 0  # 0 = Introduction
    current_chapter = 0
    current_para_lines = []
    paragraphs = []  # accumulates paragraphs for current chapter
    in_table = False
    table_lines = []

    i = content_start
    while i < len(lines):
        line = lines[i].rstrip('\n')
        stripped = line.strip()

        # Check for BOOK boundary
        book_match = BOOK_RE.match(stripped)
        if book_match:
            # Save current chapter
            if current_para_lines:
                paragraphs.append(' '.join(current_para_lines))
                current_para_lines = []
            if in_table and table_lines:
                paragraphs.append('\n'.join(table_lines))
                table_lines = []
                in_table = False
            _save_chapter(books, current_book, current_chapter, paragraphs)
            paragraphs = []

            current_book = roman_to_int(book_match.group(1))
            current_chapter = -1  # Will be set by next CHAPTER or INTRODUCTION
            # Skip the title line that follows BOOK line
            i += 1
            if i < len(lines) and TITLE_RE.match(lines[i].strip()):
                i += 1
            continue

        # Check for CHAPTER boundary
        ch_match = CHAPTER_RE.match(stripped)
        if ch_match:
            # Save current chapter
            if current_para_lines:
                paragraphs.append(' '.join(current_para_lines))
                current_para_lines = []
            if in_table and table_lines:
                paragraphs.append('\n'.join(table_lines))
                table_lines = []
                in_table = False
            _save_chapter(books, current_book, current_chapter, paragraphs)
            paragraphs = []

            current_chapter = roman_to_int(ch_match.group(1))
            # Skip the chapter title line
            i += 1
            if i < len(lines) and (TITLE_RE.match(lines[i].strip()) or lines[i].strip().startswith('OF ')):
                i += 1
            continue

        # Check for INTRODUCTION within a book
        if INTRO_RE.match(stripped) and current_book > 0:
            if current_para_lines:
                paragraphs.append(' '.join(current_para_lines))
                current_para_lines = []
            _save_chapter(books, current_book, current_chapter, paragraphs)
            paragraphs = []
            current_chapter = 0  # Introduction = chapter 0
            i += 1
            continue

        # Check for PART boundary (just note it, don't change chapter)
        part_match = PART_RE.match(stripped)
        if part_match:
            # Save any accumulated paragraph, but stay in same chapter
            if current_para_lines:
                paragraphs.append(' '.join(current_para_lines))
                current_para_lines = []
            # Add the PART title as a paragraph marker (will be included in a thought)
            i += 1
            continue

        # Handle table data
        if is_table_line(line):
            if current_para_lines:
                paragraphs.append(' '.join(current_para_lines))
                current_para_lines = []
            if not in_table:
                in_table = True
                table_lines = []
            table_lines.append(line.rstrip())
            i += 1
            continue
        elif in_table:
            # End of table block
            if table_lines:
                paragraphs.append('\n'.join(table_lines))
                table_lines = []
            in_table = False

        # Blank line = paragraph break
        if not stripped:
            if current_para_lines:
                paragraphs.append(' '.join(current_para_lines))
                current_para_lines = []
            i += 1
            continue

        # Skip certain lines
        if stripped in ('THE END', '----------------------------------------------------------------------'):
            i += 1
            continue

        # Regular text line
        if current_chapter >= 0 or current_book == 0:
            current_para_lines.append(stripped)

        i += 1

    # Save final chapter
    if current_para_lines:
        paragraphs.append(' '.join(current_para_lines))
    if in_table and table_lines:
        paragraphs.append('\n'.join(table_lines))
    _save_chapter(books, current_book, current_chapter, paragraphs)

    return books


def _save_chapter(books, book_num, chapter_num, paragraphs):
    """Save paragraphs to a book's chapter."""
    if not paragraphs:
        return
    if chapter_num < 0:
        return
    if book_num not in books:
        books[book_num] = {}
    books[book_num][chapter_num] = paragraphs[:]


def create_originals(books):
    """Create originals JSON for each book."""
    total_thoughts = 0

    for book_num in sorted(books.keys()):
        chapters = books[book_num]
        entries = []

        for ch_num in sorted(chapters.keys()):
            paragraphs = chapters[ch_num]
            chapter_id = f"{book_num}.{ch_num}"

            thoughts = segment_paragraphs(paragraphs)
            thought_num = 1

            for thought_text in thoughts:
                index = f"{book_num}.{ch_num}.{thought_num}"
                entries.append({
                    'index': index,
                    'chapter': chapter_id,
                    'thought': str(thought_num),
                    'original': thought_text
                })
                thought_num += 1

        output_path = os.path.join(OUTPUT_DIR, f'won_book{book_num}_originals.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(entries, f, indent=2, ensure_ascii=False)

        word_counts = [word_count(e['original']) for e in entries]
        print(f"Book {book_num}: {len(chapters)} chapters, {len(entries)} thoughts, "
              f"avg {sum(word_counts) // max(len(word_counts), 1)} words")

        total_thoughts += len(entries)

    return total_thoughts


def main():
    books = parse_text()

    print(f"\nParsed {len(books)} book sections")
    for book_num in sorted(books.keys()):
        chapters = books[book_num]
        total_paras = sum(len(p) for p in chapters.values())
        print(f"  Book {book_num}: {len(chapters)} chapters, {total_paras} paragraphs")

    total = create_originals(books)

    print(f"\n--- Final Stats ---")
    print(f"Total thoughts: {total}")

    # Per-book word stats
    for book_num in sorted(books.keys()):
        path = os.path.join(OUTPUT_DIR, f'won_book{book_num}_originals.json')
        with open(path, 'r', encoding='utf-8') as f:
            entries = json.load(f)
        if entries:
            wcs = [word_count(e['original']) for e in entries]
            print(f"Book {book_num}: min={min(wcs)}, max={max(wcs)}, "
                  f"avg={sum(wcs)//len(wcs)}, under60={sum(1 for w in wcs if w < 60)}, "
                  f"over400={sum(1 for w in wcs if w > 400)}")


if __name__ == '__main__':
    main()
