"""
    练习9
"""

word_list = []
word_dict = {}

with open('../data/The Old Man and the Sea.txt', 'r', encoding='utf-8') as logfile:
    logdata = logfile.readlines()
    for row in logdata:
        row = row.replace('.', '').replace(',', '').replace('?', '').\
            replace('“', '').replace('"', '').replace('\n', '').replace('\u3000', '')
        word_list = word_list + row.split(' ')
    # 将单词全转为小写
    word_list = [s.lower() for s in word_list]
    # 单词去重
    word_set = set(word_list)
    # 计算每个单词出现次数，并以字典的方式存储
    for item in word_set:
        if item != '':
            word_dict[item.lower()] = word_list.count(item.lower())
    # 按单词出现的次数排序
    sorted_word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    # 输出
    for i in range(10):
        print(sorted_word_dict[i][0] + "," + str(sorted_word_dict[i][1]))
