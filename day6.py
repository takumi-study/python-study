def greet(name):
    return "こんにちは " + name

print(greet("太郎"))

print(greet("花子"))
print(greet("田中"))


def add(a, b):
    return a + b

print(add(3, 4))

def double(x):
    return x * 2

print(double(5))

def greet(name):
    print("こんにちは " + name)

print(greet("太郎"))


def add(a, b):
    return a + b

print(add(10, 5))

def greet(name):
    print("こんにちは " + name)

print(greet("太郎"))


def greet(name):
    print("呼び出された")
    return "こんにちは " + name

print(greet("太郎"))

def add(a, b):
    print(a + b)

print(add(3, 4))

def test(x):
    return x * 2

a = test(5)
print(a)