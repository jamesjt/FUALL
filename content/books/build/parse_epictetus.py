"""
Parse Epictetus's Discourses text file into per-book originals JSON files.

Segmentation rules:
- Each paragraph (blank-line-delimited block) = 1 thought
- Merge: paragraph < ~50 words AND meaning depends on adjacent paragraph
- Split: paragraph > ~400 words AND has clear argumentative pivot
"""

import json
import re
import os

SOURCE = os.path.join(os.path.dirname(__file__), '..', 'Epictetus - Discourses')
OUTPUT_DIR = os.path.dirname(__file__)

BOOK_NAMES = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4}


def read_source():
    with open(SOURCE, 'r', encoding='utf-8') as f:
        return f.readlines()


def parse_books(lines):
    """Parse the text into a list of books, each containing chapters."""
    books = []
    current_book = None
    current_chapter = None
    current_chapter_title = None
    current_paragraphs = []
    current_para_lines = []
    reading_title = False

    # Skip header lines
    i = 0
    while i < len(lines):
        line = lines[i].rstrip('\n')
        if line.startswith('Book '):
            break
        i += 1

    while i < len(lines):
        line = lines[i].rstrip('\n')

        # Check for Book boundary
        book_match = re.match(r'^Book\s+(One|Two|Three|Four)\s*$', line)
        if book_match:
            # Save previous chapter/book
            if current_para_lines:
                current_paragraphs.append(' '.join(current_para_lines))
                current_para_lines = []
            if current_chapter is not None and current_book is not None:
                current_book['chapters'].append({
                    'number': current_chapter,
                    'title': current_chapter_title or '',
                    'paragraphs': current_paragraphs
                })
                current_paragraphs = []
            if current_book is not None:
                books.append(current_book)

            book_num = BOOK_NAMES[book_match.group(1)]
            current_book = {'number': book_num, 'name': book_match.group(1), 'chapters': []}
            current_chapter = None
            current_chapter_title = None
            reading_title = False
            i += 1
            continue

        # Check for Chapter boundary
        chapter_match = re.match(r'^Chapter\s+(\d+)\s*$', line)
        if chapter_match:
            # Save previous chapter
            if current_para_lines:
                current_paragraphs.append(' '.join(current_para_lines))
                current_para_lines = []
            if current_chapter is not None and current_book is not None:
                current_book['chapters'].append({
                    'number': current_chapter,
                    'title': current_chapter_title or '',
                    'paragraphs': current_paragraphs
                })
                current_paragraphs = []

            current_chapter = int(chapter_match.group(1))
            current_chapter_title = None
            reading_title = True
            i += 1
            continue

        # Skip separator lines
        if line.strip() == '---':
            i += 1
            continue

        # Read chapter title (first non-empty line after "Chapter N")
        if reading_title:
            stripped = line.strip()
            if stripped:
                if current_chapter_title is None:
                    current_chapter_title = stripped
                else:
                    # Multi-line title
                    current_chapter_title += ' ' + stripped
            else:
                if current_chapter_title is not None:
                    reading_title = False
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
        if current_chapter is not None:
            current_para_lines.append(line.strip())

        i += 1

    # Save final chapter/book
    if current_para_lines:
        current_paragraphs.append(' '.join(current_para_lines))
    if current_chapter is not None and current_book is not None:
        current_book['chapters'].append({
            'number': current_chapter,
            'title': current_chapter_title or '',
            'paragraphs': current_paragraphs
        })
    if current_book is not None:
        books.append(current_book)

    return books


def word_count(text):
    return len(text.split())


def try_split(text):
    """Try to split a long paragraph at argumentative pivots."""
    pivot_pattern = r'(?<=[.;])\s+(?=(?:But |Now |Again |Further |On the other hand|However |Yet |For |Hence |Therefore |Moreover |Similarly |Nor |And so |It follows |The reason is |This is why |Consider |Do you not |What then |How then ))'

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

    return result


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

    # Second pass: merge short paragraphs (<60 words)
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

    # Third pass: deduplicate
    deduped = []
    for t in thoughts:
        if not deduped or t != deduped[-1]:
            deduped.append(t)

    return deduped


def create_originals(books):
    """Create originals JSON for each book."""
    for book in books:
        book_num = book['number']
        entries = []
        thought_num = 1

        for chapter in book['chapters']:
            ch_num = chapter['number']
            chapter_id = f"{book_num}.{ch_num}"

            thoughts = segment_paragraphs(chapter['paragraphs'])

            for thought_text in thoughts:
                index = f"{book_num}.{thought_num}"
                entries.append({
                    'index': index,
                    'chapter': chapter_id,
                    'chapter_title': chapter['title'],
                    'thought': str(thought_num),
                    'original': thought_text
                })
                thought_num += 1

        output_path = os.path.join(OUTPUT_DIR, f'epictetus_book{book_num}_originals.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(entries, f, indent=2, ensure_ascii=False)

        print(f"Book {book_num} ({book['name']}): {len(book['chapters'])} chapters, {len(entries)} thoughts")

    return books


def main():
    lines = read_source()
    print(f"Read {len(lines)} lines")

    books = parse_books(lines)
    print(f"Parsed {len(books)} books")

    for book in books:
        total_paras = sum(len(ch['paragraphs']) for ch in book['chapters'])
        print(f"  Book {book['name']}: {len(book['chapters'])} chapters, {total_paras} paragraphs")

    create_originals(books)

    total = sum(
        len(json.load(open(os.path.join(OUTPUT_DIR, f'epictetus_book{b["number"]}_originals.json'))))
        for b in books
    )
    print(f"\nTotal thoughts across all books: {total}")


if __name__ == '__main__':
    main()
