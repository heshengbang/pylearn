#!/usr/bin/python
# -*- coding: UTF-8 -*-
print "Enter exit to exit enter"
words = []
while True:
	tmp = raw_input()
	if tmp == "exit":
		break
	else:
		words.append(tmp)
		print words,"继续..."

tmp = ",".join(words)
print tmp

'''
L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
print s1
'''
