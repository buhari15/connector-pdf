from connector_pdf.pdf_component import PDFComponent
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from typing import Any

from spiffworkflow_connector_command.command_interface import CommandErrorDict
from spiffworkflow_connector_command.command_interface import CommandResponseDict
from spiffworkflow_connector_command.command_interface import ConnectorCommand
from spiffworkflow_connector_command.command_interface import ConnectorProxyResponseDict

import requests
from PIL import Image
from io import BytesIO
import os

class PDFGenerator(ConnectorCommand):
    """Class for managing and generating the final PDF for SpiffWorkflow.
    
    Args:
    ConnectorCommand (class): The base class for all connector commands.
    output_path (str): The path where the PDF will be saved.
    text (str): The text to be added to the PDF.
    text_x_postion (float): The x position of the text.
    text_y_position (float): The y position of the text.
    font (str, optional): The font of the text. Defaults to "Helvetica".
    size (int, optional): The size of the text. Defaults to 12.
    page_size (tuple, optional): The size of the page. Defaults
    to A4.

    """

    def __init__(self, 
                 output_path: str, 
                 text: str, 
                 text_x_postion: float, 
                 text_y_position: float, 
                 x: float,
                 y: float,
                 width: float,
                 height: float,
                 logo_path: str,
                 font="Helvetica", 
                 size=12,
                 page_size=A4
                 ):
        self.output_path = output_path
        self.text_x_postion = text_x_postion
        self.text_y_position = text_y_position
        self.font = font
        self.size = size
        self.page_size = page_size
        self.add_text(text, text_x_postion, text_y_position, font, size)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.logo_path = logo_path
        # self.add_logo(logo_path, x, y, width, height)
    
      


    def add_text(self, text: str, text_x_postion: float, text_y_position: float, font="Helvetica", size=12):
        """This function add single line text component to the PDF Generator.
        Args:
        text (str): The text to be added to the PDF.
        x (float): The x position of the text.
        y (float): The y position of the text.
        font (str, optional): The font of the text. Defaults to "Helvetica".
        size (int, optional): The size of the text. Defaults to 12.

        """
        self.text = text
        self.text_x_postion = text_x_postion
        self.text_y_position = text_y_position
        self.font = font
        self.size = size
        
    

    def add_logo(self, logo_path: str, x: float, y: float, width: float, height: float):
        """Add logo component to the PDF."""
        self.logo_path = logo_path
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def execute(self, _config: Any, _task_data: Any) -> ConnectorProxyResponseDict:
        """Generate and save the PDF."""
        logs = []
        error: CommandErrorDict | None = None
      
        try:
            os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
            logs.append(f"PDF generated successfully at {self.output_path}")
            pdf = canvas.Canvas(self.output_path, pagesize=A4)
            pdf.setFont("Helvetica", 12)
            pdf.drawString(self.text_x_postion, self.text_x_postion, self.text)
            

            # if self.logo_path.startswith("http") or self.logo_path.startswith("https"):
            #     response = requests.get(self.logo_path)
            #     image = BytesIO(response.content)
            #     pdf.drawImage(image, self.x, self.y, width=self.width, height=self.height)
            # else:
            #     pdf.drawImage(self.logo_path, self.x, self.y, width=self.width, height=self.height)
            
            pdf.showPage()
            pdf.save()
            logs.append(f"PDF generated successfully at {self.output_path}")
    
        except Exception as e:
            logs.append(f"Error generating PDF: {e}")
            error = {
                "message": f"Error generating PDF: {e}",
                "exception": str(e),
            }
        return_response: CommandResponseDict = {
            "body": {
                "connector_response": f"PDF generated successfully at {self.output_path}",
            },
            "mimetype": "application/json",
        }
        result: ConnectorProxyResponseDict = {
            "command_response": return_response,
            "error": error,
            "command_response_version": 2,
            "spiff__logs": logs,
        }
        return result