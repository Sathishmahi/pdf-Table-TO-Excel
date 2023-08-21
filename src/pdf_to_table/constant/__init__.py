import time
import os

LOGGING_DIR_NAME = "logs"
os.makedirs(LOGGING_DIR_NAME,exist_ok=True)
CURRENT_TIME_STAMP = time.asctime().replace(" ", "_").replace(":", "_")
LOGGING_FILE_NAME = f"runing_logs_{CURRENT_TIME_STAMP}.log"