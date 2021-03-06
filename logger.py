import logging
import sys
"""Simple logger to catch all useful info"""
from logging.handlers import TimedRotatingFileHandler
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(funcName)s — %(levelname)s — %(message)s")
LOG_FILE = 'logs/log.log'


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


"""Every midnght logger opens another file"""
def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight', encoding='utf-8')
    file_handler.setFormatter(FORMATTER)
    return file_handler


"""wrapper to use logger"""
def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # better to have too much log than not enough
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False
    return logger
