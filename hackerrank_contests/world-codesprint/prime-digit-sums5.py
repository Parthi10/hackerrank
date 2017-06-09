from itertools import product
primeList = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]

def check(s,primeList,l):
    for i in range(l-2):
        num = sum(s[i:i+3])
        if num not in primeList:
            return False
    for i in range(l-3):
        num = sum(s[i:i+4])
        if num not in primeList:
            return False
    for i in range(l-4):
        num = sum(s[i:i+5])
        if num not in primeList:
            return False
    return True
q = int(input().strip())

for _ in range(q):
    n = int(input().strip())
    c = 0
    # intlist = [1,2,3,4,5,6,7,8,9,0]
    # numlist = product(intlist,repeat=n)
    # for i in numlist:
    #     if i[0]!=0 and i[0]!=7 and check(i,primeList,n):
    #         c+=1
    for i in range(10**(n-1),10**n + 1):
        i = list(map(int, str(i)))
        if i[0]!=7 and check(i,primeList,n):
            c+=1

    print(c)
    # print(time.time()-t)
