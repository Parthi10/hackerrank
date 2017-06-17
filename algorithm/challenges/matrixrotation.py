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

layers = m // 2 if m < n else n // 2  # layer = half of minimum, even no.
for e in range(layers):  # one by one rotating each layer
	per = 2 * (m + n - 4 * e) - 4  # perimeter
	r = r % per  # optimized 'r' for this layer
	xy = layer_xy(m - 2 * e, n - 2 * e, e)  # xy holds (x,y) list of this layer
	circle = [mat[i][j] for i,j in xy]  # circle holds all the elements of this layer in mat
	circle = circle[per - r:] + circle[:per - r]  # rotate the circle
	for k in range(per):  # map the matrix mat to rotated circle
		i, j = xy[k]  # get coordinates which are present in xy
		mat[i][j] = circle[k]  # get them maped with corresponding rotated element

for i in mat:
	print(" ".join(map(str, i)))
