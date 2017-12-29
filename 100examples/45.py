#!/usr/bin/python
# -*- coding: UTF-8 -*-
num = int(raw_input("求多少以内所有数字的和："))

total = 0

for i in range(1,num+1):
	total += i
	
print "1～%d的数字之和为：%d" % (num,total)