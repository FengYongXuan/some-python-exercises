"""
    挑战题（统计日志中出现的IP地址及出现的次数）
"""

import re

res = []

with open('../data/aur.log', 'r') as logfile:
    with open('ip_count.csv', 'w') as targetfile:
        logdata = logfile.readlines()
        for row in logdata:
            pattern = re.compile(r'(?:\d{0,3}\.){3}(?:\d{0,3}) -')
            res += pattern.findall(row)
        # 去重
        res_set = set(res)
        # 计算每个IP地址出现次数，并输出
        for item in res_set:
            targetfile.write(item[:-2] + ',' + str(res.count(item)) + '\n')
