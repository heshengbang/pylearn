#!/usr/bin/python
# -*- coding: UTF-8 -*-

def change(a, b):
	return (b, a)
	
a = raw_input("a的变量值为：")
b = raw_input("b的变量值为：")

a,b = change(a,b)

print "a的变量值为%s, b的变量值为%s"%(a,b)