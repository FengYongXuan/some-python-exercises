"""
    练习3
"""

num = int(input("请输入一个数字："))

if num > 10 or num < 1:
    print("请输入1-10以内的数字!")
else:
    for i in range(num):
        print((num - i) * " " + (2*i + 1) * '=')

