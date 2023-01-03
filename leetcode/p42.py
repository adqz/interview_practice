from typing import List
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
      pass

def makeTree(nodes):
  '''
  if parent node is at index i in the array then the left child of that 
  node is at index (2*i + 1) and right child is at index (2*i + 2) in the array
  '''
  i = 0
  n = TreeNode(nodes[i])
  parent = n
  while True:
    try:
      parent.left = TreeNode(nodes[2*i + 1])
      parent.right = TreeNode(nodes[2*i + 2])
    except IndexError:
      break
    i += 1
    if i%2 == 0:
      parent = parent.right
    else:
      parent = parent.left

  return n

if __name__ == '__main__':
  sol = Solution()
  root = [1,2,3,4]; x = 4; y = 3
  n = makeTree(root)
  print(n.val, n.left.val, n.right.val, n.left.left.val)