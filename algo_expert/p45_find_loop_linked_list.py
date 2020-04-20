# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # Write your code here.
    if not head:
        return -1
    visited = set()
    
    node = head
    while node:
        if node.value in visited:
            return node
        else:
            visited.add(node.value)
        node = node.next