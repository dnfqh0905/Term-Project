a = 'AAA'
b = 'BBB'
a, b = b, a
a
'BBB'
b
'AAA'
a, b, c = 'a', 'b', 'c'
a,b,c
('a', 'b', 'c')
a,b,c=b,c,a
print(a,b,c)
b c a

import turtle
import random
turtle.shape('turtle')
while(True):
    turtle.setheading(random.randint(0,360))
    turtle.forward(random.randint(100,200))
    turtle.stamp()
	
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76


for n in [1,3,4,5]:
    print(n)

	
1
3
4
5

for c in "A S D F":
    print(c)

	
A
 
S
 
D
 
F

sum=0
for i in range(1, 100+1):
    sum+=i
	
sum
5050

turtle.reset()
for x,y,r in [(200,200,50),(-200,-200,30),(100,100,50)]:
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(r)
    turtle.write(str((x,y)))


def add(a,b):
    sum=a+b
    return sum

result=add(100,10)
print(result)
110

def mul(a,b):
    return a+b,a*b
a=mul(3,4)
print(a)
(7, 12)

'hello %d' % 3.2
'hello 3'
'hello %f' % 3.2
'hello 3.200000'
'hello %.1f' % 3.2
'hello 3.2'
'coordinate: (%.1f, %.1f)' % 3.145, 3.2345
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    'coordinate: (%.1f, %.1f)' % 3.145, 3.2345
TypeError: not enough arguments for format string
'coordinate: (%.1f, %.1f)' % (3.145, 3.2345)
'coordinate: (3.1, 3.2)'

def sum(a,b):
    return a+b

sum('ASDF', 'sdf')
'ASDFsdf'



def move():
    turtle.setheading(random.randint(0, 360))
    turtle.forward(random.randint(50,300))
    turtle.stamp()
    
turtle.onkey(move, 'w')
turtle.listen()
turtle.shape('turtle')
def restart():
    turtle.reset()

	
turtle.onkey(restart, 'Escape')
