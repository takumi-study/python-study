a = 1
b = 0
if (a == 1) and (b == 0):
    print("YES a == 1 and b == 0")

a = 1
b = 0
if a == 1:
    if b == 0:
        print("YES a == 1 and b == 0")

import sys
for i in range(5):
    print(i)
    if i == 3:
        sys.exit()
print("end")

