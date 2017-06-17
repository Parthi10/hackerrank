"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def merge(headA, headB, previous_node=None):
    if headA and headB:
        larger_node = headA if headA.data>headB.data else headB
        smaller_node = headA if larger_node==headB else headB

        node1 = smaller_node.next
        node2 = larger_node

        if previous_node:
            previous_node.next = smaller_node
        merge(node1, node2, previous_node=smaller_node)
        return smaller_node
    if headA:
        if previous_node:
            previous_node.next = headA
        return headA
    if headB:
        if previous_node:
            previous_node.next = headB
        return headB


def MergeLists(headA, headB):
    return merge(headA, headB)


'''
#alternate method

def MergeLists(headA, headB):
    if headA==None:
        return headB
    elif headB==None:
        return headA
    elif headA.data<headB.data:
        headA.next = MergeLists(headA.next, headB)
        return headA

    else:
        headB.next = MergeLists(headA, headB.next)
        return headB
'''


'''

def MergeLists(headA, headB):
    if headA and headB:
        larger_node = headA if headA.data>headB.data else headB
        smaller_node = headA if larger_node==headB else headB
        smaller_node.next = MergeLists(smaller_node.next, larger_node)
        return smaller_node
    if headA:
        return headA
    if headB:
        return headB

'''
