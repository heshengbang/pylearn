#!/usr/bin/python
# -*- coding: UTF-8 -*-

题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
使用节点-环来完成

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

检查环是否正确
while True:
	print "%d --- %d --- %d"%(node.before.value,node.value,node.after.value)
	node = node.after
	if node.value == 1:
		break
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
'''


class Node:
	def __init__(self,before,value,after):
		self.before = before
		self.value = value
		self.after = after

num = int(raw_input("请输入："))
first = Node("",1,"")
node = Node("",0,"")
for i in range(num):
	if i == 0:
		first.after = Node("",0,"")
		node = first.after
		node.before = first
	else:
		node.value=i+1
		if i == num-1:
			node.after = first
		else:
			node.after = Node(0,"")
		node = node.after
node = first
while True:
	print "%d --- %d"%(node.value,node.after.value)
	if node.after.value == 1:
		break
	node = node.after
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
		
'''