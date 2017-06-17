#https://www.hackerrank.com/challenges/angry-professor
t = int(input().strip())
b=[]

for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    x=0
    for i in a:
        if (i>=0):
            x=x+1
    print(x)
    if(x<=k):
        b.append('No')
    else:
        b.append('Yes')
print(b[0])
print(b[1])