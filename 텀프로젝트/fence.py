from pico2d import *
import gfw

canvas_width = 1600
canvas_height = 900

def init():
    global fence, fpos, hp
    fence = gfw.image.load('res/Fence.png')
    fpos = canvas_width-1550, canvas_height-500

def draw():
    fence.draw(*fpos)
    draw_rectangle(*get_bb())  

def update():
    pass

def get_bb():
    global hw, hh, x, y
    hw = 50
    hh = 400
    x,y = fpos
    return x - hw, y - hh, x + hw, y + hh    