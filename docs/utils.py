# utils.py

import logging
import os
import json

def log_message(level, message, logger_name='frontend-app'):
    """Logs a message with the given level."""
    logger = logging.getLogger(logger_name)
    if level == 'ERROR':
        logger.error(message)
    elif level == 'WARNING':
        logger.warning(message)
    elif level == 'INFO':
        logger.info(message)
    elif level == 'DEBUG':
        logger.debug(message)

def load_config(file_path):
    """Loads a JSON configuration file."""
    try:
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        logging.error(f"Configuration file not found at {file_path}")
        return {}
    except json.JSONDecodeError as e:
        logging.error(f"Invalid configuration format: {e}")
        return {}

def get_env_variable(name, default=None):
    """Gets an environment variable, or a default value if not set."""
    value = os.environ.get(name)
    if value is None:
        return default
    return value