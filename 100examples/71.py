#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Student:
	stuCount = 0
	def __init__(self, name, grade):
		self.name = name
		self.grade = grade
		Student.stuCount += 1
		
	def printStu(self):
		print "学生名是：",self.name,"学生成绩是：",self.grade

def input(num):
	students = []
	while num>0:
		name = raw_input("please enter name：")
		grade = int(raw_input("please enter grade："))
		student = Student(name,grade)
		students.append(student)
		num -= 1
		
	return students
		
def output(students):
	for student in students:
		student.printStu()
		
	print "共计 %d"%Student.stuCount," 名学生"
		
num = int(raw_input("how many students you want to enter:"))
print "please enter %d students's data"%num
students = input(num)
output(students)
