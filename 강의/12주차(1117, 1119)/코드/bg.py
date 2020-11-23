from pico2d import *
import gfw
import player

def init():
	global space, stars
	space = gfw.image.load('res/outerspace.png')
	stars = gfw.image.load('res/stars.png')

def draw():
	x, y = get_canvas_width() // 2, get_canvas_height() // 2
	px, py = player.pos
	dx, dy = x-px, y-py #플레이어가 중심에서 얼마나 떨어져있는지
	space.draw(x + dx * 0.02, y + dy * 0.02) #플레이어가 움직일 때 얼마만큼 같이 움직이는지(2%만큼, 5%만큼)
	stars.draw(x + dx * 0.05, y + dy * 0.05)

def update():
	pass