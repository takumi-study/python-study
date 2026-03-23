tozai = ["三条", "四条", "五条"]
nanboku = ["堀川", "烏丸", "河原町"]
cross_table = []
for i in range(len(tozai)):
    row = []
    for j in range(len(nanboku)):
        row.append("")
    cross_table.append(row)
for u in range(len(tozai)):
    for h in range(len(nanboku)):
        cross = tozai[u] + nanboku[h]
        cross_table[u][h] = cross
for cross_list in cross_table:
    print(*cross_list, sep = ", ")

tozai = ["三条", "四条", "五条"]
nanboku = ["堀川", "烏丸", "河原町"]
cross_table = []
for i in range(len(tozai)):
    row = []
    for j in range(len(nanboku)):
        row.append(tozai[i] + nanboku[j])
    cross_table.append(row)
for cross_list in cross_table:
    print(*cross_list, sep = ", ")
