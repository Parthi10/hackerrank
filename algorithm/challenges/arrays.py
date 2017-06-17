# a=[8,4,5]
# p=0
# for i in range(0,3):
#     p=p+a[i]
#
# print(p)

#
# n = int(input().strip())
# a = []
# for a_i in range(n):
#    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
#    a.append(a_t)

#print(a[0][1])
#p,q=int(0),int(0)
#for i in range(0,n):
    #p=p+int(a[i*(n+1)])
    #q=q+int(a[(i+1)*(n-1)])
    #a[i*(n+1)]

#print(p+q)

import sys


n = int(input().strip())
a = []
for a_i in range(n):
   a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   a.append(a_t)
p,q,x=0,0,0
for i in range(0,n):
    p=p+(a[i][i])
    q=q+(a[i][n-i-1])
print(abs(p-q))
