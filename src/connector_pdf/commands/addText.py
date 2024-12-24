from connector_pdf.pdf_component import PDFComponent
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from typing import Any

from spiffworkflow_connector_command.command_interface import CommandErrorDict
from spiffworkflow_connector_command.command_interface import CommandResponseDict
from spiffworkflow_connector_command.command_interface import ConnectorCommand
from spiffworkflow_connector_command.command_interface import ConnectorProxyResponseDict


class PDFText(PDFComponent):
    """Class for adding text to the PDF."""

    def __init__(self, text: str, x: float, y: float, font="Helvetica", size=12):
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.size = size

    def draw(self, pdf: canvas.Canvas):
        pdf.setFont(self.font, self.size)
        pdf.drawString(self.x, self.y, self.text)

        # error: CommandErrorDict | None = None
     

        # return_response: CommandResponseDict = {
        #     "body": {
        #         "connector_response": f"You passed the example connector: '{self.message}'. Have a good day!",
        #     },
        #     "mimetype": "application/json",
        # }

        # result: ConnectorProxyResponseDict = {
        #     "command_response": return_response,
        #     "error": error,
        #     "command_response_version": 2,
        #     "spiff__logs": [],
        # }

        # return result
