import turtle
turtle.penup()
turtle.goto(0,-400)
turtle.pendown()
for i in range(3):
	turtle.forward(500)
	turtle.left(90)
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(500)
	turtle.right(90)
	turtle.forward(100)
	turtle.right(90)	
turtle.undo()
turtle.undo()
turtle.left(180)
for i in range(3):
	turtle.forward(500)
	turtle.left(90)
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(500)
	turtle.right(90)
	turtle.forward(100)
	turtle.right(90)
turtle.undo()
turtle.undo()

turtle.exitonclick()

 
