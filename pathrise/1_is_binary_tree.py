'''

Binary Tree properties

Each node should only have two children, if it has more than two children Immediately return invalid

Each node should only have one parent

Each node should be part of one connected tree. We can figure this out if there is more than one root. It is false

There should only be one node that does not have a parent. This is the root.

'''
from collections import defaultdict
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isBinTree(listA):
    # Maintain a hashmap initialized with a list
    # Every Node should have two children, a left and a right. Index 0 and 1.
    # Go through the list to make sure each Node has only two children.
    # If more than one root. Return false
    # Do a DFS (In Order) to construct te
    treemap = defaultdict(list)
    for i in listA:
        if i.left:
            treemap.append(treemap.left)
        if treemap.right:
            treemap.append(treemap.right)
    trackduplicates = set()
    for i in treemap:
        for j in treemap[j]:
            if j in trackduplicates:
                return False
            trackduplicates.add(j)
    # Check if two roots
    counter = 0
    for i in treemap:
        if counter == 2:
            return False
        if i not in trackduplicates:
            counter += 1
    return True


# Can do a DFS to construct the tree, but this seems unnecessary. if there is more than one root, only then there can be two trees.

a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(9)
d = TreeNode(7)
a.left = c
a.right = d
b.left = d

j = TreeNode(2)
k = TreeNode(4)
l = TreeNode(5)
j.left = k
j.right = l


print(isBinTree([j, k, l]))
print(isBinTree([a, b, c, d]))
