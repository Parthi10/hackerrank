#https://www.hackerrank.com/challenges/lonely-integer
# Head ends here
def lonelyinteger(b):
	answer = 0
	for i in range(len(b)):
		i=0 #chutiyapa it's like while loop, like its gonna run for len(b) times, the same thing
		#print(b)
		p=b[i]
		b.remove(p)# if not removed
		#print(p)
		if(p not in b):# then this will always come true
			answer=p#it this comes true now means that that's the single no.''
			break
		else:# ok if it is there so add it again, at the last, otherwise the other one will create a prob.
			b.append(p)
			#print('appended',p)
	return answer
# Tail starts here
if __name__ == '__main__':
	a = int(input())
	b = [int(x) for x in input().strip().split(" ")]
	print(lonelyinteger(b))
