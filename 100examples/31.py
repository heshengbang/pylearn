#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
letter = raw_input("please input:")
#while letter  != 'Y':
if letter == 'S':
    print ('please input second letter:')
    letter = raw_input("please input:")
    if letter == 'a' or letter == 'A':
        print ('Saturday')
    elif letter  == 'u' or letter == 'U':
        print ('Sunday')
    else:
        print ('data error')
    
elif letter == 'F':
    print ('Friday')
    
elif letter == 'M':
    print ('Monday')
    
elif letter == 'T':
    print ('please input second letter')
    letter = raw_input("please input:")
 
    if letter  == 'u' or letter == 'U':
        print ('Tuesday')
    elif letter  == 'h' or letter == 'H':
        print ('Thursday')
    else:
        print ('data error')
        
elif letter == 'W':
    print ('Wednesday')
else:
    print ('data error')