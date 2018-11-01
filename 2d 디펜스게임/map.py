from pico2d import*

class Map:
    def __init__(self):
        self.image = load_image('map.jpg')

    def update(self):
        pass

    def draw(self):
        self.image.draw(864//2,619//2)


