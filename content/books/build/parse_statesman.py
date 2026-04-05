"""
Parse Plato's Statesman (Jowett translation) into structured JSON for CSV conversion.
Skips the introduction, segments the dialogue into thoughts with chapter structure.
Four speakers: Socrates, Theodorus, The Eleatic Stranger, The Younger Socrates.
"""

import json
import os
import re
from collections import Counter

BUILD_DIR = os.path.dirname(__file__)
SOURCE = os.path.join(BUILD_DIR, '..', 'Plato - Statesman')
OUTPUT = os.path.join(BUILD_DIR, 'statesman_originals.json')

SPEAKERS = ['STRANGER', 'YOUNG SOCRATES', 'SOCRATES', 'THEODORUS']
SPEAKER_PATTERN = re.compile(r'\b(' + '|'.join(re.escape(s) for s in SPEAKERS) + r'):')

# Chapter markers: (marker_text, chapter_number, chapter_name)
# marker_text is matched against the start of the paragraph after stripping the speaker prefix.
CHAPTER_MAP = [
    # Checked in reverse order (last match wins), so list from last to first
    ("The review of all these sciences shows that none of them is political or royal", 15, "The Political Web"),
    ("There remain, however, natures still more troublesome, because they are more nearly", 14, "The Statesman's Ministers"),
    ("The idea which has to be grasped by us is not easy or familiar", 13, "The Second-Best Government"),
    ("There can be no doubt that legislation is in a manner the business of a king", 12, "Law and the True Ruler"),
    ("Is not monarchy a recognized form of government", 11, "Forms of Government"),
    ("Let us go a little nearer, in order that we may be more certain of the complexion", 10, "Identifying the Rivals"),
    ("The art of the king has been separated from the similar arts of shepherds", 9, "The Co-operative Arts"),
    ("Very likely, but you may not always think so, my sweet friend", 8, "Excess and the Mean"),
    ("But no other art or science will have a prior or better right than the royal science", 7, "The Example of Weaving"),
    ("Before we can expect to have a perfect description of the statesman we must define", 6, "After the Myth"),
    ("Listen, then, to a tale which a child would love to hear", 5, "The Age of Cronus"),
    ("I say that we should have begun at first by dividing land animals into biped", 4, "The Rivals of the Herdsman"),
    ("May not all rulers be supposed to command for the sake of producing something", 3, "The King as Herdsman"),
    ("Where shall we discover the path of the Statesman", 2, "The Art of Ruling"),
]

# Pivot words for splitting long paragraphs
PIVOT_PATTERNS = [
    r'^But ', r'^Now ', r'^And now', r'^Again,? ', r'^Further', r'^However',
    r'^Yet ', r'^For ', r'^Hence ', r'^Therefore', r'^Moreover',
    r'^Let us ', r'^There is another', r'^Some one will say',
    r'^Perhaps ', r'^Strange', r'^And I ', r'^Wherefore',
    r'^I dare say', r'^I will tell', r'^This is ', r'^Nor ',
    r'^Then ', r'^Tell us', r'^Answer', r'^What complaint',
    r'^In the first', r'^Well then', r'^And because',
    r'^And he who', r'^These are', r'^Suppose now',
    r'^Consider', r'^Listen', r'^Think not',
    r'^Take the', r'^We have', r'^Allegory', r'^Allegories',
    r'^The allegory', r'^The allegories', r'^To this allegory',
    r'^Having', r'^Next', r'^Once more',
    r'^What I ', r'^We said', r'^We must', r'^We were',
    r'^There are', r'^Allegory', r'^When ', r'^If ',
    r'^That is ', r'^The true',
]


def word_count(text):
    return len(text.split())


def strip_footnotes(text):
    """Remove Gutenberg footnote reference numbers."""
    text = re.sub(r"(?<=[.?!,;:'\"])\s+\d(?=\s|$)", '', text)
    text = re.sub(r'(?<=\w)\s+\d(?=\s+[a-z])', '', text)
    return text


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

    # No pivot found — split at sentence boundary near middle
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
    if word_count(part1) > max_words:
        result.extend(split_paragraph(part1, max_words))
    else:
        result.append(part1)
    if word_count(part2) > max_words:
        result.extend(split_paragraph(part2, max_words))
    else:
        result.append(part2)

    return result


def get_speakers(text):
    """Extract speakers in order of appearance from text."""
    speakers = []
    seen = set()
    for match in SPEAKER_PATTERN.finditer(text):
        name = match.group(1)
        # Normalize names
        if name == 'STRANGER':
            display = 'Stranger'
        elif name == 'YOUNG SOCRATES':
            display = 'Young Socrates'
        else:
            display = name.capitalize()
        if display not in seen:
            speakers.append(display)
            seen.add(display)
    return ', '.join(speakers)


def determine_chapter(text, current_num, current_name):
    """Determine which chapter a paragraph belongs to."""
    # Strip speaker prefix for matching
    clean = SPEAKER_PATTERN.sub('', text).strip()
    for marker, ch_num, ch_name in CHAPTER_MAP:
        if clean.startswith(marker):
            return ch_num, ch_name
    return current_num, current_name


def main():
    with open(SOURCE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find dialogue start: look for "STATESMAN" header then "PERSONS OF THE DIALOGUE"
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == 'STATESMAN':
            # Find first speaker line after this
            for j in range(i + 1, len(lines)):
                if SPEAKER_PATTERN.match(lines[j].strip()):
                    start_idx = j
                    break
            break

    if start_idx is None:
        print("ERROR: Could not find dialogue start")
        return

    print(f"Dialogue starts at line {start_idx + 1}")

    # Build paragraphs: blank-line delimited
    raw_paras = []
    current_lines = []

    for line in lines[start_idx:]:
        stripped = line.strip()
        if not stripped:
            if current_lines:
                raw_paras.append(' '.join(current_lines))
                current_lines = []
        else:
            current_lines.append(stripped)

    if current_lines:
        raw_paras.append(' '.join(current_lines))

    # Split paragraphs that contain embedded speaker changes mid-text
    paragraphs = []
    for para in raw_paras:
        # Find speaker markers after position 0
        splits = list(SPEAKER_PATTERN.finditer(para))
        if len(splits) <= 1:
            paragraphs.append(para)
            continue

        # First speaker is at position 0 (or near it)
        first_match = splits[0]
        pieces = []
        last_pos = 0

        for m in splits[1:]:
            # Only split if the text before this speaker label seems complete
            before = para[last_pos:m.start()].strip()
            if before and word_count(before) >= 3:
                pieces.append(before)
                last_pos = m.start()

        remaining = para[last_pos:].strip()
        if remaining:
            pieces.append(remaining)

        if pieces:
            paragraphs.extend(pieces)
        else:
            paragraphs.append(para)

    print(f"Raw paragraphs: {len(paragraphs)}")

    # Strip footnotes from all paragraphs
    paragraphs = [strip_footnotes(p) for p in paragraphs]

    # Tag paragraphs with chapter and speaker info
    tagged_paras = []
    current_ch_num = 1
    current_ch_name = 'The Inquiry Begins'
    prev_speakers = 'Stranger'

    for para in paragraphs:
        speakers = get_speakers(para) or prev_speakers
        new_num, new_name = determine_chapter(para, current_ch_num, current_ch_name)
        current_ch_num = new_num
        current_ch_name = new_name

        tagged_paras.append({
            'ch_num': current_ch_num,
            'chapter': current_ch_name,
            'speakers': speakers,
            'text': para,
            'words': word_count(para)
        })
        prev_speakers = speakers

    # Print chapter distribution
    ch_counts = Counter(p['chapter'] for p in tagged_paras)
    print(f"\nChapter distribution (paragraphs):")
    for ch_name in sorted(ch_counts.keys(), key=lambda n: next(p['ch_num'] for p in tagged_paras if p['chapter'] == n)):
        paras_in_ch = [p for p in tagged_paras if p['chapter'] == ch_name]
        total_words = sum(p['words'] for p in paras_in_ch)
        print(f"  Ch {next(p['ch_num'] for p in paras_in_ch if p['chapter'] == ch_name):>2}: {ch_name:<30} {ch_counts[ch_name]:>3} paragraphs, {total_words:>5} words")

    # Phase 1: Split long paragraphs (>400 words)
    split_paras = []
    for tp in tagged_paras:
        if tp['words'] > 400:
            pieces = split_paragraph(tp['text'])
            for piece in pieces:
                split_paras.append({
                    'ch_num': tp['ch_num'],
                    'chapter': tp['chapter'],
                    'speakers': get_speakers(piece) or tp['speakers'],
                    'text': piece,
                    'words': word_count(piece)
                })
        else:
            split_paras.append(tp)

    print(f"\nAfter splitting: {len(split_paras)} pieces")

    # Phase 2: Merge short Q&A exchanges (<60 words)
    merged = []
    i = 0
    while i < len(split_paras):
        current = split_paras[i]

        if current['words'] < 60:
            chain = [current]
            chain_words = current['words']
            j = i + 1
            while j < len(split_paras) and split_paras[j]['chapter'] == current['chapter']:
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

            if len(chain) > 1:
                combined_text = '\n\n'.join(c['text'] for c in chain)
                merged.append({
                    'ch_num': current['ch_num'],
                    'chapter': current['chapter'],
                    'speakers': get_speakers(combined_text),
                    'text': combined_text,
                    'words': chain_words
                })
                i = j
                continue

            # Single short paragraph — try merge backward/forward
            if merged and merged[-1]['chapter'] == current['chapter'] and merged[-1]['words'] + current['words'] <= 400:
                merged[-1]['text'] += '\n\n' + current['text']
                merged[-1]['words'] += current['words']
                merged[-1]['speakers'] = get_speakers(merged[-1]['text'])
                i += 1
                continue

            if i + 1 < len(split_paras) and split_paras[i + 1]['chapter'] == current['chapter']:
                split_paras[i + 1]['text'] = current['text'] + '\n\n' + split_paras[i + 1]['text']
                split_paras[i + 1]['words'] += current['words']
                split_paras[i + 1]['speakers'] = get_speakers(split_paras[i + 1]['text'])
                i += 1
                continue

        merged.append(current)
        i += 1

    # Phase 3: Final cleanup — catch any remaining shorts
    final = []
    for m in merged:
        if m['words'] < 60 and final and final[-1]['chapter'] == m['chapter'] and final[-1]['words'] + m['words'] <= 400:
            final[-1]['text'] += '\n\n' + m['text']
            final[-1]['words'] += m['words']
            final[-1]['speakers'] = get_speakers(final[-1]['text'])
        else:
            final.append(m)

    print(f"After merging: {len(final)} thoughts")

    # Build final entries with per-chapter thought numbering
    entries = []
    thought_counters = {}

    for m in final:
        ch_num = m['ch_num']
        if ch_num not in thought_counters:
            thought_counters[ch_num] = 0
        thought_counters[ch_num] += 1
        thought_num = thought_counters[ch_num]

        idx = f"{ch_num}.{thought_num}"

        entries.append({
            'index': idx,
            'chapter': m['chapter'],
            'thought': str(thought_num),
            'speakers': m['speakers'],
            'original': m['text']
        })

    # Stats
    word_counts = [word_count(e['original']) for e in entries]
    print(f"\n--- Final Stats ---")
    print(f"Total thoughts: {len(entries)}")
    print(f"Word counts: min={min(word_counts)}, max={max(word_counts)}, avg={sum(word_counts)//len(word_counts)}")
    print(f"Under 60 words: {sum(1 for w in word_counts if w < 60)}")
    print(f"Over 400 words: {sum(1 for w in word_counts if w > 400)}")

    # Per-chapter stats
    for ch_num in sorted(thought_counters.keys()):
        ch_entries = [e for e in entries if e['index'].startswith(f"{ch_num}.")]
        ch_words = [word_count(e['original']) for e in ch_entries]
        ch_name = ch_entries[0]['chapter']
        print(f"  Ch {ch_num:>2} ({ch_name:<30}): {len(ch_entries):>3} thoughts, avg {sum(ch_words)//len(ch_words):>3} words")

    # Write output
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

    print(f"\nWritten to: {OUTPUT}")


if __name__ == '__main__':
    main()
