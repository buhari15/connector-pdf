from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.units import inch

from typing import Any

from spiffworkflow_connector_command.command_interface import CommandErrorDict
from spiffworkflow_connector_command.command_interface import CommandResponseDict
from spiffworkflow_connector_command.command_interface import ConnectorCommand
from spiffworkflow_connector_command.command_interface import ConnectorProxyResponseDict
import os
import requests
from io import BytesIO

class GenPDF(ConnectorCommand):
    """Class for adding text to the PDF."""

    def __init__(self, 
                 output_path: str,
                 text: str,
                 logo_path: str = None, 
                 font_size=12, page_size=A4,
        ):
        self.output_path = output_path
        self.text = text
        self.font_size = font_size
        self.page_size = page_size
        self.logo_path = logo_path

    def execute(self, _config: Any, _task_data: Any) -> ConnectorProxyResponseDict:
        """Generate and save the PDF."""
        logs = []
        error: CommandErrorDict | None = None

        try:
            # Ensure the directory exists
            directory = os.path.dirname(self.output_path)
            if not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
                logs.append(f"Directory verified: {os.path.dirname(self.output_path)}")
            else:
                logs.append(f"Directory already exists: {os.path.dirname(self.output_path)}")
            
            if os.access(directory, os.W_OK):
                logs.append(f"Directory is writable: {os.path.dirname(self.output_path)}")
            else:
                logs.append(f"Directory is not writable: {os.path.dirname(self.output_path)}")
                raise PermissionError(f"Directory is not writable: {os.path.dirname(self.output_path)}")

            doc = SimpleDocTemplate(self.output_path, pagesize=self.page_size)
            styles = getSampleStyleSheet()
            story = []

            # Add text
            story.append(Paragraph(self.text, styles['Normal']))
            story.append(Spacer(1, 12))

            # Add logo
            if self.logo_path:
                if self.logo_path.startswith('http://') or self.logo_path.startswith('https://'):
                    response = requests.get(self.logo_path)
                    image = BytesIO(response.content)
                    img = Image(image, width=self.width, height=self.height)
                else:
                    img = Image(self.logo_path, width=self.width, height=self.height)
                story.append(img)

            doc.build(story)
            logs.append(f"PDF generated successfully at {self.output_path}")
            if os.path.exists(self.output_path):
                logs.append(f"PDF exists at {self.output_path}")
            else:
                logs.append(f"PDF does not exist at {self.output_path}")
                raise FileNotFoundError(f"PDF does not exist at {self.output_path}")

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