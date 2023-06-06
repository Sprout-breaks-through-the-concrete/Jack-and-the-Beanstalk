add_library('sound')
from environment import *
import logger
from guard import *
import object_maker
import graphic
import resource
import resource2
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
star_offset = -900
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

move_obj_list = []
move_obj_list2 = []
move_obj_list_sky = []
move_obj_list_space = []

sky_moving_anim = None

prev_mouse_x = 0
prev_mouse_y = 0

bird_list = []
bird_moving_anim = None
bird_sound = None

is_final_phase = False
break_count = 0
break_sound = None
breaking_sound = None
growing_sound = None
growing_sound_ellapsed = 0.0
break_max_count = 10

background_sound = None

breaking_target = None
beanstalk_shaking_anim = None
beanstalk_breaking_anim = None
background_color = None

def setup():
    GuardDebug()
    global stars, flower_list, beanstalk_shaking_anim, \
    breaking_target, break_sound, spacebar_shaking_anim, \
    spacebar, spacebar_list, grow_height, \
    background_color, bird_list, bird_moving_anim, \
    beanstalk_breaking_anim, breaking_sound, bird_sound, \
    prev_mouse_x, prev_mouse_y, move_obj_list, \
    move_obj_list2, move_obj_list_sky, move_obj_list_space, \
    sky_moving_anim, growing_sound, background_sound
    
    prev_mouse_x = width * 0.5
    prev_mouse_y = height
    
    break_sound = SoundFile(this, "treechop.wav")
    breaking_sound = SoundFile(this, "tree-falling.wav")
    bird_sound = SoundFile(this, "bird_sound.wav")
    growing_sound = SoundFile(this, "plant-growing.wav")
    background_sound = SoundFile(this, "sky-loop.wav")

    background_sound.loop()
    
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
    breaking_target = [resource.beanstalk7, width*0.5, height, 500, 800]
    beanstalk_shaking_anim = animation.Shaking(breaking_target, 500, 3, 5, 0, False)
    beanstalk_breaking_anim = animation.Shaking(breaking_target, 500, 3, 5, 9999999, True)
    beanstalk7_list.append(breaking_target)
    spacebar = [resource.spacebar, width * 0.95, height * 0.5, 60, 40]
    spacebar_list.append(spacebar)
    
    spacebar_shaking_anim = animation.Shaking(spacebar, 500, 1, 0, 10, True)
    spacebar_shaking_anim.start()
    background_color = color(135, 206, 250)
    bird_list.append([resource2.bird_V1, width*0.1, height*0.6, 50, 50])
    bird_list.append([resource2.bird_V2, width*0.5, height*0.5, 50, 50])
    bird_list.append([resource2.bird_V3, width*0.9, height*0.4, 50, 50])
    
    bird_moving_anim = animation.BirdMoving(bird_list, -30, width + 30, 150, 10, 2000, 0)
    
    move_obj_list.append([resource.tree, width*0.1, height*0.85, 100, 250])
    move_obj_list.append([resource.tree, width*0.3, height*0.85, 100, 250])
    move_obj_list.append([resource.tree, width*0.7, height*0.85, 100, 250])
    move_obj_list.append([resource.tree, width*0.9, height*0.85, 100, 250])
    move_obj_list.append([resource.flower, width*0.05, height*0.97, 30, 70])
    move_obj_list.append([resource.flower, width*0.15, height*0.97, 30, 70])
    move_obj_list.append([resource.flower, width*0.25, height*0.97, 30, 70])
    move_obj_list.append([resource.flower, width*0.35, height*0.97, 30, 70])
    move_obj_list.append([resource.flower, width*0.65, height*0.97, 30, 70])
    move_obj_list.append([resource.flower, width*0.75, height*0.97, 30, 70])
    move_obj_list.append([resource.flower, width*0.85, height*0.97, 30, 70])
    move_obj_list.append([resource.flower, width*0.95, height*0.97, 30, 70])
    
    move_obj_list_sky.append([resource2.cloud1, width*0.01, height*0.05, 90, 60])
    move_obj_list_sky.append([resource2.cloud1, width*0.3, height*0.1, 60, 40])
    move_obj_list_sky.append([resource2.cloud1, width, height*0.25, 90, 60])
    move_obj_list_sky.append([resource2.cloud1, width*0.8, height*0.2, 60, 40])
    move_obj_list_sky.append([resource2.cloud1, width*0.5, height*0.25, 60, 40])
    move_obj_list_sky.append([resource2.cloud1, width*0.7, height*0.01, 60, 40])
    move_obj_list_sky.append([resource2.chicken, width*0.5, height*0.2, 50, 60])
    
    sky_moving_anim = animation.BirdMoving(move_obj_list_sky, -50, width + 50, 0, 2, 0, 20)
    
    move_obj_list2.append([resource.sun, width*0.1, -200, 100, 250])
    
    move_obj_list_space.append([resource2.wire, width*0.9, -height * 2 + 100, 5, 300])
    move_obj_list_space.append([resource.moon, width*0.9, -height - 600, 100, 250])
    move_obj_list_space.append([resource2.wire, width*0.15, -height * 2, 5, 500])
    move_obj_list_space.append([resource2.haff, width*0.15, -height - 550, 60, 60])
    move_obj_list_space.append([resource2.wire, width*0.6, -height * 2, 3, 200])
    move_obj_list_space.append([resource2.haff, width*0.6, -height - 700, 40, 40])
    move_obj_list_space.append([resource2.wire, width*0.35, -height * 2, 5, 250])
    move_obj_list_space.append([resource2.pocket, width*0.35, -height - 680, 60, 60])

def draw():
    GuardDebug()
    clear()
    global grow_height, grow_speed, grow_time, \
     prev_time, flower_list, flower, \
     flower_per_size, space_per_size, spacebar, \
     space_anchor, is_final_phase, beanstalk_shaking_anim, \
     spacebar_shaking_anim, spacebar_list, \
     background_color, bird_list, bird_moving_anim, \
     beanstalk_breaking_anim, breaking_sound, move_obj_list, \
     star_offset, move_obj_list2, move_obj_list_sky, \
     move_obj_list_space, sky_moving_anim, growing_sound_ellapsed, \
     growing_sound
     
    background(background_color)
    current_time = millis()
    ellapse_time = current_time - prev_time
    grow_time += ellapse_time
    main_logger.debug("grow_time=" + str(grow_time))
    main_logger.debug("grow_height=" + str(grow_height))
    prev_time = current_time
    graphic.draw_star(stars, star_offset)
    
    graphic.draw_objects(move_obj_list)
    graphic.draw_objects(move_obj_list2)
    graphic.draw_objects(move_obj_list_sky)
    graphic.draw_objects(move_obj_list_space)
    
    if is_final_phase:
        beanstalk_shaking_anim.update(ellapse_time)
        spacebar_shaking_anim.update(ellapse_time)
        beanstalk_breaking_anim.update(ellapse_time)
        graphic.draw_static_objects(beanstalk7_list, flower_per_size, flower_anchor)
        graphic.draw_static_objects(spacebar_list, space_per_size, space_anchor)
        return
    
    if growing_sound.isPlaying():
        growing_sound_ellapsed += ellapse_time
        if growing_sound_ellapsed > 1000.0:
            growing_sound.pause()
            pass
    
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
        
    bird_moving_anim.update(ellapse_time)
    sky_moving_anim.update(ellapse_time)
    graphic.draw_objects(bird_list)
    
    if bird_moving_anim.is_show():
        if not bird_sound.isPlaying():
            bird_sound.play()
            
def try_break_beanstalk():
    global break_count, break_sound, beanstalk_shaking_anim, break_max_count, beanstalk_breaking_anim, breaking_sound
    
    if beanstalk_shaking_anim.is_anim or break_count >= break_max_count:
        return
    
    break_count += 1
    
    if break_max_count == break_count:
        breaking_sound.play()
        beanstalk_breaking_anim.start()
    else:
        break_sound.play()    
        beanstalk_shaking_anim.start()

def keyPressed():
    global is_final_phase, grow_height
    if key == ' ':
        if is_final_phase:
            try_break_beanstalk()
        elif grow_height >= PHASE_6:        
            is_final_phase = True
            try_break_beanstalk()

def mouseMoved():
    global grow_height, background_color, is_final_phase, \
    prev_mouse_x, prev_mouse_y, bird_list, \
    bird_moving_anim, move_obj_list, star_offset, \
    move_obj_list2, move_obj_list_sky, move_obj_list_space, \
    growing_sound, growing_sound_ellapsed
    
    grow_height = height - mouseY
    
    move_x = mouseX - prev_mouse_x 
    move_y = prev_mouse_y - mouseY
    
    prev_mouse_x = mouseX
    prev_mouse_y = mouseY
    
    if is_final_phase:
        return
    
    if move_y > 0:
        grow_weight = (growing_sound.duration() - 4.0) * norm(grow_height, 0, height)
        print(grow_weight)
        growing_sound.cue(grow_weight)
        growing_sound.play()
        growing_sound_ellapsed = 0.0
    
    bird_moving_anim.offset += move_y * 2
    
    for obj in move_obj_list:
        obj[2] += move_y * 1
    
    for obj in move_obj_list2:
        obj[2] += move_y * 2
        
    for obj in move_obj_list_space:
        obj[2] += move_y * 2
        
    sky_moving_anim.offset += move_y * 2
    
    star_offset += move_y * 1
    
    if mouseY >= height * 0.55: #skyblue-pink
        background_color = lerpColor(color(255, 192, 203), color(135, 206, 250), (mouseY - height * 0.55) / (height * 0.25))
    elif mouseY >= height * 0.3: #pink-purple
        background_color = lerpColor(color(128, 0, 128), color(255, 192, 203), (mouseY - height * 0.3) / (height * 0.25))
    elif mouseY >= height * 0.05:  #purple-navy
        background_color = lerpColor(color(0, 0, 128), color(128, 0, 128), (mouseY - height * 0.05) / (height * 0.25))
    else: #navy-black
        background_color = lerpColor(color(0, 0, 0), color(0, 0, 128), mouseY / (height * 0.05))
