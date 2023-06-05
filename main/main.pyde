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
mouseY = 0
mouseX_prev = 0

'''
main_logger.debug(message)
main_logger.info(message)
main_logger.warning(message)
main_logger.warning(message)
'''
main_logger = logger.get("main")

stars = []
object_list = []

x = random(WINDOW_WIDTH)
y = random(WINDOW_HEIGHT)
tx = x
ty = y
background_color = color(255)

def setup():
    '''
    GuardDebug()
    '''
    global stars, flower_list, x, y, width
    if USE_STROKE == False:
        noStroke()
    size(WINDOW_WIDTH, WINDOW_HEIGHT)
    prev_time = millis()
    stars.extend(object_maker.make_stars(0, 0, width, height, 1, 20))
    object_list.append([resource.flower, width*0.2, height*0.5, 100, 150])
    object_list.append([resource.flower, width*0.5, height*0.8, 150, 50])
    object_list.append([resource.tree, width*0.8, height*0.8, 100, 150])
    object_list.append([resource.sun, width*0.2, height*0.7, 100, 150])
    object_list.append([resource.moon, width*0.8, height*0.5, 100, 150])
    object_list.append([resource.rainbow2, width*0.8, height*0.9, 200, 100])
                
def draw():
    '''
    GuardDebug()
    '''
    clear()
    global grow_height, grow_speed, grow_time, prev_time, flower_list, flower, x, y, tx, ty, mouseX, mouseX_prev
    grow_height += GROW_SPEED
    x = lerp(x, tx, .1)
    y = lerp(y, ty, .1)
    background(background_color)
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
    
#def mouseMoved():
#    tx = mouseX
#    ty = mouseY
#    
#    frameRate(1)
#    if graphic.draw_objects(object_list)
    
    
# def keyPressed():
#     if key == CODED:
#         if keyCode == UP:
#             for object_y in object_list:
#                 object_y[2] -= 1
#                 frameRate(2000)
#         elif keyCode == DOWN:
#             for object_y in object_list:
#                 object_y[2] += 1
#                 frameRate(2000)       

#def mouseMoved():
#    if mouseY > WINDOW_HEIGHT:
#        for object_y in object_list:
#            object_y[2] -= 1
#    if mouseY <= WINDOW_HEIGHT/2:
#        for object_y in object_list:
#            object_y[2] += 1
 
#def mouseMoved():
#    if mouseY > WINDOW_WIDTH:
#        object_list[2] -= 1
#        
#    if mouseY <= WINDOW_WIDTH:
#        object_list[2] += 1

    for obj in object_list:
        x = obj[1]
        y = obj[2]
        width_obj = obj[3]
        height_obj = obj[4]
        mouse_dx = mouseX - mouseX_prev
        x += mouse_dx * 0.01
        x = constrain(x, 0, width - width_obj)
        graphic.draw_object(obj[0], x, y, width_obj, height_obj)
        obj[1] = x
    
    mouseX_prev = mouseX
        

        
         
            
    
        
    

    
    
