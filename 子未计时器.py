import time as t
import tkinter as tk

'''if __name__ == '__main__':
    print('李炎秋专属计时器')'''

class MYclock():

    # 创建对象 声明prompt 建立持续时间的列表
    def __init__(self):
        self.prompt = '未开始计时'
        self.tem_prompt = '未开始计时'
        self.lasted_time = []
        self.unit = ['时', '分', '秒', '年', '月', '日']

    # 开始函数 用于记录按下按钮时的时间
    def start(self):
        # print('开始计时')
        self.begin = t.localtime()
        return t.localtime()

    # 圈计函数 用于输出当前计时的时间
    def temporary_stop(self):
        # print('计时结束')
        self.end = t.localtime()
        # 在未进行开始函数时调用圈计函数会报错 此处采取异常处理
        try:
            t1 = '当前用时' + self._calc()
            print(t1)
        except AttributeError:
            t1 = '请先开始计时'
            print(t1)
        self.lasted_time.clear()
        # 此处返回时间 或 异常处理
        return t1

    # 停止计时函数 用于输出最终计时时间并清除开始时间
    def stop(self):
        # print('计时结束')
        self.end = t.localtime()
        # 在未进行开始函数时调用圈计函数会报错 此处采取异常处理
        try:
            t2 = '共用时' + self._calc()
            print(t2)
            # 删除开始计时属性
            del self.begin
        except AttributeError:
            t2 = '请先开始计时'
            print(t2)
        self.lasted_time.clear()
        # 此处返回时间 或 异常处理
        return t2

    def _calc(self):
        self.prompt = ' '
        for i in range(6):
            i -= 6
            self.lasted_time.append(self.end[i] - self.begin[i])
            # print(self.lasted_time)
        for i in range(6):
            if self.prompt:
                total = self.lasted_time[-6]*3600 + self.lasted_time[-5]*60 + self.lasted_time[-4]
                self.lasted_time[-6] = int(total//3600)
                self.lasted_time[-5] = (total - self.lasted_time[-6]*3600)//60
                self.lasted_time[-4] = total - self.lasted_time[-6]*3600 - self.lasted_time[-5]*60
                self.prompt += str(self.lasted_time[i]) + self.unit[i]
                # print(self.lasted_time)
        return self.prompt


ttt = MYclock()

# 初始化gui
root_window = tk.Tk()
# 创建两个架构用于显示圈计时间和结束
frame1 = tk.Frame(root_window)
frame2 = tk.Frame(root_window)
# 设置表头及框大小
root_window.title('这是一个计时器')
root_window.geometry('450x300')
# 标题文本框内的文字
label = tk.Label(root_window, text="子未计时器", font=('宋体', 20,))
label.pack(ipady=30)

var = tk.StringVar()
var.set('请开始计时')
# 设置显示时间文本
label1 = tk.Label(root_window, textvariable = var, font=('宋体', 10,)).pack()
# 设置关闭按钮
button = tk.Button(root_window, text="关闭", command=root_window.quit)
button.pack(side="bottom", ipadx=25)
# 开始计时按钮
button_start = tk.Button(root_window, text="开始计时", command=ttt.start).pack(
                        padx=0, pady=20, ipadx=25)

# 圈计按钮文本功能
def click_button1():
    # 传入圈计时间
    text = ttt.temporary_stop()
    global var
    var.set(text)

button_temstop = tk.Button(root_window, text='圈计', command=click_button1).pack(
                            padx=70, pady=0, ipadx=35, side='left')

# 结束计时按钮弹窗
def click_button2():
    # 传入结束时间
    text = ttt.stop()
    global var
    var.set(text)

button_stop = tk.Button(root_window, text='结束计时', command=click_button2).pack(
                            padx=0, pady=0, ipadx=25, side='left')
# 打开界面窗口
root_window.mainloop()

