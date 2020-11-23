import random
from pico2d import *
import gfw


canvas_width = 1600
canvas_height = 900

def init():
    global fence, fpos
    fence = gfw.image.load('res/Fence.png')
    fpos = canvas_width-1550, canvas_height-500

def draw():
    fence.draw(*fpos)

def update():
    pass
