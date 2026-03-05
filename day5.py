def greet():
    print("こんにちは")
result = greet()
print(result)


def add(a, b):
    print(a + b)

result = add(3, 5)


def add(a, b):
    return a + b

result = add(3, 5)


def test():
    return 5

a = test() + 3
print(a)


def greet():
    print("こんにちは")

greet()


def greet():
    return "こんにちは"

print(greet())


def greet():
    return "こんにちは"

message = greet()
print(message + "！！！")


def greet():
    return "こんにちは"

print(greet() + "世界")


def greet():
    return "こんにちは"

greet()


def  test():
    return 5

print(test())
print(test())


def test():
    print("実行された")
    return 5

print(test())
print(test())


def test():
    return print("実行された")

print(test())


x = print("A")
print(x)


def test():
    return 5

print(test + 3)


def test():
    return 5

x = test
print(x())