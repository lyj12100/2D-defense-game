from pico2d import*

class Map:
    def __init__(self):
        self.image = load_image('map.jpg')

    def draw(self):
        self.image.draw(684,619)

