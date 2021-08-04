"""
    练习18
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

# 设置matplotlib对中文的支持
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

movies = pd.read_csv('IMDB-Movie-Data.csv')

# 缺失值处理
for col in movies.columns:
    if not np.all(pd.notnull(movies[col])):
        movies.fillna(movies[col].mean(), inplace=True)

# 得到这些电影数据中评分的平均分
print('所有电影评分的均值：', "%.2f" % movies['Rating'].mean())

# 获取rating和runtime的分布情况
distance_r = 0.5
group_num_r = int((max(movies['Rating']) - min(movies['Rating'])) // distance_r)
plt.figure(figsize=(10,10), dpi=80)
plt.hist(movies['Rating'], bins=group_num_r)
plt.title('所有电影评分的分布', size=25)
plt.savefig('所有电影评分的分布.png')

distance_t = 10
group_num_t = int((max(movies['Runtime (Minutes)']) - min(movies['Runtime (Minutes)'])) // distance_t)
plt.figure(figsize=(10,10), dpi=80)
plt.hist(movies['Runtime (Minutes)'], bins=group_num_t)
plt.title('所有电影时长的分布', size=25)
plt.savefig('所有电影时长的分布.png')

plt.show()

# 统计电影分类的情况
print('所有电影分类的情况如下')
genre = set()
for item in movies['Genre']:
    for i in item.split(','):
        genre.add(i)
genre_table = pd.DataFrame(index=movies['Title'], columns=list(genre))

# 初始化dataframe表格
for i in genre:
    genre_table[i] = 0

# 开始统计
movies_title = list(movies['Title'])
movies_genre = []

for item in movies['Genre']:
    movies_genre.append(item.split(','))
for row in range(len(movies_title)):
    for movie_genre in movies_genre[row]:
        genre_table.loc[movies_title[row], movie_genre] = 1

total = []
for col in genre_table.columns:
    total.append(genre_table[col].sum())
genre_table.loc['总计'] = total
print(genre_table)
