#!/usr/bin/python
# -*- coding: UTF-8 -*-

num = int(raw_input("请输入："))
nums = []
for i in range(num):
    nums.append(i+1)

i=1

while len(nums)>1:
    if i%3==0:
        nums.pop(0)
    else:
        nums.insert(len(nums), nums.pop(0))
    i += 1
print nums
	