#!/bin/python3

import sys

hour = int(input().strip())
mint = int(input().strip())

table = dict(1 = 'one',
         2 = 'two',
         3 = 'three',
         4 = 'four',
         5 = 'five',
         6 = 'six',
         7 = 'seven',
         8 = 'eight',
         9 = 'nine',
         0 = 'zero'
)


#if m == 0:
    #print("%s o' clock" %h)
#elif 0 < m < 30 and m != 15:
    #print("%s past %s" %(m,h))
#elif m == 15:
    #print("quater past %s" %h)
#elif m == 30:
    #print("half past %s" %h)
#elif 30 < m < 60 and m != 45:
    #print("%s minutes to %s" %(nm,nh))

print(table)
