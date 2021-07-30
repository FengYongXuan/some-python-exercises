"""
    挑战题（爬取教务网上的新闻）
"""

import requests
from bs4 import BeautifulSoup

url = 'https://news.njfu.edu.cn/ybdt/'
r = requests.get(url=url)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')

a_list = soup.select('.title > a')
span_list = soup.select('.hits')
title_list = []
href_list = []
time_list = []

for item in a_list:
    title_list.append(item.text)
    href_list.append(item['href'])

for item in span_list:
    time_list.append(item.text[1:])

with open('news_list.csv', 'w', encoding='utf-8') as f:
    f.write(','.join(['文章标题', '发布时间', '文章链接\n']))
    for i in range(len(title_list)):
        f.write(','.join([title_list[i], time_list[i], href_list[i] + '\n']))
