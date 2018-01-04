#!/usr/bin/python
# -*- coding: UTF-8 -*-

num = int(raw_input("请输入："))

arrays = []

for i in range(num):#3
	if i >= 2:#0 1
		tmp = i + 1#1 2
		array = []
		for j in range(tmp):#0 1
			if j==0 or j==tmp-1:
				array.append(1)
			else:
				array.append(arrays[i-1][j-1]+arrays[i-1][j])
	else:
		tmp = i + 1
		array = []
		for j in range(tmp):
			array.append(1)
	arrays.append(array)		
for i in arrays:
	for j in i:
		print "%d"%j,
	print