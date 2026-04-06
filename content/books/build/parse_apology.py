"""
Parse Plato's Apology (Jowett translation) into structured JSON for CSV conversion.
Skips the introduction, segments the speech into thoughts with Part/Chapter structure.
"""

import json
import os
import re

BUILD_DIR = os.path.dirname(__file__)
SOURCE = os.path.join(BUILD_DIR, '..', 'Plato - Apology')
OUTPUT = os.path.join(BUILD_DIR, 'apology_originals.json')

# Part 2 starts after conviction (line ~193)
PART2_MARKER = "There are many reasons why I am not grieved"
# Part 3 starts after sentencing (line ~201)
PART3_MARKER = "Not much time will be gained"

# Chapter 1.2: Meletus cross-examination
CH1_2_MARKER = "I have said enough in my defence against the first class"
# Chapter 1.3: Philosopher's duty
CH1_3_MARKER = "I have said enough in answer to the charge of Meletus"

# Pivot words for splitting long paragraphs
PIVOT_PATTERNS = [
    r'^But ', r'^Now ', r'^And now', r'^Again,? ', r'^Further', r'^However',
    r'^Yet ', r'^For ', r'^Hence ', r'^Therefore', r'^Moreover',
    r'^Let us ', r'^There is another', r'^Some one will say',
    r'^Perhaps ', r'^Strange', r'^And I ', r'^Wherefore',
    r'^I dare say', r'^I will tell', r'^This is ',
]

def word_count(text):
    return len(text.split())

def find_split_point(text, target_pos):
    """Find a good sentence boundary near target_pos for splitting."""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    if len(sentences) <= 1:
        return -1

    cumulative = 0
    best_pos = -1
    for i, sent in enumerate(sentences[:-1]):
        cumulative += len(sent) + 1
        if cumulative >= target_pos * 0.5:
            best_pos = cumulative
            if cumulative >= target_pos * 0.8:
                break
    return best_pos

def split_paragraph(text, max_words=400):
    """Split a long paragraph at topic pivots or sentence boundaries."""
    if word_count(text) <= max_words:
        return [text]

    sentences = re.split(r'(?<=[.!?])\s+', text)
    if len(sentences) <= 1:
        return [text]

    # Try to find a pivot sentence near the middle
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
        # Recursively split if still too long
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

def determine_part_and_chapter(text, current_part, current_chapter):
    """Determine which part and chapter a paragraph belongs to."""
    if text.startswith(PART3_MARKER):
        return 3, '3.1'
    if text.startswith(PART2_MARKER):
        return 2, '2.1'
    if current_part == 1:
        if text.startswith(CH1_3_MARKER):
            return 1, '1.3'
        if text.startswith(CH1_2_MARKER):
            return 1, '1.2'
    return current_part, current_chapter

def main():
    with open(SOURCE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find the APOLOGY marker (the second one — first is in table of contents)
    apology_count = 0
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == 'APOLOGY':
            apology_count += 1
            if apology_count == 2:
                start_idx = i + 1
                break

    if start_idx is None:
        print("ERROR: Could not find APOLOGY marker")
        return

    print(f"Content starts at line {start_idx + 1}")

    # Extract paragraphs (blank-line delimited)
    paragraphs = []
    current_para = []

    for line in lines[start_idx:]:
        stripped = line.strip()
        if not stripped:
            if current_para:
                paragraphs.append(' '.join(current_para))
                current_para = []
        else:
            # Skip the bracketed stage direction
            if stripped.startswith('[') and stripped.endswith(']'):
                continue
            current_para.append(stripped)

    if current_para:
        paragraphs.append(' '.join(current_para))

    print(f"Raw paragraphs: {len(paragraphs)}")

    # Assign parts and chapters
    current_part = 1
    current_chapter = '1.1'
    tagged_paras = []

    for para in paragraphs:
        new_part, new_chapter = determine_part_and_chapter(para, current_part, current_chapter)
        current_part = new_part
        current_chapter = new_chapter
        tagged_paras.append({
            'part': current_part,
            'chapter': current_chapter,
            'text': para,
            'words': word_count(para)
        })

    # Print chapter distribution
    from collections import Counter
    ch_counts = Counter(p['chapter'] for p in tagged_paras)
    print(f"\nChapter distribution (paragraphs):")
    for ch in sorted(ch_counts.keys()):
        paras_in_ch = [p for p in tagged_paras if p['chapter'] == ch]
        total_words = sum(p['words'] for p in paras_in_ch)
        print(f"  {ch}: {ch_counts[ch]} paragraphs, {total_words} words")

    # Phase 1: Split long paragraphs
    split_paras = []
    for tp in tagged_paras:
        if tp['words'] > 400:
            pieces = split_paragraph(tp['text'])
            for piece in pieces:
                split_paras.append({
                    'part': tp['part'],
                    'chapter': tp['chapter'],
                    'text': piece,
                    'words': word_count(piece)
                })
        else:
            split_paras.append(tp)

    print(f"\nAfter splitting: {len(split_paras)} pieces")

    # Phase 2: Merge short paragraphs
    # Group Q&A chains in the Meletus cross-examination
    merged = []
    i = 0
    while i < len(split_paras):
        current = split_paras[i]

        # Check if this is a short Q&A exchange in chapter 1.2
        if current['chapter'] == '1.2' and current['words'] < 60:
            # Accumulate short Q&A chain
            chain = [current]
            chain_words = current['words']
            j = i + 1
            while j < len(split_paras) and split_paras[j]['chapter'] == '1.2':
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
                    'text': combined_text,
                    'words': chain_words
                })
                i = j
                continue

        # For non-Q&A short paragraphs, merge with neighbor
        if current['words'] < 60:
            # Try to merge backward
            if merged and merged[-1]['chapter'] == current['chapter'] and merged[-1]['words'] + current['words'] <= 400:
                merged[-1]['text'] += '\n\n' + current['text']
                merged[-1]['words'] += current['words']
                i += 1
                continue
            # Try to merge forward
            if i + 1 < len(split_paras) and split_paras[i + 1]['chapter'] == current['chapter']:
                split_paras[i + 1]['text'] = current['text'] + '\n\n' + split_paras[i + 1]['text']
                split_paras[i + 1]['words'] += current['words']
                i += 1
                continue

        merged.append(current)
        i += 1

    print(f"After merging: {len(merged)} thoughts")

    # Build final entries
    entries = []
    thought_counters = {}

    for m in merged:
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
