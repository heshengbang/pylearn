#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import calendar

localtime = time.localtime(time.time())
localtime2 = time.asctime( time.localtime(time.time()) )
print "本地时间为：", localtime
print "本地时间为：", localtime2
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
print "___________________输出某月日历_________________"
cal = calendar.month(2017, 12)
print "以下输出的2017年12月份的日历："
print cal;
