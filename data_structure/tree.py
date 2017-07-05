#BinarySearchTree
#every node has unique data value (int)

class Node(object):
    def __init__(self, data, left_node=None, right_node=None):

        self.data = data
        self.left_node = left_node
        self.right_node = right_node

class Tree(object):

    def __init__(self, root_node=None):
        self.root_node = root_node

    def insert(self, new_node, root):
        if root == None:
            return new_node
        if new_node.data >= root.data:
            root.right_node = insert(self, new_node, root.right_node)
        else:
            root.left_node = insert(self, new_node, root.left_node)
        return root
