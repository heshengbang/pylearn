#!/usr/bin/python
# -*- coding: UTF-8 -*-
num = raw_input("请输入一个八进制数字：")#10
result = 0
for i in range(len(num)):
    result = result*8 + ord(num[i])-ord('0')
print "八进制数字%s的十进制表示是%d"%(num,result)