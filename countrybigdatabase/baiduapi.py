#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     baiduapi
   Description :
   Author :       gaoxi
   date：          2018/1/2
-------------------------------------------------
   Change Activity:
                   2018/1/2:
-------------------------------------------------
"""
import json

import requests


url = 'http://api.map.baidu.com/?qt=s&c=236&wd=%E9%9D%92%E5%B2%9B%20%E6%96%87%E5%BC%A0%E6%9D%91&rn=10&ie=utf-8&oue=1&fromproduct=jsapi&res=api&callback=BMap._rd._cbk10790&ak=4qdl6gwAEmpyrBPBNj6VIGqR'
header = {'Referer':'http://www.gpsspg.com/iframe/maps/baidu_170418.htm?mapi=1','User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}
url_request = requests.get(url,headers=header)




print url_request.content