#!/usr/bin/python
# -*- coding:UTF-8 -*-

nums=[]
for num in range(100,1000):
	a = int(num/100)
	b = int((num-a*100)/10)
	c = int(num-a*100-b*10)
	result = a*a*a+b*b*b+c*c*c
	if num==result:
		nums.append(num)
print "所有的水仙花数：",nums