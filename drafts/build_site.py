#!/usr/bin/env python3
"""Build the draft reading site from article markdown files."""
import re
import html as html_mod
from pathlib import Path

ARTICLES_DIR = Path(__file__).parent.parent / "tasks" / "knowledge-map" / "reorg" / "articles"
OUTPUT = Path(__file__).parent / "index.html"

# Article metadata: (filename, nav_label, section)
ARTICLES = [
    ("01-foundations.md", "Foundations", "The Core Chain"),
    ("02-erosion.md", "The Erosion Mechanism", "The Core Chain"),
    ("03-beauty.md", "Beauty", "The Core Chain"),
    ("04-power.md", "Power", "The Core Chain"),
    ("05-spectrums.md", "Left vs Right", "Political Spectrums"),
    ("05a-prog-con.md", "Progressive vs Conservative", "Political Spectrums"),
    ("05b-lib-auth.md", "Liberal vs Authoritarian", "Political Spectrums"),
    ("05c-collect-indiv.md", "Collectivism vs Individualism", "Political Spectrums"),
    ("06-education.md", "Education", "Institutions"),
    ("07-mission.md", "The Mission", "Institutions"),
]

def md_to_html(md_text):
    """Convert markdown to HTML. Simple but sufficient."""
    lines = md_text.split('\n')
    html_lines = []
    in_list = False
    in_table = False
    in_blockquote = False
    bq_lines = []

    def flush_bq():
        nonlocal in_blockquote, bq_lines
        if bq_lines:
            content = ' '.join(bq_lines)
            # Check for attribution
            if '— ' in content or '-- ' in content:
                parts = re.split(r'\s*[—–]\s*', content, 1)
                if len(parts) == 2:
                    html_lines.append(f'<blockquote>{inline(parts[0])}<span class="attribution">&mdash; {inline(parts[1])}</span></blockquote>')
                else:
                    html_lines.append(f'<blockquote>{inline(content)}</blockquote>')
            else:
                html_lines.append(f'<blockquote>{inline(content)}</blockquote>')
            bq_lines = []
        in_blockquote = False

    def inline(text):
        """Process inline markdown."""
        # Bold
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        # Italic
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        # Em dash
        text = text.replace(' -- ', ' &mdash; ')
        text = text.replace(' — ', ' &mdash; ')
        return text

    for line in lines:
        stripped = line.strip()

        # Skip "Next:" links - we handle navigation differently
        if stripped.startswith('*Next:'):
            continue

        # Blockquotes
        if stripped.startswith('>'):
            in_blockquote = True
            bq_lines.append(stripped[1:].strip())
            continue
        elif in_blockquote:
            if stripped:
                flush_bq()
            else:
                flush_bq()
                continue

        # Close lists
        if in_list and not stripped.startswith('- ') and not stripped.startswith('| '):
            if not stripped.startswith('  '):
                html_lines.append('</ul>')
                in_list = False

        # Close tables
        if in_table and not stripped.startswith('|'):
            html_lines.append('</tbody></table>')
            in_table = False

        # Headings
        if stripped.startswith('# ') and not stripped.startswith('## '):
            title = stripped[2:]
            html_lines.append(f'<h1>{html_mod.escape(title)}</h1>')
            html_lines.append('<div class="byline">By Zzy</div>')
            continue
        if stripped.startswith('## '):
            html_lines.append(f'<h2>{inline(html_mod.escape(stripped[3:]))}</h2>')
            continue
        if stripped.startswith('### '):
            html_lines.append(f'<h3>{inline(html_mod.escape(stripped[4:]))}</h3>')
            continue

        # Tables
        if stripped.startswith('|'):
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            if all(set(c) <= set('- :') for c in cells):
                # Header separator - skip
                continue
            if not in_table:
                in_table = True
                html_lines.append('<table><thead><tr>')
                for cell in cells:
                    html_lines.append(f'<th>{inline(html_mod.escape(cell))}</th>')
                html_lines.append('</tr></thead><tbody>')
            else:
                html_lines.append('<tr>')
                for cell in cells:
                    html_lines.append(f'<td>{inline(html_mod.escape(cell))}</td>')
                html_lines.append('</tr>')
            continue

        # List items
        if stripped.startswith('- '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            html_lines.append(f'<li>{inline(html_mod.escape(stripped[2:]))}</li>')
            continue

        # Empty lines
        if not stripped:
            continue

        # Regular paragraphs
        html_lines.append(f'<p>{inline(html_mod.escape(stripped))}</p>')

    # Flush any remaining state
    if in_blockquote:
        flush_bq()
    if in_list:
        html_lines.append('</ul>')
    if in_table:
        html_lines.append('</tbody></table>')

    return '\n            '.join(html_lines)


def build():
    # Read and convert all articles
    articles_html = {}
    for filename, label, section in ARTICLES:
        path = ARTICLES_DIR / filename
        if path.exists():
            md = path.read_text(encoding='utf-8')
            articles_html[filename] = {
                'html': md_to_html(md),
                'label': label,
                'section': section,
                'id': filename.replace('.md', '').replace('.', '-'),
                'exists': True,
            }
        else:
            articles_html[filename] = {
                'html': f'<h1>{label}</h1><div class="byline">By Zzy</div><p>Not yet drafted.</p>',
                'label': label,
                'section': section,
                'id': filename.replace('.md', '').replace('.', '-'),
                'exists': False,
            }

    # Build nav
    nav_items = []
    current_section = None
    for filename, label, section in ARTICLES:
        if section != current_section:
            nav_items.append(f'        <div class="section-label">{section}</div>')
            current_section = section
        art = articles_html[filename]
        status = 'draft' if art['exists'] else 'planned'
        active = ' class="active"' if filename == '01-foundations.md' else ''
        nav_items.append(f'        <a href="#{art["id"]}"{active} onclick="show(\'{art["id"]}\')"><span class="status {status}"></span>{label}</a>')

    # Build articles
    article_blocks = []
    first = True
    for filename, label, section in ARTICLES:
        art = articles_html[filename]
        active = ' class="active"' if first else ''
        banner = 'DRAFT &mdash; Under review' if art['exists'] else 'PLANNED &mdash; Not yet drafted'
        article_blocks.append(f'''        <article id="{art['id']}"{active}>
            <div class="draft-banner">{banner}</div>
            {art['html']}
        </article>''')
        first = False

    # Find next article for each
    # (handled by nav, not inline links)

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Foundational Understanding &mdash; Drafts</title>
    <link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,300..900;1,8..60,300..900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --gold-accent: #d29a38;
            --gold-hover: #b8862f;
            --gold-glow: rgba(210, 154, 56, 0.15);
            --surface: #1e1e1e;
            --border-subtle: rgba(255, 255, 255, 0.06);
            --font-serif: "Source Serif 4", ui-serif, Georgia, "Times New Roman", serif;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            background: #121212;
            color: #c1c1c1;
            font-family: var(--font-serif);
            font-optical-sizing: auto;
            line-height: 1.75;
            font-size: 18px;
        }}
        nav {{
            position: fixed; top: 0; left: 0; width: 250px; height: 100vh;
            background: var(--surface); border-right: 1px solid var(--border-subtle);
            padding: 24px 16px; overflow-y: auto; z-index: 100;
        }}
        nav h1 {{
            color: var(--gold-accent); font-size: 0.85em; font-weight: 600;
            letter-spacing: 0.04em; text-transform: uppercase; margin-bottom: 8px;
        }}
        nav .subtitle {{
            color: rgba(255,255,255,0.35); font-size: 0.75em;
            font-style: italic; margin-bottom: 24px; display: block;
        }}
        nav a {{
            display: block; color: #999; text-decoration: none;
            padding: 8px 12px; font-size: 0.85em; border-radius: 6px;
            transition: all 0.15s ease; margin-bottom: 2px;
        }}
        nav a:hover {{ color: #e0e0e0; background: rgba(255,255,255,0.04); }}
        nav a.active {{ color: var(--gold-accent); background: var(--gold-glow); }}
        nav .section-label {{
            color: rgba(255,255,255,0.25); font-size: 0.7em;
            text-transform: uppercase; letter-spacing: 0.08em; padding: 16px 12px 4px;
        }}
        .status {{
            display: inline-block; width: 8px; height: 8px;
            border-radius: 50%; margin-right: 6px;
        }}
        .status.draft {{ background: var(--gold-accent); }}
        .status.planned {{ background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.25); }}
        main {{
            margin-left: 250px; max-width: 720px;
            padding: 60px 40px 120px; margin-right: auto;
        }}
        article {{ display: none; }}
        article.active {{ display: block; }}
        article h1 {{
            color: var(--gold-accent); font-size: 2em; font-weight: 700;
            margin-bottom: 8px; line-height: 1.2;
        }}
        .byline {{
            color: rgba(255,255,255,0.3); font-size: 0.85em;
            font-style: italic; margin-bottom: 40px;
        }}
        article h2 {{
            color: #e0e0e0; font-size: 1.35em; font-weight: 600;
            margin-top: 48px; margin-bottom: 16px;
        }}
        article h3 {{
            color: #d0d0d0; font-size: 1.1em; font-weight: 600;
            margin-top: 32px; margin-bottom: 12px;
        }}
        article p {{ margin-bottom: 20px; }}
        article blockquote {{
            border-left: 3px solid var(--gold-accent);
            padding: 12px 20px; margin: 24px 0; color: #aaa;
            font-style: italic; background: rgba(210, 154, 56, 0.04);
            border-radius: 0 6px 6px 0;
        }}
        blockquote .attribution {{
            display: block; margin-top: 8px; font-style: normal;
            color: var(--gold-accent); font-size: 0.85em;
        }}
        article ul, article ol {{ margin: 16px 0 20px 24px; color: #b0b0b0; }}
        article li {{ margin-bottom: 8px; }}
        article em {{ color: #d0d0d0; }}
        article strong {{ color: #e0e0e0; font-weight: 600; }}
        article table {{
            width: 100%; border-collapse: collapse; margin: 20px 0;
            font-size: 0.9em;
        }}
        article th {{
            text-align: left; padding: 10px 12px; border-bottom: 2px solid var(--gold-accent);
            color: var(--gold-accent); font-weight: 600;
        }}
        article td {{
            padding: 8px 12px; border-bottom: 1px solid var(--border-subtle); color: #b0b0b0;
        }}
        .draft-banner {{
            background: rgba(210, 154, 56, 0.08);
            border: 1px solid rgba(210, 154, 56, 0.2);
            border-radius: 8px; padding: 12px 16px; margin-bottom: 40px;
            font-size: 0.8em; color: rgba(210, 154, 56, 0.7);
        }}
        @media (max-width: 768px) {{
            nav {{ position: static; width: 100%; height: auto; border-right: none; border-bottom: 1px solid var(--border-subtle); }}
            main {{ margin-left: 0; padding: 24px 20px 80px; }}
        }}
    </style>
</head>
<body>
    <nav>
        <h1>Foundational Understanding</h1>
        <span class="subtitle">Draft Articles</span>
{chr(10).join(nav_items)}
    </nav>
    <main>
{chr(10).join(article_blocks)}
    </main>
    <script>
        function show(id) {{
            document.querySelectorAll('article').forEach(a => a.classList.remove('active'));
            document.querySelectorAll('nav a').forEach(a => a.classList.remove('active'));
            const article = document.getElementById(id);
            if (article) article.classList.add('active');
            const link = document.querySelector(`nav a[href="#${{id}}"]`);
            if (link) link.classList.add('active');
            window.scrollTo(0, 0);
        }}
        if (window.location.hash) show(window.location.hash.slice(1));
    </script>
</body>
</html>'''

    OUTPUT.write_text(page, encoding='utf-8')
    print(f"Generated: {OUTPUT}")
    print(f"Articles: {sum(1 for f,_,_ in ARTICLES if (ARTICLES_DIR/f).exists())}/{len(ARTICLES)} drafted")


if __name__ == '__main__':
    build()
