import sys 
sys.setrecursionlimit(1500)
def decToBin(n):
    if n==0: return ''
    else:
        return decToBin(n/2) + str(n%2)
n=int(input().strip())
print(decToBin(n))
