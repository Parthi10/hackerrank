#n = int(input())
#f = [0,1,1]
#def fib(f,i):
	#return f[i-1]+f[i-2]
#def fibo(n):
	#if n < max(f):
		#return [x for x in f if x<n]
	#else:
		#ind = 3
		#while max(f) < n:
			 #new = fib(f,ind)
			 #f.append(new)
			 #ind += 1
		#return f if max(f) < n else f[:len(f)-1]
			 
#print(fibo(n))	
def fibonacci(n):
	ans = [0]
	i_next = 1
	while i_next <= n:
		ans.append(i_next)
		i_next = sum(ans[-2:])
	return ans
n = int(input())
p = fibonacci(n)
print(p)
