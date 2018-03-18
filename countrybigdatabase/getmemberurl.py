#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     getlink
   Description :
   Author :       gaoxi
   date：          2017/12/30
-------------------------------------------------
   Change Activity:
                   2017/12/30:
-------------------------------------------------
"""
from geturlsoup import get_url_soup


def get_member_url(url_seed):
	url_list = []
	soup = get_url_soup(url_seed)
	soup = soup.find('td',attrs={'style':'display:none'})
	url_soup_list = soup.find_all('a',attrs={'target':'_blank'})
	for url in url_soup_list:
		url = 'http://www.o994.cn/'+url['href']
		url_list.append(url)
		# print url

	return url_list



if __name__ == '__main__':

	url_seed = 'http://www.o994.cn/Info.asp?dm=370302114000'
	# soup = get_url_soup(url_seed)
	print  get_member_url(url_seed)
