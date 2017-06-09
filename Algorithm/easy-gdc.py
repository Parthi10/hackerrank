#!/bin/python3

import sys

def is_aws(A, l):
	A.append(l)
	for i in range(len(A)):
		flag = True
		if A[i] > 1:
			for j in range(len(A)):
				if (A[j] // A[i]) * A[i] != A[j] :
					flag = False
					break
			if flag:
				return True
	A.remove(l)

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
A = [int(A_temp) for A_temp in input().strip().split(' ')]


for i in range(k,-1,-1):
	if is_aws(A,i):
		print(i)
		break
