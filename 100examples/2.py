#!/usr/bin/python
# -*- coding: UTF-8 -*-

profit_level=[0,100000,200000,400000,600000,1000000]
rate=[0.1,0.075,0.05,0.03,0.015,0.01]

profit=int(raw_input("利润:"))

bonus=0

for i in range(1,6):
	if(profit>profit_level[i]):
		var=(profit_level[i]-profit_level[i-1])*rate[i-1]
		print "if奖金为：",profit_level[i],"奖励为：",var
		bonus+=var
		if(i==5):
			var=(profit-profit_level[i])*rate[i]
			print "if奖金为：",profit_level[i],"奖励为：",var
			bonus+=var

	else:
		var=(profit-profit_level[i-1])*rate[i-1]
		print "if奖金为：",profit_level[i],"奖励为：",var
		bonus+=var
		break

print bonus

