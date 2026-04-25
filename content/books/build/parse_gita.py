"""
Parse the Bhagavad Gita (Edwin Arnold translation) into per-chapter originals JSON files.

Structure: 18 chapters, verse stanzas separated by blank lines, with speaker tags.
Segmentation: each stanza or small group of stanzas = 1 thought.
Merge stanzas < 3 lines with adjacent stanza.
"""

import json
import re
import os

SOURCE = os.path.join(os.path.dirname(__file__), '..', 'Bhagavad Gita - Arnold')
OUTPUT_DIR = os.path.dirname(__file__)

# Traditional Sanskrit chapter titles
CHAPTER_TITLES = {
    1: "Arjuna's Despair (Arjuna Vishada Yoga)",
    2: "The Yoga of Knowledge (Sankhya Yoga)",
    3: "The Yoga of Action (Karma Yoga)",
    4: "The Yoga of Wisdom (Jnana Yoga)",
    5: "The Yoga of Renunciation (Karma Sannyasa Yoga)",
    6: "The Yoga of Meditation (Dhyana Yoga)",
    7: "The Yoga of Knowledge and Realization (Jnana Vijnana Yoga)",
    8: "The Yoga of the Imperishable Brahman (Aksara Brahma Yoga)",
    9: "The Yoga of Royal Knowledge (Raja Vidya Raja Guhya Yoga)",
    10: "The Yoga of Divine Glories (Vibhuti Yoga)",
    11: "The Vision of the Universal Form (Visvarupa Darshana Yoga)",
    12: "The Yoga of Devotion (Bhakti Yoga)",
    13: "The Yoga of the Field and its Knower (Kshetra Kshetrajna Vibhaga Yoga)",
    14: "The Yoga of the Three Gunas (Gunatraya Vibhaga Yoga)",
    15: "The Yoga of the Supreme Person (Purushottama Yoga)",
    16: "The Yoga of Divine and Demonic Natures (Daivasura Sampad Vibhaga Yoga)",
    17: "The Yoga of Threefold Faith (Sraddhatraya Vibhaga Yoga)",
    18: "The Yoga of Liberation (Moksha Sannyasa Yoga)",
}

SPEAKERS = {'Krishna.', 'Arjuna.', 'Sanjaya.', 'Dhritirashtra:', 'Dhritarashtra:',
            'Krishna.', 'Arjuna.', 'Sanjaya:', 'Dhritirashtra.'}


def read_source():
    with open(SOURCE, 'r', encoding='utf-8') as f:
        return f.readlines()


def parse_chapters(lines):
    """Parse text into chapters, each containing stanzas with speaker attribution."""
    chapters = []
    current_chapter = None
    current_stanza_lines = []
    current_speaker = None
    stanzas = []

    # Find start of text
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith('CHAPTER I'):
            break
        i += 1

    while i < len(lines):
        line = lines[i].rstrip('\n')
        stripped = line.strip()

        # Check for chapter boundary
        chapter_match = re.match(r'^\s*CHAPTER\s+([IVXLC]+)\s*$', stripped)
        if chapter_match:
            # Save previous stanza and chapter
            if current_stanza_lines:
                text = '\n'.join(current_stanza_lines).strip()
                if text:
                    stanzas.append({'speaker': current_speaker, 'text': text})
                current_stanza_lines = []

            if current_chapter is not None:
                current_chapter['stanzas'] = stanzas
                chapters.append(current_chapter)
                stanzas = []

            roman = chapter_match.group(1)
            ch_num = roman_to_int(roman)
            current_chapter = {
                'number': ch_num,
                'title': CHAPTER_TITLES.get(ch_num, ''),
            }
            current_speaker = None
            i += 1
            continue

        # Check for end of text
        if stripped in ('HERE ENDS', 'THE END', '*** END OF THE PROJECT GUTENBERG EBOOK'):
            break
        if stripped.startswith('***') and 'END' in stripped:
            break

        # Skip footnotes section
        if stripped.startswith('[FN#') and len(stripped) < 10:
            i += 1
            continue

        # Check for speaker tag
        if stripped in SPEAKERS or (stripped.endswith(':') and len(stripped) < 20 and stripped[:-1].isalpha()):
            # Save current stanza
            if current_stanza_lines:
                text = '\n'.join(current_stanza_lines).strip()
                if text:
                    stanzas.append({'speaker': current_speaker, 'text': text})
                current_stanza_lines = []
            current_speaker = stripped.rstrip(':').rstrip('.')
            i += 1
            continue

        # Blank line = stanza break
        if not stripped:
            if current_stanza_lines:
                text = '\n'.join(current_stanza_lines).strip()
                if text:
                    stanzas.append({'speaker': current_speaker, 'text': text})
                current_stanza_lines = []
            i += 1
            continue

        # Regular verse line — strip leading whitespace but preserve relative indentation
        if current_chapter is not None:
            # Strip inline footnote markers like [FN#l6]
            cleaned = re.sub(r'\[FN#\w+\]', '', stripped)
            if cleaned.strip():
                current_stanza_lines.append(cleaned.strip())

        i += 1

    # Save final stanza and chapter
    if current_stanza_lines:
        text = '\n'.join(current_stanza_lines).strip()
        if text:
            stanzas.append({'speaker': current_speaker, 'text': text})
    if current_chapter is not None:
        current_chapter['stanzas'] = stanzas
        chapters.append(current_chapter)

    return chapters


def roman_to_int(s):
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    result = 0
    for i, c in enumerate(s):
        if i + 1 < len(s) and vals.get(c, 0) < vals.get(s[i + 1], 0):
            result -= vals.get(c, 0)
        else:
            result += vals.get(c, 0)
    return result


def segment_stanzas(stanzas):
    """Merge very short stanzas with adjacent ones to create thoughts."""
    if not stanzas:
        return []

    thoughts = []
    i = 0
    while i < len(stanzas):
        s = stanzas[i]
        line_count = s['text'].count('\n') + 1

        # If stanza is very short (< 3 lines), try merging with next
        if line_count < 3 and i + 1 < len(stanzas):
            next_s = stanzas[i + 1]
            # Only merge if same speaker or speaker is None
            if next_s['speaker'] == s['speaker'] or s['speaker'] is None:
                merged_text = s['text'] + '\n\n' + next_s['text']
                speaker = s['speaker'] or next_s['speaker']
                thoughts.append({'speaker': speaker, 'text': merged_text})
                i += 2
                continue

        thoughts.append(s)
        i += 1

    return thoughts


def create_originals(chapters):
    """Create originals JSON for each chapter."""
    global_thought = 1

    all_entries = []
    for chapter in chapters:
        ch_num = chapter['number']
        thoughts = segment_stanzas(chapter['stanzas'])

        ch_entries = []
        for thought in thoughts:
            speaker = thought['speaker'] or 'Narrator'
            text = thought['text']

            # Prefix with speaker if it's dialogue
            if speaker in ('Krishna', 'Arjuna', 'Sanjaya', 'Dhritirashtra'):
                original = f"[{speaker}]\n{text}"
            else:
                original = text

            entry = {
                'index': f"{ch_num}.{global_thought}",
                'chapter': str(ch_num),
                'chapter_title': chapter['title'],
                'thought': str(global_thought),
                'speaker': speaker,
                'original': original,
            }
            ch_entries.append(entry)
            global_thought += 1

        all_entries.extend(ch_entries)
        print(f"Chapter {ch_num}: {chapter['title'][:50]} — {len(ch_entries)} thoughts")

    # Write single output file (Gita is shorter than multi-book works)
    output_path = os.path.join(OUTPUT_DIR, 'gita_originals.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_entries, f, indent=2, ensure_ascii=False)

    print(f"\nTotal thoughts: {len(all_entries)}")
    return all_entries


def main():
    lines = read_source()
    print(f"Read {len(lines)} lines")

    chapters = parse_chapters(lines)
    print(f"Parsed {len(chapters)} chapters\n")

    for ch in chapters:
        print(f"  Ch {ch['number']:>2}: {len(ch['stanzas'])} stanzas — {ch['title']}")

    print()
    create_originals(chapters)


if __name__ == '__main__':
    main()
