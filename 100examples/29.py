#!/usr/bin/python
# -*- coding: UTF-8 -*-
num = int(raw_input("请输入不超过五位的数字："))

if num<0 or num>99999:
	print "输入错误！"
else:
	a=num/10000
	b=(num-a*10000)/1000
	c=(num-a*10000-b*1000)/100
	d=(num-a*10000-b*1000-c*100)/10
	e=num-a*10000-b*1000-c*100-d*10
	if a!=0:
		print "五位数，",e,d,c,b,a
	elif b!=0:
		print "四位数，",e,d,c,b
	elif c!=0:
		print "三位数，",e,d,c
	elif d!=0:
		print "两位数，",e,d
	elif e!=0:
		print "个位数，",e
	else:
		print "输入错误！"


