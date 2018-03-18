#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     combinefiles
   Description :
   Author :       gaoxi
   date：          2018/1/17
-------------------------------------------------
   Change Activity:
                   2018/1/17:
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
# for file in file_list:
# 	print file
# 读取第一个CSV文件

# df = pd.read_csv(Folder_Path +'//'+ file_list[944])
# print df
df = pd.read_csv(Folder_Path +'//'+ file_list[0])
columns = ['行政代码','省级','市级','区县','乡镇','村']
pd.colums = columns
# 将读取的第一个CSV文件写入合并后的文件保存
df.to_csv(SaveFile_Path +'//'+ SaveFile_Name, header=False,index=False)

# 循环遍历列表中各个CSV文件名，并追加到合并后的文件
for i in range(1, len(file_list)):

	if os.path.getsize(file_list[i]) != 0:
		df = pd.read_csv(Folder_Path + '//' + file_list[i], header=None)
		df.to_csv(SaveFile_Path + '//' + SaveFile_Name, index=False, header=False,mode='a+')
	else :
		print i,file_list[i].decode('gbk')