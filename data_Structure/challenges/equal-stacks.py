#!/bin/python
#python2

import sys


n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))

def get_reversed_prefix_sum(h1):
    h1_ = []
    x = 0
    for i in reversed(h1):
        x = i + x
        h1_.append(x)
    return list(reversed(h1_))

h1_reversed = get_reversed_prefix_sum(h1)
h2_reversed = get_reversed_prefix_sum(h2)
h3_reversed = get_reversed_prefix_sum(h3)


def get_ans(l1,l2,l3):
    for i in l1:
        if i in l3 and i in l2:
            return i

    return 0

n = min(n1,n2,n3)

if n1==n:
    print(get_ans(h1_reversed, h2_reversed, h3_reversed))
elif n2 == n:
    print(get_ans(h2_reversed, h1_reversed, h3_reversed))
else:
    print(get_ans(h3_reversed, h1_reversed, h2_reversed))
