def rowsearch(q,p):
	
	prow,qrow=[len(p),len(q)]# no. of rows
	pcol,qcol=[len(p[0]),len(q[0])]# 0 only for reference, pcol= no. of columns in p
	#print(prow, qrow, pcol, qcol)
	for i in range(qrow-prow+1):# for checking every row of q
		if(p[0] in q[i]):#if present in any row of q, then only bother to proceed further
			#print(i)
			for j in range(qcol-pcol+1):#j is to determine the exact column no. where this matching starts
				#print(j)
				count=0# to confirm, the correctness
				for k in range(prow):# to change the row no. of p once you find the right j, i.e, where this match starts					
					if(p[k] in q[i+k][j:j+pcol]):#if found in this sub-array of exactly same size as that of p, traversing the rows of q.
						count+=1# increase the count, as we found the sub-array which matches with p[0], then p[1]..i.e., p[k] 
						#this block of for loop will check all the rows of p to the matched sub-array of q[i].			
					else:
						break# break, we don't need to check(all the rows of p) for this value of 'j' (notice it)
				if(count == prow):
					return 'YES'
				
	return 'NO' # agar abhi tak yes na mila to kab milega!!
					

t = int(input().strip())
for a0 in range(t):
	R,C = input().strip().split(' ')
	R,C = [int(R),int(C)]
	G = []
	for _ in range(R):
		G_t = str(input().strip())
		G.append(G_t)
	r,c = input().strip().split(' ')
	r,c = [int(r),int(c)]
	P = []
	for _ in range(r):
		P_t = str(input().strip())
		P.append(P_t)
	ans=rowsearch(G,P)
	print(ans)
