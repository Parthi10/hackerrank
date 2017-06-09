import sys
'''
DOWNLOADED SOLUTION
'''

def rendez(s,slen,l,l_first,l_last, diffstart):
    #print((s,slen,l,l_first,l_last, diffstart))
    #print((l_first,l_last, diffstart))
    if l_first>=l_last:
        return
    diffstart1=diffstart
    while True:
        sm_ord_min=ord('z')+1
        sm_ord_max=ord('a')-2
        for l_i in range(l_first, l_last+1):
            sm_ord = ord(s[l[l_i]+diffstart1]) if l[l_i]+diffstart1<slen else ord('a')-1
            if sm_ord<sm_ord_min:
                sm_ord_min=sm_ord
            if sm_ord>sm_ord_max:
                sm_ord_max=sm_ord
        if sm_ord_min==sm_ord_max:
            diffstart1+=1
        else:
            break

    sm = chr(int((sm_ord_min+sm_ord_max+1)/2))
    i1=l_first
    i2=l_last
    try:
            while i1<i2:
              if l[i1]+diffstart1==slen or s[l[i1]+diffstart1] < sm:
                i1+=1
              elif l[i2]+diffstart1<slen and s[l[i2]+diffstart1] >= sm:
                i2-=1
              else:
                ll=l[i1]
                l[i1]=l[i2]
                l[i2]=ll
                i1+=1
                #i2-=1
    except:
           print((slen,l_first,l_last, i1,i2, l[i1], l[i2],diffstart, sm))
           return
    rendez(s,slen,l,l_first,i1-1,diffstart1)
    rendez(s,slen,l,i1,l_last,diffstart1)


def testcase(s,k):
    slenarray=[0]*(len(s)+1)
    for i in range(1,len(s)+1):
        slenarray[i]=slenarray[i-1]+i

    l = list(range(len(s)))
    rendez(s,len(s),l,0,len(l)-1,0)

    for i in range(len(s)):
        s0=s[l[i-1]:] if i>0 else ""
        s1=s[l[i]:]
        diffstart=0
        while diffstart<len(s0) and diffstart<len(s1) and s0[diffstart]==s1[diffstart]:
            diffstart = diffstart+1
        slen=slenarray[len(s1)]-slenarray[diffstart]
        #print(str((s0,s1,diffstart,slen,k)))
        if k<=slen:
            d=diffstart+1
            while k>0:
                if k<=d:
                    print(s1[k-1])
                    k=0
                    break
                else:
                    k=k-d
                    d=d+1
        else:
            k=k-slen

        if k==0:
            break

    #print(time.time()-t0)
    #print()



testcount = int(sys.stdin.readline())
for i in range(testcount):
    s=sys.stdin.readline()[:-1]
    k=int(sys.stdin.readline())
    #print("testcase "+str(i)+" :")
    testcase(s,k)
