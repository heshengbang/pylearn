#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

chuan = raw_input("请输入字符串：")
length = len(chuan)

def fanzhuan(string,length):
	if length-1>-1:
		sys.stdout.write(string[length-1])
		fanzhuan(string,length-1)
		
fanzhuan(chuan,length)
print