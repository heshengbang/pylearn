#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 077 #111111
b = a|3 #111111|11=111111
print "a | b is %d" % b 
b |= 7 
print "a | b is %d" % b