#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     tryseverioultimes
   Description :
   Author :       gaoxi
   date：          2018/1/20
-------------------------------------------------
   Change Activity:
                   2018/1/20:
-------------------------------------------------
"""
def getUrl_multiTry(url):
	user_agent = '"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"'
	headers = {'User-Agent': user_agent}
	maxTryNum = 10
	for tries in range(maxTryNum):
		try:
			req = urllib2.Request(url, headers=headers)
			html = urllib2.urlopen(req).read()
			break
		except:
			if tries < (maxTryNum - 1):
				continue
			else:
				logging.error("Has tried %d times to access url %s, all failed!", maxTryNum, url)
				break

	return html