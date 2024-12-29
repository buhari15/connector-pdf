from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

output_path = "/Users/buhariabubakar/Desktop/Projects/PDFGen/test_output.pdf"  # Adjust this path to an accessible location

doc = SimpleDocTemplate(output_path, pagesize=A4)
styles = getSampleStyleSheet()
story = [Paragraph("This is a test PDF.", styles['Normal'])]

try:
    doc.build(story)
    print(f"PDF generated at {output_path}")
except Exception as e:
    print(f"Error generating PDF: {e}")
