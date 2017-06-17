ans=[]
def arrsum(a,y):
    if(sum(a[:y])==sum(a[y+1:])):
        return "YES"
    else:
        return "NO"
t=int(input().strip())
for i in range(t):
    n=int(input().strip())
    numlist=[int(x) for x in input().split(' ')]
    #print(t,n,numlist)
    p=0
    for i in range(len(numlist)):

        if(arrsum(numlist,i)=="YES"):
            ans.append("YES")
            p+=1
            break
    if(p==0):
        ans.append("NO")
for i in ans:
    print(i)
             
