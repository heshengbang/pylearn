#!/usr/bin/python
# -*- coding: UTF-8 -*-
num = raw_input("请输入：")#1234
result = ""
if len(num) != 4:
    print "输入错误"
else:
    for i in range(len(num)):#1 2
        temp = (int(num[i])+5)%10#6 7
        result = str(temp) + result#6 76

print "%s"%result
