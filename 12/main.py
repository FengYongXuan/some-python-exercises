"""
    练习12
"""

import random
import time

red_balls = set()
while len(red_balls) < 6:
    red_ball = random.randint(1, 33)
    red_balls.add(red_ball)

blue_ball = random.randint(1, 16)

print("开奖结果\n红色球:", end="")
for i in range(len(red_balls)):
    time.sleep(3)
    print(list(red_balls)[i], " ", end="")

print("\n蓝色球:", end="")
time.sleep(5)
print(blue_ball, end="")

draw_lottery_date = time.strftime("%Y年%m月%d日", time.localtime())
with open(draw_lottery_date+'.txt', 'w', encoding='utf-8') as targetfile:
    targetfile.write("开奖结果\n红色球:" + str(red_balls) + "\n蓝色球:" + str(blue_ball))
