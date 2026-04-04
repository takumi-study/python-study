from turtle import *

n = 7

for i in range(n):
    forward(100)
    left(360/n)

for i in range(n):
    forward(100)
    left(720/n)

for i in range(n):
    forward(100)
    left(1080/n)

from turtle import *

m = 9

for i in range(m):
    forward(100)
    left(360/m)

for i in range(m):
    forward(100)
    left(720/m)


# 複数のタートルを動かす
from turtle import *

t1 = Turtle()
t2 = Turtle()

t1.color('red')
t2.color('blue')

for i in range(180):
    t1.forward(5)
    t2.forward(3)
    t1.left(2)
    t2.left(2)


t1 = Turtle()

t1.forward(10)

x, y = t1.pos()


# マウスクリックに対応して呼び出す
from turtle import *

def come(x, y):
    (xx, yy) = pos()
    newxy = ((xx + x)/2, (yy + y)/2)
    print(x, y)
    goto(newxy)

onscreenclick(come)
done()


import math
y = 2
x = 1
angle = math.atan2(y, x)*180/math.pi

# ウサギ型タートル
from turtle import *

ht()

rdata = ((0, 16), (-2, 14), (-3, 11), (-3, 6), (-2, 5), (-2, 7), 
(-1, 10), (-2, 7), (-2, 5), (-3, 6), (-3, 10), (-4,13), 
(-5, 13), (-4, 2), (-5, -10), (-4, -10), (-3, -4), 
(0, -5), (3, -4), (4, -10), (5, -10), (4, 2), (5, 13), 
(4, 13), (3, 10), (3, 6), (2, 5), (2, 7), (1, 10), 
(2, 7), (2, 5), (3, 6), (3, 11), (2, 14))

getscreen().register_shape("rabbit", rdata)

