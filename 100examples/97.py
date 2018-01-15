#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sys import stdout
filename = raw_input("输入文件名：")
fp = open(filename, "w")
ch = raw_input("请输入字符串：")
while ch != '#':
	fp.write(ch)
	stdout.write(ch)
	ch = raw_input('')
fp.close()