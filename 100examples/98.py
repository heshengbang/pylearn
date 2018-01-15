#!/usr/bin/python
# -*- coding: UTF-8 -*-
fp = open("text.txt", "w")
string = raw_input("please input a string:")
string = string.upper()
fp.write(string)
fp = open("text.txt","r")
print fp.read()
fp.close()