from pico2d import *
import gfw
from gobj import *
from zombie import Zombie

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
		