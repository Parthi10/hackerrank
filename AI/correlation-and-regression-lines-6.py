# # from scipy.stats.stats import pearsonr
# import numpy as np
#
import math
physics_scores = [int(x) for x in input().strip().split(' ')]
history_scores = [int(x) for x in input().strip().split(' ')]
# print(physics_scores, history_scores)
# print(len(physics_scores), len(history_scores))
# # print("%.3f" %pearsonr(physics_scores,history_scores))
# print(np.corrcoef(physics_scores, history_scores))

def average(l):
    n = len(l)
    total = sum(l)
    return total//n

def pearson_corr(l1,l2):
    n = len(l1)# should be equal to len(l2)
    x = average(l1)
    y = average(l2)
    xdiff = 0
    ydiff = 0
    diffprod = 0
    for i in range(n):
        xdiff_temp = l1[i] - x
        ydiff_temp = l2[i] - y
        diffprod += xdiff_temp * ydiff_temp
        xdiff += xdiff_temp ** 2
        ydiff += ydiff_temp ** 2
    # print(diffprod)
    # print(xdiff, ydiff)
    return diffprod / math.sqrt(xdiff * ydiff)

print(pearson_corr(physics_scores, history_scores))
