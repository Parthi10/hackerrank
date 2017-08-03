class Node(object):
    def __init__(self):
        self.children = [None] * 26
        self.isLeafNode = False

class Trie(object):
    def __init__(self):
        self.root = Node()

    def charToIndex(self, char):
        return ord(char) - ord('a')

    def insert(self, string):
        node = self.root
        for char in string:
            index = self.charToIndex(char)
            if not node.children[index]:
                node.children[index] = Node()
            node = node.children[index]
        node.isLeafNode = True


    def find(self, string):
        node = self.root
        for char in string:
            child = node.children[self.charToIndex(char)]
            if child:
                node = child
            else:
                return False

        return node.isLeafNode

    def delete(self, string):#given the string is in the trie
        node = self.root
        for char in string:
            index = self.charToIndex(char)
            child = node.children[index]
            node.children[index] = None
            parent = node
            node = child

        for child in parent.children:
            if child != None:
                return
        parent.isLeafNode = True
