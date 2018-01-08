#!/usr/bin/python
# -*- coding: UTF-8 -*-

ptr = []
for i in range(5):
	num = int(raw_input('please input a number:\n'))
	ptr.append(num)
ptr.reverse()
print ptr
