#!/usr/bin/python
# -*- coding: UTF-8 -*-
num = int(raw_input("打算输入多少个数字："))
nums = []
while num>0:
	temp = int(raw_input("请输入："))
	nums.append(temp)
	num -= 1
copy_nums = nums[:]	
for i in range(len(nums)):
	for j in range(i+1, len(nums)):
		if nums[i] < nums[j]:
			nums[i],nums[j] = nums[j],nums[i]
big = copy_nums.index(nums[0])
small = copy_nums.index(nums[len(nums)-1])

copy_nums[0],copy_nums[big] = copy_nums[big],copy_nums[0]
copy_nums[len(nums)-1],copy_nums[small] = copy_nums[small],copy_nums[len(nums)-1]
print copy_nums
			