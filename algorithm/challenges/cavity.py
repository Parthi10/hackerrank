n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
	grid_t = list(input().strip())
	grid.append(grid_t)
for i in range(1,n-1):
	for j in range(1,n-1):
		val=grid[i][j]                
		if(val>grid[i-1][j] and val>grid[i+1][j] and val>grid[i][j-1] and val>grid[i][j+1]):
			grid[i][j] = "X"
		
for i in range(n):
	for j in range(n):
		print(grid[i][j], end='')

	print('')
print('rish')