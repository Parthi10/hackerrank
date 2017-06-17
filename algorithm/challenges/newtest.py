#def gp(a,q):
	#k = 0
	#while True:
		#result = a * q**k
		#if result <=10000:
			#yield result
		#else:
			#return
		#print(k)
		#k += 1
		
		
#a, q = input().strip().split(' ')
#[a, q] = map(int, [a,q])
#gps = gp(a,q)
##print(list(gp(a,q))		)
##print(gp(a,q))
#print(gps.__next__())
#print(gps.__next__())
#print(gps.__next__())


def counter(start=0):
	n = start
	while True:
		result = yield n # A
		print(type(result), result) # B
		if result == 'Q':
			break
		n += 1
c = counter()
print(next(c)) # C
print(c.send('Wow!')) # D
print(next(c)) # E
print(c.send('Q')) # F
