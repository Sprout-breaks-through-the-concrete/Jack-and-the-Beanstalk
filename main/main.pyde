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
beanstalk1_list = []
beanstalk2_list = []
beanstalk3_list = []
beanstalk4_list = []
beanstalk5_list = []
beanstalk6_list = []
beanstalk7_list = []
flower_per_size = 10
flower_anchor = graphic.BOTTOM

def setup():
    GuardDebug()
    global stars, flower_list
    if USE_STROKE == False:
        noStroke()
    size(WINDOW_WIDTH, WINDOW_HEIGHT)
    prev_time = millis()
    stars.extend(object_maker.make_stars(0, 0, width, height, 1, 20))
    beanstalk1_list.append([resource.beanstalk1, width*0.5, height, 60, 40])
    beanstalk2_list.append([resource.beanstalk2, width*0.5, height, 100, 150])
    beanstalk3_list.append([resource.beanstalk3, width*0.5, height, 100, 150])
    beanstalk4_list.append([resource.beanstalk4, width*0.5, height, 100, 300])
    beanstalk5_list.append([resource.beanstalk5, width*0.5, height, 300, 700])
    beanstalk6_list.append([resource.beanstalk6, width*0.5, height, 400, 600])
    beanstalk7_list.append([resource.beanstalk7, width*0.5, height, 500, 800])
    
#object_list.append([resource.beanstalk1, width*0.5, height*0.9, 60, 40])
    #object_list.append([resource.beanstalk2, width*0.5, height*0.9, 100, 150])
    #object_list.append([resource.beanstalk3, width*0.5, height*0.9, 100, 150])
    #object_list.append([resource.beanstalk4, width*0.5, height*0.8, 100, 300])
    #object_list.append([resource.beanstalk5, width*0.4, height*0.6, 300, 700])
    #object_list.append([resource.beanstalk6, width*0.5, height*0.7, 400, 600])

    
def draw():
    GuardDebug()
    clear()
    global grow_height, grow_speed, grow_time, prev_time, flower_list, flower, flower_per_size
    grow_height = height - mouseY
    
    current_time = millis()
    grow_time += (current_time - prev_time)
    main_logger.debug("grow_time=" + str(grow_time))
    main_logger.debug("grow_height=" + str(grow_height))
    prev_time = current_time
    
    graphic.draw_star(stars)
    graphic.draw_objects(object_list)
    
    if grow_height < PHASE_1:
        graphic.draw_static_objects(beanstalk1_list, flower_per_size, flower_anchor)
        pass
    elif grow_height < PHASE_2:
        graphic.draw_static_objects(beanstalk2_list, flower_per_size, flower_anchor)
        pass
    elif grow_height < PHASE_3:
        graphic.draw_static_objects(beanstalk3_list, flower_per_size, flower_anchor)
        pass
    elif grow_height < PHASE_4:
        graphic.draw_static_objects(beanstalk4_list, flower_per_size, flower_anchor)
        pass
    elif grow_height < PHASE_5:
        graphic.draw_static_objects(beanstalk5_list, flower_per_size, flower_anchor)
        pass
    elif grow_height < PHASE_6:
        graphic.draw_static_objects(beanstalk6_list, flower_per_size, flower_anchor)
        pass
    else :
        graphic.draw_static_objects(beanstalk7_list, flower_per_size, flower_anchor)
        pass
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
beanstalk1_list = []
beanstalk2_list = []
beanstalk3_list = []
beanstalk4_list = []
beanstalk5_list = []
beanstalk6_list = []
beanstalk7_list = []
flower_per_size = 10
flower_anchor = graphic.BOTTOM

def setup():
    GuardDebug()
    global stars, flower_list
    if USE_STROKE == False:
        noStroke()
    size(WINDOW_WIDTH, WINDOW_HEIGHT)
    prev_time = millis()
    stars.extend(object_maker.make_stars(0, 0, width, height, 1, 20))
    beanstalk1_list.append([resource.beanstalk1, width*0.5, height, 60, 40])
    beanstalk2_list.append([resource.beanstalk2, width*0.5, height, 100, 150])
    beanstalk3_list.append([resource.beanstalk3, width*0.5, height, 100, 150])
    beanstalk4_list.append([resource.beanstalk4, width*0.5, height, 100, 300])
    beanstalk5_list.append([resource.beanstalk5, width*0.5, height, 300, 700])
    beanstalk6_list.append([resource.beanstalk6, width*0.5, height, 400, 600])
    beanstalk7_list.append([resource.beanstalk7, width*0.5, height, 500, 800])
    
#object_list.append([resource.beanstalk1, width*0.5, height*0.9, 60, 40])
    #object_list.append([resource.beanstalk2, width*0.5, height*0.9, 100, 150])
    #object_list.append([resource.beanstalk3, width*0.5, height*0.9, 100, 150])
    #object_list.append([resource.beanstalk4, width*0.5, height*0.8, 100, 300])
    #object_list.append([resource.beanstalk5, width*0.4, height*0.6, 300, 700])
    #object_list.append([resource.beanstalk6, width*0.5, height*0.7, 400, 600])

    
def draw():
    GuardDebug()
    clear()
    global grow_height, grow_speed, grow_time, prev_time, flower_list, flower, flower_per_size
    grow_height = height - mouseY
    
    current_time = millis()
    grow_time += (current_time - prev_time)
    main_logger.debug("grow_time=" + str(grow_time))
    main_logger.debug("grow_height=" + str(grow_height))
    prev_time = current_time
    
    graphic.draw_star(stars)
    graphic.draw_objects(object_list)
    
    if grow_height < PHASE_1:
        graphic.draw_static_objects(beanstalk1_list, flower_per_size, flower_anchor)
        pass
    elif grow_height < PHASE_2:
        graphic.draw_static_objects(beanstalk2_list, flower_per_size, flower_anchor)
        pass
    elif grow_height < PHASE_3:
        graphic.draw_static_objects(beanstalk3_list, flower_per_size, flower_anchor)
        pass
    elif grow_height < PHASE_4:
        graphic.draw_static_objects(beanstalk4_list, flower_per_size, flower_anchor)
        pass
    elif grow_height < PHASE_5:
        graphic.draw_static_objects(beanstalk5_list, flower_per_size, flower_anchor)
        pass
    elif grow_height < PHASE_6:
        graphic.draw_static_objects(beanstalk6_list, flower_per_size, flower_anchor)
        pass
    else :
        graphic.draw_static_objects(beanstalk7_list, flower_per_size, flower_anchor)
        pass
