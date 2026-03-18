x =  list(range(10))
print(x)

sum = 0
for i in range(10):
    sum = sum + i
print(sum)

sum = 0
for i in range(11):
    sum += i
print(sum)

for i in range(3):
    for j in range(3):
        print(i,j)

for i in range(3):
    for j in range(i):
        print(i,j)

a = [5, 1, 3, 4]
for i in range(len(a)):
    print(i, a[i])

for d in a:
    print(d)

a = [5, 1, 3, 4]
for i, d in enumerate(a):
    print(i, d)

a = [5, 1, 3, 4]
sum = 0
for i in range(len(a)):
    sum += a[i]
average = sum/len(a)
print(average)

a = []
for i in range(5):
    a.append(i*i)
a = [i*i for i in range(5)]

# x の平方根を求める
x = 2

r_new = x

diff = r_new - x/r_new
if diff < 0:
    diff = -diff
while (diff > 1.0E-6):
    r1 = r_new
    r2 = x/r1
    r_new = (r1 + r2)/2
    print(r1, r_new, r2)
    diff = r1 - r2
    if diff < 0:
        diff = -diff
    