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