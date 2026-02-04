#!/usr/bin/env python3
"""
Convert Markdown to PDF using reportlab
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfgen import canvas
import sys

def create_pdf(input_file, output_file):
    """Create PDF from markdown text file"""

    # Read the markdown file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create PDF
    doc = SimpleDocTemplate(
        output_file,
        pagesize=A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    # Container for the 'Flowable' objects
    elements = []

    # Define styles
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='#1a1a1a',
        spaceAfter=30,
        alignment=TA_CENTER
    )

    heading1_style = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        fontSize=16,
        textColor='#1a1a1a',
        spaceAfter=12,
        spaceBefore=12
    )

    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor='#333333',
        spaceAfter=10,
        spaceBefore=10
    )

    code_style = ParagraphStyle(
        'Code',
        parent=styles['Code'],
        fontSize=7,
        fontName='Courier',
        leftIndent=20,
        rightIndent=20,
        spaceAfter=10
    )

    # Split content into lines
    lines = content.split('\n')

    in_code_block = False
    code_buffer = []

    for line in lines:
        # Handle code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                # End of code block
                code_text = '\n'.join(code_buffer)
                pre = Preformatted(code_text, code_style)
                elements.append(pre)
                elements.append(Spacer(1, 0.2*inch))
                code_buffer = []
                in_code_block = False
            else:
                # Start of code block
                in_code_block = True
            continue

        if in_code_block:
            code_buffer.append(line)
            continue

        # Handle headings
        if line.startswith('# '):
            if len(elements) > 0:
                elements.append(PageBreak())
            title = line[2:].strip()
            elements.append(Paragraph(title, title_style))
            elements.append(Spacer(1, 0.3*inch))
        elif line.startswith('## '):
            heading = line[3:].strip()
            elements.append(Paragraph(heading, heading1_style))
        elif line.startswith('### '):
            heading = line[4:].strip()
            elements.append(Paragraph(heading, heading2_style))
        elif line.strip().startswith('═══'):
            elements.append(Spacer(1, 0.2*inch))
        elif line.strip().startswith('---'):
            elements.append(Spacer(1, 0.2*inch))
        elif line.strip():
            # Regular paragraph
            # Escape special characters for reportlab
            text = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            elements.append(Paragraph(text, styles['Normal']))
            elements.append(Spacer(1, 0.1*inch))
        else:
            # Empty line
            elements.append(Spacer(1, 0.1*inch))

    # Build PDF
    doc.build(elements)
    print(f"PDF created successfully: {output_file}")

if __name__ == "__main__":
    input_file = r"C:\Users\satyans\Claude workspace\D365-Contact-Center-Architecture-Map.md"
    output_file = r"C:\Users\satyans\Claude workspace\D365-Contact-Center-Architecture-Map.pdf"

    try:
        create_pdf(input_file, output_file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
