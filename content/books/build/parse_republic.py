"""
Parse Plato's Republic text file into per-book originals JSON files.

The Republic is dialogue with:
- No quotation marks
- Speaker headers like "Socrates - GLAUCON" marking section boundaries
- Continuous flowing text within sections
- Rapid-fire Q&A exchanges mixed with long monologues

Segmentation rules:
- Speaker headers → Chapter boundaries
- Paragraphs (blank-line delimited) → base units
- Merge short paragraphs (<30 words) backward
- Group rapid-fire Q&A chains into single thoughts
- Split paragraphs > 400 words at topic pivots
- Target thought size: 100-350 words
"""

import json
import re
import os

SOURCE = os.path.join(os.path.dirname(__file__), '..', 'Plato - Republic')
OUTPUT_DIR = os.path.dirname(__file__)

# Known speaker names (Title Case for narrator position, ALL CAPS for speaker position)
KNOWN_SPEAKERS = {
    'Socrates', 'Glaucon', 'Adeimantus', 'Cephalus', 'Polemarchus',
    'Thrasymachus', 'Cleitophon', 'Niceratus'
}
KNOWN_SPEAKERS_UPPER = {s.upper() for s in KNOWN_SPEAKERS}


def read_source():
    with open(SOURCE, 'r', encoding='utf-8') as f:
        return f.readlines()


def is_speaker_header(line):
    """Check if a line is a speaker header (section marker), not dialogue text."""
    stripped = line.strip()
    if not stripped:
        return False

    # Must be short (just names and dashes, no dialogue text)
    # A speaker header looks like: "Socrates - GLAUCON" or "Glaucon" or "Adeimantus -SOCRATES"
    # It should NOT contain dialogue verbs or punctuation beyond dashes

    # Remove dashes and spaces, check if all remaining parts are known names
    parts = re.split(r'\s*-\s*', stripped)
    if not parts:
        return False

    found_speaker = False
    for part in parts:
        part_clean = part.strip()
        if not part_clean:
            continue
        # Check if it's a known speaker name (case insensitive)
        if part_clean not in KNOWN_SPEAKERS and part_clean not in KNOWN_SPEAKERS_UPPER:
            return False
        found_speaker = True

    # Must have at least one actual speaker name (not just dashes)
    if not found_speaker:
        return False

    # Additional check: line should be relatively short (just names)
    if len(stripped) > 80:
        return False

    return True


def roman_to_int(s):
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    result = 0
    for i, c in enumerate(s):
        if i + 1 < len(s) and vals[c] < vals[s[i + 1]]:
            result -= vals[c]
        else:
            result += vals[c]
    return result


def word_count(text):
    return len(text.split())


def parse_books(lines):
    """Parse the Republic into books, each with speaker sections."""
    books = []
    current_book = None
    current_section = None
    current_section_num = 0
    current_paragraphs = []
    current_para_lines = []
    in_content = False  # Skip introduction

    i = 0
    while i < len(lines):
        line = lines[i].rstrip('\n')

        # Check for BOOK boundary
        book_match = re.match(r'^BOOK\s+([IVX]+)\s*$', line)
        if book_match:
            in_content = True

            # Save previous section/book
            if current_para_lines:
                current_paragraphs.append(' '.join(current_para_lines))
                current_para_lines = []
            if current_section is not None and current_book is not None:
                current_book['sections'].append({
                    'number': current_section_num,
                    'speakers': current_section,
                    'paragraphs': current_paragraphs
                })
                current_paragraphs = []
            if current_book is not None:
                books.append(current_book)

            roman = book_match.group(1)
            book_num = roman_to_int(roman)
            current_book = {'number': book_num, 'roman': roman, 'sections': []}
            current_section = None
            current_section_num = 0
            i += 1
            continue

        if not in_content:
            i += 1
            continue

        # Check for separator lines
        if line.strip().startswith('---'):
            i += 1
            continue

        # Check for THE END
        if line.strip() == 'THE END':
            i += 1
            continue

        # Check for speaker header
        if is_speaker_header(line):
            # Save previous section
            if current_para_lines:
                current_paragraphs.append(' '.join(current_para_lines))
                current_para_lines = []
            if current_section is not None:
                current_book['sections'].append({
                    'number': current_section_num,
                    'speakers': current_section,
                    'paragraphs': current_paragraphs
                })
                current_paragraphs = []

            current_section_num += 1
            current_section = line.strip()
            i += 1
            continue

        # Blank line = paragraph break
        if line.strip() == '':
            if current_para_lines:
                current_paragraphs.append(' '.join(current_para_lines))
                current_para_lines = []
            i += 1
            continue

        # Regular text line
        if current_section is not None:
            current_para_lines.append(line.strip())

        i += 1

    # Save final section/book
    if current_para_lines:
        current_paragraphs.append(' '.join(current_para_lines))
    if current_section is not None and current_book is not None:
        current_book['sections'].append({
            'number': current_section_num,
            'speakers': current_section,
            'paragraphs': current_paragraphs
        })
    if current_book is not None:
        books.append(current_book)

    return books


def try_split(text):
    """Try to split a long paragraph at topic pivots."""
    pivot_pattern = r'(?<=[.;?])\s+(?=(?:But |Now |Again |Further |However |Yet |For |Hence |Therefore |Moreover |Let us |There is another |And now |The next ))'
    parts = re.split(pivot_pattern, text)

    if len(parts) == 1:
        # Try splitting at sentence boundary roughly in half
        sentences = re.split(r'(?<=[.?])\s+', text)
        if len(sentences) >= 4:
            mid = len(sentences) // 2
            part1 = ' '.join(sentences[:mid])
            part2 = ' '.join(sentences[mid:])
            if word_count(part1) >= 50 and word_count(part2) >= 50:
                return [part1, part2]
        return [text]

    # Recombine parts that are too small
    result = []
    current = parts[0]
    for part in parts[1:]:
        if word_count(current) < 80:
            current = current + ' ' + part
        else:
            result.append(current)
            current = part
    result.append(current)

    return result


def segment_paragraphs(paragraphs):
    """Apply merge/split/grouping rules for dialogue text."""
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

    # Second pass: group rapid-fire Q&A and merge short paragraphs
    # For dialogue, aim for 120-350 word thought units
    thoughts = []
    i = 0
    while i < len(raw):
        para = raw[i]
        wc = word_count(para)

        if wc < 60:
            # Short paragraph — check if we're in a rapid-fire Q&A chain
            chain = [para]
            j = i + 1
            chain_wc = wc
            while j < len(raw) and word_count(raw[j]) < 80 and chain_wc < 350:
                chain.append(raw[j])
                chain_wc += word_count(raw[j])
                j += 1

            if len(chain) >= 2:
                merged = '\n\n'.join(chain)
                if word_count(merged) <= 400:
                    thoughts.append(merged)
                    i = j
                    continue
                else:
                    # Split the chain roughly in half
                    mid = len(chain) // 2
                    thoughts.append('\n\n'.join(chain[:mid]))
                    thoughts.append('\n\n'.join(chain[mid:]))
                    i = j
                    continue

            # Single short paragraph — merge backward or forward
            if thoughts:
                merged = thoughts[-1] + '\n\n' + para
                if word_count(merged) <= 400:
                    thoughts[-1] = merged
                    i += 1
                    continue
            if i + 1 < len(raw):
                merged = para + '\n\n' + raw[i + 1]
                if word_count(merged) <= 400:
                    thoughts.append(merged)
                    i += 2
                    continue
            thoughts.append(para)
        else:
            thoughts.append(para)
        i += 1

    # Third pass: merge any remaining short thoughts (<60 words) backward
    final = []
    for t in thoughts:
        if final and word_count(t) < 60:
            merged = final[-1] + '\n\n' + t
            if word_count(merged) <= 400:
                final[-1] = merged
                continue
        final.append(t)

    # Deduplicate consecutive identical thoughts
    deduped = []
    for t in final:
        if not deduped or t != deduped[-1]:
            deduped.append(t)

    return deduped


def create_originals(books):
    """Create originals JSON for each book."""
    for book in books:
        book_num = book['number']
        entries = []
        thought_num = 1

        for section in book['sections']:
            sec_num = section['number']
            chapter = f"{book_num}.{sec_num}"
            speakers = section['speakers']

            thoughts = segment_paragraphs(section['paragraphs'])

            for thought_text in thoughts:
                index = f"{book_num}.{thought_num}"
                entries.append({
                    'index': index,
                    'chapter': chapter,
                    'thought': str(thought_num),
                    'speakers': speakers,
                    'original': thought_text
                })
                thought_num += 1

        output_path = os.path.join(OUTPUT_DIR, f'republic_book{book_num}_originals.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(entries, f, indent=2, ensure_ascii=False)

        section_count = len(book['sections'])
        print(f"Book {book_num} ({book['roman']}): {section_count} sections, {len(entries)} thoughts")

    return books


def main():
    lines = read_source()
    print(f"Read {len(lines)} lines")

    books = parse_books(lines)
    print(f"Parsed {len(books)} books")

    for book in books:
        total_paras = sum(len(s['paragraphs']) for s in book['sections'])
        total_sections = len(book['sections'])
        speakers_list = [s['speakers'] for s in book['sections']]
        print(f"  Book {book['roman']}: {total_sections} sections, {total_paras} paragraphs")
        for s in book['sections']:
            print(f"    {book['number']}.{s['number']} [{s['speakers']}]: {len(s['paragraphs'])} paras")

    create_originals(books)

    total = sum(
        len(json.load(open(os.path.join(OUTPUT_DIR, f'republic_book{b["number"]}_originals.json'), encoding='utf-8')))
        for b in books
    )
    print(f"\nTotal thoughts across all books: {total}")


if __name__ == '__main__':
    main()
