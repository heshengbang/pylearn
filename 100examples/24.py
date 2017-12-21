#!/usr/bin/python
# -*- coding: UTF-8 -*-

z=2.0
m=1.0
num=0.00

for i in range(20):
	num += z/m
	print num
	z,m=z+m,z
	
print "数字结果为%.20f"%num

'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''
