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

def setup():
    GuardDebug()
    global stars, flower_list
    if USE_STROKE == False:
        noStroke()
    size(WINDOW_WIDTH, WINDOW_HEIGHT)
    prev_time = millis()
    stars.extend(object_maker.make_stars(0, 0, width, height, 1, 20))

    move_list.append([resource.cloud1, width*0.01, height*0.05, 90, 60])

    move_list.append([resource.cloud1, width*0.3, height*0.1, 60, 40])

    move_list.append([resource.cloud1, width, height*0.25, 90, 60])

    move_list.append([resource.cloud1, width*0.8, height*0.2, 60, 40])

    move_list.append([resource.cloud1, width*0.5, height*0.25, 60, 40])

    move_list.append([resource.cloud1, width*0.7, height*0.01, 60, 40])

    move_list.append([resource.chicken, width*0.5, height*0.2, 50, 60])

    move_list.append([resource.pocket, width*0.8, height*0.15, 60, 60])

    move_list.append([resource.haff, width*0.3, height*0.07, 60, 60])

    #object_list.append([resource.beanstalk1, width*0.5, height*0.9, 60, 40])

    #object_list.append([resource.beanstalk2, width*0.5, height*0.9, 60, 90])

    #object_list.append([resource.beanstalk3, width*0.5, height*0.9, 60, 90])

    #object_list.append([resource.beanstalk4, width*0.5, height*0.9, 60, 90])

    #object_list.append([resource.beanstalk5, width*0.5, height*0.9, 60, 90])

    #object_list.append([resource.beanstalk6, width*0.5, height*0.9, 180, 270])

    object_list.append([resource.beanstalk7, width*0.5, height*0.5, 500, 800])

    

def draw():

    GuardDebug()

    clear()

    global grow_height, grow_speed, grow_time, prev_time, flower_list, flower

    grow_height += GROW_SPEED

 

    current_time = millis()

    grow_time += (current_time - prev_time)

    main_logger.debug("grow_time=" + str(grow_time))

    main_logger.debug("grow_height=" + str(grow_height))

    prev_time = current_time

    

   

    # Background_universe

    colorMode(RGB)

    noStroke()

    fill(87,65,163,mouseY)

    rect(0, 0, width, height)

    fill(77,54,151,mouseY)

    rect(0, height/5, width, height)

    fill(69,47,147,mouseY)

    rect(0, height/2.5, width, height)

    fill(63,43,147,mouseY)

    rect(0, height/1.8, width, height)

    fill(54,37,126,mouseY)

    rect(0, height/1.7, width, height)

    fill(47,32,118,mouseY)

    rect(0, height/1.6, width, height)

    fill(34,24,102,mouseY)

    rect(0, height/1.5, width, height)

    fill(26,16,93,mouseY)

    rect(0, height/1.4, width, height)

    fill(19,13,86,mouseY)

    rect(0, height/1.3, width, height)

    fill(12,7,77,mouseY)

    rect(0, height/1.2, width, height)

    fill(1,0,65,mouseY)

    rect(0, height/1.1, width, height)

    '''

    #Background_sky

    fill(135,225,255,mouseY)

    rect(0, 0, width, height)

    fill(140,225,255,mouseY)

    rect(0, height/5, width, height)

    fill(145,225,255,mouseY)

    rect(0, height/2.5, width, height)

    fill(150,225,255,mouseY)

    rect(0, height/1.8, width, height)

    fill(155,225,255,mouseY)

    rect(0, height/1.7, width, height)

    fill(160,225,255,mouseY)

    rect(0, height/1.6, width, height)

    fill(165,225,255,mouseY)

    rect(0, height/1.5, width, height)

    fill(170,225,255,mouseY)

    rect(0, height/1.4, width, height)

    fill(175,225,255,mouseY)

    rect(0, height/1.3, width, height)

    fill(180,225,255,mouseY)

    rect(0, height/1.2, width, height)

    fill(185,225,255,mouseY)

    rect(0, height/1.1, width, height)

    '''

    graphic.draw_star(stars)

    graphic.draw_objects(object_list)

    graphic.draw_objects(move_list)

    

    for move in move_list:

        x = move[1]

        y = move[2]

        draw_width = move[3]

        new_draw_x = x

        

        if mouseX < width * 0.25:
            x -= 1
            new_draw_x = x
            if new_draw_x < 0 - draw_width * 0.5:
                new_draw_x = width + draw_width * 0.5

        if mouseX > width * 0.75:
           x += 1
           new_draw_x = x
           if new_draw_x > width + draw_width * 0.5:
                new_draw_x = 0 -draw_width * 0.5

        move[1] = new_draw_x
