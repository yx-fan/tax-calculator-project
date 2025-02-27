import logging
from config import CurrentConfig

LOG_LEVEL = logging.DEBUG if CurrentConfig.DEBUG else logging.INFO

# Set up logging to file and console
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# Set up logging to file
logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='a' # append mode
)

# Add the console handler to the root logger
logging.getLogger().addHandler(console_handler)

def log_debug(message):
    """
    Log a message with severity 'DEBUG' on the root logger.
    """
    logging.debug(message)

def log_info(message):
    """
    Log a message with severity 'INFO' on the root logger.
    """
    logging.info(message)

def log_warning(message):
    """
    Log a message with severity 'WARNING' on the root logger.
    """
    logging.warning(message)

def log_error(message):
    """
    Log a message with severity 'ERROR' on the root logger.
    """
    logging.error(message)