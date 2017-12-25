#!/usr/bin/python
# -*- coding: UTF-8 -*-
def age(num):
	if num==1:
		return 10
	else:
		return age(num-1)+2
print age(5)