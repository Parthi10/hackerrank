#
def getPosition(p):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==p:
                return [i,j]

def nextMove(n,r,c,grid):
    r_p, c_p = getPosition('p')
    if r_p<r:
        return "UP"
    elif r_p>r:
        return "BOTTOM"
    if c_p<c:
        return "LEFT"
    elif c_p>c:
        return "RIGHT"
 
n = int(input().strip())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(list(input().strip()))

print(nextMove(n,r,c,grid))
