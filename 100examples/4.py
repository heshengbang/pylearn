#!/usr/bin/python
# -*- coding: UTF-8 -*-
year = int(raw_input("year:\n"))
month = int(raw_input("month:\n"))
day = int(raw_input("day:\n"))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
sum=0
if month>0 and month<=12:
	sum+=months[month-1]
else:
	print "month is error"

sum += day

if year%400==0 or (year%4==0 and year%100!=0):
	sum += 1
	
print "这一天是这一年的第%d天" % sum
