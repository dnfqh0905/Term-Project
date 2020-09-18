import pico2d
Pico2d is prepared.
pico2d
<module 'pico2d' from 'C:\\Users\\mjy31\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages\\pico2d\\__init__.py'>
pico2d.open_canvas()
pico2d.close_canvas()
import pico2d as p
p.open_canvas()
p.close_canvas()
from random import randint
randint(1,6)
2
from random import randint as ri
ri(1,6)
5

from random import *
uniform(1,6)
2.829886806844197
randrange(10,20)
19
from pico2d import *
open_canvas()
close_canvas()

import os
os.getcwd()
'C:\\Users\\mjy31\\AppData\\Local\\Programs\\Python\\Python38'
os.listdir()
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python38.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll', 'vcruntime140_1.dll']
image = load_image('C:/Users/mjy31/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.8/new/dog.jpg')
image.draw_now(400,300)
os.chdir('C:/Users/mjy31/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.8/new')
os.listdir()
['dog.jpg']
image = load_image('dog.jpg')
close_canvas()

open_canvas()
os.chdir('C:\\Users\\mjy31\\OneDrive\\바탕 화면\\이미지')
os.listdir()
['animation_sheet.png', 'character.png', 'grass.png', 'run_animation.png']
image = load_image('character.png')
image.draw_now(300,200)
image.draw_now(400,300)
for x in (100, 700, 100):
    image.draw_now(x,500)

for x in (100, 700, 30):
    image.draw_now(x,100)

for x in (100, 701, 30):
    image.draw_now(x,100)

	
clear_canvas_now()
for y in range(100, 501, 80):
    for x in range(100, 701, 35):
    	image.draw_now(x,y)

		
for y in range(100, 501, 50):
    for x in range(100, 701, 35):
	image.draw_now(x,y)
		
os.getcwd()
'C:\\Users\\mjy31\\OneDrive\\바탕 화면\\이미지'
grass = load_image('grass.png')
grass.draw_now(400, 90)
clear_canvas_now()
