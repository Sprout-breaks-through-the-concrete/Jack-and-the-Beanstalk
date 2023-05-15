from environment import *
import logger
from guard import *
import sys
import object_maker
import graphic
import resource

grow_height = 0
grow_time = 0
prev_time = 0

logger.init()

"""
main_logger.debug(message)
main_logger.info(message)
main_logger.warning(message)
main_logger.warning(message)
"""
main_logger = logger.get("main")

stars = []
object_list = []
bird_list = []

x = 0
y = 0
xdir = 2
ydir = 5

def setup():

    GuardDebug()
    global stars, flower_list
    global x, y, diam, xdir, ydir
    
    x = width
    y = height
    xdir = 5
    ydir = 5
    
    if USE_STROKE == False:
        noStroke()
    size(WINDOW_WIDTH, WINDOW_HEIGHT)
    prev_time = millis()
    stars.extend(object_maker.make_stars(0, 0, width, height, 1, 20))
    object_list.append([resource.flower, width*0.2, height*0.5, 100, 150])
    object_list.append([resource.flower, width*0.5, height*0.8, 150, 50])
    object_list.append([resource.tree, width*0.8, height*0.8, 100, 150])
    object_list.append([resource.bird, width*0.3, height*0.3, 110, 110])
    object_list.append([resource.bird_V2, width*0.2, height*0.2, 150, 110])
    object_list.append([resource.bird_V3, width*0.8, height*0.2, 200, 200])
    
def draw():
    GuardDebug()
    clear()
    global grow_height, grow_speed, grow_time, prev_time, flower_list, flower
    global x, y, diam, xdir, ydir
    grow_height += GROW_SPEED
    
    
    current_time = millis()
    grow_time += (current_time - prev_time)
    main_logger.debug("grow_time=" + str(grow_time))
    main_logger.debug("grow_height=" + str(grow_height))
    prev_time = current_time
    


    graphic.draw_star(stars)
    graphic.draw_objects(object_list)
    if grow_height < PHASE_1:
        pass
    elif grow_height < PHASE_2:
        pass
    elif grow_height < PHASE_3: 
        pass
    else : #FINAL PHASE
        pass

   

    
    
