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

    def insert(self, new_node, base_node):
        if new_node.data > base_node.data:
            if base_node.right_node == None:
                base_node.right_node = new_node
            else:
                insert(self, new_node, base_node=base_node.right_node)
        else:#cant' be equal, an assumption :]
            if base_node.left_node == None:
                base_node.left_node = new_node
            else:
                insert(self, new_node, base_node=base_node.left_node)
