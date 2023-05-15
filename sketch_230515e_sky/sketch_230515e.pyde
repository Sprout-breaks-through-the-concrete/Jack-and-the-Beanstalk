def setup():
    size(800, 800)

def draw():
    
    
    
   
    

    if mouseY >= width / 2:
        mouse_pos = float(mouseY) / float(width)
        background(lerpColor(color(135, 206, 235),color(128, 0, 128), mouse_pos))
    else:
        mouse_pos = float(mouseY) / float(width / 2)
        background(lerpColor(color(128, 0, 128),color(135, 206, 235), mouse_pos))
        
