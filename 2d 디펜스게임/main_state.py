import random
import json
import os

from pico2d import*

import map

def draw():
    clear_canvas()
    map.draw()
    update_canvas()
