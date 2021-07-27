"""
    练习13
"""

import os
import shutil
import pathlib

suffix_list = [
    '.jpg', '.mp4', '.txt',
    '.docx', '.pptx', '.xlsx',
    '.png', '.py', '.c', '.cpp',
    '.exe', '.mp3', '.gif',
    '.o', '.px', '.q',
]
origin_dir_path = '../杂乱的文件目录'
target_dir_path = '../分类后的文件目录'

# 创建分类后的根目录
os.makedirs(target_dir_path, exist_ok=True)

# 创建分类的目录
for i in range(len(suffix_list)):
    classified_dir_path = os.path.join(target_dir_path, suffix_list[i])
    os.makedirs(classified_dir_path, exist_ok=True)

# 对文件进行分类
file_names = os.listdir(origin_dir_path)
for file_name in file_names:
    old_path = os.path.join(origin_dir_path, file_name)
    new_path = os.path.join(target_dir_path, pathlib.Path(file_name).suffix, file_name)

    # 处理多次整理时，文件同名的问题
    if os.path.isfile(os.path.join(new_path)):
        print('hello')
        file_name_new = file_name[:file_name.rfind('.')] + '_2' + file_name[file_name.rfind('.'):]
        new_path = os.path.join(target_dir_path, pathlib.Path(file_name_new).suffix, file_name_new)

    shutil.move(old_path, new_path)
