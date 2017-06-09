from itertools import product
import time

primeList = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]

def check(s,primeList,l):
    for i in range(l-2):
        num = sum(s[i:i+3])
        try:
            if num not in primeList:
                return False
            num += s[i+3]
            if num not in primeList:
                return False
            num += s[i+4]
            if num not in primeList:
                return False
        except:
            pass

    return True
# check([1,0,1])
q = int(input().strip())

for _ in range(q):
    t = time.time()
    n = int(input().strip())
    c = 0
    intlist = [1,2,3,4,5,6,7,8,9,0]
    numlist = product(intlist,repeat=n)
    ans = []
    for i in numlist:
        # print(i)
        if i[0]!=0 and check(i,primeList,n):
            c+=1
            # print(c)
            ans.append(i)

    print(c)
    print(ans)
    # print(time.time()-t)
