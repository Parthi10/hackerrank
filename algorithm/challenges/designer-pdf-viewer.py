h = list(map(int, input().strip().split(' ')))
word = [ord(x)-97 for x in list(input())]
maxHeight=1
for i in word:
    if maxHeight<h[i]:
        maxHeight = h[i]

print(maxHeight*len(word))
