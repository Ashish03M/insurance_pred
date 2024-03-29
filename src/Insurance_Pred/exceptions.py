# Import necessary modules
import sys  # Module for system-specific parameters and functions

# Import the logging module from your project
from src.Insurance_Pred.logger import logging  

# Define a function to generate error message details
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Get the exception information
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename where the exception occurred
    # Construct the error message detailing the filename, line number, and error message
    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message  # Return the constructed error message

# Define a custom exception class inheriting Exception class
class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)  # Call the constructor of the base class
        # Generate error message details using the provided error message and details
        self.error_message = error_message_detail(error_message, error_details)

    def __str__(self):
        return self.error_message  # Return the error message as a string representation of the exception
