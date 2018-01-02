#!/usr/bin/python
# -*- coding: UTF-8 -*-

while True:
	num=int(raw_input("请输入:"))
	pingfang=num*num
	if pingfang<50:
		break
	else:
		print "%d的平方是%d"%(num, pingfang)
		
exit();
	