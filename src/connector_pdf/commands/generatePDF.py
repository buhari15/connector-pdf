from connector_pdf.pdf_component import PDFComponent
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


class PDFGenerator:
    """Class for managing and generating the final PDF."""

    def __init__(self, components: list[PDFComponent], output_path: str):
        self.components = components
        self.output_path = output_path

    def generate(self):
        pdf = canvas.Canvas(self.output_path, pagesize=A4)
        for component in self.components:
            component.draw(pdf)
        pdf.save()