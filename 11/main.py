"""
    练习11
"""

import random
import sys

num = int(input('需要多少个随机注：'))
if num <= 0:
    print('请输入一个大于0的数！')
    sys.exit(0)

while num:
    red_balls = set()
    while len(red_balls) < 6:
        red_ball = random.randint(1, 33)
        red_balls.add(red_ball)

    blue_ball = random.randint(1, 16)

    try:
        flag = int(input("直接输出到屏幕上还是存到文件中？直接输出按'1',存文件按'2': "))
    except ValueError:
        print("请输入数字！")
    else:
        if flag == 1:
            print("红色球:", red_balls, "\n蓝色球:", blue_ball)
        elif flag == 2:
            with open('double_color_ball.txt', 'a', encoding='utf-8') as targetfile:
                targetfile.write("\n红色球:" + str(red_balls) + "\n蓝色球:" + str(blue_ball))
        else:
            print("请输入1或2！")

        num = num - 1
