def rem(a,b):
    l=len(a)-1
    while l>=0:
        if(a[l]==b):
            a.remove(a[l])
        l-=1            
n = int(input().strip())
arr = [int(a) for a in input().strip().split(' ')]
while len(arr)>0:
    min=1000
    for i in arr:
        if(i<min):
            min=i
    rem(arr,min)
    print(len(arr))
