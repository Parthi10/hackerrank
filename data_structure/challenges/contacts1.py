#without using classes
root = [dict(), 0]
fixed_root = root

def add(root, word, level=0):
    if level < len(word):
        char = word[level]
        if char not in root[0]:
            root[0][char] = [dict(),1]
            add(root[0][char], word, level+1)
        else:
            root[0][char][1] += 1
            add(root[0][char], word, level+1)

def find(root, word, level=0):
    while level < len(word):
        char = word[level]
        if char in root[0]:
            root = root[0][char]
            level +=1
        else:
            return 0
    return root[1]

n = int(input().strip())
for _ in range(n):
    inp = input().strip().split(' ')
    if inp[0] == 'add':
        add(fixed_root, inp[1])
    else:
        print(find(fixed_root, inp[1]))
