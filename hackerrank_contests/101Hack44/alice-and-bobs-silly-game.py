#https://www.hackerrank.com/contests/101hack44/challenges/alice-and-bobs-silly-game
import math
def getPrimeList(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

def PrimeInList(numList,prime_set):
    for i in numList:
        if i in prime_set:
            return i
    return 0

def removeMuliple(numList, number):
    for i in numList:
        if i % number == 0:
            numList.remove(i)


g = int(input())
n_set = [int(input()) for _ in range(g)]
for i in n_set:
    prime_set = getPrimeList(i+1)
    numList = list(range(i+1))
    # print(prime_set,numList)
    flag = 0 #turn for alice
    # while True:
    #     primeNum = PrimeInList(numList,prime_set)
    #     if primeNum:
    #         # removeMuliple(numList,primeNum)
    #         numList.remove(primeNum)
    #         flag=0 if flag else 1
    #     else:
    #         # print(numList)
    #         print("Alice" if flag else "Bob")
    #         break
    if i==1:
        print("Bob")
    elif i==2:
        print("Alice")
    else:
        l = len(prime_set)
        if l%2==0:
            print("Bob")
        else:
            print("Alice")


'''
WTF???? NOW IT WORKED!!!!
'''
