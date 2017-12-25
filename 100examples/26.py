#!/usr/bin/python
# -*- coding: UTF-8 -*-
num=int(raw_input("请输入要求阶乘的数字："))

def jiecheng(num) :
	if num==1 :
		return 1
	else:
		return num * jiecheng(num-1)

print "%d的阶乘结果是"%num,
print jiecheng(num)