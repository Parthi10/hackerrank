from collections import defaultdict

length = 0
count = defaultdict(int)
content = []
with open('cipher.txt') as f:
	for row in f:
		content.append(row.strip())

for row in content:
	for i in row:
		count[i] += 1
		length += 1

origfreq = defaultdict(int)

with open('freq.txt') as f:
	for row in f:
		val = row.strip().replace('\t','')
		# print(val)
		origfreq[val[0]] = val[1:]


# for value,origvalue in zip(sorted(count.values(), reverse=True), sorted(origfreq.values(), reverse=True)):
# 	print(list(count.keys())[list(count.values()).index(value)], "%.2f" %((value / length)*100),"  ", list(origfreq.keys())[list(origfreq.values()).index(origvalue)], origvalue)

def repl(row):
	row = row.replace("A", "h").replace("L", "t").replace("M", "e")
	return row


def shift(row, key):
	row = list(row)
	for i in range(len(row)):
		asc = ord(row[i])
		asc = asc+key
		if asc > 90:
			row[i] = chr(asc-26)
		else:
			row[i] = chr(asc)
		if asc < 65:
			row[i] = chr(asc+26)
	print("".join(row))

key = -26

for row in content:
	print(row)
	print(repl(row))	
	print()
	# shift(row,key)
	# print("\n")
	# print(shift(row),"\n")






