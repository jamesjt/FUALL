"""
Compile Analects of Confucius originals + output JSON into CSV.
3 versions: Original, Refashioned, Elegant, Distilled. Plus Notes.
"""

import csv
import json
import os

BUILD_DIR = os.path.dirname(__file__)
OUTPUT_CSV = os.path.join(BUILD_DIR, '..', 'Confucius - Analects.csv')

HEADER = ['Index', 'Chapter', 'Thought', 'D: Original', 'D: Refashioned', 'D: Elegant', 'D: Distilled', 'Notes']


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    rows = []

    # Title/attribution row
    rows.append({
        'Index': '',
        'Chapter': '',
        'Thought': '',
        'D: Original': '<a href="https://www.gutenberg.org/ebooks/3330">The Analects of Confucius (James Legge translation)</a>',
        'D: Refashioned': '<a href="https://www.gutenberg.org/ebooks/3330">The Analects of Confucius</a> — Refashioned by Zzy',
        'D: Elegant': '',
        'D: Distilled': '',
        'Notes': ''
    })

    originals_path = os.path.join(BUILD_DIR, 'analects_originals.json')
    output_path = os.path.join(BUILD_DIR, 'analects_output.json')

    if not os.path.exists(originals_path):
        print(f"ERROR: Missing {originals_path}")
        return

    originals = load_json(originals_path)

    outputs = {}
    if os.path.exists(output_path):
        output_data = load_json(output_path)
        for entry in output_data:
            outputs[entry['index']] = entry
    else:
        print("No output yet — version columns will be empty")

    current_chapter = None
    total_thoughts = 0

    for orig in originals:
        if orig['chapter'] != current_chapter:
            current_chapter = orig['chapter']
            title = orig.get('chapter_title', '')
            heading = f"Book {current_chapter}"
            if title:
                heading += f": {title}"
            rows.append({
                'Index': '',
                'Chapter': current_chapter,
                'Thought': '',
                'D: Original': f'<b>{heading}</b>',
                'D: Refashioned': '',
                'D: Elegant': '',
                'D: Distilled': '',
                'Notes': ''
            })

        idx = orig['index']
        out = outputs.get(idx, {})

        rows.append({
            'Index': idx,
            'Chapter': orig['chapter'],
            'Thought': orig['thought'],
            'D: Original': orig['original'],
            'D: Refashioned': out.get('refashioned', ''),
            'D: Elegant': out.get('elegant', ''),
            'D: Distilled': out.get('distilled', ''),
            'Notes': out.get('notes', '')
        })
        total_thoughts += 1

    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=HEADER, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    print(f"\nWritten {OUTPUT_CSV}")
    print(f"Total: {total_thoughts} thoughts + {len(rows) - total_thoughts - 1} heading/title rows")


if __name__ == '__main__':
    main()
