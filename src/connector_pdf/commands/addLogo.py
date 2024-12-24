from connector_pdf.pdf_component import PDFComponent
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from typing import Any

from spiffworkflow_connector_command.command_interface import CommandErrorDict
from spiffworkflow_connector_command.command_interface import CommandResponseDict
from spiffworkflow_connector_command.command_interface import ConnectorCommand
from spiffworkflow_connector_command.command_interface import ConnectorProxyResponseDict


class PDFLogo(PDFComponent):
    """Class for adding a logo to the PDF."""

    def __init__(self, logo_path: str, x: float, y: float, width: float, height: float):
        self.logo_path = logo_path
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, pdf: canvas.Canvas):
        pdf.drawImage(self.logo_path, self.x, self.y, width=self.width, height=self.height)



    # def execute(self, _config: Any, _task_data: Any) -> ConnectorProxyResponseDict:
    #     error: CommandErrorDict | None = None

    #     return_response: CommandResponseDict = {
    #         "body": {
    #             "connector_response": f"You passed the example connector: '{self.message}'. Have a good day!",
    #         },
    #         "mimetype": "application/json",
    #     }

    #     result: ConnectorProxyResponseDict = {
    #         "command_response": return_response,
    #         "error": error,
    #         "command_response_version": 2,
    #         "spiff__logs": [],
    #     }

    #     return result
