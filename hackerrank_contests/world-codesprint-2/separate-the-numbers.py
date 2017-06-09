#!/bin/python3

import sys
import itertools
   
    
q = int(input().strip())
s = []

for a0 in range(q):
    s.append(input().strip())


max_len=len(max(s))
max_len = max_len //2 

num_list = list(range(10**max_len))
print(num_list)

def check_beauty(s):
    s = list(map(int, s))
    for i in range(1, len(s)//2 +1):




for i in s:
	check_beauty(i)
