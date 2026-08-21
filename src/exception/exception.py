import sys
from typing import Optional

class MedicalCostException(Exception):
    """Custom exception that captures full traceback."""
    
    def __init__(self, error_message: str, error_details:sys):
        self.error_message = error_message
        self.error_details = error_details
        _,_,exc_tb = error_details.exc_info()
        self.line_number = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    
    def __str__(self) -> str:
        return f"Error occurred in script: [{self.file_name}] at line number: [{self.line_number}] with error message: [{self.error_message}]"
    