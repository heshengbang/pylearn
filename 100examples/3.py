#!/usr/bin/python
# -*- coding: UTF-8 -*-
		
def judge( i ):
	j = 168/i
	if(i>j and (i+j)%2==0 and (i-j)%2==0):
		m = (i+j)/2
		n = (i-j)/2
		if ((m*m - n*n)==168):
			x = n*n-100
			print "x的直为：",x
			return 1
	
	return 0

for i in range(2,85):
	if (judge(i) == 1):
		print i
	