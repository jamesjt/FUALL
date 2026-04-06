"""
Parse Aristotle's Nicomachean Ethics text file into per-book originals JSON files.

Segmentation rules:
- Each paragraph (blank-line-delimited block) = 1 thought
- Merge: paragraph < ~50 words AND meaning depends on adjacent paragraph
- Split: paragraph > ~400 words AND has clear argumentative pivot
- Poetry quotations stay with introducing paragraph
"""

import json
import re
import os

SOURCE = os.path.join(os.path.dirname(__file__), '..', 'Aristotle - Ethics')
OUTPUT_DIR = os.path.dirname(__file__)

def read_source():
    with open(SOURCE, 'r', encoding='utf-8') as f:
        return f.readlines()

def parse_books(lines):
    """Parse the text into a list of books, each containing sections."""
    books = []
    current_book = None
    current_section = None
    current_paragraphs = []
    current_para_lines = []

    # Skip header lines (title, author, translator, separator)
    i = 0
    while i < len(lines):
        line = lines[i].rstrip('\n')
        if line.startswith('BOOK '):
            break
        i += 1

    while i < len(lines):
        line = lines[i].rstrip('\n')

        # Check for BOOK boundary
        book_match = re.match(r'^BOOK\s+([IVX]+)\s*$', line)
        if book_match:
            # Save previous section/book
            if current_para_lines:
                current_paragraphs.append(' '.join(current_para_lines))
                current_para_lines = []
            if current_section is not None and current_book is not None:
                current_book['sections'].append({
                    'number': current_section,
                    'paragraphs': current_paragraphs
                })
                current_paragraphs = []
            if current_book is not None:
                books.append(current_book)

            roman = book_match.group(1)
            book_num = roman_to_int(roman)
            current_book = {'number': book_num, 'roman': roman, 'sections': []}
            current_section = None
            i += 1
            continue

        # Check for section number (standalone number on its own line)
        section_match = re.match(r'^(\d+)\s*$', line)
        if section_match and current_book is not None:
            # Save previous section
            if current_para_lines:
                current_paragraphs.append(' '.join(current_para_lines))
                current_para_lines = []
            if current_section is not None:
                current_book['sections'].append({
                    'number': current_section,
                    'paragraphs': current_paragraphs
                })
                current_paragraphs = []

            current_section = int(section_match.group(1))
            i += 1
            continue

        # Check for end markers
        if line.strip() in ('THE END', '----------------------------------------------------------------------', ''):
            if line.strip() == '':
                # Blank line = paragraph break
                if current_para_lines:
                    current_paragraphs.append(' '.join(current_para_lines))
                    current_para_lines = []
            elif line.strip() in ('THE END', '----------------------------------------------------------------------'):
                pass  # skip
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
            'number': current_section,
            'paragraphs': current_paragraphs
        })
    if current_book is not None:
        books.append(current_book)

    return books

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

def segment_paragraphs(paragraphs):
    """Apply merge/split rules to convert paragraphs into thoughts."""
    # First pass: split long paragraphs, collect all
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

    # Second pass: merge short paragraphs (<60 words) forward or backward
    thoughts = []
    i = 0
    while i < len(raw):
        para = raw[i]
        wc = word_count(para)

        if wc < 60:
            # Try merging forward first
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
            # Can't merge either way, keep as is
            thoughts.append(para)
        else:
            thoughts.append(para)
        i += 1

    # Third pass: deduplicate consecutive identical thoughts
    deduped = []
    for t in thoughts:
        if not deduped or t != deduped[-1]:
            deduped.append(t)

    return deduped

def try_split(text):
    """Try to split a long paragraph at argumentative pivots."""
    # Look for sentence-starting pivot words
    # Split at sentence boundaries where the next sentence starts with a pivot
    pivot_pattern = r'(?<=[.;])\s+(?=(?:But |Now |Again |Further |On the other hand|However |Yet |For |Hence |Therefore |Moreover |Similarly |In like manner |Nor |And so |It follows |The reason is |This is why ))'

    parts = re.split(pivot_pattern, text)

    if len(parts) == 1:
        # No good split point found - try splitting roughly in half at a sentence boundary
        sentences = re.split(r'(?<=[.])\s+', text)
        if len(sentences) >= 4:
            mid = len(sentences) // 2
            part1 = ' '.join(sentences[:mid])
            part2 = ' '.join(sentences[mid:])
            if word_count(part1) >= 50 and word_count(part2) >= 50:
                return [part1, part2]
        return [text]  # Can't split meaningfully

    # Recombine parts that are too small
    result = []
    current = parts[0]
    for part in parts[1:]:
        if word_count(current) < 100:
            current = current + ' ' + part
        else:
            result.append(current)
            current = part
    result.append(current)

    return result

def create_originals(books):
    """Create originals JSON for each book."""
    for book in books:
        book_num = book['number']
        entries = []
        thought_num = 1

        for section in book['sections']:
            sec_num = section['number']
            chapter = f"{book_num}.{sec_num}"

            thoughts = segment_paragraphs(section['paragraphs'])

            for thought_text in thoughts:
                index = f"{book_num}.{thought_num}"
                entries.append({
                    'index': index,
                    'chapter': chapter,
                    'thought': str(thought_num),
                    'original': thought_text
                })
                thought_num += 1

        output_path = os.path.join(OUTPUT_DIR, f'book{book_num}_originals.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(entries, f, indent=2, ensure_ascii=False)

        print(f"Book {book_num} ({book['roman']}): {len(book['sections'])} sections, {len(entries)} thoughts")

    return books

def main():
    lines = read_source()
    print(f"Read {len(lines)} lines")

    books = parse_books(lines)
    print(f"Parsed {len(books)} books")

    for book in books:
        total_paras = sum(len(s['paragraphs']) for s in book['sections'])
        print(f"  Book {book['roman']}: {len(book['sections'])} sections, {total_paras} paragraphs")

    create_originals(books)

    total = sum(
        len(json.load(open(os.path.join(OUTPUT_DIR, f'book{b["number"]}_originals.json'))))
        for b in books
    )
    print(f"\nTotal thoughts across all books: {total}")

if __name__ == '__main__':
    main()
