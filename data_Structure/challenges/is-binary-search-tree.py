""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def isSubtreeLesser(node, root_value):
    if node:
        if (node.data < root_value and
            isSubtreeLesser(node.left, root_value) and
            isSubtreeLesser(node.right, root_value)):
            return True
        else:
            return False
    else:
        return True

def isSubtreeGreater(node, root_value):
    if node:
        if (node.data > root_value and
        isSubtreeGreater(node.left, root_value) and
        isSubtreeGreater(node.right, root_value)):
            return True
        else:
            return False
    else:
        return True



def check_binary_search_tree_(root):
    if root:
        if (isSubtreeLesser(root.left, root_value) and
            isSubtreeGreater(root.right, root_value) and
            check_binary_search_tree_(root.left) and
            check_binary_search_tree_(root.right)):
            return True
        else:
            return False
    else:
        return True

'''
#another faster method
#https://youtu.be/yEwSGhSsT0U?t=857


def checkBST(root, min_value, max_value):
    if root:
        if (root.data>min_value and root.data<max_value and
            checkBST(root.left, min_value, root.data) and
            checkBST(root.right, root.data, max_value)):
            return True
        else:
            return False
    else:
        return True

def check_binary_search_tree_(root):
    return checkBST(root, 0, 10**4)

'''
