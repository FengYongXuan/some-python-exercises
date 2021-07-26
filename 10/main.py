"""
    练习10
"""


def cal_area(s1, s2):
    """计算直角三角形的面积"""
    return s1 * s2 * 0.5


while True:
    try:
        side1 = float(input("\n请输入第一条直角边的长度："))
        if side1 <= 0:
            print("边长要大于0！")
            continue
        side2 = float(input("请输入第二条直角边的长度："))
        if side2 <= 0:
            print("边长要大于0！")
            continue
    except ValueError:
        print("错误输入！请不要输入字符或字符串！")
    else:
        print("直角三角形的面积：", cal_area(side1, side2))
        break
