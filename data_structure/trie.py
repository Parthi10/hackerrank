class TrieNode(object):

    def __init__(self):
        self.children = [None] * 26
        self.leafNode = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def _charToIndex(self, char):
        return ord(char) - ord('a')

    def insert(self, string):
        node = self.root
        for char in string:
            index = self._charToIndex(char)
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]

        node.leafNode = True

    def search(object, key):#search for a string, True if string was inserted
        node = self.root
        for char in key:
            index = self._charToIndex(char)
            child = node.children[index]
            if child:
                node = child
            else:
                return False

        return node.leafNode #suppose, root node is not None i.e., there's sth in the trie

    
