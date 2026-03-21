tozai = ["三条", "四条", "五条"]
nanboku = ["堀川", "烏丸", "河原町"]

for i in tozai:
    for j in nanboku:
        cross = i + j
        print(cross)

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(a)

print(a[0])

print(a[0][1])

sum = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        sum += a[i][j]
print(sum)

sum = 0
for row in a:
    for element in row:
        sum += element
print(sum)

tozai = ["三条", "四条", "五条"]
nanboku = ["堀川", "烏丸", "河原町"]
cross_table = [["", "", ""], ["", "", ""], ["", "", ""]]
for i in range(len(tozai)):
    for j in range(len(nanboku)):
        cross = tozai[i] + nanboku[j]
        cross_table[i][j] = cross
print(cross_table)

cross_table = []
for i in range(5):
    row = []
    for j in range(4):
        row.append("")
    cross_table.append(row)

