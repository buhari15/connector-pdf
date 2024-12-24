from connector_pdf.pdf_elements import PDFElement
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from typing import Any

from spiffworkflow_connector_command.command_interface import CommandErrorDict
from spiffworkflow_connector_command.command_interface import CommandResponseDict
from spiffworkflow_connector_command.command_interface import ConnectorCommand
from spiffworkflow_connector_command.command_interface import ConnectorProxyResponseDict


class AddText(ConnectorCommand, PDFElement):
    def __init__(self,
        text: str,
        x: int,
        y: int,
        font: str = "Helvetica",
        size: int = 12 
    ):
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.size = size

    def execute(self, c:canvas.Canvas,  _config: Any, _task_data: Any) -> ConnectorProxyResponseDict:
        c.setFont(self.font, self.size)
        c.drawString(self.x, self.y, self.text)
        error: CommandErrorDict | None = None

        return_response: CommandResponseDict = {
            "body": {
                "connector_response": f"You passed the example connector: '{self.message}'. Have a good day!",
            },
            "mimetype": "application/json",
        }

        result: ConnectorProxyResponseDict = {
            "command_response": return_response,
            "error": error,
            "command_response_version": 2,
            "spiff__logs": [],
        }

        return result
