#!/usr/bin/python
# -*- coding:UTF-8 -*-

a = int(raw_input("请输入a: "))
n = int(raw_input("请输入n: "))

total = 0
tmp1 = 0
tmp2 = 0

for i in range(1,n+1):
	tmp2 = tmp1 + (10**(i-1))*a
	total += tmp2
	tmp1 = tmp2
	
print "结果为%d"%total

'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
Tn = 0
Sn = []
n = int(raw_input('n = '))
a = int(raw_input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print Tn
 
Sn = reduce(lambda x,y : x + y,Sn)
print "计算和为：",Sn

'''
