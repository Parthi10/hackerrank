#https://www.hackerrank.com/challenges/maxsubarray
t=int(input())
c_sa=[]
uc_sa=[]
for i in range(t):
    n=int(input())
    a=[int(x) for x in input().split(" ")]
    sumList=[]
    z=1
    p,q=-10000,-10000
    for i in range(n):
        for y in range(z,n+1):
            sumList.append(sum(a[i:y]))
        z=z+1
    for i in sumList:
        if(i>p):
            p=i
    c_sa.append(p)
    uc_sum=0
    for i in a:  # if all i's are +ve then c_sa and uc_sa are same, whole array itself
        if (i >= 0):
            uc_sum = uc_sum + i  # for uc_sa add all +ve no. irespective of other constraints
    if (uc_sum == 0):  # if all elements are -ve then for uc_sa, the least -ve no.
        for i in a:
            if (i > q):
                q = i
                #   p=i
        # c_sa.append(p)
        uc_sa.append(q)
    if (uc_sum != 0):  # some +ve no. in it
        uc_sa.append(uc_sum)

for i in range(t):# for printing final answer
    print('%s %s' %(c_sa[i],uc_sa[i]))




'''6
1
1
6
-1 -2 -3 -4 -5 -6
2
1 -2
3
1 2 3
1
-10
6
1 -1 -1 -1 -1 5'''