#!/usr/bin/python
# -*- coding: UTF-8 -*-


test = int(raw_input("选择测试方式："))
if test == 1:
	a = [1,4,6,9,13,16,19,28,40,100]
else:
	a = [100,40,28,19,16,13,9,6,4,1]

a.append(0)

num = int(raw_input("输入："))
i = len(a)-2

big = True

if a[i]<a[i-1]:
	big = False

while i>-1:
	if big and a[i]<num:
		a[i+1]=num
		break
	elif not big and a[i]>num:
		a[i+1]=num
		break
	else:
		a[i+1],a[i]=a[i],a[i+1]
		i-=1

print a
