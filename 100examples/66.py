#!/usr/bin/python
# -*- coding: UTF-8 -*-

num = int(raw_input("有多少个数字要排序："))
nums = []
while num>0:
	temp = int(raw_input("请输入："))
	nums.append(temp)
	num -= 1

for i in range(len(nums)):
	for j in range(i+1,len(nums)):
		if nums[i] < nums[j]:
			nums[i],nums[j] = nums[j],nums[i]
for i in nums:
	print "%d"%i,
print
