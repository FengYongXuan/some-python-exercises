import tkinter as tk
import os


# 当点击"完成"按钮时，用户的输入存到user_input.txt文件中并关闭窗口
def finish():
    text = inputBox.get()
    with open('user_input.txt', 'w', encoding='utf-8') as f:
        f.write(text + ',' + str(v.get()))
    window.destroy()


if __name__ == '__main__':
    window = tk.Tk()
    # 获取屏幕尺寸，使窗口位于屏幕中央
    width = 600
    height = 300
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    window.geometry('%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2))

    # 选择要搜索的教程
    tk.Label(window,
             text="要搜索的教程",
             width=20,
             height=2,
             font=('', 20)
             ).pack()
    inputBox = tk.Entry(window)
    inputBox.pack()

    # 选择你的浏览器
    tk.Label(window,
             text="选择你的浏览器",
             width=20,
             height=2,
             font=('', 20)).pack()
    v = tk.IntVar()
    tk.Radiobutton(window,
                   text="Google Chrome",
                   variable=v,
                   value=1,
                   font=('', 20)).pack()
    tk.Radiobutton(window,
                   text="Firefox",
                   variable=v,
                   value=2,
                   font=('', 20)).pack()

    # 点击"完成"按钮，调用finish函数
    tk.Button(window,
              text="完成",
              font=('', 16),
              width=10,
              command=finish,
              bg='#ddd').pack()

    window.mainloop()

    # 运行filter.py文件
    os.system("python filter.py")

