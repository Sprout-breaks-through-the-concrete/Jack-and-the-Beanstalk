from environment import STAR_COLOR
from guard import *
import logger

draw_logger = logger.get("draw")

def draw_pixel(x, y, pixel_color, per_width, per_height):
    Guard()
    prev_color = g.fillColor
    fill(pixel_color)
    rect(x, y, per_width, per_height)
    fill(prev_color)
    
    
def draw_objects(obj_list):
    Guard()
    for obj in obj_list:
        draw_object(obj[0], obj[1], obj[2], obj[3], obj[4])
    
def draw_object(resource, center_x, center_y, draw_width, draw_height):
    Guard()
    start_x = center_x - draw_width * 0.5
    start_y = center_y - draw_height * 0.5
    per_height = draw_height / max(len(resource), 1)
    for y, x_array in enumerate(resource):
        per_width = draw_width / max(len(x_array), 1)
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
