from pico2d import*
import random
import math
import threading

class Normal_Zombie:
    def __init__(self):

        self.x, self.y = random.randrange(330,482,76),619
        #self.x, self.y = 406,619
        self.frame =0
        self.dirY = 1
        self.dirX = 1
        self.normal_zombie = load_image('norm_zombie.png')


    def update(self):
        self.frame = (self.frame+1)%11



    def draw(self):

        if self.y > 375: #or self.x==406 :
            self.y -= self.dirY
            self.normal_zombie.clip_draw(0, self.frame * 31, 25, 28, self.x, self.y)
        #오른쪽으로 방향전환
        if self.y == 375 and self.x < 406:
            self.x += self.dirX
            self.normal_zombie.clip_composite_draw(0, self.frame * 31, 25, 28, 3.141592 / 2, '',
                                                   self.x, self.y, 25,28)
        #왼쪽으로 방향전환
        if self.y == 375 and self.x>406:
            self.x -= self.dirX
            self.normal_zombie.clip_composite_draw(0, self.frame * 31, 25, 28, -3.141592 / 2, '',
                                                   self.x, self.y, 25, 28)

        if self.x == 406 and self.y <= 375: #or self.x==406:
            self.y -= self.dirY
            self.normal_zombie.clip_draw(0, self.frame * 31, 25, 28, self.x, self.y)

        delay(0.05)



class Fast_Zombie:
    def __init__(self):
        self.x, self.y = random.randrange(330, 481, 75), 619
        self.frame = 0
        self.dirY = 2
        self.dirX = 2
        self.fast_zombie = load_image('fast_zombie.png')

    def update(self):
        #fast.y -= fast.dir
        self.frame = (self.frame +1)%5

    def draw(self):
        if self.y > 375: #or self.x == 406 :
            self.y -= self.dirY
            self.fast_zombie.clip_draw(0, self.frame * 47, 23, 46, self.x, self.y)
        #if self.y > 375 and self.x==406:
            #self.y -= self.dirY
            #self.fast_zombie.clip_draw(0, self.frame * 47, 23, 46, self.x, self.y)
        #오른쪽으로 방향전환
        if self.y == 375 and self.x < 406:
            self.x += self.dirX
            self.fast_zombie.clip_composite_draw(0, self.frame * 47, 23, 46, 3.141592 / 2, '',
                                                 self.x, self.y, 23,46)
        #왼쪽으로 방향전환
        if self.y == 375 and self.x>406:
            self.x -=self.dirX
            self.fast_zombie.clip_composite_draw(0, self.frame * 47, 23, 46, -3.141592 / 2, '',
                                                 self.x, self.y, 23, 46)

        if self.x == 406 and self.y <= 375:
            self.y -= self.dirY
            self.fast_zombie.clip_draw(0, self.frame * 47, 23, 46, self.x, self.y)

        delay(0.01)


#class New():
#    Normal_Zombie = None

#   def __init__(self):
#        pass

#    def add_enemy(self):
#        threading.Timer(3,Normal_Zombie)

#    def draw(self):
