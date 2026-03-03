score=75
if score>=80:
    print("優秀")
elif score>=60:
    print("合格")
else:
    print("不合格")

for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(1, 11):
    if i % 2==0:
        print(i)

x=10
if x==10:
    print("A")
if x==5:
    print("B")

for i in range(1,11):
    if i % 3 == 0:
        print(i)

for i in range(1,11):
    if i % 2 == 0 and i % 3 == 0:
        print(i)

for i in range(1, 11):
    if (i % 2 == 0 or i % 3 == 0) and i > 5:
        print(i)