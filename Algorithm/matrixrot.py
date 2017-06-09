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
	circle = [mat[p[0]][p[1]] for p in xy]  # circle holds all the elements of this layer in mat
	circle = circle[per - r:] + circle[0:per - r]  # rotate the circle
	for k in range(per):  # map the matrix mat to rotated circle
		i, j = map(int, xy[k])  # get coordinates which are present in xy
		mat[i][j] = circle[k]  # get them maped with corresponding rotated element

for i in mat:
	for k in i:
		print(k, end=' ')
	print()


# def ls(m, n, e):  # creates a list with all the outer x,y of eth layer
# 	xy = []
# 	for i in range(e, m + e):
# 		xy.append([i, e])
# 	for j in range(e + 1, n + e - 1):
# 		xy.append([m - 1 + e, j])
# 	for i in range(m - 1, -1, -1):
# 		xy.append([i + e, n - 1 + e])
# 	for j in range(n + (e-1) - 1, e, -1):
# 		xy.append([e, j])
# 	return xy
#
# m,n,r = [int(x) for x in input().strip().split(' ') ]
# mat=[]
# for i in range(m):
# 	temp=[int(x) for x in input().strip().split(' ')]
# 	mat.append(temp)
#
# layers= m//2 if m<n else n//2 # layer = half of min even no.
# cmat = []
# for i in range(m):
# 	cmat.append(mat[i][:]) # will be printed at last
# for e in range(layers):
# 	per = 2*(m+n-4*e)-4 # perimeter
# 	r = r % per #optimized r for this layer
# 	xy = ls(m-2*e,n-2*e,e) # (x,y) list of this layer
# 	xylen = len(xy)
# 	for in_ij,ij in enumerate(xy): # geting index of element ij
# 		i,j=[int(x) for x in ij]#(x,y) of element at index in_ij
# 		nin_xy = in_ij + r#new index of new i,j after inc. by r
# 		nin_xy = nin_xy if nin_xy<xylen else nin_xy-xylen
# 		x, y = [int(x) for x in xy[nin_xy]]# new (x,y) after inc. by r
# 		cmat[x][y] = mat[i][j] # final touch
# for i in cmat:
# 	for k in i:
# 		print(k, end=' ')
# 	print()
#
