#!/usr/bin/python
# -*- coding: UTF-8 -*-
a = [9,6,5,4,1]

for i in range(len(a)-1,-1,-1):
	print a[i],

'''
题目：将一个数组逆序输出。

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
if __name__ == '__main__':
    a = [9,6,5,4,1]
    N = len(a) 
    print a
    for i in range(len(a) / 2):
        a[i],a[N - i - 1] = a[N - i - 1],a[i]
    print a

'''