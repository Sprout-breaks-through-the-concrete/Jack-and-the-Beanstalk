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
move_list = []
object_list = []

x = 0
y = 0
xdir = 2
ydir = 5

def setup():
    GuardDebug()
    global stars, flower_list, move_list
    global x, y, diam, xdir, ydir, WINDOW_WIDTH, WINDOW_HEIGHT

    x = width
    y = height
    xdir = 5
    ydir = 5
    
    if USE_STROKE == False:
        noStroke()
    size(WINDOW_WIDTH, WINDOW_HEIGHT)
    prev_time = millis()
    stars.extend(object_maker.make_stars(0, 0, width, height, 1, 20))
    
    object_list.append([resource.tree, width*0.1, height*0.8, 100, 150])
    object_list.append([resource.tree, width*0.3, height*0.8, 100, 150])
    object_list.append([resource.tree, width*0.5, height*0.8, 100, 150])
    object_list.append([resource.tree, width*0.8, height*0.8, 100, 150])
    object_list.append([resource.tree, width*0.95, height*0.8, 100, 150])
    
    object_list.append([resource.flower, width*0.1, height*0.9, 50, 50])
    object_list.append([resource.flower, width*0.2, height*0.92, 50, 50])
    object_list.append([resource.flower, width*0.3, height*0.9, 50, 50])
    object_list.append([resource.flower, width*0.4, height*0.92, 50, 50])
    object_list.append([resource.flower, width*0.5, height*0.9, 50, 50])
    object_list.append([resource.flower, width*0.6, height*0.92, 50, 50])
    object_list.append([resource.flower, width*0.7, height*0.9, 50, 50])
    object_list.append([resource.flower, width*0.8, height*0.92, 50, 50])
    object_list.append([resource.flower, width*0.9, height*0.9, 50, 50])
    
    object_list.append([resource.bird_V1, width*0.1, height*0.8, 50, 50])
    object_list.append([resource.bird_V2, width*0.5, height*0.7, 50, 50])
    object_list.append([resource.bird_V3, width*0.9, height*0.6, 50, 50])

    object_list.append([resource.cloud1, width*0.01, height*0.5, 90, 60])
    object_list.append([resource.cloud1, width*0.3, height*0.6, 60, 40])
    object_list.append([resource.cloud1, width*0.6, height*0.55, 90, 60])
    object_list.append([resource.cloud1, width*0.8, height*0.5, 60, 40])
    object_list.append([resource.cloud1, width*0.5, height*0.55, 60, 40])
    object_list.append([resource.cloud1, width*0.7, height*0.6, 60, 40])



def draw():
    GuardDebug()
    clear()
    global grow_height, grow_speed, grow_time, prev_time, flower_list, flower
    global x, y, diam, xdir, ydir
    grow_height += GROW_SPEED
    
    #sky
    if mouseY >= height * 0.75: #skyblue-pink
            background(lerpColor(color(255, 192, 203), color(135, 206, 250), (mouseY - height * 0.75) / (height * 0.25)))
    elif mouseY >= height * 0.5: #pink-purple
            background(lerpColor(color(128, 0, 128), color(255, 192, 203), (mouseY - height * 0.5) / (height * 0.25)))
    elif mouseY >= height * 0.25:  #purple-navy
            background(lerpColor(color(0, 0, 128), color(128, 0, 128), (mouseY - height * 0.25) / (height * 0.25)))
    else: #navy-black
            background(lerpColor(color(0, 0, 0), color(0, 0, 128), mouseY / (height * 0.25)))

    current_time = millis()
    grow_time += (current_time - prev_time)
    main_logger.debug("grow_time=" + str(grow_time))
    main_logger.debug("grow_height=" + str(grow_height))
    prev_time = current_time
    
    graphic.draw_star(stars)
    graphic.draw_objects(object_list)
    graphic.draw_objects(move_list)
    
    for obj in object_list:
        if obj[0] == resource.bird_V1:
            obj[1] += xdir
            if obj[1] > width:
                obj[1] = -obj[3]
                
    for obj in object_list:
        if obj[0] == resource.bird_V2:
            obj[1] += xdir
            if obj[1] > width:
                obj[1] = -obj[3]
    
    for obj in object_list:
        if obj[0] == resource.bird_V3:
            obj[1] += xdir
            if obj[1] > width:
                obj[1] = -obj[3]
                
        
    for obj in object_list:
        if obj[0] == resource.cloud1:
            obj[1] += xdir
            if obj[1] > width:
                obj[1] = -obj[3]          
               

    
    if grow_height < PHASE_1:
        pass
    elif grow_height < PHASE_2:
        pass
    elif grow_height < PHASE_3: 
        pass
    else : #FINAL PHASE
        pass
        
    
       
    
    

    
    
