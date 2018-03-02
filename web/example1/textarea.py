#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cgi, cgitb

form = cgi.FieldStorage()

if form.getvalue("textcontent"):
	text_content = form.getvalue("textcontent")
else:
	text_content = "没有内容"

print "Content-type:text/html"
print 
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>菜鸟教程CGI测试实例</title>"
print "</head>"
print "<body>"
print "<h2>输入的内容是：%s</h2>" % text_content
print "</body>"
print "</html>"
