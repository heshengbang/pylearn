#!/usr/bin/python
# -*- coding: UTF-8 -*-

def judge(num):
	zs = []
	'''
	tmp=num
	i=1
	
	while(i<num):
		if tmp%i==0:
			zs.append(i)
			tmp /= i
			if i==1:
				i += 1
		else:
			i += 1
	'''
	for i in range(1,num):
		if num%i==0:
			zs.append(i)
	total = reduce(lambda x, y : x+y, zs)
	
	if total==num:
		return 1
	else:
		return 0
			
nums = []

for j in range(2,1000):
	if judge(j)==1:
		print "%d为完数"%j
		nums.append(j)

print "1000以内的完数为：",nums
	
	
'''

题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

'''