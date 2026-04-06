"""
Compile Cratylus originals + output JSON into Plato - Cratylus.csv.
"""

import csv
import json
import os

BUILD_DIR = os.path.dirname(__file__)
OUTPUT_CSV = os.path.join(BUILD_DIR, '..', 'Plato - Cratylus.csv')

HEADER = ['Index', 'Chapter', 'Thought', 'D: Original', 'D: Narrative', 'D: Refashioned', 'D: Elegant', 'D: Summary', 'D: Distilled', 'Notes']

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    rows = []

    rows.append({
        'Index': '',
        'Chapter': '',
        'Thought': '',
        'D: Original': '<a href="https://www.gutenberg.org/cache/epub/1616/pg1616-images.html">Cratylus - Plato (Benjamin Jowett translation)</a>',
        'D: Narrative': '<a href="https://www.gutenberg.org/cache/epub/1616/pg1616-images.html">Cratylus - Plato</a> - Narrative',
        'D: Refashioned': '<a href="https://www.gutenberg.org/cache/epub/1616/pg1616-images.html">Cratylus - Plato</a> - Refashioned',
        'D: Elegant': '',
        'D: Summary': '',
        'D: Distilled': '',
        'Notes': ''
    })

    originals_path = os.path.join(BUILD_DIR, 'cratylus_originals.json')
    output_path = os.path.join(BUILD_DIR, 'cratylus_output.json')

    originals = load_json(originals_path)

    outputs = {}
    if os.path.exists(output_path):
        for entry in load_json(output_path):
            outputs[entry['index']] = entry
    else:
        print(f"WARNING: Missing output file {output_path}")

    for orig in originals:
        idx = orig['index']
        out = outputs.get(idx, {})
        rows.append({
            'Index': idx,
            'Chapter': orig['chapter'],
            'Thought': orig['thought'],
            'D: Original': orig['original'],
            'D: Narrative': out.get('narrative', ''),
            'D: Refashioned': out.get('refashioned', ''),
            'D: Elegant': out.get('elegant', ''),
            'D: Summary': out.get('summary', ''),
            'D: Distilled': out.get('distilled', ''),
            'Notes': out.get('notes', '')
        })

    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=HEADER, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    total = len(originals)
    print(f"\nCSV written to: {OUTPUT_CSV}")
    print(f"Total thought rows: {total}")
    print(f"Total CSV rows: {total + 2}")

    print("\n--- Validation ---")
    seen = set()
    issues = []
    for row in rows[1:]:
        idx = row['Index']
        if not idx:
            continue
        if idx in seen:
            issues.append(f"Duplicate index: {idx}")
        seen.add(idx)
        if not row['D: Original'].strip():
            issues.append(f"{idx}: Empty original")
        if not row['D: Narrative'].strip():
            issues.append(f"{idx}: Empty narrative")
        if not row['D: Refashioned'].strip():
            issues.append(f"{idx}: Empty refashioned")

    if issues:
        print(f"Found {len(issues)} issues:")
        for issue in issues[:20]:
            print(f"  - {issue}")
    else:
        print("All validations passed!")

if __name__ == '__main__':
    main()
