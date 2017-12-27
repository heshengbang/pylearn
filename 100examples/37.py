#!/usr/bin/python
# -*- coding: UTF-8 -*-
nums = []

while True:
	temp = int(raw_input("请输入："))
	if temp == -1:
		break
	else:
		nums.append(temp)

length = len(nums)

for i in range(length):
	temp = nums[i]
	for j in range(i+1,length):
		if temp > nums[j]:
			nums[i]=nums[j]
			nums[j]=temp
			temp=nums[i]
				
print nums
'''

题目：对10个数进行排序。

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
if __name__ == "__main__":
    N = 10
    # input data
    print '请输入10个数字:\n'
    l = []
    for i in range(N):
        l.append(int(raw_input('输入一个数字:\n')))
    print
    for i in range(N):
        print l[i]
    print
 
    # 排列10个数字
    for i in range(N - 1):
        min = i
        for j in range(i + 1,N):
            if l[min] > l[j]:min = j
        l[i],l[min] = l[min],l[i]
    print '排列之后：'
    for i in range(N):
        print l[i]
'''