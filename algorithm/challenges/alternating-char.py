#https://www.hackerrank.com/challenges/alternating-characters?h_r=next-challenge&h_v=zen
t=int(input())
for i in range(t):
    s=[str(a) for a in input().strip('')]
    n=len(s)
    i=0
    count=0
    l=[]#to hold the indexes which are to be removed
    while(i<=n-1):
        if(i<=n-2):
            x=s[i]
            if(s[i+1]==x):#if two simultaneous same char remove the first one                
                count+=1
        i+=1
    
    print(count)


