import os
import logging
import sys

# Import your modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from src.logger import logging
from src.exception import CustomException

def test_logging():
    try:
        logging.info("Testing logger: This is an info log")
        logging.warning("Testing logger: This is a warning log")
        logging.error("Testing logger: This is an error log")
        print("✅ Logger test passed. Check the logs folder for the log file.")
    except Exception as e:
        print("❌ Logger test failed:", e)

def test_custom_exception():
    try:
        # Intentionally trigger an error (divide by zero)
        x = 1 / 0
    except Exception as e:
        custom_exc = CustomException(e, sys)
        print("✅ Custom Exception captured:")
        print(custom_exc)

if __name__ == "__main__":
    print("\n----- Running Logger Test -----")
    test_logging()

    print("\n----- Running Custom Exception Test -----")
    test_custom_exception()
