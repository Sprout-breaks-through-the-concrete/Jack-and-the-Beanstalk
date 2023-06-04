add_library('sound')
from environment import *
import logger
from guard import *
import object_maker
import graphic
import resource
import animation

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
spacebar_list = []
spacebar = None
space_per_size = 5
space_anchor = graphic.RIGHT
spacebar_shaking_anim = None

is_final_phase = False
break_count = 0
break_sound = None
break_max_count = 10

breaking_target = None
beanstalk_shaking_anim = None

def setup():
    GuardDebug()
    global stars, flower_list, beanstalk_shaking_anim, breaking_target, break_sound, spacebar_shaking_anim, spacebar, spacebar_list, grow_height
    break_sound = SoundFile(this, "treechop.wav")

    if USE_STROKE == False:
        noStroke()
        
    size(WINDOW_WIDTH, WINDOW_HEIGHT)
    prev_time = millis()
    stars.extend(object_maker.make_stars(0, 0, width, height, 1, 20))
    object_list.append([resource.flower, width*0.2, height*0.5, 100, 150])
    object_list.append([resource.flower, width*0.5, height*0.8, 150, 50])
    object_list.append([resource.tree, width*0.8, height*0.8, 100, 150])
    object_list.append([resource.sun, width*0.2, height*0.7, 100, 150])
    object_list.append([resource.moon, width*0.8, height*0.5, 200, 100])
    beanstalk1_list.append([resource.beanstalk1, width*0.5, height, 60, 40])
    beanstalk2_list.append([resource.beanstalk2, width*0.5, height, 100, 150])
    beanstalk3_list.append([resource.beanstalk3, width*0.5, height, 100, 150])
    beanstalk4_list.append([resource.beanstalk4, width*0.5, height, 100, 300])
    beanstalk5_list.append([resource.beanstalk5, width*0.5, height, 300, 700])
    beanstalk6_list.append([resource.beanstalk6, width*0.5, height, 400, 600])
    breaking_target = [resource.beanstalk7, width*0.5, height, 500, 800]
    beanstalk_shaking_anim = animation.Shaking(breaking_target, 500, 3, 5, 0, False)
    beanstalk7_list.append(breaking_target)
    spacebar = [resource.spacebar, width * 0.95, height * 0.5, 60, 40]
    spacebar_list.append(spacebar)
    #spacebar_list.append(spacebar)
    spacebar_shaking_anim = animation.Shaking(spacebar, 500, 1, 0, 10, True)
    spacebar_shaking_anim.start()
          
def draw():
    GuardDebug()
    clear()
    global grow_height, grow_speed, grow_time, prev_time, flower_list, flower, flower_per_size, space_per_size, spacebar, space_anchor, is_final_phase, beanstalk_shaking_anim, spacebar_shaking_anim, spacebar_list
    
    current_time = millis()
    ellapse_time = current_time - prev_time
    grow_time += ellapse_time
    main_logger.debug("grow_time=" + str(grow_time))
    main_logger.debug("grow_height=" + str(grow_height))
    prev_time = current_time
    print(grow_height)
    graphic.draw_star(stars)
    #graphic.draw_objects(object_list)
    
    if is_final_phase:
        beanstalk_shaking_anim.update(ellapse_time)
        graphic.draw_static_objects(beanstalk7_list, flower_per_size, flower_anchor)
        graphic.draw_static_objects(spacebar_list, space_per_size, space_anchor)
        return
    
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
    elif grow_height<PHASE_6:
        graphic.draw_static_objects(beanstalk6_list,flower_per_size, flower_anchor)        
        pass    
    else :
        spacebar_shaking_anim.update(ellapse_time)
        graphic.draw_static_objects(beanstalk7_list, flower_per_size, flower_anchor)
        graphic.draw_static_objects(spacebar_list, space_per_size, space_anchor)
        pass    

def try_break_beanstalk():
    global break_count, break_sound, beanstalk_shaking_anim, break_max_count
    
    if beanstalk_shaking_anim.is_anim or break_count >= break_max_count:
        return
    
    break_count += 1
    break_sound.play()
    beanstalk_shaking_anim.start()
    
    if break_max_count == break_count:
        pass

def keyPressed():
    global is_final_phase, grow_height
    if key == ' ':
        if is_final_phase:
            try_break_beanstalk()
        elif grow_height >= PHASE_6:        
            is_final_phase = True
            try_break_beanstalk()
    if mouseY >  WINDOW_HEIGHT:
        for object_y in object_list:
            object_y[2] -= 1
    if mouseY <= WINDOW_HEIGHT/2:
        for object_y in object_list:
            object_y[2] += 1
    
def mouseMoved():
    global grow_height
    grow_height = height - mouseY
