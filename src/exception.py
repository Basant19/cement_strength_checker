'''import sys	Imports system-related functions for error handling
error_message_detail()	Extracts filename, line number, and formats error messages
CustomException	A custom exception class that formats error messages
super().__init__(error_message)	Calls the parent Exception class to store the error message
def __str__(self):	Returns a formatted error message when printed
'''
import sys

def error_message_detail(error, error_detail:sys):
        '''
        Explanation
        This function takes two parameters:
        error: The actual error message.
        error_detail: The sys module to fetch detailed error information.
        
        Step-by-step execution

        1. Get error traceback
        exc_info() returns a tuple of three values:
        The exception type.
        The exception instance.
        The traceback object (exc_tb), which contains information about where the error occurred.
        
        2. Extract the filename where the error occurred
        exc_tb.tb_frame.f_code.co_filename extracts the name of the Python file where the error happened.

        3. Extract the line number where the error occurred
        exc_tb.tb_lineno gives the line number where the error occurred.

        4. Format the error message
        This creates a formatted error message that includes:
        The script filename
        The exact line number
        The error message

        '''
        _,_, exc_tb=error_detail.exc_info ()
        file_name= exc_tb.tb_frame.f_code.co_filename
        linenumber= exc_tb.tb_lineno

        error= str (error)

        error_message = "Error occured python script name [{}] line number [{}] error message [{}]".format(
            file_name, linenumber, str(error)
        )

        return error_message
         

class CustomException(Exception):
    '''Step-by-step execution

       1. This method initializes an instance of CustomException.

       2.  Call the parent class constructor :Call the parent class constructor :Calls the Exception class's 
       constructor to set up the error message.
       
       3. Generate a detailed error message :
       Calls error_message_detail() to get the detailed error message with 
       filename and line number.

       4. Override the __str__ method:
       When str(CustomException) is called, it returns the detailed error message instead of just the default exception message.
    '''
    def __init__ (self,error_message,error_details:sys):    
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_details
        )

    def __str__(self):
         return self.error_message   