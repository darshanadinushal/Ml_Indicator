import os 
import sys
import logging 
from datetime import datetime

logging_Format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
LOG_DIR=f"{datetime.now().strftime('%m_%d_%Y')}"
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H')}.log"

log_dir ="logs"
logs_path = os.path.join(os.getcwd(), log_dir, LOG_DIR)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    level= logging.INFO,
    format= logging_Format,

    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("mlIndicatorLogger")
