import tkinter as tk

# 変数
current_number = 0
first_term = 0
second_term = 0
result = 0
operation = 0

# 計算処理
def do_plus():
    global current_number, first_term, operation
    first_term = current_number
    current_number = 0
    operation = 1

def do_minus():
    global current_number, first_term, operation
    first_term = current_number
    current_number = 0
    operation = 2

def do_times():
    global current_number, first_term, operation
    first_term = current_number
    current_number = 0
    operation = 3

def do_divide():
    global current_number, first_term, operation
    first_term = current_number
    current_number = 0
    operation = 4

def do_eq():
    global second_term, result, current_number
    second_term = current_number
    if operation == 1:
        result = first_term + second_term
        current_number = result
    elif operation == 2:
        result = first_term - second_term
        current_number = result
    elif operation == 3:
        result = first_term * second_term
        current_number = result
    elif operation == 4:
        if second_term == 0:
            result = "ERROR"
            current_number = 0
        else:
            result = first_term // second_term
            current_number = result
    else:
        result = current_number

# 数字入力
def key(n):
    global current_number
    current_number = current_number * 10 + n
    show_number(current_number)

# 各ボタン
def clear():
    global current_number, first_term, operation
    current_number = 0
    first_term = 0
    operation = 0
    show_number(current_number)

def plus():
    do_plus()
    show_number(current_number)

def minus():
    do_minus()
    show_number(current_number)

def times():
    do_times()
    show_number(current_number)

def divide():
    do_divide()
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

f = tk.Frame(root)
f.grid()

e = tk.Entry(f)
e.grid(row=0, column=0, columnspan=4)

# 数字ボタン
buttons = []
for i in range(10):
    btn = tk.Button(f, text=str(i),
                    command=lambda n=i: key(n))
    buttons.append(btn)

# 特殊ボタン
bc = tk.Button(f, text="C", command=clear)

bp = tk.Button(f, text="+", command=plus)

bm = tk.Button(f, text="-", command=minus)

bt = tk.Button(f, text="×", command=times)

bd = tk.Button(f, text="÷", command=divide)

be = tk.Button(f, text="=", command=eq)

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
bm.grid(row=3, column=3)
bt.grid(row=4, column=3)
bd.grid(row=5, column=3)
be.grid(row=5, column=2)

clear()
root.mainloop()