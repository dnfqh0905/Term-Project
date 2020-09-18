import turtle
turtle
<module 'turtle' from 'C:\\Users\\mjy31\\AppData\\Local\\Programs\\Python\\Python38\\lib\\turtle.py'>
turtle.forward(100)
turtle.shape('turtle')
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(30)
turtle.forward(100)
turtle.reset()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.reset()
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)

turtle.reset()
for i in range(4) :
    turtle.forward(100)
    turtle.left(90)

	
for i in range(3) :
    turtle.forward(100)
    turtle.left(120)

	
turtle.reset()
for i in range(5) :
    turtle.forward(100)
    turtle.left(144)

	
turtle.reset()
for i in range(6) :
    turtle.forward(100)
    turtle.left(60)

	
turtle.circle(100)
turtle.reset()
turtle.right(90)
turtle.circle(100)

turtle.reset()
for i in range(6) :
    turtle.forward(100)
    turtle.left(60)
turtle.undo()
turtle.undo()

turtle.reset()
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.forward(100)
turtle.backward(100)
turtle.goto(100,100)
turtle.setheading(190)

turtle.reset()
turtle.penup()
turtle.goto(200,200)
turtle.pendown()
turtle.circle(50)
turtle.write("(200, 200)")
turtle.reset()

import random
random.randint(1,6)
6
random.randint(1,6)
6
random.randint(1,6)
3
random.randint(1,6)
2
random.uniform(1.2,3.4)
1.4008479848956683
random.uniform(1.2,3.4)
3.0614134946890186
random.uniform(1.2,3.4)
1.612251909579929

v=input("Hello")
Hello
v
''
v=input("Hello")
Hello48
v
'48'
v*10
'48484848484848484848'
type(v)
<class 'str'>

vv=int(v)
vv
48
v
'48'
type(vv)
<class 'int'>
vv * 10
480
int("Hello")
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    int("Hello")
ValueError: invalid literal for int() with base 10: 'Hello'

"KOREA" == "korea"
False
'asdf' == "asdf"
True

if vv>10:
    print("lage")
lage
vv = 56
vv = 5
if vv>10:
	print("large")

vv = 56
if vv>10:
    print("Hello")
    print("World")
	
Hello
World

if vv>10:
    print("Hello")
elif(vv<10):
    print("World")
else:
    print("END")
	
Hello
vv = 0
if vv>10:
    print("Hello")
elif(vv<10):
    print("World")
else:
    print("END")
	
World

turtle.reset()
count = 1
while(count<100):
    turtle.forward(200)
    turtle.left(30)
