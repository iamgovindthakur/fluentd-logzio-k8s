import time
import logging
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

while True:
    log_level = random.choice([logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR])
    logging.log(log_level, 'Log message from your application')
    time.sleep(1)
