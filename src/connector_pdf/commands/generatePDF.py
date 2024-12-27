from connector_pdf.pdf_component import PDFComponent
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter, A2, A3, A1, A0, B5, B4, B3, B2, B1, B0, LEGAL, ELEVENSEVENTEEN
from reportlab.lib import colors
from typing import Any
from spiffworkflow_connector_command.command_interface import CommandErrorDict
from spiffworkflow_connector_command.command_interface import CommandResponseDict
from spiffworkflow_connector_command.command_interface import ConnectorCommand
from spiffworkflow_connector_command.command_interface import ConnectorProxyResponseDict



class PDFGenerator(ConnectorCommand):
    """Class for managing and generating the final PDF for SpiffWorkflow."""

    def __init__(self, 
                 output_path: str, 
                 text: str, 
                 x: float, y: float, 
                 font="Helvetica", 
                 size=12,
                 page_size=A4
                 ):
        self.output_path = output_path
        self.x = x
        self.y = y
        # self.text = text
        self.font = font
        self.size = size
        self.page_size = page_size
        # it is working fine without the function add_text
        self.add_text(text, x, y, font, size)
      
   

    def add_text(self, text: str, x: float, y: float, font="Helvetica", size=12):
        """Add text component to the PDF."""
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.size = size
        
    

    # def add_logo(self, logo_path: str, x: float, y: float, width: float, height: float):
    #     """Add logo component to the PDF."""
    #     self.logo_path = logo_path
    #     self.x = x
    #     self.y = y
    #     self.width = width
    #     self.height = height


    def execute(self, _config: Any, _task_data: Any) -> ConnectorProxyResponseDict:
        """Generate and save the PDF."""
        logs = []
        error: CommandErrorDict | None = None
      
        try:
         
            pdf = canvas.Canvas(self.output_path, pagesize=A4)
            pdf.setFont("Helvetica", 12)
            pdf.drawString(self.x, self.y, self.text)
            pdf.showPage()
            pdf.save()
            logs.append(f"PDF generated successfully at {self.output_path}")
    

            # for component in self.components:
            #     if component['type'] == 'text':
            #         self.pdf.setFont(component['font'], component['size'])
            #         self.pdf.drawString(component['x'], component['y'], component['text'])
            # self.pdf.save()
            # logs.append(f"PDF generated successfully at {self.output_path}")
            # for component in self.components:
            #     if component['type'] == 'text':
            #         self.pdf.setFont(component['font'], component['size'])
            #         self.pdf.drawString(component['x'], component['y'], component['text'])
            # self.pdf.save()
            # logs.append(f"PDF generated successfully at {self.output_path}")
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