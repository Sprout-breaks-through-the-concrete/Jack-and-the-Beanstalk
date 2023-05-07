from guard import *
import logger

def Run():
    Guard()
    TestLogger()

def TestLogger():
    Guard()
    my_logger = logger.get("unittest")
    my_logger.debug("debug log")
    my_logger.info("info log")
    my_logger.warning("warning log")
    my_logger.error("error log")
    my_logger.critical("critical log")
     
