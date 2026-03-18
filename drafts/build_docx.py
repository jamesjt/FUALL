#!/usr/bin/env python3
"""Generate docx from the draft article markdown files."""
import re
from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

ARTICLES_DIR = Path(__file__).parent.parent / "tasks" / "knowledge-map" / "reorg" / "articles"
OUTPUT = Path(__file__).parent / "Foundations_Draft.docx"

def add_formatted_paragraph(doc, text, style='Normal'):
    p = doc.add_paragraph(style=style)
    # Handle basic markdown emphasis
    parts = re.split(r'(\*\*.*?\*\*|\*.*?\*|_.*?_)', text)
    for part in parts:
        if part.startswith('**') and part.endswith('**'):
            run = p.add_run(part[2:-2])
            run.bold = True
        elif (part.startswith('*') and part.endswith('*')) or (part.startswith('_') and part.endswith('_')):
            run = p.add_run(part[1:-1])
            run.italic = True
        else:
            p.add_run(part)
    return p

def process_markdown(doc, md_path):
    text = md_path.read_text(encoding='utf-8')
    lines = text.split('\n')
    in_blockquote = False
    blockquote_lines = []

    for line in lines:
        stripped = line.strip()

        # Skip the "Next:" link
        if stripped.startswith('*Next:'):
            continue

        # Headings
        if stripped.startswith('# ') and not stripped.startswith('## '):
            title = stripped[2:]
            p = doc.add_heading(title, level=0)
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            # Add byline
            byline = doc.add_paragraph('By Zzy')
            byline.style = doc.styles['Subtitle']
            byline.runs[0].font.color.rgb = RGBColor(0x99, 0x99, 0x99)
            # Add draft notice
            draft = doc.add_paragraph('DRAFT — Under review')
            draft.runs[0].font.color.rgb = RGBColor(0xD2, 0x9A, 0x38)
            draft.runs[0].font.size = Pt(9)
            doc.add_paragraph('')
            continue

        if stripped.startswith('## '):
            # Flush blockquote
            if blockquote_lines:
                bq_text = ' '.join(blockquote_lines)
                p = doc.add_paragraph(bq_text, style='Intense Quote')
                blockquote_lines = []
                in_blockquote = False
            doc.add_heading(stripped[3:], level=2)
            continue

        # Blockquotes
        if stripped.startswith('>'):
            in_blockquote = True
            blockquote_lines.append(stripped[1:].strip())
            continue
        elif in_blockquote and stripped:
            # Continuation of blockquote? No, flush it
            bq_text = ' '.join(blockquote_lines)
            p = doc.add_paragraph(bq_text, style='Intense Quote')
            blockquote_lines = []
            in_blockquote = False

        if in_blockquote and not stripped:
            bq_text = ' '.join(blockquote_lines)
            p = doc.add_paragraph(bq_text, style='Intense Quote')
            blockquote_lines = []
            in_blockquote = False
            continue

        # List items
        if stripped.startswith('- '):
            add_formatted_paragraph(doc, stripped[2:], style='List Bullet')
            continue

        # Empty lines
        if not stripped:
            continue

        # Regular paragraphs
        add_formatted_paragraph(doc, stripped)


def main():
    doc = Document()

    # Style the document
    style = doc.styles['Normal']
    style.font.name = 'Georgia'
    style.font.size = Pt(11)
    style.paragraph_format.space_after = Pt(8)
    style.paragraph_format.line_spacing = 1.5

    h0_style = doc.styles['Title']
    h0_style.font.color.rgb = RGBColor(0xD2, 0x9A, 0x38)

    h2_style = doc.styles['Heading 2']
    h2_style.font.size = Pt(14)

    # Set margins
    for section in doc.sections:
        section.left_margin = Inches(1.2)
        section.right_margin = Inches(1.2)
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)

    # Process articles in order
    articles = sorted(ARTICLES_DIR.glob('*.md'))
    for article_path in articles:
        process_markdown(doc, article_path)

    doc.save(str(OUTPUT))
    print(f"Generated: {OUTPUT}")


if __name__ == '__main__':
    main()
