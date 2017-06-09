#https://www.hackerrank.com/challenges/manasa-and-stones
t = int(input().strip())
for i in range(t):
    n = int(input())
    a = int(input())
    b = int(input())
    if(a!=b):
        c = a if a<b else b
        d = b if c==a else a
        ans=[]
        for j in range(n):
            temp = (n-1-j)*c + j*d
            ans.append(temp)
        for i in ans:
            print(i, end=' ')
        print()      
    else:
		
	    print((n-1)*a)
