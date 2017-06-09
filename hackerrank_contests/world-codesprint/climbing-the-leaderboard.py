#!/bin/python3

import sys

n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
# your code goes here
scores = sorted(list(set(scores)), reverse=True)
n = len(scores)
# print(scores)
j=n-1
for i in range(m):
    while j>=0:
        if alice[i] > scores[j]:
            if j==0:
                print(1)
                break
            else:
                j -= 1
        elif alice[i] == scores[j]:
            print(j+1)
            break
        else:
            print(j+2)
            break
