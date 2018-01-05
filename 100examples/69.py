#!/usr/bin/python
# -*- coding: UTF-8 -*-
num = int(raw_input("多少个人："))
nums= []
for i in range(num):
	nums.append(i+1)
i=0
j=0
while True:
	print i,j
	if (i+1)%3==0:
		nums.remove(nums[j])
	i += 1
	j += 1
	if j>= num:
		j=0
	if len(nums) == 1:
		break;

print "最后一个人的编号是%d"%nums[0]
		