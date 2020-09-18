from pico2d import *

open_canvas()
img = load_image('이미지/run_animation.png')
gra = load_image('이미지/grass.png')

frame = 0
for x in range(0, 800, 2):
	#delay(1)
	#print("Clearing Canvas")
	clear_canvas()
	#delay(1)
	#print("Drawing Grass")
	gra.draw(400,30)
	#delay(1)
	#print("Drawing Character")
	img.clip_draw(frame * 100, 0, 100, 100, x, 80)	

	update_canvas()

	#frame += 1
	#if frame >= 8:		frame = 0
	frame = (frame + 1) % 8
	
	get_events()
	delay(0.01)

delay(5)
close_canvas()
