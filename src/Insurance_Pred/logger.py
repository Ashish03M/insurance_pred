# Import necessary modules
import logging
import os
from datetime import datetime

# Define log file name based on current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Construct full path for log file within 'logs' directory in the current working directory
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Ensure 'logs' directory exists, creating it if necessary
os.makedirs(log_path, exist_ok=True)

# Construct full file path for log file
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure basic logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Set log file path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Define log message format
    level=logging.INFO,  # Set logging level to INFO
)
