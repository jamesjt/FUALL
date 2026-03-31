#!/usr/bin/env python3
"""
Convert FUALL.drawio.html into Obsidian vault notes.
One note per draw.io cell with YAML frontmatter, breadcrumbs, and wiki links.
Also copies polished articles into the vault.
"""

import json
import re
import html
import xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict
import shutil

SOURCE = Path(__file__).parent.parent.parent / "FUALL.drawio.html"
VAULT = Path(__file__).parent.parent.parent
RAW_DIR = VAULT / "raw"
ARTICLES_DIR = VAULT / "articles"
REORG_DIR = Path(__file__).parent / "reorg"

# ── Cluster definitions ──────────────────────────────────────────────

CLUSTER_FOLDERS = {
    "fundamentals":   "Fundamentals",
    "ethics":         "Ethics & Virtue",
    "values":         "Value Systems",
    "power":          "Power Domains",
    "spectrums":      "Political Spectrums",
    "prog_spectrum":  "Progressive-Conservative",
    "prog_arguments": "Progressive-Conservative",
    "prog_notes":     "Progressive-Conservative",
    "education":      "Education",
    "left_right":     "Left vs Right",
    "taxonomy":       "Taxonomy",
    "drafts":         "Drafts",
    "page2":          "Overview",
    "uncategorized":  "Uncategorized",
}

TAG_MAP = {
    "fundamentals":   "fundamentals",
    "ethics":         "ethics",
    "values":         "values",
    "power":          "power",
    "spectrums":      "spectrums",
    "prog_spectrum":  "progressive-conservative",
    "prog_arguments": "progressive-conservative",
    "prog_notes":     "progressive-conservative",
    "education":      "education",
    "left_right":     "left-right",
    "taxonomy":       "taxonomy",
    "drafts":         "drafts",
    "page2":          "overview",
    "uncategorized":  "uncategorized",
}

# Swimlane → cluster mapping (reused from extract_map.py)
SWIMLANE_CLUSTER = {
    "outline": "fundamentals",
    "wisdom": "values",
    "defining wisdom": "values",
    "core values": "values",
    "core values - zocratism": "values",
    "zocractic humanism": "values",
    "beauty": "values",
    "love": "values",
    "sin": "values",
    "spirit": "values",
    "spirit / soul": "values",
    "soul": "values",
    "value tensions": "values",
    "ethics": "ethics",
    "golden mean": "ethics",
    "god": "fundamentals",
    "god / reality": "fundamentals",
    "reality": "fundamentals",
    "quotes": "fundamentals",
    "history": "fundamentals",
    "mythos": "fundamentals",
    "domains of power": "power",
    "power structures": "power",
    "currently failing": "power",
    "aims of power": "spectrums",
    "aims of power: political spectrums": "spectrums",
    "pvc spectrum": "prog_spectrum",
    "lva spectrum": "spectrums",
    "what is the spectrum": "spectrums",
    "terminology": "left_right",
    "terminology: left vs right": "left_right",
    "progressive": "prog_spectrum",
    "conservative": "prog_spectrum",
    "progressivism": "prog_spectrum",
    "progressivism vs conservatism": "prog_arguments",
    "progressive-conservative": "prog_spectrum",
    "short": "prog_spectrum",
    "long": "prog_spectrum",
    "telos": "prog_spectrum",
    "trials": "prog_spectrum",
    "tragedy": "prog_spectrum",
    "tensions": "prog_spectrum",
    "notes: conservatism": "prog_notes",
    "notes: progressivism": "prog_notes",
    "notes: power": "prog_notes",
    "notes: sorting": "prog_notes",
    "notes: fuall": "drafts",
    "random notes": "drafts",
    "education": "education",
    "academy": "education",
    "guilds": "education",
    "temple": "education",
    "news": "education",
    "agora": "education",
    "laboratory": "education",
    "educational domains": "education",
    "old": "taxonomy",
    "drafts": "drafts",
    "drafts: power": "drafts",
    "original": "drafts",
    "gpt": "drafts",
    "grok": "drafts",
    # Page 2 swimlanes
    "fundamentals": "page2",
    "on power and politics": "page2",
    "4 domains of power": "page2",
    "4 domains of power - simple overview": "page2",
    "politics": "page2",
    "progressive - conservative": "page2",
    "uncertainty around left and right": "page2",
    "terms": "page2",
    "simple": "page2",
    "tradition": "page2",
    "tradition - history of the body of ideas": "page2",
    "tragedies": "page2",
    "tragedies - dystopian ends": "page2",
}


# ── HTML / XML parsing ───────────────────────────────────────────────

def strip_html(text):
    """Strip HTML tags, decode entities, clean up whitespace."""
    if not text:
        return ""
    text = html.unescape(text)
    text = re.sub(r'<br\s*/?>|</p>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<li[^>]*>', '- ', text, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    return text.strip()


def extract_xml_from_html(html_path):
    """Extract mxGraph XML from HTML file."""
    content = html_path.read_text(encoding='utf-8')
    match = re.search(r'data-mxgraph="([^"]*)"', content)
    if not match:
        raise ValueError("Could not find data-mxgraph attribute")
    json_str = html.unescape(match.group(1))
    data = json.loads(json_str)
    return data.get("xml", "")


def parse_diagrams(xml_str):
    """Parse mxfile XML into pages with cells and edges."""
    root = ET.fromstring(xml_str)
    pages = []

    for diagram in root.findall('.//diagram'):
        page_name = diagram.get('name', 'Unknown')
        page_cells = []
        page_edges = []

        for elem in diagram.iter():
            cell_id = elem.get('id')
            if cell_id is None:
                continue

            value = elem.get('value', '') or elem.get('label', '')
            style = elem.get('style', '')
            parent = elem.get('parent', '')
            trimmings = elem.get('Trimmings', '')

            geom = elem.find('.//mxGeometry') if elem.tag != 'mxGeometry' else None
            x = y = w = h = 0
            if geom is not None:
                x = float(geom.get('x', 0))
                y = float(geom.get('y', 0))
                w = float(geom.get('width', 0))
                h = float(geom.get('height', 0))

            is_edge = elem.get('edge') == '1' or 'edgeStyle' in style
            is_swimlane = 'swimlane' in style
            is_vertex = elem.get('vertex') == '1'

            source = elem.get('source', '')
            target = elem.get('target', '')

            if is_edge and source and target:
                page_edges.append({
                    'source': source,
                    'target': target,
                    'label': strip_html(value),
                })

            if cell_id in ('0', '1'):
                continue

            cell = {
                'id': cell_id,
                'text': strip_html(value),
                'trimmings': strip_html(trimmings),
                'style': style,
                'parent': parent,
                'x': x, 'y': y, 'w': w, 'h': h,
                'is_edge': is_edge,
                'is_swimlane': is_swimlane,
                'is_vertex': is_vertex,
            }

            if not is_edge:
                page_cells.append(cell)

        pages.append({
            'name': page_name,
            'cells': page_cells,
            'edges': page_edges,
        })

    return pages


# ── Cluster assignment ────────────────────────────────────────────────

def classify_swimlane(cell):
    text_lower = cell['text'].lower().strip()
    text_lower = re.sub(r'font style.*?>', '', text_lower).strip()
    for key, cluster in SWIMLANE_CLUSTER.items():
        if key == text_lower or text_lower.startswith(key):
            return cluster
    return None


def classify_by_position(cell):
    """Classify root-level cells by spatial position on Page 1."""
    x, y = cell['x'], cell['y']
    text_lower = cell['text'][:200].lower()

    if any(kw in text_lower for kw in ['plato', 'socrates', 'phaedo', 'republic', 'apology']):
        return "fundamentals"
    if any(kw in text_lower for kw in ['progressiv', 'conservati', 'main thesis']):
        return "prog_arguments"
    if any(kw in text_lower for kw in ['anarch', 'minarch', 'confedera', 'federa',
                                        'aristocra', 'oligarch', 'feudal', 'autocra']):
        return "spectrums"
    if any(kw in text_lower for kw in ['liberal vs auth', 'bret weinstein', 'libertarian']):
        return "left_right"
    if any(kw in text_lower for kw in ['mythos', 'game?', 'logical definition']):
        return "fundamentals"

    if y < -15000:
        return "drafts" if x > 5000 else "spectrums"
    if y < -10000:
        if x < -8000: return "left_right"
        if x < -4000: return "spectrums"
        return "prog_arguments"
    if y < -6000:
        return "left_right" if x < -10000 else "prog_notes"
    if y < -4000: return "spectrums"
    if y < -2000: return "power"
    if y < 0:
        return "drafts" if x > 5000 else "fundamentals"
    if y < 2000:
        if -10000 < x < -7000: return "taxonomy"
        return "fundamentals"
    if y < 4000:
        if -10500 < x < -9500: return "education"
        if -10000 < x < -7000: return "taxonomy"
        if x < -12000: return "ethics"
        return "fundamentals"
    if y < 6000: return "values"
    if y < 8000:
        return "values" if x < -9000 else "fundamentals"
    if y < 10000: return "fundamentals"
    if y < 12000: return "taxonomy"
    return "power"


def assign_clusters(pages):
    """Assign each cell to a cluster. Returns dict of cluster → cells."""
    clusters = defaultdict(list)
    all_cells_by_id = {}

    for page_idx, page in enumerate(pages):
        cells_by_id = {c['id']: c for c in page['cells']}
        all_cells_by_id.update(cells_by_id)
        swimlane_clusters = {}
        is_page2 = page_idx == 1

        # First pass: classify swimlanes
        for cell in page['cells']:
            if cell['is_swimlane']:
                cluster = classify_swimlane(cell)
                if cluster:
                    swimlane_clusters[cell['id']] = cluster
                elif is_page2:
                    swimlane_clusters[cell['id']] = "page2"

        # Second pass: assign all cells
        for cell in page['cells']:
            if cell['is_edge']:
                continue
            if not cell['text'] and not cell['trimmings']:
                continue

            assigned = None

            if cell['is_swimlane']:
                assigned = swimlane_clusters.get(cell['id'])

            if not assigned:
                parent_id = cell['parent']
                visited = set()
                while parent_id and parent_id not in ('0', '1') and parent_id not in visited:
                    visited.add(parent_id)
                    if parent_id in swimlane_clusters:
                        assigned = swimlane_clusters[parent_id]
                        break
                    parent_cell = cells_by_id.get(parent_id)
                    if parent_cell:
                        parent_id = parent_cell['parent']
                    else:
                        break

            if not assigned and is_page2:
                assigned = "page2"
            if not assigned and not is_page2:
                assigned = classify_by_position(cell)
            if not assigned:
                assigned = "uncategorized"

            cell['cluster'] = assigned
            cell['page_name'] = page['name']
            cell['page_idx'] = page_idx
            clusters[assigned].append(cell)

    all_edges = []
    for page in pages:
        all_edges.extend(page['edges'])

    return clusters, all_cells_by_id, all_edges


# ── Title & naming ────────────────────────────────────────────────────

def make_title(cell):
    """Extract a clean, readable title from cell content."""
    text = cell['text']
    if not text:
        if cell.get('trimmings'):
            text = cell['trimmings']
        else:
            return f"Untitled {cell['id']}"

    # Take first line
    first_line = text.split('\n')[0].strip()

    # Clean up common prefixes
    first_line = re.sub(r'^[-•·▪]\s*', '', first_line)
    first_line = re.sub(r'^\d+\.\s*', '', first_line)

    # If first line is very long, truncate at word boundary
    if len(first_line) > 80:
        truncated = first_line[:80]
        last_space = truncated.rfind(' ')
        if last_space > 30:
            first_line = truncated[:last_space]
        else:
            first_line = truncated

    # Sanitize for filesystem (Obsidian-safe)
    sanitized = re.sub(r'[<>:"/\\|?*#\[\]]', '', first_line)
    sanitized = re.sub(r'\s+', ' ', sanitized).strip('. ')

    if not sanitized or len(sanitized) < 3:
        # Fall back to more content
        words = text.split()[:10]
        sanitized = ' '.join(words)
        sanitized = re.sub(r'[<>:"/\\|?*#\[\]]', '', sanitized)
        sanitized = re.sub(r'\s+', ' ', sanitized).strip('. ')

    if not sanitized:
        return f"Untitled {cell['id']}"

    return sanitized


def get_swimlane_tag(cell, all_cells_by_id):
    """Walk parent chain to find the swimlane name for tagging."""
    parent_id = cell['parent']
    visited = set()
    while parent_id and parent_id not in ('0', '1') and parent_id not in visited:
        visited.add(parent_id)
        parent = all_cells_by_id.get(parent_id)
        if not parent:
            break
        if parent.get('is_swimlane') and parent.get('text'):
            tag = parent['text'].lower().strip()
            tag = re.sub(r'[^a-z0-9\s/-]', '', tag)
            tag = re.sub(r'\s+', '-', tag).strip('-')
            return tag[:40]
        parent_id = parent.get('parent', '')
    return None


# ── Note generation ───────────────────────────────────────────────────

def build_breadcrumb(cell, all_cells_by_id, note_titles):
    """Build breadcrumb: [[Grandparent]] > [[Parent]]"""
    chain = []
    current_id = cell.get('parent', '')
    visited = set()

    while current_id and current_id not in ('0', '1') and current_id not in visited:
        visited.add(current_id)
        parent = all_cells_by_id.get(current_id)
        if not parent:
            break
        title = note_titles.get(current_id)
        if title:
            chain.append(title)
        current_id = parent.get('parent', '')

    chain.reverse()
    if not chain:
        return ""
    return ' > '.join(f'[[{name}]]' for name in chain)


def write_note(filepath, title, cell, breadcrumb, tags, children_titles, edge_targets):
    """Write a single Obsidian-formatted note."""
    lines = ['---']
    # Escape quotes in title for YAML
    safe_title = title.replace('"', '\\"')
    lines.append(f'title: "{safe_title}"')
    if tags:
        lines.append(f'tags: [{", ".join(tags)}]')
    if cell.get('is_swimlane'):
        lines.append('type: section')
    lines.append(f'source: drawio')
    lines.append(f'cell-id: "{cell["id"]}"')
    lines.append(f'page: "{cell.get("page_name", "")}"')
    lines.append('---')
    lines.append('')

    # Breadcrumb navigation
    if breadcrumb:
        lines.append(breadcrumb)
        lines.append('')

    lines.append(f'# {title}')
    lines.append('')

    # Main content
    text = cell['text']
    if text and not cell['is_swimlane']:
        # Don't repeat title text at the start
        first_line = text.split('\n')[0].strip()
        if title.lower().startswith(first_line[:30].lower()) and len(first_line) <= len(title) + 10:
            remaining = '\n'.join(text.split('\n')[1:]).strip()
            if remaining:
                lines.append(remaining)
                lines.append('')
        else:
            lines.append(text)
            lines.append('')

    # Trimmings / extended notes
    if cell.get('trimmings'):
        lines.append('## Extended Notes')
        lines.append('')
        lines.append(cell['trimmings'])
        lines.append('')

    # Children links
    if children_titles:
        lines.append('## Contents')
        lines.append('')
        for child_title in children_titles:
            lines.append(f'- [[{child_title}]]')
        lines.append('')

    # Edge connections (links from draw.io arrows)
    if edge_targets:
        lines.append('## Connections')
        lines.append('')
        for target_title in edge_targets:
            lines.append(f'- [[{target_title}]]')
        lines.append('')

    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text('\n'.join(lines), encoding='utf-8')


def write_index(cluster_counts, note_titles, all_cells_by_id):
    """Write a master index note for the vault."""
    lines = ['---']
    lines.append('title: "Knowledge Map Index"')
    lines.append('tags: [index, MOC]')
    lines.append('---')
    lines.append('')
    lines.append('# Knowledge Map Index')
    lines.append('')
    lines.append('Extracted from `FUALL.drawio.html` — one note per cell.')
    lines.append('')

    lines.append('## Clusters')
    lines.append('')
    for cluster_id, count in sorted(cluster_counts.items(), key=lambda x: x[1], reverse=True):
        folder = CLUSTER_FOLDERS.get(cluster_id, cluster_id)
        lines.append(f'- **{folder}** — {count} notes')
    lines.append('')

    lines.append('## Articles (Polished)')
    lines.append('')
    if ARTICLES_DIR.exists():
        for f in sorted(ARTICLES_DIR.glob('*.md')):
            name = f.stem
            lines.append(f'- [[{name}]]')
    lines.append('')

    lines.append('## Raw Notes by Cluster')
    lines.append('')
    for folder_name in sorted(set(CLUSTER_FOLDERS.values())):
        folder_path = RAW_DIR / folder_name
        if folder_path.exists():
            notes = sorted(folder_path.glob('*.md'))
            if notes:
                lines.append(f'### {folder_name}')
                lines.append('')
                for note in notes:
                    lines.append(f'- [[{note.stem}]]')
                lines.append('')

    index_path = VAULT / "Index.md"
    index_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"  Index.md written")


def copy_articles():
    """Copy polished articles from reorg/ into vault with Obsidian frontmatter."""
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)

    if not REORG_DIR.exists():
        print("  No reorg/ directory found, skipping articles")
        return

    # Copy articles
    articles_src = REORG_DIR / "articles"
    if articles_src.exists():
        for src in sorted(articles_src.glob('*.md')):
            content = src.read_text(encoding='utf-8')

            # Add frontmatter if not present
            if not content.startswith('---'):
                title = src.stem.replace('-', ' ').title()
                # Clean up numbering prefix
                title = re.sub(r'^\d+[a-z]?\s*', '', title).strip()
                frontmatter = f'---\ntitle: "{title}"\ntags: [article, polished]\nsource: reorg\n---\n\n'
                content = frontmatter + content

            # Convert relative markdown links to wiki links
            content = re.sub(r'\[([^\]]+)\]\(([^)]+\.md)\)', r'[[\1]]', content)

            dest = ARTICLES_DIR / src.name
            dest.write_text(content, encoding='utf-8')
            print(f"  articles/{src.name}")

    # Copy other reorg files (outline, wisdom-notes)
    for src in REORG_DIR.glob('*.md'):
        content = src.read_text(encoding='utf-8')
        if not content.startswith('---'):
            title = src.stem.replace('-', ' ').title()
            title = re.sub(r'^\d+[a-z]?\s*', '', title).strip()
            frontmatter = f'---\ntitle: "{title}"\ntags: [article, polished]\nsource: reorg\n---\n\n'
            content = frontmatter + content
        content = re.sub(r'\[([^\]]+)\]\(([^)]+\.md)\)', r'[[\1]]', content)
        dest = ARTICLES_DIR / src.name
        dest.write_text(content, encoding='utf-8')
        print(f"  articles/{src.name}")


# ── Main ──────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("FUALL Draw.io → Obsidian Vault Export")
    print("=" * 60)

    # Parse draw.io
    print("\n1. Extracting XML from HTML...")
    xml_str = extract_xml_from_html(SOURCE)
    print(f"   XML length: {len(xml_str):,} chars")

    print("\n2. Parsing diagrams...")
    pages = parse_diagrams(xml_str)
    for i, page in enumerate(pages):
        print(f"   Page {i+1} ({page['name']}): {len(page['cells'])} cells, {len(page['edges'])} edges")

    print("\n3. Assigning clusters...")
    clusters, all_cells_by_id, all_edges = assign_clusters(pages)

    total_cells = sum(len(cells) for cells in clusters.values())
    print(f"   {total_cells} cells assigned to {len(clusters)} clusters")
    for cid, cells in sorted(clusters.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"     {CLUSTER_FOLDERS.get(cid, cid)}: {len(cells)}")

    # Generate titles for all cells
    print("\n4. Generating note titles...")
    note_titles = {}      # cell_id → title
    note_filenames = {}   # cell_id → filename (without .md)
    used_names = set()

    # First pass: generate titles
    for cid, cells in clusters.items():
        for cell in cells:
            title = make_title(cell)
            note_titles[cell['id']] = title

    # Second pass: deduplicate filenames
    for cid, cells in clusters.items():
        folder = CLUSTER_FOLDERS.get(cid, "Uncategorized")
        for cell in cells:
            title = note_titles[cell['id']]
            # Scope uniqueness within folder
            scoped_key = f"{folder}/{title}"
            name = title
            counter = 2
            while scoped_key in used_names:
                name = f"{title} ({counter})"
                scoped_key = f"{folder}/{name}"
                counter += 1
            used_names.add(scoped_key)
            note_filenames[cell['id']] = name
            # Update title if it was deduplicated
            if name != title:
                note_titles[cell['id']] = name

    print(f"   {len(note_titles)} titles generated")

    # Build parent→children map
    children_map = defaultdict(list)  # parent_id → [child_ids]
    for cid, cells in clusters.items():
        for cell in cells:
            parent_id = cell['parent']
            if parent_id in note_titles:
                children_map[parent_id].append(cell['id'])

    # Build edge connections map
    edge_connections = defaultdict(set)  # cell_id → {connected_cell_ids}
    for edge in all_edges:
        src, tgt = edge['source'], edge['target']
        if src in note_titles and tgt in note_titles:
            edge_connections[src].add(tgt)
            edge_connections[tgt].add(src)

    # Clean output directory
    if RAW_DIR.exists():
        shutil.rmtree(RAW_DIR)
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # Write notes
    print("\n5. Writing raw notes...")
    cluster_counts = {}
    for cid, cells in sorted(clusters.items()):
        folder = CLUSTER_FOLDERS.get(cid, "Uncategorized")
        folder_path = RAW_DIR / folder
        folder_path.mkdir(parents=True, exist_ok=True)

        count = 0
        for cell in cells:
            title = note_titles[cell['id']]
            filename = note_filenames[cell['id']]

            # Build tags
            tags = [TAG_MAP.get(cid, cid)]
            swimlane_tag = get_swimlane_tag(cell, all_cells_by_id)
            if swimlane_tag and swimlane_tag != tags[0]:
                tags.append(swimlane_tag)
            if cell['is_swimlane']:
                tags.append('section')

            # Build breadcrumb
            breadcrumb = build_breadcrumb(cell, all_cells_by_id, note_titles)

            # Children titles (sorted by position)
            child_ids = children_map.get(cell['id'], [])
            child_cells = [all_cells_by_id[cid_] for cid_ in child_ids if cid_ in all_cells_by_id]
            child_cells.sort(key=lambda c: (c['y'], c['x']))
            children_titles = [note_titles[c['id']] for c in child_cells]

            # Edge connections
            edge_ids = edge_connections.get(cell['id'], set())
            edge_target_titles = sorted(note_titles[eid] for eid in edge_ids if eid in note_titles)

            filepath = folder_path / f"{filename}.md"
            write_note(filepath, title, cell, breadcrumb, tags, children_titles, edge_target_titles)
            count += 1

        cluster_counts[cid] = count
        print(f"   {folder}: {count} notes")

    # Copy polished articles
    print("\n6. Copying polished articles...")
    copy_articles()

    # Write index
    print("\n7. Writing index...")
    write_index(cluster_counts, note_titles, all_cells_by_id)

    # Summary
    total_raw = sum(cluster_counts.values())
    total_articles = len(list(ARTICLES_DIR.glob('*.md'))) if ARTICLES_DIR.exists() else 0
    print("\n" + "=" * 60)
    print(f"Done! {total_raw} raw notes + {total_articles} articles → {VAULT}")
    print("=" * 60)


if __name__ == '__main__':
    main()
