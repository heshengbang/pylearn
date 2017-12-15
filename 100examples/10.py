#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time


print "After I output, will wait one second and output again."
time.sleep(1)
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
