import sys
import os

# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.exception import CustomException

def test_custom_exception():
    try:
        # Simulate an error
        1 / 0
    except Exception as e:
        # Raise your custom exception
        custom_exc = CustomException(e, sys)
        print(custom_exc)

if __name__ == "__main__":
    test_custom_exception()
