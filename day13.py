# Chapter 5

a = [5, 1, 3, 4,]
b = a[1:3]
print(b)

a = [5, 1, 3, 4]
a.append(2)
print(a)

a = [5, 1, 3, 4]
b = [2, 6]
a.extend(b)
print(a)

a = [1, 2, 3]
b = a
print(a)
print(b)

b[0] = 0
a[1] = 0
print(a)
print(b)

print(id(a), id(b))

b = a.copy()

a = 1
b = a
b = 2
print(a, b)

a = 1
b = a
print(id(a), id(b))
b = 2
print(id(a), id(b))

a = [[1, 2], [3, 4]]
b = a.copy()

b.append([5, 6])
print(a)
print(b)

b[0][0] = 0
print(a)
print(b)

x = 10
type(x)

x = 2

r_new = x
r_new_list = [r_new]

r1 = r_new
r2 = x/r1
r_new = (r1 + r2)/2
print(r1, r_new, r2)
r_new_list.append(r_new)

r1 = r_new
r2 = x/r1
r_new = (r1 + r2)/2
print(r1, r_new, r2)
r_new_list.append(r_new)

r1 = r_new
r2 = x/r1
r_new = (r1 + r2)/2
print(r1, r_new, r2)
r_new_list.append(r_new)

r1 = r_new
r2 = x/r1
r_new = (r1 + r2)/2
print(r1, r_new, r2)
r_new_list.append(r_new)
print(r_new_list)


x = 2

r_new = x
r_new_list = [r_new]

r1 = r_new
r2 = x/r1
r_new = (r1 + r2)/2
print(r1, r_new, r2)
r_new_list.append(r_new)
diff_list = [r1 - r2]

r1 = r_new
r2 = x/r1
r_new = (r1 + r2)/2
print(r1, r_new, r2)
r_new_list.append(r_new)
diff_list.append(r1 - r2)

r1 = r_new
r2 = x/r1
r_new = (r1 + r2)/2
print(r1, r_new, r2)
r_new_list.append(r_new)
diff_list.append(r1 - r2)

r1 = r_new
r2 = x/r1
r_new = (r1 + r2)/2
print(r1, r_new, r2)
r_new_list.append(r_new)
print(r_new_list)
diff_list.append(abs(r1 - r2))
print(diff_list)