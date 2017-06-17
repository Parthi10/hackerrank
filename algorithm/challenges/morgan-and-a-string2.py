import time
def whichList(s1,s2,a,b,l1,l2):#return True for S1 n False for S2
    # print("got", a,b)
    # try:
    if (a+1) < l1 and (b+1) < l2:
        if s1[a+1] < s2[b+1]:
            return True
        elif s1[a+1] > s2[b+1]:
            return False
        else:#both s[a+1]==s[b+1] equal yet again ,,time for recursion!!
            # print("optimisation",a,b)
            while  a+2<l1 and b+2<l2 and s1[a+1]==s2[b+1] :#optimise
                a+=1
                b+=1
                #if same char upto end then a+1 will be last index same for b+1, irrespective of whether they r same or not
            # print(a,b)
            # print("recursive call to whichList")
            return whichList(s1,s2,a+1,b+1,l1,l2)
    else:# BAWAAL HAI BABA
    #any one of a and b or both is at the last of their string
    #lets check who?
        # try:
        if (a+1) == l1 and (b+1) < l2: # a is at last
            if s2[b] < s1[a]:#a is last elem, b not
                return False
            elif s2[b] > s1[a]:
                return True
            else:#madafaka again same
                return whichList(s1,s2,a,b+1,l1,l2)
        elif (a+1) < l1 and (b+1) == l2: #b is at last
            if s2[b] < s1[a]:#a is last elem, b not
                return False
            elif s2[b] > s1[a]:
                return True
            else:#madafaka again same
                return whichList(s1,s2,a+1,b,l1,l2)
        elif (a+1)==l1 and (b+1) == l2:
            return True#or False doesn't matter both chars are same n are going to be 1 after another
        else:#something wrong in the program
            print("overflow")
            print(a,b,"overllllll")
            pass
    #         except Exception as e:
    #             print(e)
    #             print('inside excption')
    #             time.sleep(10)
    # except Exception as e:
    #     print(a,b,s1[a-1],s2[b-1])
    #     print(e)
    #     time.sleep(10)

final_ans = []
t = int(input())
for i in range(t):
    s1 = input().strip()
    s2 = input().strip()
    l1 = len(s1)
    l2 = len(s2)
    length = l1 +l2
    x,a,b = [0]*3
    ans = ""
    while (a+b) < length:
        # print("starting while loop with ",a,b)
        if a < l1 and b < l2:
            if s1[a] < s2[b]:
                ans+=s1[a]
                a += 1
            elif s1[a] > s2[b]:
                ans+=s2[b]
                b += 1
            else: #both equal check which side to move
                # print("calling whichList")
                if whichList(s1,s2,a,b,l1,l2):
                    ans+=s1[a]
                    a += 1
                else:
                    ans+=s2[b]
                    b += 1

        elif a < l1 and b >= l2: #s2 is exhausted
            ans+=s1[a:]
            break
        elif b < l2 and a >= l1:#s1 is exhausted
            ans+=s2[b:]
            break
    final_ans.append(ans)

print("\n".join(final_ans))
