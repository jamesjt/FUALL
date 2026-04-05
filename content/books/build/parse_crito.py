"""
Parse Plato's Crito (Jowett translation) into structured JSON for CSV conversion.
Skips the introduction, segments the dialogue into thoughts with Part/Chapter structure.
Two-speaker dialogue: Socrates and Crito.
"""

import json
import os
import re
from collections import Counter

BUILD_DIR = os.path.dirname(__file__)
SOURCE = os.path.join(BUILD_DIR, '..', 'Plato - Crito')
OUTPUT = os.path.join(BUILD_DIR, 'crito_originals.json')

# Chapter markers (text that starts the section, after stripping speaker prefix)
# Part 1: The Situation
#   1.1: Opening & the Dream
#   1.2: Crito's Appeal
CH1_2_MARKER = "Yes; the meaning is only too clear"
# Part 2: The Argument
#   2.1: Whose Opinion Matters
CH2_1_MARKER = "Dear Crito, your zeal is invaluable"
#   2.2: Principles of Justice
CH2_2_MARKER = "Are we to say that we are never intentionally to do wrong"
# Part 3: The Laws Speak
#   3.1: Prosopopoeia of the Laws
CH3_1_MARKER = "Then consider the matter in this way"
#   3.2: Conclusion
CH3_2_MARKER = "This, dear Crito, is the voice which I seem to hear"

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
    r"^'For just consider", r"^'Listen", r"^'And was that",
]

CHAPTER_MAP = [
    (CH3_2_MARKER, 3, '3.2'),
    (CH3_1_MARKER, 3, '3.1'),
    (CH2_2_MARKER, 2, '2.2'),
    (CH2_1_MARKER, 2, '2.1'),
    (CH1_2_MARKER, 1, '1.2'),
]

def word_count(text):
    return len(text.split())

def strip_footnotes(text):
    """Remove Gutenberg footnote reference numbers (standalone single digits after punctuation)."""
    # Strip trailing footnote: "word. 5" or "word? 6" or "word,' 3"
    text = re.sub(r"(?<=[.?!,;:'\"])\s+\d(?=\s|$)", '', text)
    # Strip inline footnote: "court 4 that" (single digit between words, not part of text)
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
    """Extract speakers in order of appearance from merged text."""
    speakers = []
    seen = set()
    for match in re.finditer(r'\b(SOCRATES|CRITO):', text):
        name = match.group(1).capitalize()
        if name not in seen:
            speakers.append(name)
            seen.add(name)
    return ', '.join(speakers)

def determine_chapter(text, current_part, current_chapter):
    """Determine which part and chapter a paragraph belongs to."""
    # Strip speaker prefix for matching
    clean = re.sub(r'^(SOCRATES|CRITO):\s*', '', text)
    for marker, part, chapter in CHAPTER_MAP:
        if clean.startswith(marker):
            return part, chapter
    return current_part, current_chapter

def main():
    with open(SOURCE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find dialogue start: look for "SCENE:" then skip to first speaker
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith('SCENE:'):
            # Find next non-blank line (first speaker)
            for j in range(i + 1, len(lines)):
                if lines[j].strip():
                    start_idx = j
                    break
            break

    if start_idx is None:
        print("ERROR: Could not find dialogue start")
        return

    print(f"Dialogue starts at line {start_idx + 1}")

    # Build paragraphs: blank-line delimited, then split embedded speaker changes
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
    # (e.g., Homer quote followed by "CRITO:" on same line group)
    paragraphs = []
    for para in raw_paras:
        # Find speaker markers after position 0
        splits = list(re.finditer(r'(?<=\s)(SOCRATES|CRITO):', para))
        if not splits:
            paragraphs.append(para)
            continue

        # Check if any of these are true new speakers (not the initial one)
        first_speaker = re.match(r'^(SOCRATES|CRITO):', para)
        start_pos = first_speaker.end() if first_speaker else 0

        pieces = []
        last_pos = 0
        for m in splits:
            if m.start() <= start_pos:
                continue
            # Only split if the text before this point seems complete
            # (contains actual content, not just whitespace)
            before = para[last_pos:m.start()].strip()
            if before:
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

    # Extract speaker info and clean text for each paragraph
    tagged_paras = []
    current_part = 1
    current_chapter = '1.1'
    prev_speakers = 'Socrates'

    for para in paragraphs:
        speakers = get_speakers(para) or prev_speakers
        new_part, new_chapter = determine_chapter(para, current_part, current_chapter)
        current_part = new_part
        current_chapter = new_chapter

        tagged_paras.append({
            'part': current_part,
            'chapter': current_chapter,
            'speakers': speakers,
            'text': para,
            'words': word_count(para)
        })
        prev_speakers = speakers

    # Print chapter distribution
    ch_counts = Counter(p['chapter'] for p in tagged_paras)
    print(f"\nChapter distribution (paragraphs):")
    for ch in sorted(ch_counts.keys()):
        paras_in_ch = [p for p in tagged_paras if p['chapter'] == ch]
        total_words = sum(p['words'] for p in paras_in_ch)
        print(f"  {ch}: {ch_counts[ch]} paragraphs, {total_words} words")

    # Phase 1: Split long paragraphs (>400 words)
    split_paras = []
    for tp in tagged_paras:
        if tp['words'] > 400:
            pieces = split_paragraph(tp['text'])
            for piece in pieces:
                split_paras.append({
                    'part': tp['part'],
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

        # Try to merge short Q&A chains
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
                    'part': current['part'],
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

    # Build final entries
    entries = []
    thought_counters = {}

    for m in final:
        part = m['part']
        if part not in thought_counters:
            thought_counters[part] = 0
        thought_counters[part] += 1
        thought_num = thought_counters[part]

        idx = f"{part}.{thought_num}"

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

    # Per-part stats
    for part in sorted(thought_counters.keys()):
        part_entries = [e for e in entries if e['index'].startswith(f"{part}.")]
        part_words = [word_count(e['original']) for e in part_entries]
        print(f"Part {part}: {len(part_entries)} thoughts, avg {sum(part_words)//len(part_words)} words")

    # Write output
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

    print(f"\nWritten to: {OUTPUT}")

if __name__ == '__main__':
    main()
