"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(r,val):
    if r:
        if val > r.data:
            if r.right:
                insert(r.right, val)
            else:
                r.right = Node(data=val)
        else:
            if r.left:
                insert(r.left, val)
            else:
                r.left = Node(data=val)
        return r
    else:
        return Node(data=val)
