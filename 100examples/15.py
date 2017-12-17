#!/usr/bin/python
# -*- coding: UTF-8 -*-
scope = int(raw_input("请输入一个数字："))
if scope<60:
	print "%d属于C"%scope
elif scope>59 and scope<90:
	print "%d属于B"%scope
elif scope>89:
	print "%属于A"%scope