#Runtime error at #12, maybe due to over memory usage.
class TrieNode(object):

    def __init__(self):
        self.children = [None] * 26
        self.leafNode = False
        self.partials = 0 #number of strings which can be formed after this node


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def _charToIndex(self, char):
        return ord(char) - ord('a')

    def insert(self, string):
        node = self.root
        for char in string:
            index = self._charToIndex(char)
            child = node.children[index]
            if not child:
                child = TrieNode()
                node.children[index] = child
            child.partials += 1
            node = node.children[index]

        node.leafNode = True

    def findPartial(self, key):#search for a string, True if string was inserted
        node = self.root
        for char in key:
            index = self._charToIndex(char)
            child = node.children[index]
            if child:
                node = child
            else:
                return 0

        return node.partials

T = Trie()

n = int(input().strip())
for i in range(n):
    inp = input().strip().split(' ')
    if inp[0] == 'add':
        T.insert(inp[1])
    else:
        print(T.findPartial(inp[1]))
