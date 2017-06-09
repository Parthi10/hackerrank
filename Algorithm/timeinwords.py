#!/bin/python3

import sys

hour = int(input().strip())
mint = int(input().strip())

table = {1 : 'one',
         2 : 'two',
         3 : 'three',
         4 : 'four',
         5 : 'five',
         6 : 'six',
         7 : 'seven',
         8 : 'eight',
         9 : 'nine',
         0 : 'zero',
         10 : 'ten',
         11 : 'eleven',
         12 : 'twelve',
         13 : 'thirteen',
         14 : 'fourteen',
         15 : 'fifteen',
         16 : 'sixteen',
         17 : 'seventeen',
         18 : 'eighteen',
         19 : 'nineteen',
         20 : 'twenty',




}
if len(str(hour)) == 2: #10,11,12
	h_num1,hnum2 = map(int,str(hour).strip()) #strip apart
m_num1,m_num2 = map(int, str(mint).strip()) #mint always in two digits

m = str(table[m_num1])+' '+str(table[m_num2])
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
print(m)
