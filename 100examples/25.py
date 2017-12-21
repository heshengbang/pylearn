#!/usr/bin/python
# -*- coding: UTF-8 -*- 

total=0

for i in range(1,21):
	leijia=1
	for j in range(1,i+1):
		leijia *= j
	print "%d垒乘结果为%d"%(i,leijia)
	total += leijia
	
print total


'''
题目：求1+2!+3!+...+20!的和。
'''