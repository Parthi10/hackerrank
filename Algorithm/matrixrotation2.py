m, n, r = [int(x) for x in input().strip().split(' ')]
matrix = []
for i in range(m):
	temp = [int(x) for x in input().strip().split(' ')]
	matrix.append(temp)

def get_new_coordinates(old_x, old_y, layer,r):
	pass

def get_perimeter(row, col):
	pass

def get_layer(row,col):
	pass

rotated_matrix = [[0 for i in range(n)] for j in range(m)]
layers = m // 2 if m < n else n // 2  # layer = half of minimum, even no.
for row in matrix:
	for col in row:
		layer = get_layer(row,col)
		per = get_perimeter(row,col)
		r = r % per
		new_x, new_y = get_new_coordinates(row, col, layer, r)
		rotated_matrix[new_x][new_y] = matrix[row][col]

for row i rotated_matrix:
	print(" ".join(map(str, row)))
'''
def layer_xy(m, n, e):  # creates a list with all the outer x,y of eth layer
	xy = []
	for i in range(e, m + e):
		xy.append([i, e])  # contains x,y of left side of this layer
	for j in range(e + 1, n + e - 1):
		xy.append([m - 1 + e, j])  # contains x,y of bottom side
	for i in range(m - 1, -1, -1):
		xy.append([i + e, n - 1 + e])  # contains x,y of right side
	for j in range(n + (e - 1) - 1, e, -1):
		xy.append([e, j])  # x,y of top side of this layer
	return xy


m, n, r = [int(x) for x in input().strip().split(' ')]
mat = []

for i in range(m):
	temp = [int(x) for x in input().strip().split(' ')]
	mat.append(temp)

rotated_matrix = [[0 for i in range(n)] for j in range(m)]

layers = m // 2 if m < n else n // 2  # layer = half of minimum, even no.
for e in range(layers):  # one by one rotating each layer
	per = 2 * (m + n - 4 * e) - 4  # perimeter
	r = r % per  # optimized 'r' for this layer
	xy = layer_xy(m - 2 * e, n - 2 * e, e)  # xy holds (x,y) list of this layer
	for i in range(per):
		try:
			rotated_matrix[xy[i][0]][xy[i][1]] = mat[xy[i-r][0]][xy[i-r][1]]
		except:
			rotated_matrix[xy[i][0]][xy[i][1]] = mat[xy[i-r+per][0]][xy[i-r+per][1]]
			# pass
for i in rotated_matrix:
	print(" ".join(map(str, i)))
'''
