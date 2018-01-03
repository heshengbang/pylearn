#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 077
b = a ^ 3 # 111111^11=111100=60
print 'The a ^ 3 = %d' % b
b ^= 7 # 111100^000111=111011=
print 'The a ^ 3 = %d' % b
