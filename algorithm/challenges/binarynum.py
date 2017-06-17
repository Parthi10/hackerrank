
import sys
ans = []
def dec_to_bin(x):
	return int(bin(x)[2:])
n = int(input().strip())
binary = str(dec_to_bin(n))
for i in range(len(binary)):
	if binary[i] == '1':
		p = 0
		for j in range(i,len(binary)):

			if binary[j] == '1':
				p += 1
			else:
				break
		ans.append(p)


print(ans)

