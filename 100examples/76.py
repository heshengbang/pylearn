#!/usr/bin/python
# -*- coding: UTF-8 -*-
def myFunction(num):
	result = 0.0
	if num%2==0:
		for i in range(2,num+1,2):
			result += 1.0/i
	else:
		for i in range(1,num+1,2):
			result += 1.0/i
	return result
num=0
while not num<0:
	num = int(raw_input("请输入："))
	print myFunction(num)
	