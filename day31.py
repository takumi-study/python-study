def square_root(x):
    '引数 x の平方根を求める'
    rnew = x
    #
    diff = rnew - x/rnew
    if diff < 0:
        diff = -diff
    while (diff > 1.0E-6):
        r1 = rnew
        r2 = x/r1
        rnew = (r1 + r2)/2
        print(r1, rnew, r2)
        diff = r1 - r2
        if diff < 0:
            diff = -diff
    return rnew
# ここからメインプログラム
v = 2
r = square_root(v)
print("結果は ", r)

help(square_root)


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

    r = square_root(x)
    print(x, "の平方根は", r, "です")
