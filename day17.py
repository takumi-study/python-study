x = 2

r_new = x

while True:
    r1 = r_new
    r2 = x/r1
    r_new = (r1 + r2)/2
    print(r1, r_new, r2)
    diff = r1 - r2
    if diff < 0:
        diff = -diff
    if diff <= 1.0E-6:
        break
