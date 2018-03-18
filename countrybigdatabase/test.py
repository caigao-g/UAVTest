#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       gaoxi
   date：          2018/1/18
-------------------------------------------------
   Change Activity:
                   2018/1/18:
-------------------------------------------------
"""

import pandas as pd
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

Folder_Path = r'F:/countrybigdatabase/countyfiles'
SaveFile_Path = r'F:/countrybigdatabase/combine'
SaveFile_Name = r'shandong.csv'  # 合并后要保存的文件名

# 修改当前工作目录
os.chdir(Folder_Path)
# 将该文件夹下的所有文件名存入一个列表
file_list = os.listdir(Folder_Path)
for i in file_list:
	print i.decode('gbk')
