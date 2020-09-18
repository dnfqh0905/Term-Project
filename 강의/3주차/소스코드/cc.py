from pico2d import *
from random import randint as rint
from random import random as rfloat

class Boy: 
	def __init__(self): 
		self.x = rint(100, 700)
		self.y = rint(100, 500)
		self.image = load_image('../../이미지/run_animation.png')
		self.dx = rfloat()
		self.frame = rint(0, 7)
	def draw(self):
		self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
	def update(self):
		self.x += self.dx * 5
		self.frame = (self.frame + 1) % 8	

class Grass:
	def __init__(self):
		self.x, self.y = 400, 30
		self.image = load_image('../../이미지/grass.png')
	def draw(self):
		self.image.draw(self.x, self.y)
