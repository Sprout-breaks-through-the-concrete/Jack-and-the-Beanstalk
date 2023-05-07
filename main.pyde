import colors
from environment import *
import logger
from guard import *
import unittest
import sys
import object_maker
import graphic

grow_height = 0
grow_time = 0
prev_time = 0

logger.init()

main_logger = logger.get("main")

if RUN_UNITTEST:
    Guard()
    main_logger.info("unittest start")
    unittest.Run()
    main_logger.info("unittest end")
    sys.exit()
    
stars = []

def setup():
    GuardDebug()
    global stars
    if USE_STROKE == False:
        noStroke()
    size(WINDOW_WIDTH, WINDOW_HEIGHT)
    prev_time = millis()
    stars.extend(object_maker.make_stars(0, 0, width, height, 3, 20))
    
def draw():
    clear()
    GuardDebug()
    global grow_height, grow_speed, grow_time, prev_time
    grow_height += GROW_SPEED
    
    current_time = millis()
    grow_time += (current_time - prev_time)
    main_logger.debug("grow_time=" + str(grow_time))
    main_logger.debug("grow_height=" + str(grow_height))
    prev_time = current_time
    
    graphic.draw_star(stars)
    
    if grow_height < PHASE_1:
        pass
    elif grow_height < PHASE_2:
        pass
    elif grow_height < PHASE_3: 
        pass
    else : #FINAL PHASE
        pass
       
    
    

    
    
