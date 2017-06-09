#!/bin/python3

import sys

bra_list = {
            ']': '[',
            ')': '(',
            '}': '{',
    }

def isBalanced(bras):
    bra_stack = []
    for bra in bras:
        if bra_stack and bra_stack[-1] == bra_list.get(bra):
            bra_stack.pop()
        else:
            bra_stack.append(bra)

    return "YES" if bra_stack == [] else "NO"

t = int(input().strip())
for a0 in range(t):
    bras = list(input().strip())

    print(isBalanced(bras))
