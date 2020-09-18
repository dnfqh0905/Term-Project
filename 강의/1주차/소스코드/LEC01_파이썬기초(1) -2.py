v=3.14
v*6**2
113.04

r=6
v*r**2
113.04

area = v*r**2
print(area)
113.04

name1 = "ASDF"
name2 = "가나다라"
print(name1)
ASDF
print(name2)
가나다라

order = 4
pi = 3.14
name = "ASDF"
type(order)
<class 'int'>
type(pi)
<class 'float'>
type(name)
<class 'str'>

4>3
True
4>-3
True

a = 123 <456
print(a)
True
type(a)
<class 'bool'>

first = "ASDF"
last = "QWER"
name = first + " " + last
name
'ASDF QWER'
print(name)
ASDF QWER
name*2
'ASDF QWERASDF QWER'
name[0]
'A'
name[-1]
'R'
name[5]
'Q'

title = "Python 2D Game Programming"
title[0:6]
'Python'
title[7:9]
'2D'
title[:6]
'Python'
title[-11]
'P'
title[::6]
'P mgn'
list = ["Python", "2D", "Game", "Programming"]
list[0]
'Python'
list[:3]
['Python', '2D', 'Game']

score = { 'Python' : 80, '2D' : 85, 'Game' : 98, 'Programming' : 100}
type(score)
<class 'dict'>
score['Game']
98
score['a']
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    score['a']
KeyError: 'a'
score['a'] = 0
score
{'Python': 80, '2D': 85, 'Game': 98, 'Programming': 100, 'a': 0}
del score['a']
score
{'Python': 80, '2D': 85, 'Game': 98, 'Programming': 100}
score.keys()
dict_keys(['Python', '2D', 'Game', 'Programming'])
score.values()
dict_values([80, 85, 98, 100])
'Game' in score
True
'a' in score
False
score.clear()
score
{}

a1 = (1,2,3)
a2 = (1,)
a3 = ()
a4 = 1,2,3,4
a4
(1, 2, 3, 4)
type(a4)
<class 'tuple'>
a5 = (1, 'a', "ASDF", (1,2))
a1[1:]
(2, 3)
a1 + a5
(1, 2, 3, 1, 'a', 'ASDF', (1, 2))

b1 = {1,2,3}
type(b1)
<class 'set'>
b1 = {1,2,2,4}
b1
{1, 2, 4}
c1 = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,]
b1 = set(c1)
b1
{1, 2, 3, 4, 5}
>>> b2 = {6,7,8,9}
>>> b1 + b2
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    b1 + b2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> b1 | b2
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> b1 &b2
set()
>>> b2 - b1
{8, 9, 6, 7}
>>> b1 - b2
{1, 2, 3, 4, 5}
>>> b1.add(8)
>>> b1
{1, 2, 3, 4, 5, 8}
>>> b2.remove(8)
>>> b2
{9, 6, 7}
>>> 
