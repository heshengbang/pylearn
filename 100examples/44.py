#!/usr/bin/python
# -*- coding: UTF-8 -*-
X = [[12,7,3],
	 [4 ,5,6],
	 [7 ,8,9]]
 
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0,],
		  [0,0,0,],
		  [0,0,0,]]

for i in range(3):
	for j in range(3):
		result[i][j]=X[i][j]+Y[i][j]
		
for i in range(3):
	print result[i]