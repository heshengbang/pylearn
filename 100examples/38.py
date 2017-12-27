#!/usr/bin/python
# -*- coding: UTF-8 -*-

nums = []

for i in range(3):
	nums.append([])
	for j in range(3):
		tmp = float(raw_input("请输入："))
		nums[i].append(tmp)
total = 0.0
for i in range(3):
	total += nums[i][i]
print total