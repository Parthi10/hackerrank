#https://www.hackerrank.com/challenges/cube-summation
T = int(input())
for _ in range(T):
    N, M = map(int,input().strip().split(' '))
    d = {}
    for _ in range(M):
        inp = [int(x) if x != 'UPDATE' and x != 'QUERY' else x for x in input().strip().split(' ')]
        if inp[0] == 'UPDATE':
            d[(inp[1],inp[2],inp[3])] = inp[4]
        else:
            ans = 0
            for k in d.keys():
                flag = True
                for i in range(1,4):
                    if not k[i-1] >= inp[i] or not k[i-1] <= inp[3+i]:
                        flag = False
                        break
                if flag: ans += d[k]
            print (ans)



'''
T = int(input())
for _ in range(T):
    N, M = map(int,input().strip().split(' '))
    matrix = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N)]
    # print (matrix)
    for _ in range(M):
        inp = [int(x) if x != 'UPDATE' and x != 'QUERY' else x for x in input().strip().split(' ')]
        # print (inp)
        if inp[0] == 'UPDATE':
            matrix[inp[1]-1][inp[2]-1][inp[3]-1] = inp[4]
        else:
            ans = 0
            for i in range(inp[1]-1, inp[4]):
                for j in range(inp[2]-1, inp[5]):
                    for k in range(inp[3]-1, inp[6]):
                        # print(i,j,k)
                        ans += matrix[i][j][k]
            print (ans)
'''
