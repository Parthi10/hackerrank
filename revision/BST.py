class Node(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class BST(object):
    def __init__(self, root):
        self.root = root

    def insertNode(self, node, root=self.root):
        if root is None:
            self.root = node
            return node
        elif node.data < root.data:
            root.left = self.insertNode(node, root=root.left)
        else:
            root.right = self.insertNode(node, root=root.right)


    def searchNode(self, data, root=self.root):
        if root is None:
            return False

        if root.data == data:
            return True

        elif node.data < data:
            return self.searchNode(data, root=root.left)

        else:
            return self.searchNode(data, root=root.right)

    def deleteNode(self, data, root=self.root, parent=None):#given node is in Tree
        if root.data == data:
            if root.left and root.right:
                min_node = root.right
                while True:
                    next_min = min_node.left
                    if next_min:
                        min_node = next_min
                    else:
                        root.data = min_node.data
                        min_node = None
                        break

            elif root.right:
                if parent:
                    parent.right = root.right
                else:#in case of root node of tree (self.root)
                    self.root = root.right
            else:
                if parent:
                    parent.right = root.left
                else:#in case of root node of tree (self.root)
                    self.root = root.left

        elif root.data < data:
            self.deleteNode(data, root=root.left)
        else:
            self.deleteNode(data, root=root.right)
