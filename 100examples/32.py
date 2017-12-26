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
	'''	
num = len(words)
num -= 1
while num>-1:
	print words[num],
	num -= 1
	'''
for i in words[::-1]:
	print i,