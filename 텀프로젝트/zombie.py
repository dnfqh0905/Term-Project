import random
from pico2d import *
import gfw
from gobj import *

class Zombie:
    FPS = 12
    def __init__(self):
        self.pos = random.choice([(1200, 500), (1200, 300), (1200, 700), (1200, 100)])
        self.delta = 0.3, 0
        self.speed = 200
        self.y = get_canvas_height()
        self.image = gfw.image.load(RES_DIR + '/Monster.png')
        self.time = 0
        self.fidx = 0

    def update(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * Zombie.FPS)

        x,y = self.pos
        dx,dy = self.delta
        x -= dx * self.speed * gfw.delta_time
        y -= dy

        self.pos = x,y

    def draw(self):
        self.image.draw(*self.pos)