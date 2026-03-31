#!/usr/bin/env python3
"""
Populate an Obsidian canvas with nodes from FUALL.drawio.html,
preserving spatial layout, swimlane groups, and edge connections.
Links each node to its corresponding raw note in the vault.
"""

import json
import re
import html
import xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict
import uuid

SOURCE = Path(__file__).parent.parent.parent / "FUALL.drawio.html"
VAULT = Path(__file__).parent.parent.parent
RAW_DIR = VAULT / "raw"

# One canvas per draw.io page
CANVAS_NAMES = {
    0: "Claude Work here.canvas",   # Page 1 — main knowledge map
    1: "Page 2 Overview.canvas",    # Page 2 — condensed overview
}

# Minimum node dimensions for readability
MIN_WIDTH = 200
MIN_HEIGHT = 60

# Cluster → color mapping (Obsidian canvas colors 1-6)
CLUSTER_COLORS = {
    "fundamentals": "3",    # yellow
    "values": "6",          # purple
    "power": "1",           # red
    "spectrums": "5",       # cyan
    "education": "4",       # green
    "prog_spectrum": "2",   # orange
    "prog_arguments": "2",  # orange
    "prog_notes": "2",      # orange
    "ethics": "6",          # purple
    "left_right": "2",      # orange
    "taxonomy": None,
    "drafts": None,
    "page2": "5",           # cyan
    "uncategorized": None,
}


# ── HTML / XML parsing (shared with export script) ────────────────────

def strip_html(text):
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
    content = html_path.read_text(encoding='utf-8')
    match = re.search(r'data-mxgraph="([^"]*)"', content)
    if not match:
        raise ValueError("Could not find data-mxgraph attribute")
    json_str = html.unescape(match.group(1))
    data = json.loads(json_str)
    return data.get("xml", "")


def parse_all_cells(xml_str):
    """Parse mxfile XML, return all cells and edges per page."""
    root = ET.fromstring(xml_str)
    pages = []

    for diagram in root.findall('.//diagram'):
        page_name = diagram.get('name', 'Unknown')
        cells = {}   # id → cell dict
        edges = []   # list of edge dicts

        for elem in diagram.iter():
            cell_id = elem.get('id')
            if cell_id is None:
                continue

            value = elem.get('value', '') or elem.get('label', '')
            style = elem.get('style', '')
            parent = elem.get('parent', '')

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
                edges.append({
                    'id': cell_id,
                    'source': source,
                    'target': target,
                    'label': strip_html(value),
                })

            cell = {
                'id': cell_id,
                'text': strip_html(value),
                'style': style,
                'parent': parent,
                'x': x, 'y': y, 'w': w, 'h': h,
                'is_edge': is_edge,
                'is_swimlane': is_swimlane,
                'is_vertex': is_vertex,
            }
            cells[cell_id] = cell

        pages.append({
            'name': page_name,
            'cells': cells,
            'edges': edges,
        })

    return pages


# ── Coordinate resolution ─────────────────────────────────────────────

def resolve_absolute_positions(cells):
    """Convert draw.io relative coordinates to absolute positions."""
    abs_pos = {}  # id → (abs_x, abs_y)

    def get_abs(cell_id, visited=None):
        if visited is None:
            visited = set()
        if cell_id in abs_pos:
            return abs_pos[cell_id]
        if cell_id in visited:
            return (0, 0)
        visited.add(cell_id)

        cell = cells.get(cell_id)
        if not cell:
            return (0, 0)

        parent_id = cell['parent']
        if parent_id in ('', '0', '1') or parent_id not in cells:
            abs_pos[cell_id] = (cell['x'], cell['y'])
            return abs_pos[cell_id]

        px, py = get_abs(parent_id, visited)
        ax = px + cell['x']
        ay = py + cell['y']
        abs_pos[cell_id] = (ax, ay)
        return (ax, ay)

    for cell_id in cells:
        get_abs(cell_id)

    return abs_pos


# ── Cell → file path mapping ──────────────────────────────────────────

def build_cell_to_filepath():
    """Scan vault raw notes and build cell-id → relative file path map."""
    mapping = {}
    for md_file in RAW_DIR.rglob('*.md'):
        try:
            head = md_file.read_text(encoding='utf-8')[:500]
            match = re.search(r'cell-id:\s*"([^"]+)"', head)
            if match:
                rel_path = str(md_file.relative_to(VAULT))
                mapping[match.group(1)] = rel_path
        except Exception:
            pass
    return mapping


# ── Edge side calculation ──────────────────────────────────────────────

def compute_edge_sides(src_x, src_y, src_w, src_h, tgt_x, tgt_y, tgt_w, tgt_h):
    """Determine best fromSide/toSide based on relative node positions."""
    src_cx = src_x + src_w / 2
    src_cy = src_y + src_h / 2
    tgt_cx = tgt_x + tgt_w / 2
    tgt_cy = tgt_y + tgt_h / 2

    dx = tgt_cx - src_cx
    dy = tgt_cy - src_cy

    if abs(dx) > abs(dy):
        # Horizontal relationship
        from_side = "right" if dx > 0 else "left"
        to_side = "left" if dx > 0 else "right"
    else:
        # Vertical relationship
        from_side = "bottom" if dy > 0 else "top"
        to_side = "top" if dy > 0 else "bottom"

    return from_side, to_side


# ── Cluster detection (simplified) ────────────────────────────────────

SWIMLANE_CLUSTER = {
    "outline": "fundamentals", "wisdom": "values",
    "defining wisdom": "values", "core values": "values",
    "beauty": "values", "love": "values", "sin": "values",
    "spirit": "values", "soul": "values", "value tensions": "values",
    "ethics": "ethics", "golden mean": "ethics",
    "god": "fundamentals", "reality": "fundamentals",
    "quotes": "fundamentals", "history": "fundamentals",
    "mythos": "fundamentals", "domains of power": "power",
    "power structures": "power", "currently failing": "power",
    "aims of power": "spectrums", "pvc spectrum": "prog_spectrum",
    "lva spectrum": "spectrums", "what is the spectrum": "spectrums",
    "terminology": "left_right", "progressive": "prog_spectrum",
    "conservative": "prog_spectrum", "progressivism": "prog_spectrum",
    "progressivism vs conservatism": "prog_arguments",
    "progressive-conservative": "prog_spectrum",
    "short": "prog_spectrum", "long": "prog_spectrum",
    "telos": "prog_spectrum", "trials": "prog_spectrum",
    "tragedy": "prog_spectrum", "tensions": "prog_spectrum",
    "notes: conservatism": "prog_notes", "notes: progressivism": "prog_notes",
    "notes: power": "prog_notes", "notes: sorting": "prog_notes",
    "notes: fuall": "drafts", "random notes": "drafts",
    "education": "education", "academy": "education",
    "guilds": "education", "temple": "education",
    "news": "education", "agora": "education",
    "laboratory": "education", "educational domains": "education",
    "old": "taxonomy", "drafts": "drafts",
    "fundamentals": "page2", "on power and politics": "page2",
    "4 domains of power": "page2", "politics": "page2",
    "progressive - conservative": "page2",
    "uncertainty around left and right": "page2",
    "terms": "page2", "simple": "page2",
    "tradition": "page2", "tragedies": "page2",
}


def get_cluster_for_cell(cell, cells):
    """Walk parent chain to find cluster via swimlane."""
    current_id = cell['id']
    visited = set()
    while current_id and current_id not in ('0', '1') and current_id not in visited:
        visited.add(current_id)
        c = cells.get(current_id)
        if not c:
            break
        if c['is_swimlane'] and c['text']:
            text_lower = c['text'].lower().strip()
            text_lower = re.sub(r'font style.*?>', '', text_lower).strip()
            for key, cluster in SWIMLANE_CLUSTER.items():
                if key == text_lower or text_lower.startswith(key):
                    return cluster
        current_id = c.get('parent', '')
    return None


# ── Canvas builder ─────────────────────────────────────────────────────

def build_canvas_for_page(page, cell_to_filepath):
    """Build Obsidian canvas JSON from a single draw.io page."""
    canvas_nodes = []
    canvas_edges = []
    node_id_set = set()

    cells = page['cells']
    edges = page['edges']

    # Resolve absolute positions
    abs_pos = resolve_absolute_positions(cells)

    # First pass: collect IDs that edges need so we can include empty cells
    edge_endpoint_ids = set()
    for edge in edges:
        edge_endpoint_ids.add(edge['source'])
        edge_endpoint_ids.add(edge['target'])

    # Build nodes (skip root cells 0, 1 and edges)
    for cell_id, cell in cells.items():
        if cell_id in ('0', '1'):
            continue
        if cell['is_edge']:
            continue

        has_content = bool(cell['text']) or cell['is_swimlane']
        needed_by_edge = cell_id in edge_endpoint_ids

        if not has_content and not needed_by_edge:
            continue

        abs_x, abs_y = abs_pos.get(cell_id, (cell['x'], cell['y']))
        w = max(cell['w'], MIN_WIDTH)
        h = max(cell['h'], MIN_HEIGHT)

        node = {
            'id': cell_id,
            'x': int(abs_x),
            'y': int(abs_y),
            'width': int(w),
            'height': int(h),
        }

        if cell['is_swimlane']:
            node['type'] = 'group'
            node['label'] = cell['text'] or 'Group'
            cluster = get_cluster_for_cell(cell, cells)
            color = CLUSTER_COLORS.get(cluster) if cluster else None
            if color:
                node['color'] = color

        elif cell_id in cell_to_filepath:
            node['type'] = 'file'
            node['file'] = cell_to_filepath[cell_id]
            cluster = get_cluster_for_cell(cell, cells)
            color = CLUSTER_COLORS.get(cluster) if cluster else None
            if color:
                node['color'] = color

        else:
            text = cell['text'] if cell['text'] else '(empty)'
            if len(text) > 500:
                text = text[:500] + '...'
            node['type'] = 'text'
            node['text'] = text

        canvas_nodes.append(node)
        node_id_set.add(cell_id)

    # Process edges
    for edge in edges:
        src_id = edge['source']
        tgt_id = edge['target']

        if src_id not in node_id_set or tgt_id not in node_id_set:
            continue

        src_cell = cells.get(src_id, {})
        tgt_cell = cells.get(tgt_id, {})
        src_ax, src_ay = abs_pos.get(src_id, (0, 0))
        tgt_ax, tgt_ay = abs_pos.get(tgt_id, (0, 0))

        from_side, to_side = compute_edge_sides(
            src_ax, src_ay, max(src_cell.get('w', 0), MIN_WIDTH), max(src_cell.get('h', 0), MIN_HEIGHT),
            tgt_ax, tgt_ay, max(tgt_cell.get('w', 0), MIN_WIDTH), max(tgt_cell.get('h', 0), MIN_HEIGHT),
        )

        canvas_edge = {
            'id': edge['id'],
            'fromNode': src_id,
            'fromSide': from_side,
            'toNode': tgt_id,
            'toSide': to_side,
        }
        if edge.get('label'):
            canvas_edge['label'] = edge['label']

        canvas_edges.append(canvas_edge)

    return {'nodes': canvas_nodes, 'edges': canvas_edges}


# ── Main ──────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("FUALL Draw.io → Obsidian Canvases (one per page)")
    print("=" * 60)

    print("\n1. Parsing draw.io XML...")
    xml_str = extract_xml_from_html(SOURCE)
    pages = parse_all_cells(xml_str)
    for i, page in enumerate(pages):
        non_edge = sum(1 for c in page['cells'].values()
                       if c['id'] not in ('0', '1') and not c['is_edge'])
        print(f"   Page {i+1} ({page['name']}): {non_edge} cells, {len(page['edges'])} edges")

    print("\n2. Building cell → file path mapping...")
    cell_to_filepath = build_cell_to_filepath()
    print(f"   Mapped {len(cell_to_filepath)} cells to vault notes")

    for page_idx, page in enumerate(pages):
        canvas_name = CANVAS_NAMES.get(page_idx, f"Page {page_idx + 1}.canvas")
        canvas_path = VAULT / canvas_name

        print(f"\n3.{page_idx+1}. Building canvas for {page['name']}...")
        canvas = build_canvas_for_page(page, cell_to_filepath)

        groups = sum(1 for n in canvas['nodes'] if n['type'] == 'group')
        files = sum(1 for n in canvas['nodes'] if n['type'] == 'file')
        texts = sum(1 for n in canvas['nodes'] if n['type'] == 'text')
        print(f"   {len(canvas['nodes'])} nodes ({groups} groups, {files} file links, {texts} text)")
        print(f"   {len(canvas['edges'])} edges")

        canvas_path.write_text(json.dumps(canvas, indent=2, ensure_ascii=False), encoding='utf-8')
        size_kb = canvas_path.stat().st_size / 1024
        print(f"   → {canvas_name} ({size_kb:.1f} KB)")

    print("\n" + "=" * 60)
    print("Done! Two canvases written to the vault.")
    print("=" * 60)


if __name__ == '__main__':
    main()
