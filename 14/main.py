"""
    练习14
"""

import requests
import time

with open('userInfo.csv', 'w', encoding='utf-8') as f:
    f.write(','.join(['用户编号', '用户名', '用户的等级', '是否存在' + '\n']))
    for i in range(1, 501):
        time.sleep(3)
        url = "https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp".format(i)
        r = requests.get(url=url)
        info = r.json()
        if info['code'] == 0:
            f.write(','.join([
                str(info['data']['mid']),
                str(info['data']['name']),
                str(info['data']['level']),
                '用户存在\n'
            ]))
        else:
            f.write(str(i) + ', , ,' + '用户不存在\n')

