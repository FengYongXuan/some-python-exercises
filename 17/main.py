"""
    练习17
"""

import pandas as pd
import numpy as np

info = pd.read_csv('bilibili_user.csv')

# 对于等级那一列缺失的值，用该列所有值的平均数来填充
info['用户的等级'].fillna(info['用户的等级'].mean(), inplace=True)

# 对数据进行分组统计
user_lv = info['用户的等级']
bins = [-1, 1, 3, 5, 6]
lv_groups = pd.cut(user_lv, bins)
dummies = pd.get_dummies(lv_groups)

# 输出
print('新用户', dummies[dummies.columns[0]].sum())
print('普通用户', dummies[dummies.columns[1]].sum())
print('老用户', dummies[dummies.columns[2]].sum())
print('骨灰级用户', dummies[dummies.columns[3]].sum())
