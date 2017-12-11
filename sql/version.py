#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

db = MySQLdb.connect("localhost", "root", "", "TESTDB")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print "Database version: %s" % data

db.close()
