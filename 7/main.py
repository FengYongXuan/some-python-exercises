"""
    练习7
"""

try:
    content = float(input("用户请输入："))
except ValueError:
    print("无法判定输入数据的类型！")
else:
    if int(content) == content:
        print("输入的是整数")
    else:
        print("输入的是浮点数")
