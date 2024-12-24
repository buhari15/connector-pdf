from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A0, A1, A2, A3
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors


class PDFElement:
    def draw(self, c: canvas.Canvas):
        raise NotImplementedError("To be added")