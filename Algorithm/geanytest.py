t = int(input().strip())
for i in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    tot_choc=n//c
    wrap=tot_choc
    #print(tot_choc, wrap)
    while wrap >= m:
        extra_choc = wrap//m
        wrap-=m*extra_choc
        wrap+=extra_choc
        tot_choc+= extra_choc
    print(tot_choc)        
