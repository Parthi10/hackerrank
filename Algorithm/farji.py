#https://www.hackerrank.com/challenges/maxsubarray
t=int(input())
c_sa=[] #to hold max of contigous subarray
uc_sa=[] #to hold max of uncontigous subarray
sumList=[]
for i in range(t):
    p, q = -10000, -10000  # as the question says min value of any element
    z=1
    n=int(input())
    a=[int(i) for i in input().strip().split(" ")]
    #print(a)
    count=0
    uc_sum=0
    for i in a: #if all i's are +ve then c_sa and uc_sa are same, whole array itself
        if(i>=0):
            count=count+1
            uc_sum=uc_sum+i #for uc_sa add all +ve no. irespective of other constraints
    if(uc_sum==0):#if all elements are -ve then for uc_sa, the least -ve no.
        for i in a:
          if(i>q):
              q=i
              #print(q)
        uc_sa.append(q)
    if(uc_sum!=0):
        uc_sa.append(uc_sum)
    if(count==n): #if all elements are +ve, c_sa= whole array itself
        c_sa.append(sum(a))

    for i in range(n):# we need to store sum(a[i:y]) in list, its the sum of elements of all possible contigous
        for y in range(z,n+1):# sub arrays..for example n=2, we need a[0:2], a[0:1], a[1:2] there sums..
            sumList.append(sum(a[i:y]))# add the sum of all possible contgous sub arrays in sumList
        z=z+1
    for i in sumList:#to determine which no. in sumlist is max
        if(i>p):
            p=i
    c_sa.append(p)
# for i in range(t):# for printing final answer
#      print('%s %s' %(c_sa[i],uc_sa[i]))
# test with 1 -2
print(c_sa)
#print(uc_sa)
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