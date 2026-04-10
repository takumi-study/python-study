import tkinter as tk
from tkinter import PhotoImage

# -------------------------
# メインウィンドウ
# -------------------------
root = tk.Tk()
root.title("トランプ表示")

# -------------------------
# 画像ファイルリスト
# -------------------------
import os

cardImages = []
for file in os.listdir("Cards"):
    if file.endswith(".png"):
        cardImages.append("Cards/" + file)

cardImages.sort()

# -------------------------
# 画像読み込み（重要）
# -------------------------
cardImageWidgets = []
for file in cardImages:
    try:
        img = PhotoImage(file=file)
        cardImageWidgets.append(img)
    except Exception as e:
        print(f"読み込みエラー: {file}")

# -------------------------
# インデックス管理
# -------------------------
index = 0

# -------------------------
# ラベル（画像表示）
# -------------------------
label = tk.Label(root, image=cardImageWidgets[index])
label.pack(pady=10)

# -------------------------
# コールバック関数
# -------------------------
def forward():
    global index
    if index < len(cardImageWidgets) - 1:
        index += 1
        label.config(image=cardImageWidgets[index])

def back():
    global index
    if index > 0:
        index -= 1
        label.config(image=cardImageWidgets[index])

# -------------------------
# ボタン
# -------------------------
frame = tk.Frame(root)
frame.pack()

btn_back = tk.Button(frame, text="← 前", command=back)
btn_back.pack(side="left", padx=5)

btn_forward = tk.Button(frame, text="次 →", command=forward)
btn_forward.pack(side="left", padx=5)

# -------------------------
# 実行
# -------------------------
root.mainloop()