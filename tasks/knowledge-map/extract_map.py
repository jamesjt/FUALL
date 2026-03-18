#!/usr/bin/env python3
"""
Extract content from FUALL.drawio.html and generate categorized markdown files.
Preserves spatial relationships and cross-references from the knowledge map.
"""

import json
import re
import html
import xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict

SOURCE = Path(__file__).parent.parent.parent / "FUALL.drawio.html"
OUTPUT = Path(__file__).parent

# --- Cluster definitions ---
# Each cluster has: id, filename, title, description, related clusters
CLUSTERS = {
    "fundamentals":    {"file": "01-fundamentals.md",        "title": "Fundamentals & Outline"},
    "ethics":          {"file": "02-ethics-virtue.md",       "title": "Ethics & Virtue"},
    "values":          {"file": "03-value-systems.md",       "title": "Value Systems"},
    "power":           {"file": "04-power-domains.md",       "title": "Power Domains & Structures"},
    "spectrums":       {"file": "05-political-spectrums.md", "title": "Political Spectrums"},
    "prog_spectrum":   {"file": "06a-prog-con-spectrum.md",  "title": "Progressive-Conservative: Spectrum Model"},
    "prog_arguments":  {"file": "06b-prog-con-arguments.md", "title": "Progressive-Conservative: Arguments & Essays"},
    "prog_notes":      {"file": "06c-prog-con-notes.md",     "title": "Progressive-Conservative: Working Notes"},
    "education":       {"file": "07-education.md",           "title": "Education & Institutions"},
    "left_right":      {"file": "08-left-right.md",          "title": "Left vs Right Terminology"},
    "taxonomy":        {"file": "09-taxonomy-old.md",        "title": "Taxonomy & Legacy Notes"},
    "drafts":          {"file": "10-drafts-notes.md",        "title": "Drafts & Working Notes"},
    "page2":           {"file": "11-page2-overview.md",      "title": "Page 2: Condensed Overview"},
    "uncategorized":   {"file": "99-uncategorized.md",       "title": "Uncategorized Items"},
}

RELATED = {
    "fundamentals":    ["power", "values", "spectrums"],
    "ethics":          ["values", "fundamentals"],
    "values":          ["ethics", "fundamentals", "education"],
    "power":           ["spectrums", "fundamentals", "prog_spectrum"],
    "spectrums":       ["prog_spectrum", "left_right", "power"],
    "prog_spectrum":   ["prog_arguments", "prog_notes", "spectrums", "left_right"],
    "prog_arguments":  ["prog_spectrum", "prog_notes", "spectrums"],
    "prog_notes":      ["prog_spectrum", "prog_arguments", "spectrums"],
    "education":       ["fundamentals", "values"],
    "left_right":      ["spectrums", "prog_spectrum"],
    "taxonomy":        ["fundamentals"],
    "drafts":          ["prog_arguments"],
    "page2":           ["fundamentals", "spectrums", "power"],
}

# Swimlane name → cluster mapping
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

# Max chars before we consider something a "full embedded text" to exclude
FULL_TEXT_THRESHOLD = 10000


def strip_html(text):
    """Strip HTML tags, decode entities, clean up whitespace."""
    if not text:
        return ""
    # Decode HTML entities
    text = html.unescape(text)
    # Replace <br>, <br/>, <p> with newlines
    text = re.sub(r'<br\s*/?>|</p>', '\n', text, flags=re.IGNORECASE)
    # Replace <li> with bullet points
    text = re.sub(r'<li[^>]*>', '- ', text, flags=re.IGNORECASE)
    # Strip all remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Decode again (sometimes double-encoded)
    text = html.unescape(text)
    # Clean up whitespace
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    return text.strip()


def extract_xml_from_html(html_path):
    """Extract the mxGraph XML from the HTML file's data-mxgraph attribute."""
    content = html_path.read_text(encoding='utf-8')

    # Find data-mxgraph attribute
    match = re.search(r'data-mxgraph="([^"]*)"', content)
    if not match:
        raise ValueError("Could not find data-mxgraph attribute")

    # Decode HTML entities to get JSON
    json_str = html.unescape(match.group(1))
    data = json.loads(json_str)
    xml_str = data.get("xml", "")

    return xml_str


def parse_diagrams(xml_str):
    """Parse the mxfile XML and return cells organized by page."""
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

            # Get value/label from either mxCell value or object label
            value = elem.get('value', '') or elem.get('label', '')
            style = elem.get('style', '')
            parent = elem.get('parent', '')

            # Check for Trimmings attribute (essay content on <object> elements)
            trimmings = elem.get('Trimmings', '')

            # Get geometry
            geom = elem.find('.//mxGeometry') if elem.tag != 'mxGeometry' else None
            # Also check if this element IS inside an mxCell that has geometry
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

            clean_text = strip_html(value)
            clean_trimmings = strip_html(trimmings)

            cell = {
                'id': cell_id,
                'raw_value': value,
                'text': clean_text,
                'trimmings': clean_trimmings,
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


def classify_swimlane(cell):
    """Try to match a swimlane cell's text to a cluster."""
    text_lower = cell['text'].lower().strip()
    # Remove HTML font-size wrappers that might remain
    text_lower = re.sub(r'font style.*?>', '', text_lower).strip()

    for key, cluster in SWIMLANE_CLUSTER.items():
        if key == text_lower or text_lower.startswith(key):
            return cluster
    return None


def classify_by_position(cell):
    """Classify a root-level (parent=1) cell by its spatial position on Page 1.

    Based on observed spatial zones in the diagram:
    - Political structures & govt forms: y < -15000
    - CvI/LvA notes & political analysis: y -15000 to -10000, x < -4000
    - Progressive arguments & essays: y -15000 to -10000, x >= -4000
    - Left/Right terminology: y -10000 to -6000, x < -10000
    - Progressive thesis & notes: y -10000 to -6000, x >= -10000
    - Political spectrums (LvA terms): y -6000 to -4000
    - Power domains: y -4000 to -2000
    - Mythos & philosophy: y -2000 to 0, x < 5000
    - Drafts & civic strategy: y -2000 to 0, x >= 5000
    - Taxonomy (insects, birds, bacteria): y 0 to 4000, x -10000 to -7000
    - Education/trivium cells: y 2000 to 4000, x -11000 to -9000
    - Epistemology/philosophy: y 4000 to 6000
    - Plato & readings: y 6000 to 9000, x > -9000
    - Defining Wisdom area: y 6000 to 8000, x < -9000
    - Bad science, anomie, etc.: y > 12000
    """
    x, y = cell['x'], cell['y']
    text_lower = cell['text'][:200].lower()

    # Keyword-based overrides (more reliable than pure position)
    if any(kw in text_lower for kw in ['plato', 'socrates', 'phaedo', 'republic', 'apology']):
        # Skip full Plato texts
        if len(cell['text']) > FULL_TEXT_THRESHOLD:
            return None  # Will be skipped
        return "fundamentals"  # Plato references go to fundamentals

    if any(kw in text_lower for kw in ['progressiv', 'conservati', 'main thesis']):
        return "prog_arguments"

    if any(kw in text_lower for kw in ['anarch', 'minarch', 'confedera', 'federa', 'republic', 'aristocra', 'oligarch', 'feudal', 'autocra']):
        return "spectrums"  # Government forms

    if any(kw in text_lower for kw in ['liberal vs auth', 'bret weinstein', 'libertarian']):
        return "left_right"

    if any(kw in text_lower for kw in ['mythos', 'game?', 'logical definition']):
        return "fundamentals"

    # Spatial zones
    if y < -15000:
        if x > 5000:
            return "drafts"
        return "spectrums"  # Government forms, political structures

    if y < -10000:
        if x < -8000:
            return "left_right"  # CvI notes area
        if x < -4000:
            return "spectrums"
        return "prog_arguments"  # Progressive essays

    if y < -6000:
        if x < -10000:
            return "left_right"
        return "prog_notes"

    if y < -4000:
        return "spectrums"  # LvA terms, political spectrum terms

    if y < -2000:
        return "power"

    if y < 0:
        if x > 5000:
            return "drafts"
        return "fundamentals"

    if y < 2000:
        # Taxonomy zone (insects, animals)
        if -10000 < x < -7000:
            return "taxonomy"
        return "fundamentals"

    if y < 4000:
        # Mixed: education concepts + taxonomy + Aristotle
        if -10500 < x < -9500:
            return "education"  # Trivium: Academy, Guild, Temple, etc.
        if -10000 < x < -7000:
            return "taxonomy"  # Birds, bacteria
        if x < -12000:
            return "ethics"  # Aristotle area
        return "fundamentals"

    if y < 6000:
        return "values"  # Epistemology, wisdom, existence questions

    if y < 8000:
        if x < -9000:
            return "values"  # Defining wisdom area
        return "fundamentals"  # Plato readings

    if y < 10000:
        return "fundamentals"  # More philosophy

    if y < 12000:
        return "taxonomy"  # Near the "Old" swimlane

    # Far south: bad science, social decay, etc.
    return "power"  # Failing institutions area


def assign_clusters(pages):
    """Assign each cell to a cluster. Returns dict[cluster_id] -> list of cells."""
    clusters = defaultdict(list)

    for page_idx, page in enumerate(pages):
        cells_by_id = {c['id']: c for c in page['cells']}
        swimlane_clusters = {}  # swimlane_id -> cluster_id

        # Page 2 goes to page2 cluster by default
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

            # Skip cells with empty text and no trimmings
            if not cell['text'] and not cell['trimmings']:
                continue

            # Skip full embedded reference texts
            if len(cell['text']) > FULL_TEXT_THRESHOLD:
                # Check if it's a known reference text
                text_start = cell['text'][:200].lower()
                if any(kw in text_start for kw in ['apology', 'socrates', 'nicomachean', 'aristotle', 'plato']):
                    continue

            # Determine cluster
            assigned = None

            # If it's a swimlane, use its own classification
            if cell['is_swimlane']:
                assigned = swimlane_clusters.get(cell['id'])

            # If not, check its parent chain
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

            # Default for page 2
            if not assigned and is_page2:
                assigned = "page2"

            # For unassigned page 1 cells, classify by spatial position
            if not assigned and not is_page2:
                assigned = classify_by_position(cell)

            # None means explicitly excluded (e.g., full reference texts)
            if assigned is None:
                continue

            if not assigned:
                assigned = "uncategorized"

            cell['page'] = page['name']
            cell['page_idx'] = page_idx
            clusters[assigned].append(cell)

        # Store edges per page
        clusters[f"_edges_{page_idx}"] = page['edges']
        clusters[f"_cells_by_id_{page_idx}"] = cells_by_id

    return clusters


def format_cell_content(cell, indent=""):
    """Format a single cell's content for markdown output."""
    lines = []
    text = cell['text']

    if not text and not cell.get('trimmings'):
        return ""

    # Truncate very long content
    if len(text) > 3000:
        text = text[:3000] + f"\n\n[... truncated, {len(cell['text'])} total chars]"

    if cell['is_swimlane']:
        return ""  # Swimlanes become headers, not content

    lines.append(f"{indent}- **{text[:100]}**" if len(text) > 100 else f"{indent}- {text}")
    if len(text) > 100:
        # Multi-line content: indent under the bullet
        for line in text[100:].split('\n'):
            if line.strip():
                lines.append(f"{indent}  {line.strip()}")

    if cell.get('trimmings'):
        trimmings = cell['trimmings']
        if len(trimmings) > 3000:
            trimmings = trimmings[:3000] + f"\n\n[... truncated, {len(cell['trimmings'])} total chars]"
        lines.append(f"{indent}  > **Extended notes:**")
        for line in trimmings.split('\n'):
            if line.strip():
                lines.append(f"{indent}  > {line.strip()}")

    return '\n'.join(lines)


def get_spatial_context(cells):
    """Generate a spatial context description for a group of cells."""
    if not cells:
        return ""

    positioned = [c for c in cells if c['x'] != 0 or c['y'] != 0]
    if not positioned:
        return ""

    min_x = min(c['x'] for c in positioned)
    max_x = max(c['x'] + c['w'] for c in positioned)
    min_y = min(c['y'] for c in positioned)
    max_y = max(c['y'] + c['h'] for c in positioned)

    return f"> **Spatial extent:** x: {min_x:.0f} to {max_x:.0f}, y: {min_y:.0f} to {max_y:.0f}"


def build_hierarchy(cells):
    """Organize cells into parent-child hierarchy."""
    by_id = {c['id']: c for c in cells}
    children = defaultdict(list)
    roots = []

    for cell in cells:
        parent = cell['parent']
        if parent in by_id:
            children[parent].append(cell)
        else:
            roots.append(cell)

    return roots, children, by_id


def write_cluster_file(cluster_id, cells, all_clusters, edges_p1, edges_p2, cells_by_id_p1, cells_by_id_p2):
    """Write a single cluster markdown file."""
    info = CLUSTERS[cluster_id]
    filepath = OUTPUT / info['file']

    lines = [f"# {info['title']}\n"]

    # Related clusters
    related = RELATED.get(cluster_id, [])
    if related:
        lines.append("## Related Clusters\n")
        for r in related:
            r_info = CLUSTERS.get(r, {})
            lines.append(f"- [{r_info.get('title', r)}]({r_info.get('file', '')})")
        lines.append("")

    # Spatial context
    spatial = get_spatial_context(cells)
    if spatial:
        lines.append(spatial)
        lines.append("")

    # Separate swimlanes from content cells
    swimlanes = [c for c in cells if c['is_swimlane']]
    content = [c for c in cells if not c['is_swimlane']]

    # Build parent→children map for this cluster's cells
    all_ids = {c['id'] for c in cells}
    parent_children = defaultdict(list)
    orphans = []

    for cell in content:
        if cell['parent'] in all_ids:
            parent_children[cell['parent']].append(cell)
        else:
            orphans.append(cell)

    # Write swimlane sections
    if swimlanes:
        # Sort swimlanes by position (top to bottom, left to right)
        swimlanes.sort(key=lambda c: (c['y'], c['x']))

        for sw in swimlanes:
            if not sw['text']:
                continue
            sw_title = sw['text'][:200].replace('\n', ' ')
            lines.append(f"## {sw_title}\n")

            # Spatial context for this section
            section_cells = [sw] + parent_children.get(sw['id'], [])
            sc = get_spatial_context(section_cells)
            if sc:
                lines.append(sc)
                lines.append("")

            # Children of this swimlane
            children = parent_children.get(sw['id'], [])
            children.sort(key=lambda c: (c['y'], c['x']))

            for child in children:
                formatted = format_cell_content(child)
                if formatted:
                    lines.append(formatted)

                # Grandchildren
                grandchildren = parent_children.get(child['id'], [])
                grandchildren.sort(key=lambda c: (c['y'], c['x']))
                for gc in grandchildren:
                    formatted = format_cell_content(gc, indent="  ")
                    if formatted:
                        lines.append(formatted)

            lines.append("")

    # Write orphan cells (not under any swimlane in this cluster)
    if orphans:
        orphans.sort(key=lambda c: (c['y'], c['x']))
        lines.append("## Additional Notes\n")
        sc = get_spatial_context(orphans)
        if sc:
            lines.append(sc)
            lines.append("")
        for cell in orphans:
            formatted = format_cell_content(cell)
            if formatted:
                lines.append(formatted)
        lines.append("")

    # Connections involving cells in this cluster
    cluster_cell_ids = all_ids
    relevant_edges = []

    all_cells_lookup = {}
    all_cells_lookup.update(cells_by_id_p1)
    all_cells_lookup.update(cells_by_id_p2)

    for edge in list(edges_p1) + list(edges_p2):
        if edge['source'] in cluster_cell_ids or edge['target'] in cluster_cell_ids:
            source_text = all_cells_lookup.get(edge['source'], {}).get('text', edge['source'])
            target_text = all_cells_lookup.get(edge['target'], {}).get('text', edge['target'])
            if source_text and target_text:
                # Truncate long labels
                s = source_text[:80].replace('\n', ' ')
                t = target_text[:80].replace('\n', ' ')
                relevant_edges.append(f"- {s} → {t}")

    if relevant_edges:
        lines.append("## Connections\n")
        for edge in relevant_edges:
            lines.append(edge)
        lines.append("")

    # Review section
    lines.append("## Review Status\n")
    lines.append("- [ ] Content reviewed for accuracy")
    lines.append("- [ ] Redundancies identified")
    lines.append("- [ ] Missing connections noted")
    lines.append("- [ ] Ready for integration")
    lines.append("")

    filepath.write_text('\n'.join(lines), encoding='utf-8')
    return len(cells)


def write_index(clusters, all_cluster_ids):
    """Write the master index file."""
    filepath = OUTPUT / "00-index.md"

    lines = [
        "# FUALL Knowledge Map — Index\n",
        "Extracted from `FUALL.drawio.html`. Each file below contains a categorized",
        "slice of the knowledge map with spatial relationships preserved.\n",
        "## Files\n",
        "| File | Cluster | Items |",
        "|------|---------|-------|",
    ]

    for cid in all_cluster_ids:
        if cid.startswith('_'):
            continue
        info = CLUSTERS.get(cid, {})
        count = len(clusters.get(cid, []))
        if count > 0:
            lines.append(f"| [{info.get('file', '')}]({info.get('file', '')}) | {info.get('title', cid)} | {count} |")

    lines.append("")

    # Spatial overview
    lines.append("## Spatial Overview (Page 1 approximate layout)\n")
    lines.append("```")
    lines.append("                        TOP (negative Y)")
    lines.append("                            |")
    lines.append("  LEFT/RIGHT        Political Spectrums          DRAFTS")
    lines.append("  TERMINOLOGY       LvA / PvC / Aims             GPT/Grok")
    lines.append("                            |                    rewrites")
    lines.append("                    Notes: Power/Sorting")
    lines.append("                            |")
    lines.append("  QUOTES            Domains of Power        OUTLINE")
    lines.append("  DEFINING          God/Reality              Mythos")
    lines.append("  WISDOM                    |                    EDUCATION")
    lines.append("                    ETHICS                   (Academy, Guilds,")
    lines.append("                            |                 Temple, News,")
    lines.append("  RANDOM NOTES      Spirit/Soul              Agora, Lab)")
    lines.append("                    Love / Sin")
    lines.append("                            |")
    lines.append("  OLD/TAXONOMY      Beauty")
    lines.append("                            |")
    lines.append("                        BOTTOM (positive Y)")
    lines.append("```\n")

    # Cross-cluster relationships
    lines.append("## Cross-Cluster Relationships\n")
    for cid, related in RELATED.items():
        info = CLUSTERS.get(cid, {})
        related_names = [CLUSTERS.get(r, {}).get('title', r) for r in related]
        lines.append(f"- **{info.get('title', cid)}** ↔ {', '.join(related_names)}")
    lines.append("")

    # Review order
    lines.append("## Suggested Review Order\n")
    lines.append("1. `11-page2-overview.md` — Start here (curated summary)")
    lines.append("2. This index — verify the big picture")
    lines.append("3. `01-fundamentals.md` → `04-power-domains.md` → `05-political-spectrums.md`")
    lines.append("4. `06a` → `06b` → `06c` (progressivism deep-dive)")
    lines.append("5. `07-education.md`")
    lines.append("6. Remaining files as needed")
    lines.append("")

    filepath.write_text('\n'.join(lines), encoding='utf-8')


def main():
    print("Extracting XML from HTML...")
    xml_str = extract_xml_from_html(SOURCE)
    print(f"  XML length: {len(xml_str):,} chars")

    print("Parsing diagrams...")
    pages = parse_diagrams(xml_str)
    for i, page in enumerate(pages):
        print(f"  Page {i+1} ({page['name']}): {len(page['cells'])} cells, {len(page['edges'])} edges")

    print("Assigning clusters...")
    clusters = assign_clusters(pages)

    edges_p1 = clusters.pop('_edges_0', [])
    edges_p2 = clusters.pop('_edges_1', [])
    cells_by_id_p1 = clusters.pop('_cells_by_id_0', {})
    cells_by_id_p2 = clusters.pop('_cells_by_id_1', {})

    print("\nCluster sizes:")
    total = 0
    active_clusters = []
    for cid, cells in sorted(clusters.items()):
        if cells:
            print(f"  {cid}: {len(cells)} cells")
            total += len(cells)
            active_clusters.append(cid)
    print(f"  TOTAL: {total} cells assigned")

    print("\nWriting markdown files...")
    for cid in active_clusters:
        count = write_cluster_file(cid, clusters[cid], clusters, edges_p1, edges_p2, cells_by_id_p1, cells_by_id_p2)
        info = CLUSTERS.get(cid, {})
        print(f"  {info.get('file', cid)}: {count} items")

    write_index(clusters, active_clusters)
    print(f"  00-index.md: written")

    print("\nDone!")


if __name__ == '__main__':
    main()
