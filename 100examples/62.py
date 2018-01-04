#!/usr/bin/python
# -*- coding: UTF-8 -*-
big_str = raw_input("请输入所有字符：")
little_str = raw_input("请输入你要查找的字符：")
index = big_str.find(little_str)
print "%s在%s的第%d个字符处。"%(little_str, big_str, index)