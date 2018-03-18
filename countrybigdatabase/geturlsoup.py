#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urllib2test
   Description :
   Author :       gaoxi
   date：          2017/12/30
-------------------------------------------------
   Change Activity:
                   2017/12/30:
-------------------------------------------------
"""
import urllib2
from bs4 import BeautifulSoup
import logging
from agent import headers
def get_url_soup(url):
	maxtrytimes = 10
	for trytimes in range(maxtrytimes):
		try:
			url_request = urllib2.Request(url)
			url_request.add_header('user-agent',headers())
			url_code = urllib2.urlopen(url_request,timeout=50000)
			url_content = url_code.read().decode('gbk').encode('utf-8')
			url_soup = BeautifulSoup(url_content,'html.parser')
			# url_soup = BeautifulSoup(url_content, 'lxml')
			return url_soup
			break
		except :
			if trytimes < (maxtrytimes - 1):
				continue
			else:
				print logging.error("Has tried %d times to access url %s, all failed!"%(maxtrytimes, url))

if __name__ == "__main__":
	url_seed = 'http://www.o994.cn/Info.asp?dm=370811018000'  # 山东省 青岛市 平度市 田庄镇
	print get_url_soup(url_seed)