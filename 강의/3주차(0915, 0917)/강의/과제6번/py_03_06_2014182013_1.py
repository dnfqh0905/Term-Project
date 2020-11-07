from pico2d import *
from helper import move_toward, delta

class Boy: 
	def __init__(self): 
		self.x, self.y = get_canvas_width() // 2, 85  
		self.image = load_image('../res/run_animation.png')
		self.dx = 0
		self.dy = 0
		self.frame = 0
	def draw(self):
		self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
	def update(self):
		self.x += self.dx * 5
		self.y += self.dy * 5
		self.frame = (self.frame + 1) % 8

class Grass:
	def __init__(self):
		self.x, self.y = 400, 30
		self.image = load_image('../res/grass.png')
	def draw(self):
		self.image.draw(self.x, self.y)

def handle_events():
	global running, boy
	evts = get_events()
	for e in evts:
		if e.type == SDL_QUIT:
			running = False
		elif e.type == SDL_KEYDOWN:
			if e.key == SDLK_ESCAPE:
				running = False
			elif e.key ==SDLK_LEFT:
				boy.dx -= 1
			elif e.key ==SDLK_RIGHT:
				boy.dx += 1
		elif e.type == SDL_KEYUP:
			if e.key ==SDLK_LEFT:
				boy.dx += 1
			elif e.key ==SDLK_RIGHT:
				boy.dx -= 1
		elif e.type == SDL_MOUSEBUTTONDOWN:
			boy.x, boy.y = move_toward((boy.x, boy.y), delta((boy.x, boy.y), (e.x, e.y), 10), (e.x, e.y))

open_canvas()


boy = Boy() 
grass = Grass()

running = True

while running :

	clear_canvas()
	grass.draw()
	boy.draw()	
	
	update_canvas()

	handle_events()

	boy.update() 
	

	delay(0.01)

close_canvas()
