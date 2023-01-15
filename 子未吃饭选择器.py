from random import *
import tkinter as tk

food_warehouse = ['面条', '炸串', '炒米粉', '麻辣香锅', '兰州拉面', '螺蛳粉', '米线', '泡面', '麻辣烫', '冒菜',
                  '米饭', '包子', '鸭血粉丝', '汉堡炸鸡', '不吃饭']

def food_choice():
    return food_warehouse[randint(0,len(food_warehouse)-1)]

# 初始化gui
root_window = tk.Tk()
# 设置表头及框大小
root_window.title('专治吃饭困难')
root_window.geometry('450x300')
# 标题文本框内的文字
label = tk.Label(root_window, text="子未吃饭选择器", font=('宋体', 20,))
label.pack(ipady=30)

var = tk.StringVar()
var.set('今天吃什么')
switch = True
while switch:
    for i in range(len(food_warehouse)-1):
        text = food_warehouse[i]
        var.set(text)
# 设置显示文本
label_var = tk.Label(root_window, textvariable=var, font=('宋体', 10,)).pack()

def click_button():
    # 传入食物
    text = food_choice()
    global var, switch
    var.set(text)
    switch = False
# 开始按钮
button_start = tk.Button(root_window, text="就是你了！", command=click_button).pack(
                        padx=0, pady=20, ipadx=25)

# 打开界面窗口
root_window.mainloop()