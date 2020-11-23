import random
from pico2d import *
import gfw
from gobj import *

class Zombie:
    def __init__(self):
        self.pos = random.choice([(1700, 500), (1700, 300), (1700, 700), (1700, 100)])
        self.delta = 0.3, 0
        self.speed = 200
        self.image = gfw.image.load('res/Monster.png')
        self.time = 0
        self.atk = 50

    def update(self):
        self.time += gfw.delta_time

        x,y = self.pos
        dx,dy = self.delta
        x -= dx * self.speed * gfw.delta_time
        y -= dy

        self.pos = x,y

    def draw(self):
        self.image.draw(*self.pos)
        draw_rectangle(*self.get_bb())    

    def get_bb(self):
        hw = self.image.w - 60
        hh = self.image.h - 100
        x,y = self.pos
        return x - hw, y - hh, x + hw, y + hh        