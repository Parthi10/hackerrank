t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x in input().split(" ")]
    sumList=[]
    z=1
    p=-10000
    for i in range(n):
        for y in range(z,n+1):
            sumList.append(sum(a[i:y]))
            #print(sum(a[i:y]))
        z=z+1
    for i in sumList:
        if(i>p):
            p=i
    print(p)

    #see h_theMaxSubArray for comments

