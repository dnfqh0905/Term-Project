from pico2d import *

open_canvas()
img = load_image('이미지/character.png')
gra = load_image('이미지/grass.png')

for x in range(0, 800, 2):
	clear_canvas_now()
	gra.draw_now(400,30)
	img.draw_now(x, 80)	
	delay(0.01)

delay(5)
close_canvas()
