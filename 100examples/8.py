#!/usr/bin/python
# -*- coding:UTF-8 -*-

for i in range(1,10):
	print
	for j in range(1,i+1):
		print "%d*%d=%d"%(i,j,i*j),#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,