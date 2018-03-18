#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     make_test
   Description :
   Author :       gaoxi
   date：          2018/3/17
-------------------------------------------------
   Change Activity:
                   2018/3/17:
-------------------------------------------------
"""
import linecache

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

testq = 'zonghetest.txt'

maxline = len((open(testq).readlines()))+1
# print maxline
for i in range(1,maxline,2):
	question = linecache.getline(testq, i)
	with open('test3.txt','a+') as tt:
		tt.writelines(question)
	answer = linecache.getline(testq,i+1)
	with open('answers3.txt','a+') as aa:
		aa.writelines(answer)