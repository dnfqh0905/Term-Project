import gfw
from pico2d import *
import gobj

canvas_width = 1300
canvas_height = 900

def enter():
    gfw.world.init(['tile', 'fence', 'ui', 'menu'])
    
    for y in range(canvas_height, 0, -200):
        for x in range(0, canvas_width, 200):
            tile = gobj.ImageObject('tile_1.png', x, y)
            gfw.world.add(gfw.layer.tile, tile)
    fence = gobj.ImageObject('Fence.png', canvas_width//20, canvas_height//2.25)
    gfw.world.add(gfw.layer.fence, fence)
    ui = gobj.ImageObject('Wood.png', canvas_width//9.5, canvas_height//1.07)
    gfw.world.add(gfw.layer.ui, ui)
    menu = gobj.ImageObject('menu.png', canvas_width//1.1, canvas_height//1.07)
    gfw.world.add(gfw.layer.menu, menu)

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()