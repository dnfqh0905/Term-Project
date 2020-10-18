from pico2d import *
import gfw

RES_DIR = './res'

class ImageObject:
	def __init__(self, imageName, x, y):
		self.image = gfw.image.load(RES_DIR + '/' + imageName)
		self.x, self.y = x, y
	def draw(self):
		self.image.draw(self.x, self.y)
	def update(self):
		pass

if __name__ == "__main__":
	print("This file is not supposed to be executed directly.")