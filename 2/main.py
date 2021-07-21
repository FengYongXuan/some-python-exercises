"""
    练习2
"""


def cal_area(s1, s2):
    """计算直角三角形的面积"""
    return s1 * s2 * 0.5


side1 = float(input("请输入第一条直角边的长度："))
side2 = float(input("请输入第二条直角边的长度："))
print("直角三角形的面积：", cal_area(side1, side2))
