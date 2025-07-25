import logging
import os
from datetime import datetime

# Generate unique log filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs folder path
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Full path to the log file (inside the folder)
log_file_path = os.path.join(logs_dir, LOG_FILE)

# Set up logging
logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
