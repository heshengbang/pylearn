#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","","TESTDB" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()

db.close()
