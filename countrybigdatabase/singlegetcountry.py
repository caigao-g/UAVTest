#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     singlegetcountry
   Description :
   Author :       gaoxi
   date：          2018/1/18
-------------------------------------------------
   Change Activity:
                   2018/1/18:
-------------------------------------------------
"""
from geturlsoup import get_url_soup
import re
import pandas as pd

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

members = []
def get_country_list(url): # 获得本镇（乡，街道）的村委会（社区）列表
	# sheng_name_list = []
	# shi_name_list = []
	# xian_name_list = []
	# zhen_name_list = []
	soup = get_url_soup(url)
	# print soup
	country_name_list = []
	pattern = re.compile(u'\>[\u4e00-\u9fa5]+\<')
	code_pattern = re.compile('\d{15}')
	global members
	membership_soup = soup.find('tr', attrs={'class': 'tdbg', 'onmouseout': "this.className='tdbg'"})
	# print membership_soup
	membership_list = membership_soup.find_all('a')
	for membership in membership_list:
		membership = str(membership).decode('utf-8')
		member = re.findall(pattern,membership)# 匹配各级隶属
		# print member[0][1:-1]
		members.append(member[0][1:-1])

	country_list = soup.find_all('a',attrs={'target':'_blank'})
	for country in country_list:
		country_name = country.string.encode('utf-8')
		country_code = re.findall(code_pattern,str(country))[0][0:12]
		# 将各级隶属和村名填入列表
		country_name_list.append([country_code,members[-2],members[-3],members[-4],members[-5],country_name])
		# sheng_name_list.append(members[-2])
		# shi_name_list.append(members[-3])
		# xian_name_list.append(members[-4])
		# zhen_name_list.append(members[-5])

	return country_name_list



url_seed = 'http://www.o994.cn/Info.asp?dm=130132202000' # 山东省 济南

columns = ['行政代码','省级','市级','区县','乡镇','村']
coutries = pd.DataFrame(get_country_list(url_seed),columns=columns)
filename = ''
for member in members[-2:-6:-1]:
	filename += member
filename += '.csv'
print filename
coutries.to_csv(filename, sep='	', header=False, index=False)
