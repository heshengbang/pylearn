#!/usr/bin/python
# -*- coding: UTF-8 -*-
num=int(raw_input("请输入要判断的五位数:"))
if num<10000 or num>99999:
	print "输入错误"
else:
	wu=num/10000
	si=(num - wu*10000)/1000
	san=(num - wu*10000 - si*1000)/100
	er=(num - wu*10000 - si*1000-san*100)/10
	yi=num - wu*10000 - si*1000-san*100-er*10
	if wu==yi and si==er:
		print "%d是回文数"%num
	else:
		print "%d不是回文数"%num