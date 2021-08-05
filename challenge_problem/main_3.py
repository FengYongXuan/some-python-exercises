"""
    挑战题（统计学生签到情况）
"""

import pandas as pd
import re
import datetime

register_info = pd.read_csv("class_register.data")

stu_name = set()
register_date = set()

# 获取dataframe表格的x,y轴数据
for name in register_info['打卡身份']:
    name = re.sub(r"[0-9]*", "", name)
    stu_name.add(name)
for date in register_info['打卡时间']:
    register_date.add(date[:10])

# 初始化dataframe表格
register_date_list = list(register_date)
register_date_list.sort()
register_table = pd.DataFrame(index=list(stu_name), columns=register_date_list)
for i in register_date:
    register_table[i] = 0

# 统计每个人每天打卡次数
row_num = len(register_info['打卡身份'])
for i in range(row_num):
    target_date = register_info.iloc[i, 4][:10]
    target_name = register_info.iloc[i, 6]
    target_name = re.sub(r"[0-9]*", "", target_name)
    register_table.loc[target_name, target_date] += 1

# 汇总缺卡的情况
register_table['absent_time'] = [0 for i in range(len(stu_name))]
for date in register_table.columns[:-2]:
    # 处理没上课还有人打卡的情况
    if register_table[date].sum() < 5:
        register_table = register_table.drop(date, axis=1)
    else:
        for name in register_table.index:
            register_time = register_table.loc[name][date]
            if register_time < 2:
                register_table.loc[name, 'absent_time'] += 2 - register_time

# 汇总异常打卡的情况
register_table['abnormal_time'] = [0 for i in range(len(stu_name))]
am_register, pm_register = [], []

for row in register_info['打卡时间']:
    target_time = datetime.datetime.strptime(row[11:], '%H:%M:%S')
    if target_time < datetime.datetime.strptime('12:00:00', '%H:%M:%S'):
        am_register.append(target_time)
    else:
        pm_register.append(target_time)
am_register.sort()
pm_register.sort()

# 获取上午、下午打卡时间的中位数
median_am = am_register[len(am_register) // 2]
median_pm = pm_register[len(pm_register) // 2]

for i in range(row_num):
    target_name = register_info.iloc[i, 6]
    target_name = re.sub(r"[0-9]*", "", target_name)
    target_time = datetime.datetime.strptime(register_info.iloc[i, 4][11:], '%H:%M:%S')
    time_dif_1 = ((target_time - median_am).days * 86400 + (target_time - median_am).seconds) // 60
    time_dif_2 = ((target_time - median_pm).days * 86400 + (target_time - median_pm).seconds) // 60
    if abs(time_dif_1) < 5 or abs(time_dif_2) < 5:
        pass
    else:
        register_table.loc[target_name, 'abnormal_time'] += 1

print('学生上课打卡情况汇总如下\n', register_table)
