from pico2d import *

def handle_events():
	global running, x, dx
	evts = get_events()
	for e in evts:
		if e.type == SDL_QUIT:
			running = False
		elif e.type == SDL_KEYDOWN:
			if e.key == SDLK_ESCAPE:
				running = False
			elif e.key ==SDLK_LEFT:
				dx -= 1
			elif e.key ==SDLK_RIGHT:
				dx += 1
		elif e.type == SDL_KEYUP:
			if e.key ==SDLK_LEFT:
				dx += 1
			elif e.key ==SDLK_RIGHT:
				dx -= 1

open_canvas()
img = load_image('../../이미지/run_animation.png')
gra = load_image('../../이미지/grass.png')

running = True
x = get_canvas_width() // 2
dx = 0
frame = 0
while running :
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

	#x += 2
	x += dx * 5
	#frame += 1
	#if frame >= 8:		frame = 0
	frame = (frame + 1) % 8	

	handle_events()

	delay(0.01)

#delay(5)
close_canvas()
