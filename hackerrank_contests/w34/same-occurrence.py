#!/bin/python3

import sys

if __name__ == "__main__":
    n, q = input().strip().split(' ')
    n, q = [int(n), int(q)]
    arr = list(map(int, input().strip().split(' ')))
    for a0 in range(q):
        x, y = input().strip().split(' ')
        x, y = [int(x), int(y)]
        # Write Your Code Here
