#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
jia=['a','b','c']
yi=['x','y','z']
for i in jia:
	for j in yi:
		if i=='a' and j=='x':
			continue
		elif i=='c' and j=='x':
			continue
		elif i=='c' and j=='z':
			continue
		else:
			print i,
			print "--",
			print j
			yi.remove(j)
			break
'''

for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print 'order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k))
