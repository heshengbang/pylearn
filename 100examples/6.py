#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
num = int(raw_input("你要第几个斐波那契数列：\n"))
sum = 0
a = 0
b = 1
if num<=0:
	print "输入信息错误"
for i in range(0,num):
	if i>=2:
		if i%2==0:
			a=a+b
			print "第",i,"个斐波那契数为%d"%a
		if i%2==1:
			b=b+a
			print "第",i,"个斐波那契数为%d"%b
	if i==0:
		print "第",i,"个斐波那契数为%d"%a
	if i==1:
		print "第",i,"个斐波那契数为%d"%b
sum=a+b		
print "第",num,"个斐波那契数为%d"%sum

'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
 
# 输出了第10个斐波那契数列
num = int(raw_input("你要第几个斐波那契数列：\n"))
print fib(num)
