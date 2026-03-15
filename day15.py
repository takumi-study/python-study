# x の平方根を求める
x = 2

r_new =x

for i in range(10):
    r1 = r_new
    r2 = x/r1
    r_new = (r1 + r2)/2
    print(r1, r_new, r2)

x = 2

r_new =x

for i in range(10):
    r1 = r_new
    r2 = x/r1
    r_new = (r1 + r2)/2
print(r1, r_new, r2)

x = 2

r_new =x

for i in range(10000):
    r1 = r_new
    r2 = x/r1
    r_new = (r1 + r2)/2
print(r1, r_new, r2)

x = 2

r_new =x

for i in range(10000):
    r1 = r_new
    r2 = x/r1
    r_new = (r1 + r2)/2
print(r1, r_new, r2)

for i in range(10):
    if i == 1:
        continue
    if i == 8:
        break
    print(i)

