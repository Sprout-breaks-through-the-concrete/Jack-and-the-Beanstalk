import os
import logging
from environment import LOG_DIR, LOG_LEVEL

LOG_FORMAT = '%(asctime)s [%(levelname)s] %(name)s : %(message)s'
LOG_FORMATTER = logging.Formatter(LOG_FORMAT)

loggers = {}

def init():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(format = LOG_FORMAT, level = LOG_LEVEL, filemode = 'a')

def get(logger_name):
    if logger_name in loggers.keys():
        return loggers[logger_name]
    
    logger = logging.getLogger(logger_name)
    
    loggers[logger_name] = logger
    
    return logger
