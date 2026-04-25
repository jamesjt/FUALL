"""
Parse the Analects of Confucius (Legge translation) into originals JSON.

Structure: 20 Books, each with numbered Chapters (CHAP. / CHAPTER).
Many chapters have sub-numbered verses (1., 2., 3.).
Each chapter = 1 thought (they're already short).
Merge sub-verses within a chapter into a single thought.
"""

import json
import re
import os

SOURCE = os.path.join(os.path.dirname(__file__), '..', 'Confucius - Analects')
OUTPUT_DIR = os.path.dirname(__file__)

BOOK_TITLES = {
    1: "Hsio R (Learning)",
    2: "Wei Chang (Government)",
    3: "Pa Yih (Eight Rows of Dancers)",
    4: "Le Jin (Virtue)",
    5: "Kung-ye Ch'ang",
    6: "Yung Yey",
    7: "Shu R (Transmission)",
    8: "T'ai-Po",
    9: "Tsze Han (The Master Seldom Spoke)",
    10: "Heang Tang (In His Village)",
    11: "Hsien Tsin (The Forerunners)",
    12: "Yen Yuan",
    13: "Tsze-Lu",
    14: "Hsien Wan",
    15: "Wei Ling Kung",
    16: "Ke She",
    17: "Yang Ho",
    18: "Wei Tsze (The Viscount of Wei)",
    19: "Tsze-Chang",
    20: "Yao Yueh (Yao Said)",
}


def read_source():
    with open(SOURCE, 'r', encoding='utf-8') as f:
        return f.readlines()


def parse_books(lines):
    """Parse text into books, each containing chapters."""
    books = []
    current_book = None
    current_chapter = None
    current_lines = []

    # Find start
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith('BOOK I.'):
            break
        i += 1

    while i < len(lines):
        line = lines[i].rstrip('\n')
        stripped = line.strip()

        # End of text
        if stripped.startswith('*** END OF THE PROJECT GUTENBERG'):
            break

        # Book boundary
        book_match = re.match(r'^BOOK\s+([IVXLC]+)\.\s*(.*)', stripped)
        if book_match:
            # Save previous chapter
            if current_lines and current_chapter is not None:
                text = ' '.join(current_lines).strip()
                text = re.sub(r'\s+', ' ', text)
                if text:
                    current_book['chapters'].append({
                        'number': current_chapter,
                        'text': text
                    })
                current_lines = []

            if current_book is not None:
                books.append(current_book)

            roman = book_match.group(1)
            book_num = roman_to_int(roman)
            book_name = book_match.group(2).strip().rstrip('.')
            current_book = {
                'number': book_num,
                'name': book_name,
                'title': BOOK_TITLES.get(book_num, book_name),
                'chapters': []
            }
            current_chapter = None
            i += 1
            continue

        # Chapter boundary
        chap_match = re.match(r'^\s*(?:CHAP(?:TER)?\.?\s+)([IVXLC]+)\.\s*(.*)', stripped)
        if chap_match:
            # Save previous chapter
            if current_lines and current_chapter is not None:
                text = ' '.join(current_lines).strip()
                text = re.sub(r'\s+', ' ', text)
                if text:
                    current_book['chapters'].append({
                        'number': current_chapter,
                        'text': text
                    })
                current_lines = []

            roman = chap_match.group(1)
            current_chapter = roman_to_int(roman)
            # Rest of the line is the start of the chapter text
            remainder = chap_match.group(2).strip()
            if remainder:
                current_lines.append(remainder)
            i += 1
            continue

        # Regular text
        if stripped and current_book is not None:
            # Remove page numbers (standalone numbers)
            if re.match(r'^\d+$', stripped):
                i += 1
                continue
            current_lines.append(stripped)

        # Blank line — just continue (chapters are delimited by CHAP markers)
        i += 1

    # Save final chapter and book
    if current_lines and current_chapter is not None:
        text = ' '.join(current_lines).strip()
        text = re.sub(r'\s+', ' ', text)
        if text:
            current_book['chapters'].append({
                'number': current_chapter,
                'text': text
            })
    if current_book is not None:
        books.append(current_book)

    return books


def roman_to_int(s):
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    result = 0
    for i, c in enumerate(s):
        if i + 1 < len(s) and vals.get(c, 0) < vals.get(s[i + 1], 0):
            result -= vals.get(c, 0)
        else:
            result += vals.get(c, 0)
    return result


def create_originals(books):
    """Create originals JSON."""
    all_entries = []
    global_thought = 1

    for book in books:
        book_num = book['number']
        for chapter in book['chapters']:
            ch_num = chapter['number']
            text = chapter['text']

            # Clean up sub-verse numbers (1. 2. 3.) into flowing text
            text = re.sub(r'\s*(\d+)\.\s*', '\n', text)
            text = text.strip()

            entry = {
                'index': f"{book_num}.{ch_num}",
                'chapter': str(book_num),
                'chapter_title': book['title'],
                'thought': str(global_thought),
                'original': text
            }
            all_entries.append(entry)
            global_thought += 1

        print(f"Book {book_num:>2} ({book['title'][:40]:<40}): {len(book['chapters'])} chapters")

    output_path = os.path.join(OUTPUT_DIR, 'analects_originals.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_entries, f, indent=2, ensure_ascii=False)

    print(f"\nTotal thoughts: {len(all_entries)}")
    return all_entries


def main():
    lines = read_source()
    print(f"Read {len(lines)} lines")

    books = parse_books(lines)
    print(f"Parsed {len(books)} books\n")

    create_originals(books)


if __name__ == '__main__':
    main()
