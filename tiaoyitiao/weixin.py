#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     weixin
   Description :
   Author :       gaoxi
   date：          2018/1/8
-------------------------------------------------
   Change Activity:
                   2018/1/8:
-------------------------------------------------
"""
import os

def get_screen_image():
	os.system('adb.exe shell creencap -p 手机存储/headpic.jpg')

get_screen_image()