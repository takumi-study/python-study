def f():
    print("f says Hello")

# 関数を引数でもらって実行する関数
def F(y):
    print("In F, ", end="")
    y()

# f を実行
f()

# f を F に渡して F を実行
F(f)


def f(a, b = 2, c = 3):
    return a + b + c

f(1, 1, 1)

f(1)

f(1, c = 2)


from turtle import *
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)


n = 5
for i in range(n):
    forward(100)
    left(360/n)

m = 5
for i in range(m):
    forward(100)
    left(720/m)

done()
