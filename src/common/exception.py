import sys
import traceback
from src.common.logger import logger

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """Generates a detailed error message with file name, line number, and error description."""
    exc_type, exc_value, exc_tb = error_detail.exc_info()
    tb_info = traceback.extract_tb(exc_tb)
    
    if tb_info:
        file_name, line_number, func_name, _ = tb_info[-1]  # Get the last traceback entry
        error_message = (
            f"Error occurred in script: [{file_name}], "
            f"Function: [{func_name}], "
            f"Line number: [{line_number}], "
            f"Error message: [{str(error)}]"
        )
    else:
        error_message = f"Error message: [{str(error)}] (No traceback available)"
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
        # Log the error
        logger.error(self.error_message)
    
    def __str__(self):
        return self.error_message
    