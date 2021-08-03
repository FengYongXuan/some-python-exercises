"""
    练习16
"""

import matplotlib.pyplot as plt
from pylab import mpl

# 设置matplotlib对中文的支持
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

lv_num = [0, 0, 0, 0, 0, 0, 0]
user_id = []
user_lv = []

# 获取数据
with open('bilibili_user.csv', 'r', encoding='utf-8') as f:
    invalid_content = f.readline()  # 舍弃文件第一行内容
    info = f.readlines()
    for row in info:
        index1 = row.find(',')
        index2 = row.find(',', index1 + 1)

        if row[index1:index2] != ',':
            user_id.append(int(row[:index1]))
            user_lv.append(int(row[index2 + 1]))
            lv_num[int(row[index2 + 1])] = lv_num[int(row[index2 + 1])] + 1

# 绘制散点图
plt.figure(figsize=(20, 10), dpi=80)
plt.title('b站前500用户的id和level散点图', size=30)
plt.xlabel('用户ID', size=20, loc='right')
plt.ylabel('level', size=20, loc='top')
plt.xticks(list(range(0, 501, 50)))
plt.yticks(list(range(7)))
plt.tick_params(axis='both', labelsize=20)
plt.scatter(user_id, user_lv, s=30)
plt.savefig('b站前500用户的id和level散点图.png')

# 绘制饼图
plt.figure(figsize=(20, 15), dpi=50)
plt.title('b站前500用户的等级分布饼图', size=45)
data_list = [num / len(user_id) for num in lv_num]
label_list = ['LV0', 'LV1', 'LV2', 'LV3', 'LV4', 'LV5', 'LV6']
distance = (0, 0, 0, 0, 0, 0.1, 0)
patches, l_text, p_text = plt.pie(data_list, labels=label_list, autopct="%.2f%%", explode=distance, shadow=True)
for t in l_text:
    t.set_size(40)
for t in p_text:
    t.set_size(40)
plt.savefig('b站前500用户的等级分布饼图.png')

# 绘制柱状图
plt.figure(figsize=(20, 15), dpi=50)
plt.title('b站前500用户的等级分布柱状图', size=45)
x_list = ['LV0', 'LV1', 'LV2', 'LV3', 'LV4', 'LV5', 'LV6']
plt.xlabel('level', size=30, loc='right')
plt.ylabel('number', size=30, loc='top')
plt.tick_params(axis='both', labelsize=30)
for a, b in zip(x_list, lv_num):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=30)
plt.bar(x_list, lv_num, width=0.5)
plt.savefig('b站前500用户的等级分布柱状图.png')

plt.show()