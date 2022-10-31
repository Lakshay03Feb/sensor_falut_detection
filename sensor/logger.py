import logging
import os
from datetime import datetime
from from_root import from_root

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# print(LOG_FILE)

LOGS_PATH = os.path.join(from_root(),"logs")

# print(LOGS_PATH)

os.makedirs(LOGS_PATH,exist_ok=True)

LOGS_PATH_FILE = os.path.join(LOGS_PATH,LOG_FILE)

# print(LOGS_PATH_FILE)

logging.basicConfig(
    filename=LOGS_PATH_FILE,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)




