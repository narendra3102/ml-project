import sys
from src.pipeline.logger import logging   # ✅ Corrected import

def error_message_detail(error, error_detail: sys):
    """
    Returns detailed error message with file name, line number and error text.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error in script [{0}] at line [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
        logging.error(self.error_message)   

