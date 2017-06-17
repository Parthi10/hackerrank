import math as m
t=int(input().strip())
for i in range(t):
    a,b=input().strip().split(' ')
    ans=0
    a,b=int(a),int(b)
    for i in range(a,b+1):
        if(round(m.sqrt(i),2)*round(m.sqrt(i),2)==i):
            ans+=1
            
    print(ans)         
