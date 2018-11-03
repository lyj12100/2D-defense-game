from pico2d import*
import game_world




class Tower1:
    def __init__(self):
        self.x, self.y = 403,100
        global x,y
        self.tower1 = load_image('Tank1.png')

    def update(self):
        self.tower1

    def draw(self):
        self.tower1.draw_now(self.x,self.y)

    def handle_event(self):
        events = get_events()
        for event in events:
            while event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                self.tower1.draw(event.x,event.y)
