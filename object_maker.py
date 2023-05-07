import random
from guard import *

def make_stars(left, top, range_x, range_y, particle_size, star_count):
    Guard()
    result = []
    for i in range(star_count):
        rand_x = random.randint(left, left + range_x)
        rand_y = random.randint(top, top + range_y)
        
        start_angle = random.uniform(0, TWO_PI)
        per_angle = TWO_PI * 0.2
        half_angle = TWO_PI * 0.1
        
        for point_idx in range(5):
            point_x = rand_x + cos((start_angle + point_idx) * per_angle) * particle_size
            point_y = rand_y + sin((start_angle + point_idx) * per_angle) * particle_size
            result.append([point_x, point_y])
            point_x = rand_x + cos((start_angle + point_idx) * per_angle + half_angle) * particle_size * 5.0
            point_y = rand_y + sin((start_angle + point_idx) * per_angle + half_angle) * particle_size * 5.0
            result.append([point_x, point_y])
            
    return result
