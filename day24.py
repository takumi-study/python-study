# 入力された数値の平方根を求める
import sys

while True:
    x = input("平方根を求めたい正の数値を入力してください ")

    if x == "end":
        print("終了")
        break
    try:
        x = float(x)
    except ValueError:
        print(x,"は数値に変換できません")
        continue
    except Exception:
        print("予期せぬエラーが発生しました")
        sys.exit()
    if x <= 0:
        print(x,"は正の数値ではありません")
        continue
## 正しい入力が得られた際の処理
    r = x
    while True:
        r_new = (r + x / r) / 2
        if abs(r - r_new) / r_new < 1e-6:
            break
        r = r_new
    
    print(x, "の平方根は", r_new, "です")


# 円周率の近似値を求める
import math

x = 100
s = 0

for i in range(x):
    if i % 2 == 0:
        s += 1 /(i * 2 + 1)
    if i % 2 == 1:
        s -= 1 /(i * 2 + 1)

print(math.pi, s * 4)

## xを極端に大きくして比較
x = 100000
s = 0

for i in range(x):
    if i % 2 == 0:
        s += 1 /(i * 2 + 1)
    if i % 2 == 1:
        s -= 1 /(i * 2 + 1)

print(math.pi, s * 4)

## 細かい点の改良版
x = 100000
s = 0

for i in range(x):
    if i % 2 == 0:
        s += 1 /(i * 2 + 1)
    else:
        s -= 1 /(i * 2 + 1)

print(math.pi)
print(s * 4)