#!/usr/bin/python
# -*- coding: UTF-8 -*-

num1 = int(raw_input("请输入："))
num2 = int(raw_input("请输入："))

if num1 < num2:
	print "%d小于%d"%(num1,num2)
elif num1 == num2:
	print "%d等于%d"%(num1,num2)
else:
	print "%d大于%d"%(num1,num2)
