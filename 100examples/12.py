#!/usr/bin/python
# -*- coding: UTF-8 -*-

from math import sqrt
from sys import stdout

count=0
nums=[]
flag=0

for num in range(3,20000):
	k = int(sqrt(num+1))
	for i in range(2, k+1):
		if num%i==0:
			flag=0
			break
		if num%i!=0 and i==k:
			flag=1
			
	if flag==1:
		flag=0
		count+=1
		nums.append(num)
			

print "101～200间质数有%d"%count,"分别是",nums
			