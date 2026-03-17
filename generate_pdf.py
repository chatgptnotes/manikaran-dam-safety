"""
Generate a professional PDF from the Dam Safety Startup Complete Plan markdown file.
Uses markdown -> HTML -> styled HTML file, then reportlab for PDF generation.
"""

import markdown
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib import colors

# ── Paths ──
INPUT_MD = os.path.join(os.path.dirname(__file__), "Dam_Safety_Startup_Complete_Plan.md")
OUTPUT_PDF = os.path.join(os.path.dirname(__file__), "Dam_Safety_Startup_Complete_Plan.pdf")
OUTPUT_HTML = os.path.join(os.path.dirname(__file__), "Dam_Safety_Startup_Complete_Plan.html")

# ── Read markdown ──
with open(INPUT_MD, "r", encoding="utf-8") as f:
    md_text = f.read()

# ── Generate standalone HTML (bonus: user can also open this in browser) ──
html_body = markdown.markdown(md_text, extensions=["tables", "fenced_code", "toc"])

html_full = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dam Safety Compliance Platform — Complete Startup Plan</title>
<style>
  @page {{ size: A4; margin: 20mm; }}
  body {{
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #1a1a1a;
    max-width: 210mm;
    margin: 0 auto;
    padding: 20mm;
    background: #fff;
  }}
  h1 {{
    color: #1a3c6e;
    font-size: 22pt;
    border-bottom: 3px solid #1a3c6e;
    padding-bottom: 8px;
    margin-top: 40px;
    page-break-before: auto;
  }}
  h1:first-of-type {{
    font-size: 28pt;
    text-align: center;
    border-bottom: none;
    margin-top: 0;
  }}
  h2 {{
    color: #2a5a9e;
    font-size: 16pt;
    margin-top: 30px;
    border-bottom: 1px solid #ccc;
    padding-bottom: 4px;
  }}
  h3 {{
    color: #3a6ab5;
    font-size: 13pt;
    margin-top: 20px;
  }}
  table {{
    border-collapse: collapse;
    width: 100%;
    margin: 15px 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
  }}
  th {{
    background-color: #1a3c6e;
    color: white;
    padding: 8px 10px;
    text-align: left;
    font-weight: 600;
  }}
  td {{
    padding: 6px 10px;
    border: 1px solid #ddd;
    vertical-align: top;
  }}
  tr:nth-child(even) {{
    background-color: #f5f7fa;
  }}
  tr:hover {{
    background-color: #e8edf5;
  }}
  strong {{
    color: #1a3c6e;
  }}
  code {{
    background: #f0f2f5;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 9.5pt;
    font-family: 'Consolas', 'Courier New', monospace;
  }}
  pre {{
    background: #1e2330;
    color: #e0e0e0;
    padding: 15px;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 9pt;
    line-height: 1.4;
    page-break-inside: avoid;
  }}
  pre code {{
    background: none;
    padding: 0;
    color: #e0e0e0;
  }}
  blockquote {{
    border-left: 4px solid #2a5a9e;
    margin: 15px 0;
    padding: 10px 20px;
    background: #f0f4fa;
    color: #333;
  }}
  hr {{
    border: none;
    border-top: 2px solid #1a3c6e;
    margin: 30px 0;
  }}
  a {{
    color: #2a5a9e;
    text-decoration: none;
  }}
  .cover-meta {{
    text-align: center;
    color: #555;
    font-size: 11pt;
    margin-bottom: 40px;
  }}
  @media print {{
    body {{ padding: 0; }}
    h1 {{ page-break-before: always; }}
    h1:first-of-type {{ page-break-before: avoid; }}
    table {{ font-size: 8.5pt; }}
    pre {{ font-size: 8pt; }}
  }}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_full)
print(f"HTML generated: {OUTPUT_HTML}")

# ── Generate PDF using reportlab ──
# Parse the markdown into sections and render with reportlab

BLUE_DARK = HexColor("#1a3c6e")
BLUE_MED = HexColor("#2a5a9e")
BLUE_LIGHT = HexColor("#3a6ab5")
GREY_BG = HexColor("#f5f7fa")
GREY_BORDER = HexColor("#cccccc")
WHITE = HexColor("#ffffff")

styles = getSampleStyleSheet()

# Custom styles
styles.add(ParagraphStyle(
    "CustomTitle", parent=styles["Title"],
    fontSize=24, textColor=BLUE_DARK, spaceAfter=6,
    alignment=TA_CENTER, fontName="Helvetica-Bold"
))
styles.add(ParagraphStyle(
    "Subtitle", parent=styles["Normal"],
    fontSize=12, textColor=HexColor("#555555"),
    alignment=TA_CENTER, spaceAfter=30
))
styles.add(ParagraphStyle(
    "H1", parent=styles["Heading1"],
    fontSize=18, textColor=BLUE_DARK, spaceBefore=24, spaceAfter=10,
    fontName="Helvetica-Bold", borderWidth=0,
    borderColor=BLUE_DARK, borderPadding=4
))
styles.add(ParagraphStyle(
    "H2", parent=styles["Heading2"],
    fontSize=14, textColor=BLUE_MED, spaceBefore=18, spaceAfter=8,
    fontName="Helvetica-Bold"
))
styles.add(ParagraphStyle(
    "H3", parent=styles["Heading3"],
    fontSize=12, textColor=BLUE_LIGHT, spaceBefore=14, spaceAfter=6,
    fontName="Helvetica-Bold"
))
styles.add(ParagraphStyle(
    "BodyText2", parent=styles["BodyText"],
    fontSize=10, leading=14, alignment=TA_LEFT,
    spaceAfter=6, fontName="Helvetica"
))
styles.add(ParagraphStyle(
    "BulletItem", parent=styles["BodyText"],
    fontSize=10, leading=14, leftIndent=20,
    bulletIndent=10, spaceAfter=3
))
styles.add(ParagraphStyle(
    "CodeBlock", parent=styles["Code"],
    fontSize=8, leading=10, fontName="Courier",
    backColor=HexColor("#f0f2f5"), borderWidth=0.5,
    borderColor=GREY_BORDER, borderPadding=8,
    spaceBefore=6, spaceAfter=6
))
styles.add(ParagraphStyle(
    "TableCell", parent=styles["Normal"],
    fontSize=8.5, leading=11, fontName="Helvetica"
))
styles.add(ParagraphStyle(
    "TableHeader", parent=styles["Normal"],
    fontSize=8.5, leading=11, fontName="Helvetica-Bold",
    textColor=WHITE
))
styles.add(ParagraphStyle(
    "TableCellBold", parent=styles["Normal"],
    fontSize=8.5, leading=11, fontName="Helvetica-Bold"
))

def make_table(headers, rows, col_widths=None):
    """Create a styled reportlab table from headers and row data."""
    # Build table data with Paragraphs for text wrapping
    table_data = []
    header_row = [Paragraph(h, styles["TableHeader"]) for h in headers]
    table_data.append(header_row)

    for row in rows:
        cells = []
        for i, cell in enumerate(row):
            cell_text = str(cell).strip()
            if cell_text.startswith("**") and cell_text.endswith("**"):
                cell_text = cell_text[2:-2]
                cells.append(Paragraph(cell_text, styles["TableCellBold"]))
            else:
                cells.append(Paragraph(cell_text, styles["TableCell"]))
        table_data.append(cells)

    if col_widths:
        t = Table(table_data, colWidths=col_widths, repeatRows=1)
    else:
        t = Table(table_data, repeatRows=1)

    style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLUE_DARK),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 9),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 8.5),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 5),
        ("TOPPADDING", (0, 1), (-1, -1), 5),
        ("GRID", (0, 0), (-1, -1), 0.5, GREY_BORDER),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, GREY_BG]),
    ])
    t.setStyle(style)
    return t


def parse_md_table(lines, start_idx):
    """Parse a markdown table starting at start_idx. Returns (headers, rows, end_idx)."""
    headers = [h.strip() for h in lines[start_idx].strip("|").split("|")]
    # Skip separator line
    row_idx = start_idx + 2
    rows = []
    while row_idx < len(lines) and "|" in lines[row_idx] and lines[row_idx].strip():
        row = [c.strip() for c in lines[row_idx].strip("|").split("|")]
        rows.append(row)
        row_idx += 1
    return headers, rows, row_idx


def build_story(md_text):
    """Convert markdown text into a list of reportlab flowables."""
    story = []
    lines = md_text.split("\n")
    i = 0
    in_code_block = False
    code_buffer = []

    # Title page
    story.append(Spacer(1, 60))
    story.append(Paragraph("Dam Safety Compliance Platform", styles["CustomTitle"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Complete Startup Plan", styles["CustomTitle"]))
    story.append(Spacer(1, 20))
    story.append(Paragraph(
        "An Independent Venture for Affordable Dam Monitoring<br/>"
        "&amp; Regulatory Compliance in India",
        styles["Subtitle"]
    ))
    story.append(Spacer(1, 30))
    story.append(Paragraph("March 2026 &nbsp;|&nbsp; Version 2.0", styles["Subtitle"]))
    story.append(Spacer(1, 20))
    story.append(HRFlowable(width="60%", thickness=2, color=BLUE_DARK))
    story.append(Spacer(1, 20))
    story.append(Paragraph(
        "Featuring complete sensor price comparison:<br/>"
        "Chinese manufacturers vs. Geokon (USA) vs. Encardio Rite (India)<br/>"
        "with 50-80% cost savings via import-assemble-sell model",
        ParagraphStyle("CoverNote", parent=styles["Normal"],
                       fontSize=11, alignment=TA_CENTER, textColor=HexColor("#666666"),
                       leading=16)
    ))
    story.append(PageBreak())

    # Skip the first few lines (title and subtitle already rendered)
    # Find where actual content starts after the first ---
    while i < len(lines):
        line = lines[i].strip()
        if line == "---":
            i += 1
            break
        i += 1

    # Skip table of contents section
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("# 1.") or line.startswith("# 1 "):
            break
        i += 1

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Code blocks
        if stripped.startswith("```"):
            if in_code_block:
                code_text = "\n".join(code_buffer)
                story.append(Paragraph(
                    code_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br/>"),
                    styles["CodeBlock"]
                ))
                code_buffer = []
                in_code_block = False
            else:
                in_code_block = True
                code_buffer = []
            i += 1
            continue

        if in_code_block:
            code_buffer.append(line.rstrip())
            i += 1
            continue

        # Empty lines
        if not stripped:
            i += 1
            continue

        # H1
        if stripped.startswith("# ") and not stripped.startswith("## "):
            text = stripped[2:].strip()
            story.append(PageBreak())
            story.append(Paragraph(text, styles["H1"]))
            story.append(HRFlowable(width="100%", thickness=1.5, color=BLUE_DARK))
            story.append(Spacer(1, 6))
            i += 1
            continue

        # H2
        if stripped.startswith("## "):
            text = stripped[3:].strip()
            story.append(Spacer(1, 8))
            story.append(Paragraph(text, styles["H2"]))
            i += 1
            continue

        # H3
        if stripped.startswith("### "):
            text = stripped[4:].strip()
            story.append(Paragraph(text, styles["H3"]))
            i += 1
            continue

        # HR
        if stripped == "---":
            story.append(Spacer(1, 6))
            story.append(HRFlowable(width="100%", thickness=1, color=GREY_BORDER))
            story.append(Spacer(1, 6))
            i += 1
            continue

        # Tables
        if "|" in stripped and stripped.startswith("|"):
            # Check if next line is separator
            if i + 1 < len(lines) and "---" in lines[i + 1]:
                headers, rows, end_idx = parse_md_table(lines, i)
                if headers and rows:
                    t = make_table(headers, rows)
                    story.append(Spacer(1, 4))
                    story.append(t)
                    story.append(Spacer(1, 4))
                i = end_idx
                continue

        # Bullet points
        if stripped.startswith("- ") or stripped.startswith("* "):
            text = stripped[2:].strip()
            text = format_inline(text)
            story.append(Paragraph(f"• {text}", styles["BulletItem"]))
            i += 1
            continue

        # Numbered lists
        if len(stripped) > 2 and stripped[0].isdigit() and stripped[1] in ".)" or (len(stripped) > 3 and stripped[:2].isdigit() and stripped[2] in ".)"):
            # Find the text after the number
            dot_pos = stripped.find(".")
            if dot_pos > 0 and dot_pos < 4:
                text = stripped[dot_pos+1:].strip()
                num = stripped[:dot_pos]
                text = format_inline(text)
                story.append(Paragraph(f"{num}. {text}", styles["BulletItem"]))
                i += 1
                continue

        # Blockquotes
        if stripped.startswith("> "):
            text = stripped[2:].strip()
            text = format_inline(text)
            story.append(Paragraph(
                text,
                ParagraphStyle("Quote", parent=styles["BodyText2"],
                               leftIndent=20, borderWidth=0, textColor=HexColor("#444444"),
                               fontSize=10, fontName="Helvetica-Oblique")
            ))
            i += 1
            continue

        # Regular paragraphs
        text = format_inline(stripped)
        if text:
            story.append(Paragraph(text, styles["BodyText2"]))
        i += 1

    return story


def format_inline(text):
    """Convert markdown inline formatting to reportlab XML."""
    import re
    # Bold: **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Italic: *text*
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    # Inline code: `text`
    text = re.sub(r'`(.+?)`', r'<font face="Courier" size="8">\1</font>', text)
    # Links: [text](url) -> just text
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    return text


def header_footer(canvas, doc):
    """Add header and footer to each page."""
    canvas.saveState()
    page_num = canvas.getPageNumber()

    # Footer
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(HexColor("#888888"))
    canvas.drawString(20*mm, 10*mm, "Dam Safety Compliance Platform — Startup Plan")
    canvas.drawRightString(A4[0] - 20*mm, 10*mm, f"Page {page_num}")

    # Header line (except page 1)
    if page_num > 1:
        canvas.setStrokeColor(HexColor("#e0e0e0"))
        canvas.setLineWidth(0.5)
        canvas.line(20*mm, A4[1] - 15*mm, A4[0] - 20*mm, A4[1] - 15*mm)

    # Footer line
    canvas.line(20*mm, 14*mm, A4[0] - 20*mm, 14*mm)

    canvas.restoreState()


# Build the PDF
doc = SimpleDocTemplate(
    OUTPUT_PDF,
    pagesize=A4,
    leftMargin=20*mm,
    rightMargin=20*mm,
    topMargin=20*mm,
    bottomMargin=20*mm,
    title="Dam Safety Compliance Platform - Complete Startup Plan",
    author="Dam Safety Startup"
)

print("Parsing markdown...")
story = build_story(md_text)

print("Generating PDF...")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)

print(f"PDF generated: {OUTPUT_PDF}")
print(f"HTML generated: {OUTPUT_HTML}")
print("Done!")
