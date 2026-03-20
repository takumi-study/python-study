import sys
while True:
    x = input("正の数値を入力してください ")
    try:
        x = float(x)
    except ValueError:
        print(x, "は数値に変換できません")
        continue
    except:
        print("予期していないエラーです")
        sys.exit()
    if x <= 0:
        print("x、”は正の数値ではありません")
        continue
# 以下は正しい入力が得られた時の処理
    print(x)
    break

a = 2
b = 1
diff = a - b

diff = abs(diff)

import math

c = math.pi

math.sqrt(2)

c = 2.99792458e8
na = 6.02214076e23
form = '光速は{0:12.8g} m/s, アボガドロ数は{1:12.8g} mol**(-1)です'
print(form.format(c, na))
