class Shaking:
    def __init__(self, obj, time, move_speed, range_x, range_y, is_repeat):
        self.obj = obj
        self.start_x = self.obj[1]
        self.start_y = self.obj[2]
        self.time_anim = 0.0
        self.shake_time = time
        self.is_anim = False
        self.range_x = range_x
        self.range_y = range_y
        self.norm_x = 1
        self.norm_y = 1
        self.move_speed = move_speed
        self.is_repeat = is_repeat
        
    def start(self):
        self.is_anim = True
        
    def stop(self):
        self.is_anim = False
        self.obj[1] = self.start_x
        self.obj[2] = self.start_y 
        self.time_anim = 0.0
        self.norm_x = 1
        self.norm_y = 1
        
    def update(self, ellapse):
        if not self.is_anim:
            return
         
        self.time_anim += ellapse
        if self.time_anim < self.shake_time or self.is_repeat:
            if self.norm_x > 0:
                self.obj[1] = min(self.obj[1] + self.norm_x * self.move_speed, self.start_x + self.range_x)
                
                if self.obj[1] == (self.start_x + self.range_x):
                    self.norm_x *= -1
                pass
            else:
                self.obj[1] = max(self.obj[1] + self.norm_x * self.move_speed, self.start_x - self.range_x)
                if self.obj[1] == (self.start_x - self.range_x):
                    self.norm_x *= -1
                pass
                
            if self.norm_y > 0:
                self.obj[2] =  min(self.obj[2] + self.norm_y * self.move_speed, self.start_y + self.range_y)
                if self.obj[2] == (self.start_y + self.range_y):
                    self.norm_y *= -1
                pass
            else:
                self.obj[2] =  max(self.obj[2] + self.norm_y * self.move_speed, self.start_y - self.range_y)
                if self.obj[2] == (self.start_y - self.range_y):
                    self.norm_y *= -1
                pass
        else:
            self.stop()
            
    
