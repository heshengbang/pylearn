#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
a = int(raw_input("请输入第一个数字：\n"))
b = int(raw_input("请输入第二个数字：\n"))
c = int(raw_input("请输入第三个数字：\n"))

if a>b:
	tmp=a
	a=b
	b=tmp
if a>c:
	tmp=a
	a=c
	c=tmp
if b>c:
	tmp=b
	b=c
	c=tmp
print a,b,c

'''
l = []
for i in range(3):
    x = int(raw_input('integer:\n'))
    l.append(x)
l.sort()
print l
	