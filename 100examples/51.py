#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 077 #0开头的是八进制 01110111
b = a & 3 # 01110111 & 0000011 = 11

print "a & b = %d"%b # 11
b &= 7 # 011 & 111 = 011
print "a & b = %d"%b