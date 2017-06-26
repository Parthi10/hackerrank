#!/bin/python3

import sys
from itertools import combinations_with_replacement
from fractions import Fraction

n = int(input().strip())
toy_types = []
for a0 in range(n):
    ai, bi, ci = input().strip().split(' ')
    ai, bi, ci = [int(ai), int(bi), int(ci)]
    toy_types.append(sorted([ai,bi,ci]))
combos = combinations_with_replacement(list(range(n)), 2)

# print(toy_types)

volume_sum = 0
num = 0
for combo in combos:
    i, j = list(combo)
    l,b,h=0,0,0
    for i in toy_types[i:j+1]:
        l_temp,b_temp, h_temp = i
        if l_temp>l: l= l_temp
        if b_temp>b: b= b_temp
        if h_temp>h: h= h_temp
    volume_sum += l*b*h
    num+=1

f = Fraction(volume_sum, num)
m = 10**9 + 7
q =  f.denominator
p = f.numerator
q_inv = pow(q, m-2, m)
print((p*q_inv )% m)
