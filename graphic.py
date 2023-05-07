from environment import STAR_COLOR
from guard import *

def draw_pixel(x, y, color, diameter):
    Guard()
    prev_color = g.fillColor
    fill(particle_color)
    square(x, y, diameter)
    fill(prev_color)
    
    
def draw_object(object, center_x, center_y, obj_color, diameter):
    Guard()
    start_x = center_x - diameter * 0.5
    start_y = center_y - diameter * 0.5
    per_heigth = diameter / y
    for y in object:    
        per_width = diameter / len(object[y])
        for x in object[y]:
            draw_x = start_x + per_width * x 
            draw_y = start_y + per_height * y 
            
            draw_pixel(draw_x, draw_y, obj_color, diameter)
            
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
