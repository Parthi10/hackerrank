#!/usr/bin/python3
def maxXor(l, r):
    p = l ^ r
    ans = 1
    while p:
        ans <<= 1
        p >>= 1
    return ans - 1


if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print(maxXor(l, r))
