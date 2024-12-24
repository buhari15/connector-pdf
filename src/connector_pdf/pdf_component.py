from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A0, A1, A2, A3
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors


class PDFComponent:
    """Base class for PDF components."""

    def draw(self, pdf: canvas.Canvas):
        """Draw the component on the canvas. Must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement the draw method.")