from pico2d import*

class Normal_Zombie:
    def __init__(self):
        self.x, self.y = 300,619
        self.frame =0
        self.dir = 1
        self.normal_zombie = load_image('norm_zombie.png')

    def update(self):
        self.y -= self.dir
        self.frame = (self.frame+1)%11

    def draw(self):
        self.normal_zombie.clip_draw(0,self.frame*31,25,28,300,self.y)



