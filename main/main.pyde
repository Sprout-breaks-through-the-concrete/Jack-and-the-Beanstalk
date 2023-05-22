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
activity_list = []

def setup():
    GuardDebug()
    global stars, flower_list
    if USE_STROKE == False:
        noStroke()
    size(WINDOW_WIDTH, WINDOW_HEIGHT)
    prev_time = millis()
    stars.extend(object_maker.make_stars(0, 0, width, height, 1, 20))
    object_list.append([resource.flower, width*0.2, height*0.5, 100, 150])
    object_list.append([resource.flower, width*0.5, height*0.8, 150, 50])
    object_list.append([resource.tree, width*0.8, height*0.8, 100, 150])
    activity_list.append([resource.rainbow2, width*0.8, height*0.5, 200, 100])  
    object_list.append([resource.mountain, width*0.5, height*0.5, 250, 50]) 
    object_list.append([resource.sun, width*0.2, height*0.7, 100, 150])
        
def draw():
    GuardDebug()
    clear()
    global grow_height, grow_speed, grow_time, prev_time, flower_list, flower, activity_list
    grow_height += GROW_SPEED
    
    current_time = millis()
    grow_time += (current_time - prev_time)
    main_logger.debug("grow_time=" + str(grow_time))
    main_logger.debug("grow_height=" + str(grow_height))
    prev_time = current_time
    
    graphic.draw_star(stars)
    graphic.draw_objects(object_list)
    
    pic = graphic.draw_objects(object_list)
    
    if pic < mouseX+0.01/width:
        pic = lerp(20,30,.2)
    elif pic > mouseX+0.01/width:
        pic = lerp(20,30,.2)


    
    if mouseX > width/2:
        graphic.draw_objects(activity_list)

    else:
        color(255)
    
    
       
        
    
    if grow_height < PHASE_1:
        pass
    elif grow_height < PHASE_2:
        pass
    elif grow_height < PHASE_3: 
        pass
    else : #FINAL PHASE
        pass
   
   
   
    
    

    
    
