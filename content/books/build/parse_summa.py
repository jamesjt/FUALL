"""
Parse Thomas Aquinas's Summa Theologica Part I (Prima Pars) into structured JSON.
Source: Project Gutenberg #17611 (Fathers of the English Dominican Province translation).
Structure: 118 Questions, 582 Articles in scholastic format.
Each Article = one thought. Articles over 800 words split at scholastic boundaries.
"""

import json
import os
import re
from collections import Counter

BUILD_DIR = os.path.dirname(__file__)
SOURCE = os.path.join(BUILD_DIR, '..', 'Summa Theologica, Part I (Prima Pars)')
OUTPUT = os.path.join(BUILD_DIR, 'summa_p1_originals.json')

# Patterns
QUESTION_PATTERN = re.compile(r'^QUESTION\s+(\d+)\s*$', re.MULTILINE)
QUESTION_TITLE_PATTERN = re.compile(r'^([A-Z][A-Z\s,\'()]+?)(?:\s*\(in\s+\w+\s+Articles?\))?$')
ARTICLE_HEADER = re.compile(
    r'^(FIRST|SECOND|THIRD|FOURTH|FIFTH|SIXTH|SEVENTH|EIGHTH|NINTH|TENTH|'
    r'ELEVENTH|TWELFTH|THIRTEENTH|FOURTEENTH|FIFTEENTH|SIXTEENTH)\s+ARTICLE\s+'
    r'\[I,\s*Q\.\s*(\d+),\s*Art\.\s*\d+\]'
)
ORDINAL_TO_NUM = {
    'FIRST': 1, 'SECOND': 2, 'THIRD': 3, 'FOURTH': 4, 'FIFTH': 5,
    'SIXTH': 6, 'SEVENTH': 7, 'EIGHTH': 8, 'NINTH': 9, 'TENTH': 10,
    'ELEVENTH': 11, 'TWELFTH': 12, 'THIRTEENTH': 13, 'FOURTEENTH': 14,
    'FIFTEENTH': 15, 'SIXTEENTH': 16
}
SEPARATOR = re.compile(r'^_{5,}\s*$')

# Q116 is missing its QUESTION header in the Gutenberg text — provide title manually
MISSING_QUESTION_TITLES = {
    116: 'Of Fate'
}

# Scholastic section markers for splitting long articles
RESPONDEO = re.compile(r'^I answer that,')
REPLY_OBJ = re.compile(r'^Reply Obj(?:ection)?\.\s*1:')


def word_count(text):
    return len(text.split())


def clean_question_title(raw_title):
    """Clean up question title: title-case, strip article count."""
    title = raw_title.strip()
    # Remove "(in X Articles)" suffix
    title = re.sub(r'\s*\(in\s+\w+\s+Articles?\)\s*$', '', title, flags=re.IGNORECASE)
    # Title case
    words = title.split()
    result = []
    small_words = {'of', 'the', 'in', 'and', 'or', 'a', 'an', 'to', 'for', 'by', 'as', 'is', 'on', 'at', 'with', 'from', 'into', 'not'}
    for i, w in enumerate(words):
        if i == 0 or w.lower() not in small_words:
            result.append(w.capitalize())
        else:
            result.append(w.lower())
    return ' '.join(result)


def extract_article_title(text):
    """Extract the article's question title (line after the header)."""
    lines = text.strip().split('\n')
    # Skip the header line, find the title
    for line in lines[1:]:
        stripped = line.strip()
        if stripped and stripped.startswith('Whether'):
            return stripped
        if stripped and not ARTICLE_HEADER.match(stripped):
            return stripped
    return ''


def split_article(text, max_words=800):
    """Split a long article at scholastic boundaries if over max_words."""
    if word_count(text) <= max_words:
        return [text]

    lines = text.split('\n')
    paragraphs = []
    current = []
    for line in lines:
        if line.strip() == '':
            if current:
                paragraphs.append('\n'.join(current))
                current = []
        else:
            current.append(line)
    if current:
        paragraphs.append('\n'.join(current))

    # Find respondeo and first reply positions
    respondeo_idx = None
    reply_idx = None
    for i, para in enumerate(paragraphs):
        stripped = para.strip()
        if respondeo_idx is None and RESPONDEO.match(stripped):
            respondeo_idx = i
        if reply_idx is None and REPLY_OBJ.match(stripped):
            reply_idx = i

    # Try splitting at Reply Obj. 1 first (objections+answer | replies)
    if reply_idx and reply_idx > 0:
        part1 = '\n\n'.join(paragraphs[:reply_idx])
        part2 = '\n\n'.join(paragraphs[reply_idx:])
        if word_count(part1) >= 100 and word_count(part2) >= 50:
            parts = []
            if word_count(part1) > max_words and respondeo_idx and respondeo_idx < reply_idx:
                # Further split: objections | respondeo+rest
                obj_part = '\n\n'.join(paragraphs[:respondeo_idx])
                resp_part = '\n\n'.join(paragraphs[respondeo_idx:reply_idx])
                if word_count(obj_part) >= 80 and word_count(resp_part) >= 80:
                    parts.append(obj_part)
                    parts.append(resp_part)
                else:
                    parts.append(part1)
            else:
                parts.append(part1)
            parts.append(part2)
            return parts

    # Try splitting at Respondeo (objections+sed contra | answer+replies)
    if respondeo_idx and respondeo_idx > 0:
        part1 = '\n\n'.join(paragraphs[:respondeo_idx])
        part2 = '\n\n'.join(paragraphs[respondeo_idx:])
        if word_count(part1) >= 100 and word_count(part2) >= 100:
            return [part1, part2]

    # No good split point found — return as-is
    return [text]


def main():
    with open(SOURCE, 'r', encoding='utf-8') as f:
        text = f.read()

    # Skip header lines (title + URL)
    lines = text.split('\n')
    # Find first QUESTION
    start = 0
    for i, line in enumerate(lines):
        if line.strip().startswith('QUESTION'):
            start = i
            break

    text = '\n'.join(lines[start:])

    # Split into sections by separator (underscores appear inline at end of paragraphs)
    sections = re.split(r'\s*_{5,}\s*', text)
    print(f"Raw sections after separator split: {len(sections)}")

    # Parse questions and articles
    entries = []
    current_q_num = None
    current_q_title = None
    article_count = 0
    question_count = 0

    for section in sections:
        section = section.strip()
        if not section:
            continue

        # Check if this section starts with a QUESTION header
        q_match = QUESTION_PATTERN.match(section)
        if q_match:
            current_q_num = int(q_match.group(1))
            # Extract question title (next non-empty line after QUESTION N)
            section_lines = section.split('\n')
            title_line = ''
            for line in section_lines[1:]:
                stripped = line.strip()
                if stripped:
                    title_line = stripped
                    break
            current_q_title = clean_question_title(title_line)
            question_count += 1

            # Check if this section also contains the first article
            art_match = ARTICLE_HEADER.search(section)
            if art_match:
                # Split: question intro before article, article text from header onward
                art_start = section.index(art_match.group(0))
                q_intro = section[:art_start].strip()
                article_text = section[art_start:].strip()

                # Save question intro as thought 0
                if q_intro and word_count(q_intro) > 10:
                    # Strip QUESTION N line itself from intro
                    intro_lines = q_intro.split('\n')
                    intro_body = []
                    past_header = False
                    for line in intro_lines:
                        if not past_header:
                            if QUESTION_PATTERN.match(line.strip()):
                                continue
                            # Skip the title line too (it becomes the chapter name)
                            if QUESTION_TITLE_PATTERN.match(line.strip()):
                                past_header = True
                                continue
                            past_header = True
                        intro_body.append(line)
                    intro_text = '\n'.join(intro_body).strip()
                    if intro_text and word_count(intro_text) > 5:
                        entries.append({
                            'index': f'{current_q_num}.0',
                            'chapter': f'Q{current_q_num}: {current_q_title}',
                            'thought': '0',
                            'original': intro_text
                        })

                # Process the article — use ordinal for article number
                art_a = ORDINAL_TO_NUM.get(art_match.group(1), 1)
                # Only switch questions on FIRST ARTICLE with different Q number
                # (handles missing QUESTION headers like Q116; ignores typos in later articles)
                header_q = int(art_match.group(2))
                if header_q != current_q_num and art_match.group(1) == 'FIRST':
                    current_q_num = header_q
                    current_q_title = MISSING_QUESTION_TITLES.get(header_q, f'Question {header_q}')
                    question_count += 1
                article_count += 1

                parts = split_article(article_text)
                if len(parts) == 1:
                    entries.append({
                        'index': f'{current_q_num}.{art_a}',
                        'chapter': f'Q{current_q_num}: {current_q_title}',
                        'thought': str(art_a),
                        'original': article_text
                    })
                else:
                    suffixes = 'abcdefgh'
                    for pi, part in enumerate(parts):
                        entries.append({
                            'index': f'{current_q_num}.{art_a}{suffixes[pi]}',
                            'chapter': f'Q{current_q_num}: {current_q_title}',
                            'thought': f'{art_a}{suffixes[pi]}',
                            'original': part
                        })
            else:
                # Question header with intro only, no article in this section
                intro_lines = section.split('\n')
                intro_body = []
                past_header = False
                for line in intro_lines:
                    if not past_header:
                        if QUESTION_PATTERN.match(line.strip()):
                            continue
                        if QUESTION_TITLE_PATTERN.match(line.strip()):
                            past_header = True
                            continue
                        past_header = True
                    intro_body.append(line)
                intro_text = '\n'.join(intro_body).strip()
                if intro_text and word_count(intro_text) > 5:
                    entries.append({
                        'index': f'{current_q_num}.0',
                        'chapter': f'Q{current_q_num}: {current_q_title}',
                        'thought': '0',
                        'original': intro_text
                    })

            continue

        # Check if this is an article section
        art_match = ARTICLE_HEADER.match(section)
        if art_match:
            art_a = ORDINAL_TO_NUM.get(art_match.group(1), 1)
            # Only switch questions on FIRST ARTICLE with different Q number
            header_q = int(art_match.group(2))
            if header_q != current_q_num and art_match.group(1) == 'FIRST':
                current_q_num = header_q
                current_q_title = MISSING_QUESTION_TITLES.get(header_q, f'Question {header_q}')
                question_count += 1
            article_count += 1

            parts = split_article(section)
            if len(parts) == 1:
                entries.append({
                    'index': f'{current_q_num}.{art_a}',
                    'chapter': f'Q{current_q_num}: {current_q_title}',
                    'thought': str(art_a),
                    'original': section
                })
            else:
                suffixes = 'abcdefgh'
                for pi, part in enumerate(parts):
                    entries.append({
                        'index': f'{current_q_num}.{art_a}{suffixes[pi]}',
                        'chapter': f'Q{current_q_num}: {current_q_title}',
                        'thought': f'{art_a}{suffixes[pi]}',
                        'original': part
                    })
            continue

        # Remaining sections: could be question-only intros or stray text
        if current_q_num and word_count(section) > 20:
            # Check if it's a new question without separator
            q_inline = QUESTION_PATTERN.match(section)
            if q_inline:
                current_q_num = int(q_inline.group(1))
                section_lines = section.split('\n')
                for line in section_lines[1:]:
                    stripped = line.strip()
                    if stripped:
                        current_q_title = clean_question_title(stripped)
                        break
                question_count += 1

    # Stats
    print(f"\nQuestions found: {question_count}")
    print(f"Articles found: {article_count}")
    print(f"Total entries (with splits and intros): {len(entries)}")

    word_counts = [word_count(e['original']) for e in entries]
    print(f"\n--- Word Count Stats ---")
    print(f"Min: {min(word_counts)}, Max: {max(word_counts)}, Avg: {sum(word_counts)//len(word_counts)}")
    print(f"Under 100 words: {sum(1 for w in word_counts if w < 100)}")
    print(f"100-400 words: {sum(1 for w in word_counts if 100 <= w < 400)}")
    print(f"400-800 words: {sum(1 for w in word_counts if 400 <= w < 800)}")
    print(f"Over 800 words: {sum(1 for w in word_counts if w >= 800)}")

    # Chapter distribution
    ch_counts = Counter(e['chapter'] for e in entries)
    print(f"\n--- Chapter Distribution (first 10) ---")
    for ch in sorted(ch_counts.keys(), key=lambda c: int(re.search(r'Q(\d+)', c).group(1)))[:10]:
        ch_entries = [e for e in entries if e['chapter'] == ch]
        ch_words = sum(word_count(e['original']) for e in ch_entries)
        print(f"  {ch:<45} {ch_counts[ch]:>3} entries, {ch_words:>5} words")
    print(f"  ... ({len(ch_counts)} chapters total)")

    # Validation
    print(f"\n--- Validation ---")
    seen_indices = set()
    issues = []
    for e in entries:
        idx = e['index']
        if idx in seen_indices:
            issues.append(f"Duplicate index: {idx}")
        seen_indices.add(idx)
        if not e['original'].strip():
            issues.append(f"{idx}: Empty original")

    if issues:
        print(f"Found {len(issues)} issues:")
        for issue in issues[:20]:
            print(f"  - {issue}")
    else:
        print("All validations passed!")

    # Write output
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

    print(f"\nWritten to: {OUTPUT}")


if __name__ == '__main__':
    main()
