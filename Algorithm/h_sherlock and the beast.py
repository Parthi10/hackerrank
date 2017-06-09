#https://www.hackerrank.com/challenges/sherlock-and-the-beast?h_r=next-challenge&h_v=zen

num=[]
t = int(input().strip())
for a0 in range(t):
    n5,n3=[],[]
    n = int(input().strip())
    for i in range(n):
        if(i%3==0):
            n5.append[i]
        elif(i%5==0):
            n3.append[i]
    for x in n5:
        for y in n3:
            if(x+y==n):
                m=str('5'*y)+str('3'*x)
                num.append(m)

