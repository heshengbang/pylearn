#!/usr/bin/python
# -*- coding: UTF-8 -*-
num = [2, 8, 6, 1, 78, 45, 34, 2]

index = int(raw_input("向后移动多少："))

if index > len(num):
	print "输入出错"
	exit()

num1 = num[:len(num)-index]
num2 = num[len(num)-index:]
num2.extend(num1)
print "原来的数组",num


print "替换后的数组",num2
