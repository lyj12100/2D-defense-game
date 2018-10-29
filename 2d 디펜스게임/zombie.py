from pico2d import*

class MoveState:
    @staticmethod
    def enter(zombie):
        zombie.frame = 0
        zombie.dir = zombie.velocity

    @staticmethod
    def exit(zombie):
        pass

    @staticmethod
    def do(zombie):
        zombie.frame = (zombie.frame+1)%11
        zombie.y += zombie.velocity

    @staticmethod
    def draw(zombie):
        zombie.image.clip_draw(0,zombie.frame*31,25,28,300,y)

class Zombie:
    def __init__(self):
        self.x, self.y = 300,619
        self.image = load_image('norm_zombie.png')
        self.dir = 1

    def update(self):
        self.velocity += 1



