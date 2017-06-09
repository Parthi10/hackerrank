primeSet3 = 303
primeSet3_zero = 37
primeSet4 = 280
primeSet4_zero = 135
primeSet5 = 218
primeSet5_zero = 175

p = [218,95,101,295,513]
modulo = 10**9 + 7
q = int(input().strip())
for _ in range(q):
    n = int(input().strip())
    if n>=5:
        if n//5 == 1:
            if n==5:
                print((primeSet5)%modulo)
            elif n>5:# n --> 6,7,8,9
                print(p[n%5]%modulo)
        elif n//5 > 1: #n -- 10 n more
            repeat = n // 5
            extra = n % 5 # can be 0,1,2,3,4,
            ans = (primeSet5) * ((primeSet5_zero) ** repeat)
            if extra == 4:
                print((ans*(primeSet4_zero))%modulo)
            elif extra == 3:
                print((ans*(primeSet3_zero))%modulo)
            elif extra == 2:# 2
                print((ans*85)%modulo)
            elif extra == 1:
                print((ans*92)%modulo)
            elif extra == 0:
                print(ans%modulo)
    elif n==4:
        print((primeSet4) %modulo)
    elif n==3:
        print((primeSet3) %modulo)
