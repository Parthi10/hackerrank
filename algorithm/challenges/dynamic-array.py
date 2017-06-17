#https://www.hackerrank.com/challenges/dynamic-array
N, Q = map(int, input().split(' ')) #take two space seperated ints
lastAns = 0
seqList = [[] for _ in range(N)]
for _ in range(Q):
    i,x,y = map(int, input().split(' '))
    index = (x ^ lastAns) % N
    seq = seqList[index]
    if i == 1:
        seqList[index].append(y)
    elif i == 2:
        lastAns = seq[y % len(seq)]
        print (lastAns)
