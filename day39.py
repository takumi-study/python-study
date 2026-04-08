import tkinter as tk

# 変数
current_number = 0
first_term = 0
second_term = 0
result = 0

# 計算処理
def do_plus():
    global current_number, first_term
    first_term = current_number
    current_number = 0

def do_eq():
    global second_term, result, current_number
    second_term = current_number
    result = first_term + second_term
    current_number = 0

# 数字入力
def key(n):
    global current_number
    current_number = current_number * 10 + n
    show_number(current_number)

# 各ボタン
def clear():
    global current_number
    current_number = 0
    show_number(current_number)

def plus():
    do_plus()
    show_number(current_number)

def eq():
    do_eq()
    show_number(result)

# 表示
def show_number(num):
    e.delete(0, tk.END)
    e.insert(0, str(num))

# GUI
root = tk.Tk()

# ★ 背景色設定
f = tk.Frame(root, bg='#ffffc0')
f.grid()

# 共通フォント
font_style = ('Helvetica', 14)

# 数字ボタン（白）
buttons = []
for i in range(10):
    btn = tk.Button(
        f, text=str(i),
        command=lambda n=i: key(n),
        bg="white",
        width=2,
        font=font_style
    )
    buttons.append(btn)

# 特殊ボタン
bc = tk.Button(f, text="C", command=clear,
               bg="red", width=2, font=font_style)

bp = tk.Button(f, text="+", command=plus,
               bg="green", width=2, font=font_style)

be = tk.Button(f, text="=", command=eq,
               bg="green", width=2, font=font_style)

# 配置
buttons[1].grid(row=3, column=0)
buttons[2].grid(row=3, column=1)
buttons[3].grid(row=3, column=2)
buttons[4].grid(row=2, column=0)
buttons[5].grid(row=2, column=1)
buttons[6].grid(row=2, column=2)
buttons[7].grid(row=1, column=0)
buttons[8].grid(row=1, column=1)
buttons[9].grid(row=1, column=2)
buttons[0].grid(row=4, column=0)

bc.grid(row=1, column=3)
bp.grid(row=2, column=3)
be.grid(row=4, column=3)

# Entry（フォント設定）
e = tk.Entry(f, font=font_style)
e.grid(row=0, column=0, columnspan=4)

clear()

root.mainloop()