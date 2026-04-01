def square_root(x):
    '引数xの平方根を求める'
    r = x
    while True:
        rnew = (r + x / r) / 2
        if abs(r - rnew) / rnew < 1e-6:
            break
        r = rnew
    return rnew

def get_positive_numeral():
    import sys
    while True:
        y = input("平方根を求めたい正の数値を入力してください ")

        if y == "end":
            print("終了")
            break
        try:
            y = float(y)
        except ValueError:
            print(y,"は数値に変換できません")
            continue
        except Exception:
            print("予期せぬエラーが発生しました")
            sys.exit()
        if y <= 0:
            print(y,"は正の数値ではありません")
            continue
        return y

while True:
    z = get_positive_numeral()
    if z is None:
        break 
    r = square_root(z)
    print(z, "の平方根は", r, "です")

