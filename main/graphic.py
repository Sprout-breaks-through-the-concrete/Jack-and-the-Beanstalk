from environment import STAR_COLOR
from guard import *
import logger

draw_logger = logger.get("draw")

TOP = 1
BOTTOM = 2
LEFT = 3
RIGHT = 4
CENTER = 5

def draw_pixel(x, y, pixel_color, per_width, per_height):
    Guard()
    prev_color = g.fillColor
    fill(pixel_color)
    rect(x, y, per_width, per_height)
    fill(prev_color)
    
    
def draw_objects(obj_list):
    Guard()
    for obj in obj_list:
        draw_object(obj[0], obj[1], obj[2], obj[3], obj[4], CENTER)
        
        
def draw_static_objects(obj_list, per_size, anchor):
    Guard()
    for obj in obj_list:
        draw_object(obj[0], obj[1], obj[2], per_size, per_size, anchor)
    
def draw_object(resource, center_x, center_y, draw_width, draw_height, anchor):
    Guard()
    
    start_x = center_x
    start_y = center_y
    per_height = draw_height
    per_width = draw_width
    
    objects = list(resource)
    
    if anchor == CENTER:
        start_x = center_x - draw_width * 0.5
        start_y = center_y - draw_height * 0.5
        per_height = draw_height / max(len(objects), 1)
    elif anchor == BOTTOM:
        objects.reverse()
        per_height *= -1
    elif anchor == RIGHT or anchor == LEFT:
        start_y = center_y - max(len(objects) * per_height, 1) * 0.5
    
    for y, objects_x in enumerate(objects):
        x_array = list(objects_x)
        if anchor == CENTER:
            per_width = draw_width / max(len(x_array), 1)
        elif anchor == TOP or anchor == BOTTOM:
            start_x = center_x - max(len(x_array) * per_width, 1) * 0.5
        elif anchor == RIGHT:
            x_array.reverse()
            per_width = draw_width * -1
            
        for x, obj_color in enumerate(x_array):
            draw_x = start_x + per_width * x
            draw_y = start_y + per_height * y
            if obj_color is not None:
                draw_pixel(draw_x, draw_y, obj_color, per_width, per_height)
    
def draw_star(star):
    Guard()
    prev_color = g.fillColor
    fill(STAR_COLOR)
    
    vertex_idx = 0
    
    beginShape()
    for vertex_pos in star:
        vertex(vertex_pos[0], vertex_pos[1])
        vertex_idx += 1
        
        # one star haves 10 vertexs 
        if vertex_idx > 9:
            endShape()
            beginShape()
            vertex_idx = 0
    endShape()
    
    fill(prev_color)
