import random
import json
import os

from pico2d import*

import game_framework
import game_world

import tower
from zombie import Normal_Zombie
from zombie import Fast_Zombie


from map import Map

name = "MainState"

normal_zombie = None
fast_zombie = None
tower1 = None
map = None


def enter():
    global normal_zombie ,fast_zombie, map, tower1
    normal_zombie = Normal_Zombie()
    fast_zombie = Fast_Zombie()
    tower1 = tower.Tower1()
    map = Map()
    game_world.add_object(map,0)
    game_world.add_object(normal_zombie,1)

    game_world.add_object(fast_zombie,1)
    game_world.add_object(tower1,1)

def exit():
    game_world.clear()

def pause():
    pass
def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
