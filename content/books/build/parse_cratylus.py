"""
Parse Plato's Cratylus (Jowett translation) into structured JSON for CSV conversion.
Single dialogue with 3 speakers: Socrates, Hermogenes, Cratylus.
"""

import json
import os
import re

BUILD_DIR = os.path.dirname(__file__)
SOURCE = os.path.join(BUILD_DIR, '..', 'Plato - Cratylus')
OUTPUT = os.path.join(BUILD_DIR, 'cratylus_originals.json')

SPEAKER_RE = re.compile(r'^(SOCRATES|HERMOGENES|CRATYLUS):\s*(.*)', re.DOTALL)

PIVOT_PATTERNS = [
    r'^But ', r'^Now ', r'^And now', r'^Again,? ', r'^Further',
    r'^However', r'^Yet ', r'^For ', r'^Hence ', r'^Therefore',
    r'^Moreover', r'^Let us ', r'^There is ', r'^Perhaps ',
    r'^I say ', r'^I will ', r'^This is ', r'^Wherefore',
    r'^In the ', r'^The ', r'^Such ', r'^We ', r'^And if ',
    r'^Take ', r'^Then ', r'^Suppose ',
]


def word_count(text):
    return len(text.split())


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

    # No pivot -- split at sentence boundary near middle
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


def detect_part(turns, i):
    """
    Determine which part a turn belongs to based on dialogue flow.
    Part 1: Introduction & convention vs nature debate (~first 120 turns)
    Part 2: Etymological section (bulk of dialogue with Hermogenes)
    Part 3: Dialogue with Cratylus (~last 180 lines / ~90 turns)
    """
    # We'll detect Part 3 by looking for when Cratylus becomes the primary respondent
    # This happens around the passage where Socrates transitions to addressing Cratylus directly
    pass  # Will assign parts after parsing all turns


def main():
    with open(SOURCE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print(f"Total lines: {len(lines)}")

    # Parse speaker turns (skip header lines 1-4)
    turns = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if i < 5:  # Skip header
            continue
        if not stripped:
            continue

        m = SPEAKER_RE.match(stripped)
        if m:
            speaker = m.group(1)
            text = m.group(2).strip()
            turns.append({
                'speaker': speaker,
                'text': text,
                'line': i + 1,
                'words': word_count(text)
            })

    print(f"Raw speaker turns: {len(turns)}")

    # Detect part boundaries
    # Part 3: Find where Cratylus becomes primary interlocutor
    # Look for a stretch of 5+ consecutive turns where Cratylus (not Hermogenes) responds
    part3_start = len(turns)
    cratylus_streak = 0
    for i, turn in enumerate(turns):
        if turn['speaker'] == 'CRATYLUS':
            cratylus_streak += 1
            if cratylus_streak >= 3 and i > len(turns) * 0.6:
                # Found the Cratylus section -- backtrack to find the transition
                # Go back to the first CRATYLUS in this cluster
                j = i
                while j > 0 and (turns[j-1]['speaker'] == 'CRATYLUS' or turns[j-1]['speaker'] == 'SOCRATES'):
                    if turns[j-1]['speaker'] == 'HERMOGENES':
                        break
                    j -= 1
                part3_start = j
                break
        else:
            if turn['speaker'] == 'HERMOGENES':
                cratylus_streak = 0

    # Part 1 vs Part 2: The etymological section begins when Socrates starts
    # analyzing specific names via Homer (~line 350). Detect by looking for
    # the Homer/Protagoras transition or the first name-etymology passage.
    part2_start = 0
    for i, turn in enumerate(turns):
        if i < 20:  # Skip early turns
            continue
        if i >= part3_start:
            break
        # Look for markers of the etymology section starting
        text_lower = turn['text'].lower()
        if turn['speaker'] == 'SOCRATES' and (
            'homer' in text_lower and 'gods call' in text_lower or
            'protagoras' in text_lower and 'fitness of names' in text_lower or
            'let us consider' in text_lower and 'poet' in text_lower
        ):
            part2_start = i
            break

    # Fallback: if no marker found, use ~22% of turns
    if part2_start == 0:
        part2_start = len(turns) // 5

    # Assign parts
    for i, turn in enumerate(turns):
        if i >= part3_start:
            turn['part'] = 3
        elif i >= part2_start:
            turn['part'] = 2
        else:
            turn['part'] = 1

    # Print part distribution
    for p in [1, 2, 3]:
        part_turns = [t for t in turns if t['part'] == p]
        total_words = sum(t['words'] for t in part_turns)
        print(f"Part {p}: {len(part_turns)} turns, {total_words} words "
              f"(lines {part_turns[0]['line']}-{part_turns[-1]['line']})")

    # Phase 1: Split long turns
    split_turns = []
    for turn in turns:
        if turn['words'] > 400:
            pieces = split_paragraph(turn['text'])
            for piece in pieces:
                split_turns.append({
                    'speaker': turn['speaker'],
                    'text': piece,
                    'words': word_count(piece),
                    'part': turn['part']
                })
        else:
            split_turns.append(turn)

    print(f"After splitting: {len(split_turns)} pieces")

    # Phase 2: Merge short turns and group Q&A chains
    merged = []
    i = 0
    while i < len(split_turns):
        current = split_turns[i]

        # Short turn -- try to group as Q&A chain
        if current['words'] < 60:
            chain = [current]
            chain_words = current['words']
            j = i + 1
            while j < len(split_turns) and split_turns[j]['part'] == current['part']:
                next_t = split_turns[j]
                if next_t['words'] < 80 and chain_words + next_t['words'] <= 350:
                    chain.append(next_t)
                    chain_words += next_t['words']
                    j += 1
                elif next_t['words'] < 60 and chain_words + next_t['words'] <= 400:
                    chain.append(next_t)
                    chain_words += next_t['words']
                    j += 1
                else:
                    break

            if len(chain) > 1:
                speakers = list(dict.fromkeys(c['speaker'] for c in chain))
                combined = '\n\n'.join(c['text'] for c in chain)
                merged.append({
                    'speaker': ', '.join(speakers),
                    'text': combined,
                    'words': chain_words,
                    'part': current['part']
                })
                i = j
                continue

            # Single short turn -- merge with neighbor
            if merged and merged[-1]['part'] == current['part'] and merged[-1]['words'] + current['words'] <= 400:
                merged[-1]['text'] += '\n\n' + current['text']
                merged[-1]['words'] += current['words']
                i += 1
                continue
            elif i + 1 < len(split_turns) and split_turns[i+1]['part'] == current['part']:
                split_turns[i+1]['text'] = current['text'] + '\n\n' + split_turns[i+1]['text']
                split_turns[i+1]['words'] += current['words']
                i += 1
                continue

        merged.append(current)
        i += 1

    # Phase 3: Final merge for remaining short thoughts
    final = []
    for m in merged:
        if m['words'] < 60 and final and final[-1]['part'] == m['part'] and final[-1]['words'] + m['words'] <= 400:
            final[-1]['text'] += '\n\n' + m['text']
            final[-1]['words'] += m['words']
        else:
            final.append(m)

    print(f"After merging: {len(final)} thoughts")

    # Build entries
    entries = []
    thought_counters = {}
    for thought in final:
        part = thought['part']
        if part not in thought_counters:
            thought_counters[part] = 0
        thought_counters[part] += 1
        t_num = thought_counters[part]

        idx = f"{part}.{t_num}"
        entries.append({
            'index': idx,
            'chapter': str(part),
            'thought': str(t_num),
            'speakers': thought.get('speaker', ''),
            'original': thought['text']
        })

    # Stats
    word_counts = [word_count(e['original']) for e in entries]
    print(f"\n--- Final Stats ---")
    print(f"Total thoughts: {len(entries)}")
    print(f"Word counts: min={min(word_counts)}, max={max(word_counts)}, avg={sum(word_counts)//len(word_counts)}")
    print(f"Under 60 words: {sum(1 for w in word_counts if w < 60)}")
    print(f"Over 400 words: {sum(1 for w in word_counts if w > 400)}")

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
