from pico2d import *
import gfw
from gobj import *

class Character:	
	def __init__(self):         
		self.pos = 1300, 680
		self.image = gfw.image.load('res/Character_1.png')

	def update(self):
		pass

	def draw(self):
		self.image.draw(*self.pos)
		draw_rectangle(*self.get_bb()) 

	def get_bb(self):
		hw = self.image.w - 80
		hh = self.image.h - 80
		x,y = self.pos
		return x - hw, y - hh, x + hw, y + hh	
		