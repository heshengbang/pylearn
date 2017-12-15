#!/usr/bin/python
# -*- coding:UTF-8 -*-
num = int(raw_input("请输入第几月：\n"))
sum = 0
a,b = 1,1

if num<1:
	print "输入有误"
if num==1:
	sum = a+b
	#print "当前第%d个月，有兔子%d只"%(num,2)
if num==2:
	sum = a+b
	#print "当前第%d个月，有兔子%d只"%(num,2)

for i in range(3,num+1):
	if i%2==1:
		sum = a+b
		a=a+b
		#print "当前第%d个月，有兔子%d只"%(i,a),
	if i%2==0:
		sum = a+b
		b=b+a
		#print "当前第%d个月，有兔子%d只"%(i,b)
		
print "当前第%d个月，有兔子%d只"%(num,sum)
