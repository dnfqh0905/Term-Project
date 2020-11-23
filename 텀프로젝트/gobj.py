from pico2d import *
import gfw

class ImageObject:
	def __init__(self, imageName, x, y):
		self.image = gfw.image.load('res/' + imageName)
		self.x, self.y = x, y
	def draw(self):
		self.image.draw(self.x, self.y)
	def update(self):
		pass

def collides_box(a, b):
	(la, ba, ra, ta) = a.get_bb()
	(lb, bb, rb, tb) = b.get_bb()

	if la > rb: return False
	if ra < lb: return False
	if ba > tb: return False
	if ta < bb: return False

	return True

def draw_collision_box():
	for obj in gfw.world.all_objects():
		if hasattr(obj, 'get_bb'):
			draw_rectangle(*obj.get_bb())

if __name__ == "__main__":
	print("This file is not supposed to be executed directly.")