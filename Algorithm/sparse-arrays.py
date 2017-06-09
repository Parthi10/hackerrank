N = int(input())
strArray = []
for _ in range(N):
    strArray.append(input().strip())
Q = int(input())
for _ in range(Q):
    query = input()
    print(strArray.count(query)) #count how many times query occured in strArray
