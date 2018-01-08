#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Node:
	def __init__(self,before,value,after):
		self.before = before
		self.value = value
		self.after = after
num = int(raw_input("请输入："))

circle = []
for i in range(num):
	node = Node("",i+1,"")
	circle.append(node)
for i in range(num):
	if i == 0:
		circle[i].before = circle[num-1]
		circle[i].after = circle[i+1]
	elif i == num-1:
		circle[i].before = circle[i-1]
		circle[i].after = circle[0]
	else:
		circle[i].before = circle[i-1]
		circle[i].after = circle[i+1]
node = circle[0]
'''
while True:
	print "%d --- %d --- %d"%(node.before.value,node.value,node.after.value)
	node = node.after
	if node.value == 1:
		break
'''
count=1
while True:
	if count % 3 == 0:
		print "%d"%node.value
		node.before.after = node.after
		before = node.before
		node = node.after
		node.before = before
	else:
		node = node.after
	count += 1
	if count == 4:
		count = 1
	if node == node.before or node.after == node:
		break
print node.value
		
		