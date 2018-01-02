#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
num1 = int(raw_input("请输入："))
num2 = int(raw_input("请输入："))

bijiao = lambda x,y : (x>y)*x + (x<y)*y

print "%d和%d中，%d是大的"%(num1,num2,bijiao(num1,num2))
