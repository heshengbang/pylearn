#!/usr/bin/python
# -*- coding: UTF-8 -*-

heigh = 100.00

total=0.00
up10=0.00

for i in range(1,11):
	total += heigh
	heigh /= 2
	if i==10:
		up = heigh
	else:
		total += heigh
		
print "第十次触地经过%.8f米，第十次反弹高度为%.8f米"%(total, up)



'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''