from pico2d import *
import gfw
from gobj import *

canvas_width = 1600
canvas_height = 900

class Character:	
	def __init__(self):         
		self.pos = 1300, 700
		self.image = gfw.image.load('res/Character_1.png')

	def update(self):
		pass

	def draw(self):
		self.image.draw(*self.pos)
		draw_rectangle(*self.get_bb()) 

	def get_bb(self):
		hw = self.image.w - 150
		hh = self.image.h - 120
		x,y = self.pos
		return x - hw, y - hh, x + hw, y + hh	
		