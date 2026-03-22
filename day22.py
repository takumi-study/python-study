tozai = ["三条", "四条", "五条"]
nanboku = ["堀川", "烏丸", "河原町"]
cross_table = []
for i in range(len(tozai)):
    street = []
    for j in range(len(nanboku)):
        cross = tozai[i] + nanboku[j]
        street.append(cross)
    cross_table.append(street)

street = ["三条河原町", "三条烏丸", "三条堀川"]
for i in range(len(street)):
    if i < len(street) - 1:
        print(street[i], end = ", ") # 最後以外は", "を追加
    else:
        print(street[i]) # 最後は改行

street = ["三条河原町", "三条烏丸", "三条堀川"]
print(*street, sep = ", ")
