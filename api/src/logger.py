"""This file is to setup logging configuration for this project."""

#============================#
#---------- Imports ---------#
#============================#

import logging
import os
from datetime import datetime

#==========================#
#---- Config for Logging --#
#==========================#

# Timestamp for the run
TIMESTAMP = datetime.now().strftime('%H_%M_%S')  # time for run-specific file
DATE_FOLDER = datetime.now().strftime('%d_%b_%Y')  # folder per day

# Paths
BASE_LOG_DIR = os.path.join(os.getcwd(), "src", "logs", DATE_FOLDER)
os.makedirs(BASE_LOG_DIR, exist_ok=True)

LOG_FILE = f'{TIMESTAMP}.log'
LOG_FILE_PATH = os.path.join(BASE_LOG_DIR, LOG_FILE)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


if __name__ == "__main__":
    logging.info("Started logging")
    logging.info(f"Logs are being saved to: {LOG_FILE_PATH}")