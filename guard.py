import logger
import os
from inspect import currentframe

class GuardInfo:
    def __init__(self):
        back_frame = currentframe().f_back
        self.logger = logger.get("guard")
        self.caller = os.path.basename(back_frame.f_code.co_filename) + ":" + str(back_frame.f_lineno) + " -> " + back_frame.f_code.co_name
        self.logger.info("call stack(" + self.caller +")")
        
Guard = GuardInfo
        
class GuardDebug:
    def __init__(self):
        back_frame = currentframe().f_back
        self.logger = logger.get("guard")
        self.caller = os.path.basename(back_frame.f_code.co_filename) + ":" + str(back_frame.f_lineno) + " -> " + back_frame.f_code.co_name
        self.logger.debug("call stack(" + self.caller +")")
