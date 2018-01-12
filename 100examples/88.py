#!/usr/bin/python
# -*- coding: UTF-8 -*-
num = 8
while num>0:
    read = int(raw_input("请输入数字："))
    if read<1 or read>50:
        print "重新输入"
    else:
        for i in range(read):
            print "*",
        print
        num -= 1
print "---end---"