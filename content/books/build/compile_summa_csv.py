"""
Compile Summa Theologica Part I originals + output JSON into CSV.
Format: Index, Chapter, Thought, D: Original, D: Refashioned, D: Elegant, D: Summary, D: Distilled, Notes
"""

import csv
import json
import os

BUILD_DIR = os.path.dirname(__file__)
OUTPUT_CSV = os.path.join(BUILD_DIR, '..', 'Aquinas - Summa Theologica I.csv')

HEADER = ['Index', 'Chapter', 'Thought', 'D: Original', 'D: Refashioned', 'D: Elegant', 'D: Summary', 'D: Distilled', 'Notes']

GUTENBERG_URL = 'https://www.gutenberg.org/cache/epub/17611/pg17611-images.html'


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    rows = []

    # Row 2: Title/attribution
    rows.append({
        'Index': '',
        'Chapter': '',
        'Thought': '',
        'D: Original': f'<a href="{GUTENBERG_URL}">Summa Theologica, Part I (Prima Pars) - Thomas Aquinas (Dominican Province translation)</a>',
        'D: Refashioned': f'<a href="{GUTENBERG_URL}">Summa Theologica I - Aquinas</a> - Refashioned',
        'D: Elegant': f'<a href="{GUTENBERG_URL}">Summa Theologica I - Aquinas</a> - Elegant',
        'D: Summary': '',
        'D: Distilled': '',
        'Notes': ''
    })

    originals_path = os.path.join(BUILD_DIR, 'summa_p1_originals.json')
    output_path = os.path.join(BUILD_DIR, 'summa_p1_output.json')

    if not os.path.exists(originals_path):
        print(f"ERROR: Missing {originals_path}")
        return

    originals = load_json(originals_path)

    # Load output if available
    outputs = {}
    if os.path.exists(output_path):
        output_data = load_json(output_path)
        for entry in output_data:
            outputs[entry['index']] = entry
    else:
        print(f"Note: No output file {output_path} — rewrite columns will be empty")

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

    # Write CSV
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=HEADER, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    total_thoughts = len(originals)
    print(f"\nCSV written to: {OUTPUT_CSV}")
    print(f"Total thought rows: {total_thoughts}")
    print(f"Total CSV rows (including header + attribution): {total_thoughts + 2}")

    # Validation
    print("\n--- Validation ---")
    seen_indices = set()
    issues = []
    for row in rows[1:]:
        idx = row['Index']
        if not idx:
            continue
        if idx in seen_indices:
            issues.append(f"Duplicate index: {idx}")
        seen_indices.add(idx)

        if not row['D: Original'].strip():
            issues.append(f"{idx}: Empty original")

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
