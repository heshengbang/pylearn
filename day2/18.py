#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
 
# 重命名文件test1.txt到test2.txt。
os.rename( "foo.txt", "test2.txt" )
print os.getcwd()+"/foo.txt"
