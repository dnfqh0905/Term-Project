import random
import gfw
from pico2d import *
import gobj
from zombie import Zombie
import fence
from character import Character

canvas_width = 1600
canvas_height = 900

def enter():
    gfw.world.init(['tile', 'fence', 'character', 'zombie', 'ui', 'menu'])    
    
    for y in range(canvas_height, 0, -200):
        for x in range(-100, canvas_width, 200):
            tile = gobj.ImageObject('tile_1.png', x, y)
            gfw.world.add(gfw.layer.tile, tile)
    fence.init()
    gfw.world.add(gfw.layer.fence, fence)
    ui = gobj.ImageObject('Wood.png', canvas_width-1450, canvas_height-55)
    gfw.world.add(gfw.layer.ui, ui)
    menu = gobj.ImageObject('menu.png', canvas_width-100, canvas_height-55)
    gfw.world.add(gfw.layer.menu, menu)

    global character
    character = Character()

    global zombie_time
    zombie_time = 1

    global font
    font = gfw.font.load('res/CookieRun Regular.ttf', 40)

    global gold
    gold = 1000

def check_enemy(e):
    global gold, destroy
    if gobj.collides_box(character, e):
        gfw.world.remove(e)
        gold += 100
    if gobj.collides_box(fence, e):
        e.speed = 0


def create():	
    gfw.world.add(gfw.layer.character, character)

def update():
    gfw.world.update()
    gobj.draw_collision_box()

    global zombie_time
    zombie_time -= gfw.delta_time
    if zombie_time <= 0:
        gfw.world.add(gfw.layer.zombie, Zombie())
        zombie_time = 5

    for e in gfw.world.objects_at(gfw.layer.zombie):
        check_enemy(e)    

def draw():
    gfw.world.draw()
    menu_pos = get_canvas_width() - 170, get_canvas_height() - 50
    font.draw(*menu_pos, 'MENU', (255,255,255))
    gold_pos = get_canvas_width() - 1550, get_canvas_height() - 60
    font.draw(*gold_pos, 'Coin:%d' % gold, (0,0,0))


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
    elif e.type == SDL_MOUSEBUTTONDOWN:
    	create()            

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()