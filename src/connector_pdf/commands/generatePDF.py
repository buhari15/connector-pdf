from connector_pdf.pdf_component import PDFComponent
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from spiffworkflow_connector_command.command_interface import CommandErrorDict
from spiffworkflow_connector_command.command_interface import CommandResponseDict
from spiffworkflow_connector_command.command_interface import ConnectorCommand
from spiffworkflow_connector_command.command_interface import ConnectorProxyResponseDict

# class PDFGenerator:
#     """Class for managing and generating the final PDF."""

#     def __init__(self, output_path: str):
#         self.output_path = output_path
#         self.pdf = canvas.Canvas(self.output_path, pagesize=A4)
#         self.components = []

#         def add_text(self, text: str, x:float, y:float, font="Helvetica", size=12):
#             self.components.append({

#             })
        
#             # self.pdf.setFont(font, size)
#             # self.pdf.drawString(x, y, text)


#     def generate(self):
#         # pdf = canvas.Canvas(self.output_path, pagesize=A4)
#         # for component in self.components:
#         #     component.draw(pdf)
#         self.pdf.save()


class PDFGenerator:
    """Class for managing and generating the final PDF for SpiffWorkflow."""

    def __init__(self, output_path: str):
        self.output_path = output_path
        self.pdf = canvas.Canvas(self.output_path, pagesize=A4)
        self.components = []

    def add_text(self, text: str, x: float, y: float, font="Helvetica", size=12):
        """Add text component to the PDF."""
        self.components.append({
            'type': 'text',
            'text': text,
            'x': x,
            'y': y,
            'font': font,
            'size': size
        })

    def generate(self, _config: any, _task_data: any) -> ConnectorProxyResponseDict:
        """Generate and save the PDF."""
        logs = []
        error: CommandErrorDict | None = None
        try:
            for component in self.components:
                if component['type'] == 'text':
                    self.pdf.setFont(component['font'], component['size'])
                    self.pdf.drawString(component['x'], component['y'], component['text'])
            self.pdf.save()
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