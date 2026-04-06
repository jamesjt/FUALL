"""
Compile all book originals + output JSONs into a single Aristotle Ethics CSV.
Matches the On Liberty CSV format: Index, Chapter, Thought, D: Original, D: Refashioned, D: Elegant, D: Summary, D: Distilled, Notes
"""

import csv
import json
import os

BUILD_DIR = os.path.dirname(__file__)
OUTPUT_CSV = os.path.join(BUILD_DIR, '..', 'Aristotle - Ethics.csv')

HEADER = ['Index', 'Chapter', 'Thought', 'D: Original', 'D: Refashioned', 'D: Elegant', 'D: Summary', 'D: Distilled', 'Notes']

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    rows = []

    # Row 2: Title/attribution (matching On Liberty pattern)
    rows.append({
        'Index': '',
        'Chapter': '',
        'Thought': '',
        'D: Original': '<a href="http://classics.mit.edu//Aristotle/nicomachaen.html">Nicomachean Ethics - Aristotle (W.D. Ross translation)</a>',
        'D: Refashioned': '<a href="http://classics.mit.edu//Aristotle/nicomachaen.html">Nicomachean Ethics - Aristotle</a> - Refashioned',
        'D: Elegant': '',
        'D: Summary': '',
        'D: Distilled': '',
        'Notes': ''
    })

    total_thoughts = 0
    missing_outputs = []

    for book_num in range(1, 11):
        originals_path = os.path.join(BUILD_DIR, f'book{book_num}_originals.json')
        output_path = os.path.join(BUILD_DIR, f'book{book_num}_output.json')

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
            missing_outputs.append(book_num)
            print(f"WARNING: Missing output for Book {book_num}, will use empty version columns")

        for orig in originals:
            idx = orig['index']
            out = outputs.get(idx, {})

            rows.append({
                'Index': idx,
                'Chapter': orig['chapter'],
                'Thought': orig['thought'],
                'D: Original': orig['original'],
                'D: Refashioned': out.get('refashioned', ''),
                'D: Elegant': out.get('elegant', ''),
                'D: Summary': out.get('summary', ''),
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

    print(f"\nCSV written to: {OUTPUT_CSV}")
    print(f"Total thought rows: {total_thoughts}")
    print(f"Total CSV rows (including header + attribution): {total_thoughts + 2}")

    if missing_outputs:
        print(f"\nWARNING: Missing output files for books: {missing_outputs}")

    # Validation
    print("\n--- Validation ---")
    seen_indices = set()
    issues = []
    for row in rows[1:]:  # skip attribution row
        idx = row['Index']
        if not idx:
            continue
        if idx in seen_indices:
            issues.append(f"Duplicate index: {idx}")
        seen_indices.add(idx)

        if not row['D: Original'].strip():
            issues.append(f"{idx}: Empty original")
        if not row['D: Refashioned'].strip():
            issues.append(f"{idx}: Empty refashioned")

    if issues:
        print(f"Found {len(issues)} issues:")
        for issue in issues[:20]:
            print(f"  - {issue}")
        if len(issues) > 20:
            print(f"  ... and {len(issues) - 20} more")
    else:
        print("All validations passed!")

if __name__ == '__main__':
    main()
