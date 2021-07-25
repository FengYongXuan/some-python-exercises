"""
    练习5
"""

import sys
import turtle

t = turtle.Turtle(shape='turtle')

side_len = int(input("请输入等边三角形的边长："))
if side_len < 100 or side_len > 200:
    print("等边三角形的边长应在100-200之间!")
    sys.exit(0)

radius = int(input("请输入圆的半径："))
if radius < 100 or radius > 200:
    print("圆的半径应在100-200之间!")
    sys.exit(0)

# 绘制等边三角形
for i in range(3):
    t.forward(side_len)
    t.right(120)

# 绘制圆
t.penup()
t.goto(0, 10)
t.pendown()
t.circle(radius)
t.hideturtle()
turtle.mainloop()


