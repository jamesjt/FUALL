"""
Compile Epictetus Discourses originals + output JSONs into a single CSV.
4 versions: Original, Refashioned, Elegant, Distilled (no Summary).
"""

import csv
import json
import os

BUILD_DIR = os.path.dirname(__file__)
OUTPUT_CSV = os.path.join(BUILD_DIR, '..', 'Epictetus - Discourses.csv')

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
        'D: Original': '<a href="https://classics.mit.edu/Epictetus/discourses.html">The Discourses - Epictetus (George Long translation)</a>',
        'D: Refashioned': '<a href="https://classics.mit.edu/Epictetus/discourses.html">The Discourses - Epictetus</a> - Refashioned by Zzy',
        'D: Elegant': '',
        'D: Distilled': '',
        'Notes': ''
    })

    total_thoughts = 0

    for book_num in range(1, 5):
        originals_path = os.path.join(BUILD_DIR, f'epictetus_book{book_num}_originals.json')
        output_path = os.path.join(BUILD_DIR, f'epictetus_book{book_num}_output.json')

        if not os.path.exists(originals_path):
            print(f"WARNING: Missing {originals_path}")
            continue

        originals = load_json(originals_path)

        # Load output if available
        outputs = {}
        if os.path.exists(output_path):
            output_data = load_json(output_path)
            for entry in output_data:
                outputs[entry['index']] = entry
        else:
            print(f"No output yet for Book {book_num} — version columns will be empty")

        # Add chapter heading rows
        current_chapter = None
        for orig in originals:
            # Insert chapter heading row when chapter changes
            if orig['chapter'] != current_chapter:
                current_chapter = orig['chapter']
                title = orig.get('chapter_title', '')
                heading = f"Chapter {orig['chapter'].split('.')[1]}"
                if title:
                    heading += f": {title}"
                rows.append({
                    'Index': '',
                    'Chapter': orig['chapter'],
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

    # Write CSV
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=HEADER, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    print(f"\nWritten {OUTPUT_CSV}")
    print(f"Total: {total_thoughts} thoughts + {len(rows) - total_thoughts - 1} heading/title rows")


if __name__ == '__main__':
    main()
