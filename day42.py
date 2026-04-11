import tkinter as tk
import math
import time

# ウィンドウ作成
root = tk.Tk()
root.title("Analog Clock")

# キャンバス作成
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# 中心と半径
cx, cy = 150, 150
r = 120

def draw_clock():
    canvas.delete("all")

    # 円（時計の枠）
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r)

    # 時刻取得
    t = time.localtime()
    sec = t.tm_sec
    minute = t.tm_min
    hour = t.tm_hour % 12

    # 角度計算（ラジアン）
    sec_angle = math.radians(sec * 6)
    min_angle = math.radians(minute * 6)
    hour_angle = math.radians(hour * 30 + minute * 0.5)

    # 秒針
    sx = cx + r * 0.9 * math.sin(sec_angle)
    sy = cy - r * 0.9 * math.cos(sec_angle)
    canvas.create_line(cx, cy, sx, sy, fill="red")

    # 分針
    mx = cx + r * 0.7 * math.sin(min_angle)
    my = cy - r * 0.7 * math.cos(min_angle)
    canvas.create_line(cx, cy, mx, my, width=2)

    # 時針
    hx = cx + r * 0.5 * math.sin(hour_angle)
    hy = cy - r * 0.5 * math.cos(hour_angle)
    canvas.create_line(cx, cy, hx, hy, width=3)

    # 1秒ごとに更新
    root.after(1000, draw_clock)

# 初回呼び出し
draw_clock()

# メインループ
root.mainloop()