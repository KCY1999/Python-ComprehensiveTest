import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import os
import cv2
from tkinter import filedialog
import numpy as np
#import mouse

window = tk.Tk()
window.title("HW")
window.geometry('600x480')

nb = ttk.Notebook(window)

page1 = tk.Frame(nb, bg='yellowgreen')
page2 = tk.Frame(nb, bg='pink')
page3 = tk.Frame(nb, bg='pink')
page4 = tk.Frame(nb, bg='black')
page5 = tk.Frame(nb, bg='purple')

nb.add(page1, text="page1")
nb.add(page2, text="page2")
nb.add(page3, text="page3")
nb.add(page4, text="page4")
nb.add(page5, text="page5")
nb.pack(fill="both", expand="yes")

t1 = tk.Label(page1, text='BMI 計算器', fg='BLUE', bg='yellowgreen')
t1.pack()

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = round(float(weight) / (float(height)/100)**2,2)
        result = '你的 BMI 指數為：{} {}'.format(bmi, total_bmi(bmi))
        result_label.configure(text=result)
    except:
        tk.messagebox.showwarning(title='嘿', message='輸入數字好不')
        height_entry.delete(0, 'end')
        weight_entry.delete(0, 'end')


def total_bmi(bmi):
    if bmi < 10 or bmi > 40:
        return '搞啥 你輸入錯了吧'
    elif bmi >= 10 and bmi <18.5:
        return '你不胖'
    elif bmi >= 18.5 and bmi < 24:
        return '你不算胖'
    elif bmi >= 24:
        return '你胖'

height_frame = tk.Frame(page1)
height_frame.pack(side=tk.TOP)
height_label = tk.Label(height_frame, text='身高（cm）', fg='BLUE', bg='yellowgreen')
height_label.pack(side=tk.LEFT)
height_entry = tk.Entry(height_frame)
height_entry.pack(side=tk.LEFT)

weight_frame = tk.Frame(page1)
weight_frame.pack(side=tk.TOP)
weight_label = tk.Label(weight_frame, text='體重（kg）', fg='BLUE', bg='yellowgreen')
weight_label.pack(side=tk.LEFT)
weight_entry = tk.Entry(weight_frame)
weight_entry.pack(side=tk.LEFT)

result_label = tk.Label(page1)
result_label.pack()

calculate = tk.Button(page1, text='計算', command=calculate_bmi, fg='Red')
calculate.pack()
#################################################################################################################
def calculate_triangle():
    try:
        side1 = int(side1_import.get())
        side2 = int(side2_import.get())
        side3 = int(side3_import.get())

        result = '判斷結果：{}{}{}是{}'.format(side1, side2, side3, decide_triangle(side1, side2, side3))
        result_label2.configure(text=result, fg='indigo')
    except:
        tk.messagebox.showwarning(title='嘿', message='輸入數字好不')

def decide_triangle(a,b,c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b == c:
            return '正三角形'
        elif (a == b or a == c or b == c):
            return '等腰三角形'
        elif (a * a + b * b == c * c) or (a * a + b * b == c * c) or (a * a + b * b == c * c):
            return '直角三角形'
        else:
            return '三角形'
    else:
        return '這不是三角形'

title = tk.Label(page2, text='三角形判斷', fg='black', bg='pink')
title.pack()
title.place(x=0, y=25)

label1 = tk.Label(page2, text='邊長1', fg='indigo', bg='pink')
label1.pack()
label1.place(x=50, y=50, heigh=25)

label2 = tk.Label(page2, text='邊長2', fg='indigo', bg='pink')
label2.pack()
label2.place(x=50, y=75, heigh=25)

label3 = tk.Label(page2, text='邊長3', fg='indigo', bg='pink')
label3.pack()
label3.place(x=50, y=100, heigh=25)

side1_import = tk.Entry(page2, textvariable='side1')
side1_import.pack()
side1_import.place(x=90, y=50)

side2_import = tk.Entry(page2, textvariable='side2')
side2_import.pack()
side2_import.place(x=90, y=75)

side3_import = tk.Entry(page2, textvariable='side3')
side3_import.pack()
side3_import.place(x=90, y=100)

calculate2 = tk.Button(page2, text='計算', command=calculate_triangle, fg='Red')
calculate2.pack()
calculate2.place(x=250, y=75)

result_label2 = tk.Label(page2)
result_label2.pack()
result_label2.place(x=300, y=75)
#################################################################################################################
draw = False
mod = False

px, py = -1, -1

def idraw():
    global px, py, draw, mod
    def draw_circle(event, x, y, flags, param):
        global px, py, draw, mod

        if event == cv2.EVENT_LBUTTONDOWN:
            draw = True
            px, py = x, y

        elif event == cv2.EVENT_MOUSEMOVE:
            if draw == True:
                if mod == True:
                    cv2.rectangle(img, (px, py), (x, y), (0, 255, 0), -1)
                else:
                    cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

        elif event == cv2.EVENT_LBUTTONUP:
            draw = False
            if mod == True:
                cv2.rectangle(img, (px, py), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

    filename = filedialog.askopenfilename(title='開啟png檔案', filetypes=[('png', '*.png')])
    img = cv2.imread(filename)
    name = str(filename).rstrip(".png").split('/', 4)[4]

    print(filename)
    print(name)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)

    while (1):
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        print(k)
        if k == ord('m'):
            mod = not mod
        elif k == 27:
            break
        elif k == 115:
            cv2.imwrite(name + ".png", img)

    cv2.destroyAllWindows()

drawing1 = tk.Button(page3, text='開啟檔案', command=idraw, fg='Black')
drawing1.place(x=240, height=50, width=70)
#################################################################################################################

data = {}

def readfile():
    fileName = "test.txt"

    if os.path.isfile(fileName):
        opfile = open(fileName, "r")
        line = opfile.readline()
        oo = line.split(':', 1)[0]
        oo1 = line.rstrip().split(':', 1)[1]
        data.update({oo: oo1})
        print(data)

        while line != '':
            line = opfile.readline()
            if(line!=''):
                oo = line.split(':', 1)[0]
                oo1 = line.rstrip("\n").split(':', 1)[1]
                data.update({oo: oo1})
                print(data.keys())
                print(data.values())

        value_print.configure(text=data.values(), fg='BLUE')
        key_print.configure(text=data.keys(), fg='BLUE')
        try:
            value_print.configure(text=data[select.get()],fg='red')
        except:
            tk.messagebox.showwarning(title='嘿', message='輸入錯誤')
        opfile.close()

drawing1 = tk.Button(page4, text='字典',command=readfile, fg='Blue')
drawing1.place(x=240, height=50, width=90)

value_print = tk.Label(page4, text="value", fg='Blue')
value_print.place(x=240, y=120)

key_print = tk.Label(page4, text="key", fg='Blue')
key_print.place(x=240, y=170)

select = tk.Entry(page4, textvariable='select')
select.pack()
select.place(x=240, y=75)



window.mainloop()