#!/usr/bin/python
# -*- coding: UTF-8 -*-
str1 = raw_input("请输入一个字符串：")
str2 = raw_input("请输入一个子字符串：")
ncount = str1.count(str2)
print "%s在%s中出现了%d次"%(str2,str1,ncount)