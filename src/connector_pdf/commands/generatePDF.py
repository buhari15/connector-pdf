from connector_pdf.pdf_component import PDFComponent
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


class PDFGenerator:
    """Class for managing and generating the final PDF."""

    def __init__(self, output_path: str):
        self.output_path = output_path
        self.pdf = canvas.Canvas(self.output_path, pagesize=A4)

    
    def add_text(self, text: str, x:float, y:float, font="Helvetica", size=12):
        self.pdf.setFont(font, size)
        self.pdf.drawString(x, y, text)


    def generate(self):
        # pdf = canvas.Canvas(self.output_path, pagesize=A4)
        # for component in self.components:
        #     component.draw(pdf)
        self.pdf.save()