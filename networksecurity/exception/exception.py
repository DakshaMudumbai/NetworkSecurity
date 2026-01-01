import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        self.error_message = error_message

        _, _, exc_tb = error_detail.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return (
            f"Error occurred in python script name [{self.filename}] "
            f"at line number [{self.lineno}] "
            f"error message [{str(self.error_message)}]"
        )
    
if __name__ == "__main__":
    try:
        logger.logging.info("Divide by zero error")
        a = 1 / 0
    except Exception as e:
        raise NetworkSecurityException(e, sys)