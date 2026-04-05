"""
Parse Plato's Laws (Jowett translation) into per-book JSON files for CSV conversion.
12 books of dialogue between Athenian Stranger, Cleinias, and Megillus.
"""

import json
import os
import re
from collections import Counter

BUILD_DIR = os.path.dirname(__file__)
SOURCE = os.path.join(BUILD_DIR, '..', 'Plato - Laws')

# Speaker patterns
SPEAKER_FULL = {
    'Athenian Stranger': 'Athenian Stranger',
    'Cleinias': 'Cleinias',
    'Megillus': 'Megillus',
}
SPEAKER_ABBREV = {
    'Ath': 'Athenian Stranger',
    'Cle': 'Cleinias',
    'Meg': 'Megillus',
}

# Regex to detect speaker at start of line
# Matches: "Ath. ", "Cle. ", "Meg. ", "Athenian Stranger. ", "Cleinias. ", "Megillus. "
# Also handles: "Cle....." (ellipsis continuation), "(Ath. " (parenthetical)
SPEAKER_RE = re.compile(
    r'^(?:\()?'  # optional opening paren
    r'(Athenian Stranger|Cleinias|Megillus|Ath|Cle|Meg)'
    r'\.[\s.]'  # period followed by space or more periods
)

BOOK_HEADER_RE = re.compile(r'^BOOK\s+([IVXL]+)$')
SEPARATOR_RE = re.compile(r'^-{20,}$')
PERSONS_RE = re.compile(r'^Persons\s', re.IGNORECASE)

# Roman numeral conversion (handles VIIII = 8)
ROMAN_MAP = {
    'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'IIII': 4,
    'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'VIIII': 8,
    'IX': 9, 'X': 10, 'XI': 11, 'XII': 12,
}

PIVOT_PATTERNS = [
    r'^But ', r'^Now ', r'^And now', r'^Again,? ', r'^Further',
    r'^However', r'^Yet ', r'^For ', r'^Hence ', r'^Therefore',
    r'^Moreover', r'^Let us ', r'^There is another', r'^Perhaps ',
    r'^I say ', r'^I will ', r'^This is ', r'^Wherefore',
    r'^In the ', r'^The ', r'^Such ', r'^We ', r'^And if ',
]


def word_count(text):
    return len(text.split())


def detect_speaker(line):
    """Detect if a line starts with a speaker tag. Returns (speaker_name, text_after) or None."""
    m = SPEAKER_RE.match(line)
    if not m:
        return None

    speaker_key = m.group(1)
    speaker_name = SPEAKER_FULL.get(speaker_key, SPEAKER_ABBREV.get(speaker_key))
    if not speaker_name:
        return None

    # Extract the text after the speaker tag
    rest = line[m.end():].strip()
    # Handle ellipsis: "Cle..... Moreover" -> strip leading dots
    rest = re.sub(r'^\.+\s*', '', rest)
    # Handle parenthetical closing
    if line.startswith('('):
        rest = rest.rstrip(')')
        rest = '(' + speaker_key + '.) ' + rest

    return speaker_name, rest


def split_paragraph(text, max_words=400):
    """Split a long paragraph at topic pivots or sentence boundaries."""
    if word_count(text) <= max_words:
        return [text]

    sentences = re.split(r'(?<=[.!?])\s+', text)
    if len(sentences) <= 1:
        return [text]

    mid_word = word_count(text) // 2
    cumulative_words = 0
    best_pivot = -1
    best_dist = float('inf')

    for i, sent in enumerate(sentences):
        if i == 0:
            cumulative_words += word_count(sent)
            continue
        for pattern in PIVOT_PATTERNS:
            if re.match(pattern, sent):
                dist = abs(cumulative_words - mid_word)
                if dist < best_dist and cumulative_words >= 50:
                    best_pivot = i
                    best_dist = dist
                break
        cumulative_words += word_count(sent)

    if best_pivot > 0:
        part1 = ' '.join(sentences[:best_pivot])
        part2 = ' '.join(sentences[best_pivot:])
        result = []
        result.extend(split_paragraph(part1, max_words))
        result.extend(split_paragraph(part2, max_words))
        return result

    # No pivot — split at sentence boundary near middle
    cumulative_words = 0
    best_split = len(sentences) // 2
    best_dist = float('inf')
    for i, sent in enumerate(sentences[:-1]):
        cumulative_words += word_count(sent)
        dist = abs(cumulative_words - mid_word)
        if dist < best_dist and cumulative_words >= 50:
            best_split = i + 1
            best_dist = dist

    part1 = ' '.join(sentences[:best_split])
    part2 = ' '.join(sentences[best_split:])
    result = []
    for p in [part1, part2]:
        if word_count(p) > max_words:
            result.extend(split_paragraph(p, max_words))
        else:
            result.append(p)
    return result


def segment_paragraphs(paragraphs):
    """Apply merge/split/grouping heuristics to produce well-sized thoughts."""
    # Phase 1: Split long paragraphs
    split_paras = []
    for p in paragraphs:
        wc = word_count(p['text'])
        if wc > 400:
            pieces = split_paragraph(p['text'])
            for piece in pieces:
                split_paras.append({
                    'speaker': p['speaker'],
                    'text': piece,
                    'words': word_count(piece)
                })
        else:
            split_paras.append({
                'speaker': p['speaker'],
                'text': p['text'],
                'words': wc
            })

    # Phase 2: Group Q&A chains and merge short paragraphs
    merged = []
    i = 0
    while i < len(split_paras):
        current = split_paras[i]

        # Short paragraph — try to group as Q&A chain
        if current['words'] < 60:
            chain = [current]
            chain_words = current['words']
            j = i + 1
            while j < len(split_paras):
                next_p = split_paras[j]
                if next_p['words'] < 80 and chain_words + next_p['words'] <= 350:
                    chain.append(next_p)
                    chain_words += next_p['words']
                    j += 1
                elif next_p['words'] < 60 and chain_words + next_p['words'] <= 400:
                    chain.append(next_p)
                    chain_words += next_p['words']
                    j += 1
                else:
                    break

            if len(chain) > 1 and chain_words >= 40:
                speakers = list(dict.fromkeys(c['speaker'] for c in chain if c['speaker']))
                combined_text = '\n\n'.join(c['text'] for c in chain)
                merged.append({
                    'speaker': ', '.join(speakers) if speakers else '',
                    'text': combined_text,
                    'words': chain_words
                })
                i = j
                continue

            # Single short paragraph — merge with neighbor
            if merged and merged[-1]['words'] + current['words'] <= 400:
                merged[-1]['text'] += '\n\n' + current['text']
                merged[-1]['words'] += current['words']
                if current['speaker'] and current['speaker'] not in merged[-1]['speaker']:
                    merged[-1]['speaker'] += ', ' + current['speaker']
                i += 1
                continue
            elif i + 1 < len(split_paras) and split_paras[i + 1]['words'] + current['words'] <= 400:
                split_paras[i + 1]['text'] = current['text'] + '\n\n' + split_paras[i + 1]['text']
                split_paras[i + 1]['words'] += current['words']
                if current['speaker']:
                    split_paras[i + 1]['speaker'] = current['speaker'] + ', ' + split_paras[i + 1]['speaker']
                i += 1
                continue

        merged.append(current)
        i += 1

    # Phase 3: Final merge pass for remaining short thoughts
    final = []
    for m in merged:
        if m['words'] < 60 and final and final[-1]['words'] + m['words'] <= 400:
            final[-1]['text'] += '\n\n' + m['text']
            final[-1]['words'] += m['words']
        else:
            final.append(m)

    return final


def main():
    with open(SOURCE, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n').rstrip('\r') for line in f.readlines()]

    print(f"Total lines: {len(lines)}")

    # Parse into books
    books = {}
    current_book = None
    current_lines = []
    skip_next_blank = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Detect separator
        if SEPARATOR_RE.match(stripped):
            skip_next_blank = True
            continue

        # Detect book header
        m = BOOK_HEADER_RE.match(stripped)
        if m:
            if current_book is not None:
                books[current_book] = current_lines
            roman = m.group(1)
            current_book = ROMAN_MAP.get(roman)
            if current_book is None:
                print(f"WARNING: Unknown Roman numeral: {roman}")
                current_book = len(books) + 1
            current_lines = []
            skip_next_blank = True
            continue

        # Skip "Persons OF THE DIALOGUE" line
        if PERSONS_RE.match(stripped):
            continue

        # Skip header lines before first book
        if current_book is None:
            continue

        current_lines.append(line)

    # Don't forget the last book
    if current_book is not None:
        books[current_book] = current_lines

    print(f"Books found: {sorted(books.keys())}")
    for bnum in sorted(books.keys()):
        print(f"  Book {bnum}: {len(books[bnum])} lines")

    # Process each book
    grand_total = 0

    for book_num in sorted(books.keys()):
        book_lines = books[book_num]

        # Parse speaker turns
        paragraphs = []
        current_speaker = ''
        current_text_lines = []

        for line in book_lines:
            stripped = line.strip()

            # Skip empty lines — they separate paragraphs
            if not stripped:
                if current_text_lines:
                    text = ' '.join(current_text_lines)
                    paragraphs.append({
                        'speaker': current_speaker,
                        'text': text.strip(),
                    })
                    current_text_lines = []
                continue

            # Check for speaker header
            speaker_match = detect_speaker(stripped)
            if speaker_match:
                # Save previous paragraph if any
                if current_text_lines:
                    text = ' '.join(current_text_lines)
                    paragraphs.append({
                        'speaker': current_speaker,
                        'text': text.strip(),
                    })
                    current_text_lines = []

                speaker_name, rest_text = speaker_match
                current_speaker = speaker_name
                if rest_text:
                    current_text_lines.append(rest_text)
            else:
                current_text_lines.append(stripped)

        # Don't forget last paragraph
        if current_text_lines:
            text = ' '.join(current_text_lines)
            paragraphs.append({
                'speaker': current_speaker,
                'text': text.strip(),
            })

        # Filter out empty paragraphs
        paragraphs = [p for p in paragraphs if p['text'].strip()]

        # Add word counts
        for p in paragraphs:
            p['words'] = word_count(p['text'])

        raw_count = len(paragraphs)
        raw_words = sum(p['words'] for p in paragraphs)

        # Segment into thoughts
        thoughts = segment_paragraphs(paragraphs)

        # Build entries
        entries = []
        for t_num, thought in enumerate(thoughts, 1):
            idx = f"{book_num}.{t_num}"
            entries.append({
                'index': idx,
                'chapter': str(book_num),
                'thought': str(t_num),
                'speakers': thought['speaker'],
                'original': thought['text']
            })

        # Stats
        word_counts = [word_count(e['original']) for e in entries]
        avg_wc = sum(word_counts) // len(word_counts) if word_counts else 0
        under_60 = sum(1 for w in word_counts if w < 60)
        over_400 = sum(1 for w in word_counts if w > 400)

        print(f"Book {book_num}: {raw_count} paragraphs -> {len(entries)} thoughts "
              f"(avg {avg_wc}w, <60: {under_60}, >400: {over_400})")

        grand_total += len(entries)

        # Write output
        output_path = os.path.join(BUILD_DIR, f'laws_book{book_num}_originals.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(entries, f, ensure_ascii=False, indent=2)

    print(f"\nGrand total: {grand_total} thoughts across {len(books)} books")


if __name__ == '__main__':
    main()
