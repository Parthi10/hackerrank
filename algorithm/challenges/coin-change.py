#!/bin/python3

import sys
###############
# y y+1 (increases sideways) varies with column
# x -> varies with rows
# x+1 ->

def getWays(n, m, c, dp):
    for x in range(1, m):
        for y in range(1, n+1):
            units = y
            largestCoin = c[x]
            if largestCoin > units:
                dp[x][y] = dp[x-1][y]
            else:
                dp[x][y] = dp[x-1][y] + dp[x][y-largestCoin]

    return dp[m-1][n]

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
dp = [[0 for x in range(n+1)] for y in range(m)]

c = list(map(int, input().strip().split(' ')))
for y in range(n+1):
    dp[0][y] = 1 if y % c[0] == 0 else 0
for x in range(m):
    dp[x][0] = 1

ways = getWays(n, m, c, dp)
print(ways)
