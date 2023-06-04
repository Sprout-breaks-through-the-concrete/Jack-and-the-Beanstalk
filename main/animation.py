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
            
    
class BirdMoving:
    def __init__(self, obj_list, start_x, end_x, moving_height, move_speed, interval, offset):
        self.obj_list = obj_list
        self.is_moving = [True for x in range(len(obj_list))]
        self.ellapsed_time = [0.0 for x in range(len(obj_list))]
        self.obj_x_pos = [obj[1] for obj in obj_list]
        self.obj_heights = [obj[2] for obj in obj_list]
        self.start_x = float(start_x)
        self.end_x = float(end_x)
        self.moving_height = moving_height
        self.interval = interval
        self.move_speed = move_speed
        self.offset = offset
    
    def update(self, ellapse):
        
        for idx, obj in enumerate(self.obj_list):
            self.ellapsed_time[idx] += ellapse
            
            if self.is_moving[idx]:
                self.obj_x_pos[idx] += self.move_speed
                obj[1] = self.obj_x_pos[idx]
                weight = -sin(TWO_PI * norm((self.obj_x_pos[idx] - self.start_x) / (self.end_x - self.start_x), -1, 1))
                print(weight)
                obj[2] = self.obj_heights[idx] + self.moving_height * weight + self.offset
                
                if self.obj_x_pos[idx] > self.end_x:
                    self.is_moving[idx] = False
                    self.ellapsed_time[idx] = 0.0
                
                #if self.ellapsed_time < self.moving_time:
                    #anim_weight = float(self.ellapsed_time) / self.end_x
                    #obj_x_pos[idx] += m
                    #obj[1] = 
                    #obj[1] = lerp(self.start_x, self.end_x, anim_weight)
                    #obj[2] = lerp(self.obj_heights[idx], self.obj_heights[idx] + self.moving_height, )
                #else:
                    #obj[1] = self.end_x
                    #obj[2] = self.obj_heights[idx]
                    #self.is_moving[idx] = False
            else:
                if self.ellapsed_time[idx] < self.interval:
                    pass
                else:
                    self.is_moving[idx] = True
                    self.ellapsed_time[idx] = 0.0
                    self.obj_x_pos[idx] = self.start_x
                    obj[1] = self.obj_x_pos[idx]
                    
    def is_show(self):
        for obj in self.obj_list:
            if 0 <= obj[2] <= height:
                return True
        return False
        
